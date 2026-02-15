# Skill: guardrails-linter

Check markdown and docs for disallowed phrasing and safe terminology; produce pass/fail and local_audit entry if redaction applied.

## Inputs

- Files to check: markdown/docs under repo (e.g. docs/, ayllu/, venezuela/, civic-houses/)
- `ops/GUARDRAILS.md` (rules: disallowed phrasing, safe terminology, privacy red lines)

## Outputs

- Pass/fail report (stdout or file)
- If redaction applied: entry in `local_audit/guardrail_redactions.md` (local-only; not committed). Format per docs/local_audit_redaction_format.md.

## Steps

1. Read GUARDRAILS.md for disallowed patterns and safe terms.
2. Scan target files for disallowed phrasing (e.g. “represent”, “we represent Venezuela”, “government in exile” as claim).
3. Report matches with file path and line/snippet.
4. If human or agent performs redaction: append to local_audit/guardrail_redactions.md with date, file, before/after, rule, reasoning, who, commit/PR.

## Commands

- No dedicated script yet. Manual: grep -r "represent" --include="*.md" .; review against GUARDRAILS.
- Future: `python scripts/guardrails_lint.py [paths]` writing to local_audit when redaction logged.

## Quality checklist

- [ ] All disallowed patterns from GUARDRAILS checked.
- [ ] Redaction log format matches docs/local_audit_redaction_format.md.
- [ ] local_audit/ never committed (.gitignore).

## Failure modes

- False positives: tighten patterns (e.g. “no representation claims” as allowed phrase in meta-docs).
- Missing GUARDRAILS: ensure ops/GUARDRAILS.md exists and is read first.
