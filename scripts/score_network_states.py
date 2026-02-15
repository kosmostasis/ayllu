#!/usr/bin/env python3
"""
Score Network States societies (heuristic bootstrap). Human-in-the-loop.
Uses: id, name, mission, baseLocations, discord, application, tags.
Usage: python score_network_states.py PATH_TO/societies.csv
Writes network-states/outputs/: top_success_like.md, top_venezuela_similar.md, clusters.md, white_spaces.md.
"""
import csv
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


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


def heuristic_score(row: dict) -> Score:
    tags = _tag_set(row)
    text = _text(row, "mission", "name", "baseLocations")
    s = Score()

    # Territory: tags
    if "geographic" in tags or "charter" in tags or "city" in tags:
        s.territory_density = 2
    if "pop-up" in tags or "popup" in tags or "events" in tags or "hybrid" in tags:
        s.territory_density = max(s.territory_density, 1)
    if "virtual" in tags and s.territory_density == 0:
        s.territory_density = 0  # explicit virtual

    # Territory: mission/location mentions
    if any(x in text for x in ("physical", "land", "island", "city", "charter")):
        s.territory_density = max(s.territory_density, 1)

    # Legitimacy: charter, governance, legal
    if "charter" in tags or "legal" in text or "governance" in text:
        s.legitimacy_path = min(2, s.legitimacy_path + 1)
    if "compliance" in text or "credible" in text:
        s.legitimacy_path = max(s.legitimacy_path, 1)

    # Economic: mission
    if any(x in text for x in ("econom", "revenue", "invest", "job", "business", "crypto", "token")):
        s.economic_engine = max(s.economic_engine, 1)
    if "investment" in text or "revenue" in text:
        s.economic_engine = max(s.economic_engine, 2)

    # Identity / DACC: tags and mission
    if "privacy" in tags or "identity" in tags or "zk" in tags:
        s.dacc_alignment = 2
        s.identity_credentials = 2
    if "identity" in text or "credential" in text or "passport" in text:
        s.identity_credentials = max(s.identity_credentials, 1)
    if "decentral" in text or "resilience" in text:
        s.dacc_alignment = max(s.dacc_alignment, 1)

    # Governance / security: mission
    if "governance" in text or "voting" in text or "decision" in text:
        s.governance_security = max(s.governance_security, 1)
    if "dispute" in text or "safety" in text:
        s.governance_security = max(s.governance_security, 1)

    # Execution: has links
    has_discord = bool((row.get("discord") or "").strip())
    has_app = bool((row.get("application") or "").strip())
    if has_discord and has_app:
        s.execution_capacity = 2
    elif has_discord or has_app:
        s.execution_capacity = 1

    # Venezuela / diaspora similarity: tags + baseLocations
    if "diaspora" in tags or "migration" in tags:
        s.venezuela_similarity = 2
    elif "latin" in text or "venezuela" in text or "colombia" in text or "latam" in text:
        s.venezuela_similarity = 2
    elif "remittance" in text or "migration" in text:
        s.venezuela_similarity = 1
    # baseLocations often has country names
    loc = _normalize(row.get("baseLocations") or "")
    if any(c in loc for c in ("venezuela", "colombia", "panama", "ecuador", "peru", "chile", "argentina", "mexico", "brazil", "latin", "latam", "caribbean")):
        s.venezuela_similarity = max(s.venezuela_similarity, 1)

    return s


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


def main(path: str, out_dir_arg: Optional[str] = None) -> list:
    rows = load_rows(path)
    scored = []
    for r in rows:
        s = heuristic_score(r)
        name = r.get("name") or r.get("Name") or "?"
        scored.append((s.total(), name, s, r))
    scored.sort(reverse=True, key=lambda x: (x[0], x[1]))
    return scored


def write_outputs(scored: list, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)

    with open(out_dir / "top_success_like.md", "w") as f:
        f.write("# Top success-like (heuristic)\n\n")
        f.write("Ranked by composite score (territory + execution + economic + governance + identity/DACC + legitimacy).\n\n")
        for total, name, s, _ in scored[:30]:
            f.write(f"- **{total}** {name} — territory={s.territory_density} exec={s.execution_capacity} economic={s.economic_engine} gov={s.governance_security} id={s.identity_credentials} dacc={s.dacc_alignment} legit={s.legitimacy_path}\n")

    v = [(t, n, sc, row) for t, n, sc, row in scored if sc.venezuela_similarity > 0]
    v.sort(reverse=True, key=lambda x: (x[2].venezuela_similarity, x[0]))
    with open(out_dir / "top_venezuela_similar.md", "w") as f:
        f.write("# Top Venezuela-similar (diaspora / Latam / migration signals)\n\n")
        for total, name, s, r in v[:30]:
            loc = (r.get("baseLocations") or "").strip() or "—"
            f.write(f"- **{total}** {name} (venezuela_similarity={s.venezuela_similarity}) — {loc}\n")

    # Clusters by inferred type
    by_type = defaultdict(list)
    for _, name, s, r in scored:
        t = _infer_type(r)
        by_type[t].append(name)
    with open(out_dir / "clusters.md", "w") as f:
        f.write("# Clusters (by inferred type from tags)\n\n")
        for typ in ("geographic", "virtual", "hybrid", "pop-up", "other"):
            names = by_type.get(typ, [])
            f.write(f"## {typ}\n\n")
            for n in names[:50]:
                f.write(f"- {n}\n")
            if len(names) > 50:
                f.write(f"- ... and {len(names) - 50} more\n")
            f.write("\n")

    with open(out_dir / "white_spaces.md", "w") as f:
        f.write("# White spaces\n\n")
        f.write("Gaps and opportunities from clustering and scoring.\n\n")
        f.write("- **High execution, low territory:** societies with discord/application but virtual-only — potential for hybrid or pop-up.\n")
        f.write("- **Venezuela-similar (diaspora/Latam):** see top_venezuela_similar.md for diaspora-fit candidates.\n")
        f.write("- **High territory, low economic:** geographic/charter societies with weak economic signals — opportunity for economic playbook.\n")
        f.write("- **Manual tagging:** add columns or tags for economic model, identity rails, territory strategy to refine clusters.\n")


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else ""
    if not path or not Path(path).exists():
        print("Usage: python score_network_states.py PATH_TO/societies.csv", file=sys.stderr)
        sys.exit(1)

    scored = main(path)
    print("Top 25 (total, name, score):")
    for total, name, s, _ in scored[:25]:
        print(total, name, s)

    out_dir = Path(__file__).resolve().parent.parent / "network-states" / "outputs"
    write_outputs(scored, out_dir)
    print(f"\nWrote: {out_dir}/top_success_like.md, top_venezuela_similar.md, clusters.md, white_spaces.md")
