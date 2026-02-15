# ayllu

Mono-repo for **ayllu** (white-label state OS primitives, COFOG-aligned) and **Venezuela** diaspora civic infrastructure. Complementary to host-state power structures; no representation claims.

## Structure

- **`ayllu/`** — State OS primitives: taxonomy, modules, practices, schemas, templates.
- **`venezuela/`** — Diaspora civic infra: Plan País + MCM sources, blueprint, civic-houses.
- **`network-states/`** — Ingest, rubric, and **out/** (canonical NS outputs: top_success, top_venezuela_fit, clusters, confidence). Legacy **outputs/** deprecated; use `ns_ingest_score.py`.
- **`scripts/`** — Fetch (Plan País/MCM, societies.csv), corpus download, NS scoring, Civic House kit generator.

## Canon (locked)

- **Ministry of State Capacity (Systems & Delivery)** — delivery, evaluation, procurement.
- **Ministry of Future, Risk, and Civilizational R&D** — foresight, risk preparedness.

## Quick start

```bash
# Venezuela corpus (Plan País mesas + MCM)
./scripts/fetch_plan_pais_and_mcm.sh [OUT_DIR]

# Network States dataset
./scripts/fetch_network_states_csv.sh [OUT_DIR]

# Score societies (canonical: writes network-states/out/ with confidence grades)
python scripts/ns_ingest_score.py [PATH_TO/societies.csv]
# Or: ./scripts/fetch_network_states_csv.sh ./downloads && python scripts/ns_ingest_score.py ./downloads/network-states/societies.csv
```

See the Cursor pack spec for full workflow and Civic House starter kit.
