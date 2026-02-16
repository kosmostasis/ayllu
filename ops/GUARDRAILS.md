# Guardrails — wording and privacy

Tracked in repo. Any automated or manual guardrail edit must be logged in **local-only** `local_audit/guardrail_redactions.md` (see [../docs/local_audit_redaction_format.md](../docs/local_audit_redaction_format.md)). Do not commit `local_audit/`.

**Path conventions (hard rules):**

- **B1) Absolute paths forbidden** — Never write or reference `/Users/…` paths in patches, scripts, docs, or configs. All outputs must be repo-relative.
- **B2) External docs** — If an input doc exists outside repo (Desktop/Downloads/etc.), copy it into `inbox/external_docs/<original_filename>` first. Only operate on the in-repo copy. See `scripts/import_external_docs.sh`.
- **B3) Standard locations** — `scripts/`, `inbox/external_docs/`, `references/`, `ops/`, `docs/`, `apps/`, `packages/`, `countries/`.
- **Pre-commit check:** Run `scripts/check_no_absolute_paths.sh` before committing. Fails if staged diff contains `/Users/`.

---

## Disallowed phrasing

- Any claim of **representation** (e.g. “we represent Venezuela”, “representative of the Venezuelan people”, “in the name of”).
- Language implying **sovereign or diplomatic status** (e.g. “embassy” in the sense of state representation; “government in exile” as if we were that entity).
- **Guarantees or commitments** we cannot keep (e.g. legal advice, immigration outcomes).

---

## Safe terminology (prefer)

- **Civic House** — node in diaspora civic infrastructure.
- **Diaspora civic infrastructure** — services, credentials, coordination; complementary to host-state structures.
- **Complementary services** / **complementary posture** — we complement; we do not replace or represent.
- **Host-nation compliant** — operations respect host-country law and norms.
- **No representation claims** — explicit constraint in all public-facing positioning.

---

## Privacy red lines

- **No sensitive personal data** (e.g. IDs, health, finances, location detail) in repo or docs without an explicit **data policy** and **minimization** (collect only what is necessary).
- Credentialing and contributions ledger: define **issuer, revocation, dispute, retention** in spec before handling personal data.
- When in doubt: do not commit personal data; document in local_audit if redaction was applied.
