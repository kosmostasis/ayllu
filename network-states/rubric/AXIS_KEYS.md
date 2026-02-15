# Axis keys and pipeline reference

## Current axis keys (in rubric and pipeline)

- `legitimacy_path`
- `territory_density`
- `economic_engine`
- `identity_credentials`
- `governance_security`
- `dacc_alignment`
- `execution_capacity`
- `cosmo_localism` (added in rubric v0.3; pipeline must include in Score and total)

## Modifier key

- `venezuela_similarity` — Venezuela fit modifier (range -2 to +2). Leadership pack calls it "Venezuela fit"; repo keeps `venezuela_similarity` for pipeline compatibility.

## Pipeline location

- **Scoring scripts:** [scripts/ns_ingest_score.py](../../scripts/ns_ingest_score.py) and [scripts/score_network_states.py](../../scripts/score_network_states.py)
- **Data model:** Fixed `Score` dataclass in those scripts; no separate axis index file. Axis set is hardcoded in code.
- **Adding a new axis:** Add the key to `rubric.yml` under `axes:` and add the same field to the `Score` dataclass and to `total()` in both scripts; add heuristic logic as needed.
