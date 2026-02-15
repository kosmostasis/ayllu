# AylluOS — Executive Summary for Leadership Review

**Audience:** Koss, Lead Engineering  
**Purpose:** Single exportable brief on current state, next steps, and recommendations. Use for prioritization and resource decisions.  
**Status:** For review; do not treat as implementation checklist until approved.

---

## 1. Current state (what’s in place)

The **ayllu** mono-repo implements the AylluOS Cursor Recommendations playbook (Option A). Six main areas:

| Area | Contents |
|------|----------|
| **ayllu/** | State OS: taxonomy (COFOG, ministry_crosswalk), modules (core, meta_capabilities CANON, weird_revealing), practices (6 standards), schemas, templates. **spec/** (COUNTRY_RUNTIME_SPEC), **runtime/** (country.template.yml, venezuela.yml as first “live” CRC with theme_priority). |
| **venezuela/** | **sources/** (INDEX + hashes), **corpus/** (plan-pais, mcm with INDEX + provenance), **spec/** (plan-pais_compendium canonical + “what’s missing” annex, diff_map), **blueprint/**, **civic-houses/starter-kit/**. |
| **network-states/** | **rubric/** (rubric.yml v0.2), **out/** canonical (top_success, top_venezuela_fit, clusters, white_spaces, confidence_summary A/B/C), **overrides/** (manual_tags.yml). Legacy outputs/ deprecated. |
| **civic-houses/** | **templates/**, **ops/**, **spec/credentialing_v0.md** (protocol boundary), **kits/** (e.g. Miami-USA). Kit generator in scripts. |
| **ops/** | STATUS.md (per-agent), ORCHESTRATION.md (worktrees, roles), GUARDRAILS.md (disallowed phrasing, safe terms, privacy). Redaction format in docs; local_audit/ gitignored. |
| **Scripts, references, skills** | download_corpus.sh, ns_ingest_score.py (canonical NS), generate_civic_house_kit.py, guardrails_lint.py, clone_references.sh. references/README committed; cloned repos gitignored. Eight Cursor Skills under skills/. |

**Design constants:** COFOG taxonomy; “no representation claims”; complementary to host-state. **Canon:** Ministry of State Capacity (Systems & Delivery); Ministry of Future, Risk & Civilizational R&D.

---

## 2. Recommended next steps (for leadership to assign)

| Order | Area | Action | Owner |
|-------|------|--------|--------|
| 1 | Ops | Keep STATUS.md updated: last shipped = playbook; next 3 tasks reflect current repo. | Orchestrator |
| 2 | Content | **Fill compendium and diff_map** from Venezuela corpus (PDF extraction or manual). Unlocks product/policy use of Plan País vs MCM and “what’s missing vs AylluOS.” | WS1 / product |
| 3 | AylluOS | **Schema validation** (and optional CLI/API) for taxonomy and CRC so runtime configs and modules can be validated before use. | OS Architect |
| 4 | Civic House | **Pilot one city** (e.g. Miami-USA): one lead, one venue, one concrete service; report into metrics/ops. | WS3 / ops |
| 5 | NS dashboard | Use **top_venezuela_fit** and **white_spaces** in product/strategy (diaspora fit, comparables). Consider running **guardrails_lint** in CI or pre-commit. | WS2 / product |

---

## 3. Suggestions (from Ayni)

These are recommendations for Koss and Lead Engineering to accept, reject, or adapt. **Do not implement** until leadership has reviewed.

### 3.1 Single source of truth for NS outputs

**Suggestion:** Treat **network-states/out/** as the only canonical location for NS dashboard outputs. All scripts (including any legacy use of score_network_states.py) should write there. **network-states/outputs/** should remain deprecated (README only); no new outputs under outputs/.

**Rationale:** Avoids confusion between top_success_like vs top_success, top_venezuela_similar vs top_venezuela_fit, and ensures confidence grades live in one place.

---

### 3.2 One compendium location

**Suggestion:** Treat **venezuela/spec/plan-pais_compendium.md** as the single canonical compendium. Any edits (filling executive summaries, key policies, “what’s missing” annex) happen only there. **venezuela/sources/** keeps a stub or link to the spec file so there is no duplicate to maintain.

**Rationale:** One file to update when content is filled; spec is the right home for “what’s missing relative to AylluOS.”

---

### 3.3 Guardrails in CI

**Suggestion:** Add a **guardrails check** to CI or pre-commit (e.g. run `scripts/guardrails_lint.py`) that fails if disallowed phrasing (see ops/GUARDRAILS.md) appears in committed docs. Redactions and reasoning stay in **local_audit/** only (not committed); the check only prevents disallowed phrasing from landing in the repo.

**Rationale:** Reduces risk of representation claims or sovereign language slipping into public-facing content.

---

### 3.4 References: clone once, document only

**Suggestion:** Keep **references/** as “clone once, document only”: cloned repos (Bitnation, compdemocracy, liminalvillage, network-states, etc.) are **not** committed—e.g. gitignore `references/*` and keep only **references/README.md** committed with clone URLs and instructions. Run clone_references.sh locally or in a one-off setup.

**Rationale:** Repo stays small; references are clearly read-only inputs, not part of the product tree.

---

### 3.5 Venezuela CRC as first “live” config

**Suggestion:** Evolve **ayllu/runtime/venezuela.yml** as the first real CRC: tie enabled modules and priorities to Plan País/MCM themes (e.g. justice, electoral, economy, public_admin, social, education_culture). Keep **blueprint_ref** to venezuela/blueprint so positioning and constraints stay in one place. Use it as the engineering target for “load CRC and drive behavior.”

**Rationale:** Gives a concrete reference config and clarifies how the generic OS applies to the Venezuela application.

---

### 3.6 Credentialing: stay at protocol boundary for now

**Suggestion:** Keep **civic-houses/spec/credentialing_v0.md** as a **protocol boundary** (issuer, revocation, disputes, privacy) with **no implementation** (no VC format, ledger, or ZK yet). Do not start implementation until at least one pilot Civic House node is running and can feed back requirements. Use the spec to screen partners and tools.

**Rationale:** Avoids overbuilding before real use cases; spec is sufficient for governance and procurement discussions.

---

### 3.7 Leadership visibility

**Suggestion:** Keep **docs/EXECUTIVE_SUMMARY.md** (or this document, if renamed as the canonical one) as the **single entry point** for “what’s done and what engineering should do.” Update it when STATUS or structure changes so new joiners and leadership always see the full picture (ops, runtime, corpus, out/, credentialing, skills).

**Rationale:** One place for onboarding and for aligning leadership and engineering on priorities.

---

## 4. Decisions to unblock agents

Leadership may need to decide:

- **Corpus in git:** Corpus binaries are gitignored; only provenance and INDEX are committed. Should any corpus artifacts (e.g. extracted text from PDFs) ever be committed, or stay out-of-repo only?
- **Pilot city ownership:** Who owns the “first Civic House pilot” (lead, venue, first service) and reports into metrics/ops—WS3 agent, a named ops lead, or an external partner?
- **NS manual overrides:** Who is allowed to edit **network-states/overrides/manual_tags.yml** (e.g. product vs. engineering), and how often should ns_ingest_score be re-run after overrides?

---

## 5. One-line state

**AylluOS:** Spine (CRC, taxonomy, modules, practices) and ops/guardrails/skills are in place; Venezuela corpus and NS dashboard have capture and scoring with provenance and confidence; Civic House has templates, credentialing boundary, and a kit generator with one example kit. **Next:** Keep STATUS current, fill compendium/diff_map, add schema validation, run one Civic House pilot, and use NS out/ and top_venezuela_fit in product. **Suggestions above** are for leadership review before implementation.

---

*Document produced for Koss and Lead Engineering. Exportable; update as decisions are made.*
