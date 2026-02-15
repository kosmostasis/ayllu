#!/usr/bin/env python3
"""
Lightweight guardrails check: scan markdown/docs for disallowed phrasing (ops/GUARDRAILS.md).
Exits 0 if clean, 1 if any match. Use in CI or pre-commit. Redactions belong in local_audit only.
"""
import re
import sys
from pathlib import Path
from typing import List, Tuple

# High-signal disallowed patterns (from GUARDRAILS). Allowlisted phrases are excluded after match.
DISALLOWED = [
    (r"\bwe\s+represent\s+(?:Venezuela|the\s+Venezuelan)", "representation claim"),
    (r"representative\s+of\s+the\s+Venezuelan\s+people", "representation claim"),
    (r"government\s+in\s+exile", "sovereign/diplomatic language"),
    (r"\bin\s+the\s+name\s+of\s+(?:Venezuela|the\s+Venezuelan)", "representation claim"),
]
# Allowed: "no representation claims" etc. — do not flag lines that are meta (e.g. "avoid representation claims")
ALLOWLIST = re.compile(r"no\s+representation\s+claims|avoid.*representation|disallowed.*representation", re.I)


def check_file(path: Path) -> List[Tuple[int, str, str]]:
    hits = []
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return []
    for i, line in enumerate(text.splitlines(), 1):
        if ALLOWLIST.search(line):
            continue
        for pat, label in DISALLOWED:
            if re.search(pat, line, re.I):
                hits.append((i, line.strip()[:80], label))
                break
    return hits


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    paths = sys.argv[1:] if len(sys.argv) > 1 else ["."]
    # Meta-docs that quote disallowed phrases by design (do not scan)
    exclude_rel = {"ops/GUARDRAILS.md", "docs/local_audit_redaction_format.md", "skills/guardrails-linter/SKILL.md"}
    to_scan = []
    for p in paths:
        path = (repo_root / p).resolve()
        if path.is_file():
            if path.suffix.lower() in (".md", ".mdx", ".txt") and "local_audit" not in path.parts:
                try:
                    if str(path.relative_to(repo_root)) in exclude_rel:
                        continue
                except ValueError:
                    pass
                to_scan.append(path)
        elif path.is_dir():
            for f in path.rglob("*"):
                if f.suffix.lower() not in (".md", ".mdx", ".txt") or "local_audit" in f.parts or ".git" in f.parts:
                    continue
                try:
                    if str(f.relative_to(repo_root)) in exclude_rel:
                        continue
                except ValueError:
                    pass
                to_scan.append(f)
    total = 0
    for f in sorted(set(to_scan)):
        try:
            rel = f.relative_to(repo_root)
        except ValueError:
            rel = f
        hits = check_file(f)
        for line_no, snippet, label in hits:
            print(f"{rel}:{line_no}: [{label}] {snippet}")
            total += 1
    if total:
        print(f"\nGuardrails: {total} potential violation(s). See ops/GUARDRAILS.md. Log redactions in local_audit/ only.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
