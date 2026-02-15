# Executive Summary — Ayllu Repo (Current State)

**Purpose:** Single entry point for leadership and engineering: what’s done and what to do next across AylluOS, Venezuela application, Civic House, and Network States (NS) dashboard.

---

## 1. What’s in place

Single **mono-repo** (`ayllu`) with six main areas:

- **`ayllu/`** — Generic state OS (AylluOS): taxonomy, modules, practices, schemas, templates; **spec/** (COUNTRY_RUNTIME_SPEC); **runtime/** (country.template.yml, venezuela.yml as first “live” CRC).
- **`venezuela/`** — Venezuela application: **sources/** (INDEX + hashes), **corpus/** (plan-pais, mcm with INDEX + provenance), **spec/** (plan-pais_compendium canonical, diff_map), **blueprint/**, **civic-houses/starter-kit/**.
- **`network-states/`** — Rubric (rubric.yml), **out/** (canonical: top_success.md, top_venezuela_fit.md, clusters, white_spaces, confidence_summary), **overrides/** (manual_tags.yml).
- **`civic-houses/`** — Top-level: **templates/**, **ops/**, **spec/credentialing_v0.md**, **kits/** (e.g. Miami-USA); kit generator in scripts.
- **`ops/`** — STATUS.md (per-agent), ORCHESTRATION.md (worktrees, roles), GUARDRAILS.md (disallowed phrasing, safe terms, privacy). Redaction log format in docs/local_audit_redaction_format.md; local_audit/ is gitignored.
- **`scripts/`** — fetch_plan_pais_and_mcm.sh, fetch_network_states_csv.sh, download_corpus.sh, ns_ingest_score.py (canonical NS scoring with confidence), score_network_states.py (writes to out/), generate_civic_house_kit.py, guardrails_lint.py, clone_references.sh.
- **`references/`** — README with clone list (Bitnation, compdemocracy, liminalvillage, network-states, Snapshot, GSA); cloned repos are gitignored.
- **`skills/`** — Eight Cursor Skills (country-runtime-generator, cofog-crosswalk-builder, ns-dashboard-ingest-and-score, civic-house-kit-generator, corpus-capture-with-provenance, compendium-synthesizer, guardrails-linter, module-template-generator).

Design constraints: COFOG taxonomy, “no representation claims,” complementary to host-state. Two **canon** meta-ministries: State Capacity (Systems & Delivery) and Future, Risk & Civilizational R&D.

---

## 2. AylluOS (generic state OS)

**Status:** Spine and CRC in place; ready for schema validation and tooling.

**Done:**

- **Taxonomy:** ayllu/taxonomy/ (cofog.yml, ministry_crosswalk.yml).
- **Modules:** core/, meta_capabilities/ (CANON), weird_revealing/; procurement playbook, critical risk preparedness.
- **Practices:** Six practice standards + missing_state_muscles.
- **Schemas:** ministry_module.schema.json, practice_standard.schema.json.
- **Templates:** charter, policy_spec, budget_module.
- **Spec:** ayllu/spec/COUNTRY_RUNTIME_SPEC.md.
- **Runtime:** ayllu/runtime/templates/country.template.yml; ayllu/runtime/venezuela.yml (first live CRC with theme_priority from Plan País/MCM).

**Engineering directions:**

- Schema validation for taxonomy and CRC; optional CLI/API to load and validate runtime configs.
- Flesh out practice standards and link to modules.
- Evolve venezuela.yml as the reference “load CRC and drive behavior” target.

---

## 3. Venezuela application

**Status:** Corpus layout and provenance in place; compendium and diff_map ready to be filled.

**Done:**

- **Sources:** venezuela/sources/ — INDEX, hashes; link to canonical compendium at venezuela/spec/plan-pais_compendium.md.
- **Corpus:** venezuela/corpus/plan-pais/, venezuela/corpus/mcm/ — INDEX + provenance; scripts/download_corpus.sh writes here and updates provenance.
- **Compendium (canonical):** venezuela/spec/plan-pais_compendium.md — mesa structure + “what’s missing relative to AylluOS” annex. sources/plan-pais_compendium.md is a stub pointing to spec.
- **Diff map:** venezuela/sources/diff_map.md — Plan País vs MCM tables (to fill).
- **Blueprint:** venezuela/blueprint/ (one_liner, venezuela_overrides.yml).

**Engineering directions:**

- PDF extraction pipeline to populate compendium and diff_map.
- Use compendium/diff_map to drive Venezuela overrides and CRC theme_priority.

---

## 4. Civic House

**Status:** Templates, ops, credentialing boundary, and kit generator in place; one example kit (Miami-USA).

**Done:**

- **Top-level civic-houses/:** templates/ (brand, node_ops, service_catalog, events_playbook), ops/ (safety, financial_controls, dispute_resolution, metrics), spec/credentialing_v0.md (protocol boundary: issuer, revocation, disputes, privacy), kits/ (e.g. Miami-USA).
- **Script:** scripts/generate_civic_house_kit.py (city + country → kit under civic-houses/kits/).
- **Venezuela starter kit:** venezuela/civic-houses/starter-kit/ (brand, node_ops, service_catalog, events, safety, financial, dispute, metrics, pilot_city_shortlist).

**Engineering directions:**

- Pilot one city (one lead, venue, service); report into metrics/ops.
- Keep credentialing at protocol boundary until pilot feedback; use spec to screen partners and tools.

---

## 5. Network States dashboard

**Status:** Ingest, scoring with confidence, and canonical outputs in place.

**Done:**

- **Ingest:** scripts/fetch_network_states_csv.sh.
- **Rubric:** network-states/rubric/rubric.yml (v0.2).
- **Canonical outputs:** network-states/out/ — top_success.md, top_venezuela_fit.md, clusters.md, white_spaces.md, confidence_summary.md (A/B/C grades). Written by scripts/ns_ingest_score.py. Legacy network-states/outputs/ deprecated (README points to out/).
- **Overrides:** network-states/overrides/manual_tags.yml (human-in-the-loop).

**Engineering directions:**

- Use top_venezuela_fit and white_spaces in product/strategy.
- Data model for societies + scores; richer clustering; optional dashboard UI.

---

## 6. Ops and guardrails

- **ops/STATUS.md** — Per-agent (OS Architect, WS1 Corpus, WS2 Landscape, WS3 Civic House): objective, last shipped, next 3 tasks, blockers.
- **ops/ORCHESTRATION.md** — Worktrees, roles, link to plan and GUARDRAILS.
- **ops/GUARDRAILS.md** — Disallowed phrasing, safe terminology, privacy red lines.
- **scripts/guardrails_lint.py** — Lightweight check for disallowed phrases; use in CI or pre-commit. Redactions logged in local_audit/ only (gitignored).

---

## 7. Suggested engineering priorities

| Priority | Workstream   | Focus                                                                 |
|----------|---------------|-----------------------------------------------------------------------|
| 1        | AylluOS       | Schema validation for taxonomy + CRC; evolve venezuela.yml.          |
| 2        | Venezuela     | Fill compendium/diff_map (PDF extraction or manual).                 |
| 3        | Civic House   | Pilot one city; keep credentialing at protocol boundary.            |
| 4        | NS dashboard  | Use out/ and top_venezuela_fit in product; optional guardrails in CI. |

---

## 8. Repo quick reference

- **Root:** README.md — structure, quick start (download_corpus, ns_ingest_score).
- **Venezuela:** venezuela/README.md; corpus and compendium canonical locations (corpus/, spec/).
- **Ops:** ops/STATUS.md, ops/GUARDRAILS.md.
- **Scripts:** Run from repo root; downloads/ and local_audit/ gitignored; references/* gitignored (README.md kept).
- **Design spec:** External Cursor pack (ayllu); this repo is the implementation artifact.
