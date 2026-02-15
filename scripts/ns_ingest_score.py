#!/usr/bin/env python3
"""
NS dashboard ingest and score. Writes to network-states/out/.
Uses rubric (network-states/rubric/rubric.yml), optional overrides (network-states/overrides/manual_tags.yml).
Outputs: top_success.md, top_venezuela_fit.md, clusters.md, white_spaces.md; confidence grade A/B/C per row.
Usage: python ns_ingest_score.py [PATH_TO/societies.csv]
Default CSV: downloads/network-states/societies.csv relative to repo root.
"""
import csv
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    import yaml
except ImportError:
    yaml = None

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CSV = REPO_ROOT / "downloads" / "network-states" / "societies.csv"
OUT_DIR = REPO_ROOT / "network-states" / "out"
RUBRIC_PATH = REPO_ROOT / "network-states" / "rubric" / "rubric.yml"
OVERRIDES_PATH = REPO_ROOT / "network-states" / "overrides" / "manual_tags.yml"


@dataclass
class Score:
    legitimacy_path: int = 0
    territory_density: int = 0
    economic_engine: int = 0
    identity_credentials: int = 0
    governance_security: int = 0
    dacc_alignment: int = 0
    execution_capacity: int = 0
    venezuela_similarity: int = 0

    def total(self) -> int:
        return (
            self.legitimacy_path + self.territory_density + self.economic_engine
            + self.identity_credentials + self.governance_security + self.dacc_alignment
            + self.execution_capacity + self.venezuela_similarity
        )


def _normalize(s: str) -> str:
    return (s or "").strip().lower()


def _tag_set(row: dict) -> set:
    raw = row.get("tags") or row.get("Tags") or ""
    return {_normalize(t) for t in re.split(r"[,;|\s]+", raw) if t.strip()}


def _text(row: dict, *keys: str) -> str:
    return " ".join(_normalize(row.get(k) or "") for k in keys)


def confidence_grade(row: dict) -> str:
    """A = has mission + baseLocations + tags; B = missing one; C = minimal."""
    has_mission = bool((row.get("mission") or "").strip())
    has_locations = bool((row.get("baseLocations") or "").strip())
    has_tags = bool((row.get("tags") or "").strip())
    n = sum([has_mission, has_locations, has_tags])
    if n >= 3:
        return "A"
    if n >= 2:
        return "B"
    return "C"


def heuristic_score(row: dict) -> Score:
    tags = _tag_set(row)
    text = _text(row, "mission", "name", "baseLocations")
    s = Score()
    if "geographic" in tags or "charter" in tags or "city" in tags:
        s.territory_density = 2
    if "pop-up" in tags or "popup" in tags or "events" in tags or "hybrid" in tags:
        s.territory_density = max(s.territory_density, 1)
    if "virtual" in tags and s.territory_density == 0:
        s.territory_density = 0
    if any(x in text for x in ("physical", "land", "island", "city", "charter")):
        s.territory_density = max(s.territory_density, 1)
    if "charter" in tags or "legal" in text or "governance" in text:
        s.legitimacy_path = min(2, s.legitimacy_path + 1)
    if "compliance" in text or "credible" in text:
        s.legitimacy_path = max(s.legitimacy_path, 1)
    if any(x in text for x in ("econom", "revenue", "invest", "job", "business", "crypto", "token")):
        s.economic_engine = max(s.economic_engine, 1)
    if "investment" in text or "revenue" in text:
        s.economic_engine = max(s.economic_engine, 2)
    if "privacy" in tags or "identity" in tags or "zk" in tags:
        s.dacc_alignment = 2
        s.identity_credentials = 2
    if "identity" in text or "credential" in text or "passport" in text:
        s.identity_credentials = max(s.identity_credentials, 1)
    if "decentral" in text or "resilience" in text:
        s.dacc_alignment = max(s.dacc_alignment, 1)
    if "governance" in text or "voting" in text or "decision" in text:
        s.governance_security = max(s.governance_security, 1)
    if "dispute" in text or "safety" in text:
        s.governance_security = max(s.governance_security, 1)
    has_discord = bool((row.get("discord") or "").strip())
    has_app = bool((row.get("application") or "").strip())
    if has_discord and has_app:
        s.execution_capacity = 2
    elif has_discord or has_app:
        s.execution_capacity = 1
    if "diaspora" in tags or "migration" in tags:
        s.venezuela_similarity = 2
    elif "latin" in text or "venezuela" in text or "colombia" in text or "latam" in text:
        s.venezuela_similarity = 2
    elif "remittance" in text or "migration" in text:
        s.venezuela_similarity = 1
    loc = _normalize(row.get("baseLocations") or "")
    if any(c in loc for c in ("venezuela", "colombia", "panama", "ecuador", "peru", "chile", "argentina", "mexico", "brazil", "latin", "latam", "caribbean")):
        s.venezuela_similarity = max(s.venezuela_similarity, 1)
    return s


def load_overrides() -> Dict[str, dict]:
    if not OVERRIDES_PATH.exists() or yaml is None:
        return {}
    with open(OVERRIDES_PATH, encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    overrides_list = data.get("overrides") or []
    return {o["society_id"]: o for o in overrides_list if o.get("society_id")}


def apply_override(score: Score, row: dict, overrides: Dict[str, dict]) -> tuple:
    sid = (row.get("id") or "").strip()
    conf = confidence_grade(row)
    if sid in overrides:
        o = overrides[sid]
        if o.get("confidence_override"):
            conf = o["confidence_override"]
        for key, val in (o.get("manual_score_overrides") or {}).items():
            if hasattr(score, key):
                setattr(score, key, int(val))
    return score, conf


def _infer_type(row: dict) -> str:
    tags = _tag_set(row)
    if "geographic" in tags or "charter" in tags:
        return "geographic"
    if "virtual" in tags:
        return "virtual"
    if "hybrid" in tags:
        return "hybrid"
    if "pop-up" in tags or "popup" in tags or "events" in tags:
        return "pop-up"
    return "other"


def load_rows(path: str) -> list:
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(r)
    return rows


def main(csv_path: str) -> list:
    rows = load_rows(csv_path)
    overrides = load_overrides()
    scored = []
    for r in rows:
        s = heuristic_score(r)
        s, conf = apply_override(s, r, overrides)
        name = r.get("name") or r.get("Name") or "?"
        sid = r.get("id") or "?"
        scored.append((s.total(), name, sid, s, r, conf))
    scored.sort(reverse=True, key=lambda x: (x[0], x[1]))
    return scored


def write_outputs(scored: list) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    with open(OUT_DIR / "top_success.md", "w") as f:
        f.write("# Top success (heuristic + confidence)\n\n")
        f.write("Ranked by composite score. Confidence: A = complete data, B = missing one field, C = minimal.\n\n")
        for total, name, sid, s, _, conf in scored[:30]:
            f.write(f"- **{total}** [{conf}] {name} — territory={s.territory_density} exec={s.execution_capacity} economic={s.economic_engine} gov={s.governance_security} id={s.identity_credentials} dacc={s.dacc_alignment} legit={s.legitimacy_path}\n")

    v = [(t, n, sid, sc, row, conf) for t, n, sid, sc, row, conf in scored if sc.venezuela_similarity > 0]
    v.sort(reverse=True, key=lambda x: (x[3].venezuela_similarity, x[0]))
    with open(OUT_DIR / "top_venezuela_fit.md", "w") as f:
        f.write("# Top Venezuela fit (diaspora / Latam / migration signals)\n\n")
        for total, name, _, s, r, conf in v[:30]:
            loc = (r.get("baseLocations") or "").strip() or "—"
            f.write(f"- **{total}** [{conf}] {name} (venezuela_similarity={s.venezuela_similarity}) — {loc}\n")

    by_type = defaultdict(list)
    for _, name, _, _, r, _ in scored:
        t = _infer_type(r)
        by_type[t].append(name)
    with open(OUT_DIR / "clusters.md", "w") as f:
        f.write("# Clusters (by inferred type from tags)\n\n")
        for typ in ("geographic", "virtual", "hybrid", "pop-up", "other"):
            names = by_type.get(typ, [])
            f.write(f"## {typ}\n\n")
            for n in names[:50]:
                f.write(f"- {n}\n")
            if len(names) > 50:
                f.write(f"- ... and {len(names) - 50} more\n")
            f.write("\n")

    with open(OUT_DIR / "white_spaces.md", "w") as f:
        f.write("# White spaces\n\n")
        f.write("Gaps and opportunities from clustering and scoring.\n\n")
        f.write("- **High execution, low territory:** societies with discord/application but virtual-only — potential for hybrid or pop-up.\n")
        f.write("- **Venezuela fit (diaspora/Latam):** see top_venezuela_fit.md for diaspora-fit candidates.\n")
        f.write("- **High territory, low economic:** geographic/charter societies with weak economic signals — opportunity for economic playbook.\n")
        f.write("- **Manual overrides:** edit network-states/overrides/manual_tags.yml and re-run to apply.\n")

    # Confidence summary
    with open(OUT_DIR / "confidence_summary.md", "w") as f:
        f.write("# Confidence grades (data completeness)\n\n")
        a = sum(1 for _, _, _, _, _, c in scored if c == "A")
        b = sum(1 for _, _, _, _, _, c in scored if c == "B")
        c = sum(1 for _, _, _, _, _, c in scored if c == "C")
        f.write(f"- A (mission + baseLocations + tags): {a}\n")
        f.write(f"- B (missing one): {b}\n")
        f.write(f"- C (minimal): {c}\n")


if __name__ == "__main__":
    csv_path = sys.argv[1] if len(sys.argv) > 1 else str(DEFAULT_CSV)
    if not csv_path or not Path(csv_path).exists():
        print("Usage: python ns_ingest_score.py [PATH_TO/societies.csv]", file=sys.stderr)
        print(f"Default: {DEFAULT_CSV}", file=sys.stderr)
        sys.exit(1)

    scored = main(csv_path)
    print("Top 25 (total, name, confidence, score):")
    for total, name, _, s, _, conf in scored[:25]:
        print(total, f"[{conf}]", name, s)

    write_outputs(scored)
    print(f"\nWrote: {OUT_DIR}/top_success.md, top_venezuela_fit.md, clusters.md, white_spaces.md, confidence_summary.md")
