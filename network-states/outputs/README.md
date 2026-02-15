# Deprecated: use network-states/out/ instead

NS dashboard outputs are now written to **network-states/out/** by:

- `scripts/ns_ingest_score.py` (canonical: top_success.md, top_venezuela_fit.md, clusters.md, white_spaces.md, confidence_summary.md)

The legacy script `score_network_states.py` also writes to **out/** as of the standardization. Do not add new files under this `outputs/` folder.
