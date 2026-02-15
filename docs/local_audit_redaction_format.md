# Local audit — guardrail redaction log format

The folder `local_audit/` and its contents are **local-only** and must not be committed (see `.gitignore`). Use it to record every guardrail intervention (redaction or edit triggered by [ops/GUARDRAILS.md](../ops/GUARDRAILS.md)).

## Required format for `local_audit/guardrail_redactions.md`

For every intervention, add an entry with:

- **Date/time** (ISO or unambiguous)
- **File path** (relative to repo root)
- **Exact excerpt before** (short; 1–2 lines)
- **Exact excerpt after** (short; 1–2 lines)
- **Rule triggered** (reference to GUARDRAILS.md, e.g. “Disallowed phrasing: representation”)
- **Reasoning** (one line)
- **Who performed** (agent name or “human”)
- **Link to PR or commit hash** (if the change was committed)

## Example

```markdown
### 2025-02-15T14:00Z
- **File:** docs/some_doc.md
- **Before:** We represent the Venezuelan diaspora.
- **After:** This project supports diaspora civic infrastructure for Venezuelans and allies.
- **Rule:** Disallowed phrasing — representation claims
- **Reasoning:** Avoid any claim of representation.
- **Who:** human
- **Commit:** abc1234
```

## Attachments

Optional: store diffs or screenshots in `local_audit/guardrail_redactions/` (also local-only). Reference them from the main log by filename.
