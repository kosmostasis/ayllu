# AylluOS Venezuela MVP — Readiness checklist

**Purpose:** Launch gates vs nice-to-haves; who can mark passed; evidence paths.

---

## 1. Checklist items: launch gates vs nice-to-haves

| Gate | Type | Description |
|------|------|-------------|
| **CRC drives behavior** | Launch gate | `ayllu/runtime/venezuela.yml` must drive product (enabled modules, IA, feature flags). Today: **static only** — no code loads it. |
| **Compendium + diff_map filled** | Launch gate | `venezuela/spec/plan-pais_compendium.md` and `venezuela/sources/diff_map.md` must meet minimum content threshold for non-empty UX. Today: **placeholders only**. |
| **Guardrails in CI** | Launch gate | `scripts/guardrails_lint.py` must run in CI; disallowed phrasing blocked from merge. Today: **not in CI**. |
| **Trust/safety for contributions** | Launch gate | Rate limits, moderation path, reporting, guardrails in UI copy. Today: **spec only** (ops docs); no app implementation. |
| **Schema validation** | Nice-to-have | Taxonomy + CRC schema validation before use. |
| **Vercel rollback** | Nice-to-have | Documented rollback for deployment. Today: **no Vercel config**. |
| **Civic House pilot** | Nice-to-have | One city pilot (lead, venue, service). Enables credentialing feedback. |

---

## 2. Does `ayllu/runtime/venezuela.yml` drive product behavior?

**No.** It is **static config only**. No code path loads it.

**Evidence:** Grep for `venezuela.yml`, `load.*yaml`, `runtime.*config`, `country.*yml` in `*.py`, `*.js`, `*.ts`, `*.tsx`, `*.jsx` returns **no matches**.

**References:** Docs describe it as the "engineering target" for "load CRC and drive behavior" (EXECUTIVE_SUMMARY.md, EXECUTIVE_SUMMARY_FOR_LEADERSHIP.md), but no implementation exists. The CRC is used by:
- `skills/country-runtime-generator/SKILL.md` (agent instructions)
- `ayllu/spec/COUNTRY_RUNTIME_SPEC.md` (spec)
- `ops/STATUS.md` (task tracking)

**Code path:** None. To drive behavior, a future app would need to:
1. Load `ayllu/runtime/venezuela.yml` (e.g. via `yaml.safe_load` or equivalent)
2. Read `modules.theme_priority`, `modules.optional`, `constraints.*`
3. Render navigation/IA from `theme_priority`; gate features from `optional`; apply `constraints` to copy/UX

---

## 2b. Demo path (if CRC drove behavior)

**N/A** — CRC does not drive behavior today. A demo would require:
1. Implement a loader (e.g. `scripts/load_crc.py` or app bootstrap)
2. Edit `venezuela.yml` (e.g. change `theme_priority` to `[justice, social]`)
3. Run app; verify Areas/navigation reflect new order

---

## 3. Minimum filled-content threshold for compendium + diff_map

**Current state:**
- `venezuela/spec/plan-pais_compendium.md`: 9 mesas, all with placeholders (`*(Extract from PDF.)*`, `*(Bullet points.)*`). Annex "What's missing" has structure but no filled content.
- `venezuela/sources/diff_map.md`: Tables present; cells are placeholders (`*(e.g. ...)*`).

**Proposed numeric definition for non-empty UX:**

| Artifact | Minimum threshold |
|----------|-------------------|
| **plan-pais_compendium.md** | **Top 6 mesas** with: (a) Executive summary filled (≥2 sentences each), (b) Key policies filled (≥3 bullets each). Mesas 1–6 = Administración Pública, Discapacidad, Economía y Energía, Medios, Política Social, RRII. |
| **diff_map.md** | **3 sections** with at least 50% of cells filled: Tone and framing, Sequencing (100h/100d), and one of Institutional reforms or Economic program. Summary paragraph filled. |

**Rationale:** 6 mesas cover core policy areas; diff_map gives Plan País vs MCM context. Below this, UX would show empty cards or "Coming soon" everywhere.

---

## 4. MVP trust/safety controls for user contributions

| Control | Exists? | Evidence |
|---------|---------|----------|
| **Rate limits** | No | No app code; no API. |
| **Moderation** | Spec only | `civic-houses/ops/safety_and_conduct.md`, `venezuela/civic-houses/starter-kit/safety_and_conduct.md` — "Designate contact for reporting; act on reports." No implementation. |
| **Reporting path** | Spec only | MOBILE_PRINCIPLES: "Dispute / report path for corrections." Ops docs: reporting contact. No UI or backend. |
| **Guardrails in UI copy** | Partial | `ops/GUARDRAILS.md` + `scripts/guardrails_lint.py` scan **committed docs** only. No runtime check on user-submitted content. |
| **Data minimization** | Spec only | GUARDRAILS, credentialing_v0. No app handling user data. |

**Missing for MVP:**
- Runtime guardrails on contribution text (block disallowed phrasing before save)
- Rate limiting on contribution endpoints
- Moderation queue or triage path
- "Report" button and backend handler

---

## 5. CI/CD gates and rollback

| Gate | Exists? | Evidence |
|------|---------|----------|
| **Schema validation** | No | No CI workflow; no schema validation step. |
| **Guardrails lint** | No (script exists, not in CI) | `scripts/guardrails_lint.py` — run manually. No `.github/workflows/`. |
| **Tests** | No | No `pytest`, `jest`, or test runner config found. |
| **Vercel deployment** | No | No `vercel.json`, no Vercel config. No `package.json` (no frontend app). |
| **Rollback story** | N/A | No deployment pipeline. |

**Rollback:** When Vercel is introduced, standard approach: redeploy previous commit via Vercel dashboard or `vercel rollback`; no custom rollback documented today.

---

## 6. Explicit MVP non-goals (confirmed)

| Non-goal | Source |
|----------|--------|
| **Credential issuance** | `civic-houses/spec/credentialing_v0.md`: "protocol boundary"; "Out of scope: Specific technical implementation... Issuer infrastructure or tooling." EXECUTIVE_SUMMARY_FOR_LEADERSHIP: "no implementation... until at least one pilot." |
| **Fund custody** | `civic-houses/ops/financial_controls.md`: node funds separate from personal; transparency. No custody product; nodes manage their own. |
| **Public corpus library** | Corpus in `venezuela/corpus/`; `references/` cloned locally, gitignored. No public-facing corpus browse/search. |
| **VC format / ledger / ZK** | credentialing_v0: "Out of scope (for later)". |

---

## Output tables

### Gate / Status / Owner / Evidence

| Gate | Status | Owner | Evidence |
|------|--------|-------|----------|
| CRC drives behavior | ❌ Not met | OS Architect / Lead Eng | No code path; `grep` empty for venezuela.yml load |
| Compendium filled (6 mesas) | ❌ Not met | WS1 Corpus | `venezuela/spec/plan-pais_compendium.md` — placeholders |
| Diff_map filled (3 sections) | ❌ Not met | WS1 Corpus | `venezuela/sources/diff_map.md` — placeholders |
| Guardrails in CI | ❌ Not met | Ops / Lead Eng | No `.github/workflows/`; `scripts/guardrails_lint.py` manual only |
| Trust/safety (rate limit, moderation, report) | ❌ Not met | WS5 / Lead Eng | Spec in ops; no app |
| Schema validation | ❌ Not met | OS Architect | No CI step |
| Vercel rollback documented | N/A | Ops | No Vercel config |

### Top 5 blockers

1. **CRC not wired** — venezuela.yml is static; no product reads it. Must implement loader and wire to IA/navigation/feature flags.
2. **Compendium + diff_map empty** — UX would show empty content. Need ≥6 mesas + 3 diff_map sections filled.
3. **No CI** — No guardrails lint, schema validation, or tests in pipeline. Disallowed phrasing can land in repo.
4. **No trust/safety in app** — Contributions (when implemented) have no rate limits, moderation, or reporting. Guardrails apply to docs only.
5. **No deployment pipeline** — No Vercel/frontend; no rollback story. MVP assumes some deploy path.

### Who can mark each gate "passed"

| Gate | Who can mark passed |
|------|---------------------|
| CRC drives behavior | OS Architect or Lead Engineering (after loader + wiring) |
| Compendium filled | WS1 Corpus Agent or product (after content meets threshold) |
| Diff_map filled | WS1 Corpus Agent or product |
| Guardrails in CI | Ops or Lead Engineering (after adding workflow) |
| Trust/safety | WS5 UI/UX or Lead Engineering (after implementation) |
| Schema validation | OS Architect |
| Vercel rollback | Ops (when deployment exists) |
