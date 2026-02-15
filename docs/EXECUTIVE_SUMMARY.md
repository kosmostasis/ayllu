# Executive Summary — Ayllu Repo (Current State)

**Purpose:** Brief for leadership and input for engineering on four workstreams: AylluOS (generic), Venezuela application, Civic House starter kit, and Network States (NS) dashboard.

---

## 1. What’s in place

Single **mono-repo** (`ayllu`) with four main areas:

- **`ayllu/`** — Generic state OS (AylluOS)
- **`venezuela/`** — Venezuela-specific application (sources, blueprint, Civic House)
- **`network-states/`** — NS dashboard ingest, rubric, and outputs
- **`scripts/`** — Fetch and scoring pipelines (Venezuela corpus, NS CSV)

Design constraints are explicit: COFOG taxonomy, “no representation claims,” complementary to host-state structures. Two **canon** meta-ministries are fixed: State Capacity (Systems & Delivery) and Future, Risk & Civilizational R&D.

---

## 2. AylluOS (generic state OS)

**Status:** Skeleton in place; ready for engineering to turn into a real “OS” (data model, APIs, tooling).

**Done:**

- **Taxonomy:** `ayllu/taxonomy/` — `cofog.yml` (10 COFOG functions), `ministry_crosswalk.yml` (COFOG ↔ ministry/module names and meta-capabilities).
- **Modules:** `ayllu/modules/` — `core/` (baseline ministries placeholder), `meta_capabilities/` (CANON: State Capacity + Future/Risk/R&D with README, procurement playbook, critical risk preparedness), `weird_revealing/` (optional signal modules).
- **Practices:** `ayllu/practices/` — Six practice standards (delivery, evidence & evaluation, data governance, maintenance, foresight) plus “missing state muscles” overview; all are short specs/skeletons.
- **Schemas:** `ayllu/schemas/` — `ministry_module.schema.json`, `practice_standard.schema.json` (JSON Schema draft-07).
- **Templates:** `ayllu/templates/` — charter, policy_spec, budget_module (fill-in-the-blank).

**Engineering directions:**

- Implement validation/tooling against the schemas; add versioning and optional API for taxonomy/modules/practices.
- Flesh out practice standards (delivery, evaluation, foresight) into implementable specs and link them to modules.
- Optionally add a “runtime” or config layer that instantiates a given country/context from taxonomy + overrides.

---

## 3. Venezuela application

**Status:** Corpus and structure in place; analysis frameworks ready to be filled and used by product/ops.

**Done:**

- **Sources:** `venezuela/sources/` — INDEX of Plan País (9 mesas, 2019) and MCM corpus (Venezuela Tierra de Gracia, Plan para VZLA, Se trata de la libertad, landing HTML). SHA-256 hashes in INDEX for integrity.
- **Fetch:** `scripts/fetch_plan_pais_and_mcm.sh` — downloads all listed PDFs/HTML and builds a ZIP (ZIP not in git; store in private artifact store).
- **Compendium:** `venezuela/sources/plan-pais_compendium.md` — one section per mesa with placeholders for executive summary + key policies (to be filled from PDFs).
- **Diff map:** `venezuela/sources/diff_map.md` — Plan País vs MCM comparison tables (tone, 100h/100d sequencing, institutional reforms, economic program); structure ready, content to be filled from corpus.
- **Blueprint:** `venezuela/blueprint/` — `one_liner.md`, `venezuela_overrides.yml` (positioning, constraints, source priority, civic-house stack).

**Engineering directions:**

- Add PDF text extraction (e.g. pdftotext or cloud) and optional pipeline to populate compendium and diff_map from the indexed files.
- Use compendium + diff_map to drive Venezuela-specific “overrides” or feature flags in AylluOS (e.g. sequencing, institutional reform themes).
- Keep Venezuela as the first **application** of the generic OS (ayllu + venezuela_overrides + Civic House).

---

## 4. Civic House starter kit

**Status:** Operational and product spec only; no code. Ready for engineering to implement tooling, templates, and (later) platform features.

**Done:**

- **Starter kit** in `venezuela/civic-houses/starter-kit/`:
  - **brand.md** — name, tone, do/don’t (no representation claims).
  - **node_ops.md** — how to start a Civic House (steps, prerequisites).
  - **service_catalog_v0.md** — credentialing, opportunities, mutual aid, learning, events.
  - **events_playbook.md** — formats (meetup, info session, workshop, round table) and norms.
  - **safety_and_conduct.md** — venue, conduct, incidents, review.
  - **financial_controls.md** — treasury, separation of funds, audit, reporting.
  - **dispute_resolution.md** — tiers (informal, mediation, escalation).
  - **metrics.md** — node- and network-level metrics; privacy.
  - **pilot_city_shortlist.md** — Miami, Madrid, Bogotá, Lima, Panama City (candidates).
- Placeholder dirs: `venezuela/civic-houses/ops/`, services/, legal_compliance/.

**Engineering directions:**

- Turn the starter kit into **templates** (e.g. Markdown or structured YAML/JSON) that can be generated per node or per pilot city.
- Build minimal **node onboarding flow** (form or CLI) that produces a node “pack” from these docs.
- Later: credential primitives, issuance/revocation policy, and contributions ledger (align with identity/credentialing roadmap).

---

## 5. Network States dashboard dive

**Status:** Ingest and heuristic scoring in place; clustering and white-space notes started. Ready to go deeper (data model, manual tags, product use cases).

**Done:**

- **Ingest:** `scripts/fetch_network_states_csv.sh` — pulls [Network States of the Internet](https://github.com/thenetworkstate/network-states-of-the-internet) `societies.csv` into `downloads/network-states/`.
- **Rubric:** `network-states/rubric/rubric.yml` — seven axes (legitimacy_path, territory_density, economic_engine, identity_credentials, governance_security, dacc_alignment, execution_capacity) plus venezuela_similarity modifier; composite = sum(axes) + modifier.
- **Scoring:** `scripts/score_network_states.py` — heuristic scoring from CSV columns: `name`, `mission`, `baseLocations`, `discord`, `application`, `tags`. Uses mission/location text and tag normalization; writes outputs under `network-states/outputs/`.
- **Outputs:**
  - `network-states/outputs/top_success_like.md` — top 30 by composite score with axis breakdown.
  - `network-states/outputs/top_venezuela_similar.md` — societies with diaspora/Latam/migration signals and baseLocations.
  - `network-states/outputs/clusters.md` — clusters by inferred type (geographic, virtual, hybrid, pop-up, other) from tags.
  - `network-states/outputs/white_spaces.md` — short notes on gaps (e.g. high execution/low territory, Venezuela-similar, high territory/low economic).

**Engineering directions:**

- **Go deeper on NS dashboard:**
  - Add a **data model** (e.g. normalized tables or JSON schema) for societies + scores + clusters so rubric and scores are queryable and versioned.
  - Introduce **manual tags** (e.g. economic model, identity rails, territory strategy) and optional manual overrides to scores; re-run pipeline and persist results.
  - **Clustering:** move from “inferred type from tags” to richer clustering (e.g. by multiple dimensions, or by score profiles) and expose in outputs/reports.
  - **Venezuela lens:** maintain and refine “Venezuela-similar” list and white-space narrative for diaspora/civic-house prioritization.
- Optionally: small **dashboard UI** or report generator (e.g. top lists, filters by type/region, export) fed from the same data and rubric.

---

## 6. Suggested engineering priorities (for boss to assign)

| Priority | Workstream      | Suggested focus                                                                 |
|----------|-----------------|-----------------------------------------------------------------------------------|
| 1        | AylluOS         | Schemas + validation; versioned taxonomy; link practices to modules.            |
| 2        | Venezuela       | PDF extraction pipeline; populate compendium/diff_map; tie overrides to AylluOS. |
| 3        | Civic House     | Templates + node onboarding flow from starter-kit docs; pilot cities.            |
| 4        | NS dashboard    | Data model + manual tags; richer clustering; Venezuela-similar and white-space as product inputs. |

---

## 7. Repo quick reference

- **Root:** `README.md` — structure, canon, quick start commands.
- **Venezuela:** `venezuela/README.md` — sources, blueprint, civic-houses.
- **Scripts:** Run from repo root; `downloads/` is gitignored.
- **Design spec:** External Cursor pack (generic-civics → ayllu) defines full workflow; this repo is the implementation artifact.
