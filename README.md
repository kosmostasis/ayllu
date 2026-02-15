# ayllu

Mono-repo for **ayllu** (white-label state OS primitives, COFOG-aligned) and **Venezuela** diaspora civic infrastructure. Complementary to host-state power structures; no representation claims.

## Structure

- **`ayllu/`** — State OS primitives: taxonomy, modules, practices, schemas, templates.
- **`venezuela/`** — Diaspora civic infra: Plan País + MCM sources, blueprint, civic-houses.
- **`network-states/`** — Ingest, rubric, and outputs for the Network States dashboard.
- **`scripts/`** — Fetch (Plan País/MCM, societies.csv) and scoring pipelines.

## Canon (locked)

- **Ministry of State Capacity (Systems & Delivery)** — delivery, evaluation, procurement.
- **Ministry of Future, Risk, and Civilizational R&D** — foresight, risk preparedness.

## Quick start

```bash
# Venezuela corpus (Plan País mesas + MCM)
./scripts/fetch_plan_pais_and_mcm.sh [OUT_DIR]

# Network States dataset
./scripts/fetch_network_states_csv.sh [OUT_DIR]

# Score societies (heuristic bootstrap)
python scripts/score_network_states.py DOWNLOADS/network-states/societies.csv
```

See the Cursor pack spec for full workflow and Civic House starter kit.
