# Ops status — parallel agents

**Rule:** Each agent edits only their own section. Update Last shipped, Next 3 tasks, Blockers.

---

## OS Architect

- **Objective:** AylluOS spine (COUNTRY_RUNTIME_SPEC, runtime templates, country YAML stubs).
- **Last shipped:** Playbook PR 1 — COUNTRY_RUNTIME_SPEC.md, country.template.yml, ayllu/runtime/venezuela.yml stub.
- **Next 3 tasks:** (1) Schema validation for taxonomy + CRC (2) Evolve venezuela.yml with Plan País/MCM module themes (3) Optional CLI/API to load and validate runtime configs
- **Blockers / decisions needed from Koss:** —

---

## WS1 Corpus Agent

- **Objective:** Plan País + MCM corpus capture, provenance, indexing, compendium.
- **Last shipped:** Playbook PR 2 — venezuela/corpus/ layout, download_corpus.sh, provenance schema, venezuela/spec/plan-pais_compendium.md (with “what’s missing” annex).
- **Next 3 tasks:** (1) Fill compendium and diff_map from corpus (PDF extraction or manual) (2) Keep venezuela/spec/ as canonical compendium; sources/INDEX links to it (3) Decide: commit extracted text or keep out-of-repo
- **Blockers / decisions needed from Koss:** —

---

## WS2 Landscape Agent

- **Objective:** NS dashboard ingest, enrichment, clustering, scoring, manual overrides, confidence.
- **Last shipped:** Playbook PR 3 — network-states/out/, overrides/manual_tags.yml, confidence A/B/C, ns_ingest_score.py.
- **Next 3 tasks:** (1) Standardize on out/ as canonical NS output; deprecate outputs/ in README (2) Use top_venezuela_fit and white_spaces in product/strategy (3) Optional: guardrails-linter script for docs
- **Blockers / decisions needed from Koss:** Who may edit manual_tags.yml; re-run cadence for ns_ingest_score

---

## WS3 Civic House Agent

- **Objective:** Civic House kits/templates, ops playbooks, credentialing boundary, kit generator.
- **Last shipped:** Playbook PR 4 — civic-houses/templates, ops, spec/credentialing_v0.md, kits/Miami-USA, generate_civic_house_kit.py.
- **Next 3 tasks:** (1) Pilot one city (e.g. Miami-USA): one lead, one venue, one service; report into metrics/ops (2) Keep credentialing at protocol boundary until pilot feedback (3) Generate kits for other pilot cities from shortlist
- **Blockers / decisions needed from Koss:** Pilot city ownership (WS3 vs named ops lead vs partner)

---

## WS4 Brand Agent

- **Objective:** Brand voice, narrative pillars, STYLE_GUIDE compliance.
- **Required reading:** [AGENT_REQUIRED_READING.md](AGENT_REQUIRED_READING.md) — brand/STYLE_GUIDE.md, GUARDRAILS.md.
- **Last shipped:** —
- **Next 3 tasks:** (1) Apply STYLE_GUIDE to any new copy (2) Ensure Cosmo-Localism and d/acc appear where principles are stated (3) No representation claims; use safe terminology per GUARDRAILS
- **Blockers / decisions needed from Koss:** —

---

## WS5 UI/UX Agent

- **Objective:** Mobile-first UX, MOBILE_PRINCIPLES, Area page pattern, contribution flows.
- **Required reading:** [AGENT_REQUIRED_READING.md](AGENT_REQUIRED_READING.md) — ux/MOBILE_PRINCIPLES.md, brand/STYLE_GUIDE.md, GUARDRAILS.md.
- **Last shipped:** —
- **Next 3 tasks:** (1) Follow MOBILE_PRINCIPLES for any UI work (2) One next action per screen; trust cues on claims (3) No critical-path poetry
- **Blockers / decisions needed from Koss:** —
