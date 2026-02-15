#!/usr/bin/env python3
"""
Score Network States societies (heuristic bootstrap). Human-in-the-loop.
Usage: python score_network_states.py PATH_TO/societies.csv
Outputs to stdout; optionally write network-states/outputs/ from caller.
"""
import csv
import sys
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


def heuristic_score(row: dict) -> Score:
    tags = (row.get("tags") or "").lower()
    s = Score()

    if "geographic" in tags or "charter" in tags or "city" in tags:
        s.territory_density = 2
    if "pop-up" in tags or "popup" in tags or "events" in tags:
        s.territory_density = max(s.territory_density, 1)

    if "privacy" in tags or "identity" in tags or "zk" in tags:
        s.dacc_alignment = 2
        s.identity_credentials = 2

    if row.get("discord") or row.get("application"):
        s.execution_capacity = 1

    if "diaspora" in tags or "migration" in tags:
        s.venezuela_similarity = 1

    return s


def load_rows(path: str) -> list[dict]:
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(r)
    return rows


def main(path: str, out_dir: Optional[str] = None) -> list:
    rows = load_rows(path)
    scored = []
    for r in rows:
        s = heuristic_score(r)
        scored.append((s.total(), r.get("name") or r.get("Name") or "?", s, r))
    scored.sort(reverse=True, key=lambda x: x[0])
    return scored


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
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "top_success_like.md", "w") as f:
        f.write("# Top success-like (heuristic)\n\n")
        for total, name, s, r in scored[:25]:
            f.write(f"- {total} **{name}** — {s}\n")
    with open(out_dir / "top_venezuela_similar.md", "w") as f:
        v = [(t, n, sc, row) for t, n, sc, row in scored if sc.venezuela_similarity > 0]
        v.sort(reverse=True, key=lambda x: (x[2].venezuela_similarity, x[0]))
        f.write("# Top Venezuela-similar (diaspora/migration signals)\n\n")
        for total, name, s, _ in v[:25]:
            f.write(f"- {total} **{name}** (venezuela_similarity={s.venezuela_similarity})\n")
    with open(out_dir / "clusters.md", "w") as f:
        f.write("# Clusters (by type / economic / identity / territory)\n\n")
        f.write("Cluster by: type (virtual/hybrid/geographic/pop-up), economic model, identity rails, territory strategy.\n")
        f.write("(Populate after manual tagging or enriched schema.)\n")
    with open(out_dir / "white_spaces.md", "w") as f:
        f.write("# White spaces\n\n")
        f.write("Gaps and opportunities identified from clustering and scoring.\n")
        f.write("(Populate after analysis.)\n")
