# Canonical repo structure — AylluOS

**Purpose:** Standard folders and rules for the AylluOS mono-repo. Use when adding new content or onboarding.

---

## Canonical folders

| Folder | Purpose |
|--------|---------|
| `apps/` | Next.js deployables (e.g. venezuela, console) |
| `packages/` | Shared libs |
| `countries/` | Country-specific configs + corpora |
| `scripts/` | Clone refs, import docs, generators, checks |
| `references/` | Cloned upstream repos (via `scripts/clone_references.sh`) |
| `inbox/external_docs/` | External docs staging (import before use) |
| `ops/` | Orchestration, guardrails, readiness, debugging |
| `docs/` | Human documentation |

**Current mapping:** `venezuela/` is the first country; `ayllu/` holds state OS primitives; `network-states/` and `civic-houses/` are domain-specific. `apps/` and `packages/` are placeholders for future deployables.

---

## Path rules

- **No absolute paths** — Never write or reference `/Users/…` in code, scripts, docs, or patches. All outputs must be repo-relative.
- **Pre-commit check:** Run `scripts/check_no_absolute_paths.sh` before committing. Fails if staged diff contains `/Users/`.
- **External docs:** Import to `inbox/external_docs/` first via `scripts/import_external_docs.sh`; operate only on on the in-repo copy.

---

## External docs import policy

1. If an input doc exists outside repo (Desktop, Downloads, etc.), copy it into `inbox/external_docs/<original_filename>`.
2. Do not reference or operate on the external path. Use only the in-repo copy.
3. See `scripts/import_external_docs.sh` for importing.

---

## Repo rename (ayllu → AylluOS)

Do not rename on GitHub until approved. See `ops/RENAME_TO_AYLLUOS.md` for the checklist. Internal docs may refer to "AylluOS" conceptually; URLs remain until rename is executed.
