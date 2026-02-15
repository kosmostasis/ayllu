# Skill: ns-dashboard-ingest-and-score

Ingest Network States societies.csv, apply rubric and optional overrides, produce clusters and ranked lists with confidence.

## Inputs

- societies.csv (e.g. from `scripts/fetch_network_states_csv.sh` or downloads/network-states/societies.csv)
- `network-states/rubric/rubric.yml`
- Optional: `network-states/overrides/manual_tags.yml`

## Outputs

- `network-states/out/top_success.md`
- `network-states/out/top_venezuela_fit.md`
- `network-states/out/clusters.md`
- `network-states/out/white_spaces.md`
- `network-states/out/confidence_summary.md`

## Steps

1. Fetch CSV if needed: run `./scripts/fetch_network_states_csv.sh [OUT_DIR]`.
2. Optionally edit `network-states/overrides/manual_tags.yml` for manual score/tag overrides.
3. Run `python scripts/ns_ingest_score.py [PATH_TO/societies.csv]`.
4. Review out/*.md; iterate on rubric or overrides if needed.

## Commands

```bash
./scripts/fetch_network_states_csv.sh ./downloads
python scripts/ns_ingest_score.py ./downloads/network-states/societies.csv
```

## Quality checklist

- [ ] Rubric version matches rubric.yml (e.g. 0.2).
- [ ] Confidence grades A/B/C present in top_success and confidence_summary.
- [ ] Manual overrides applied when overrides file exists and has entries.

## Failure modes

- CSV missing or wrong path: run fetch script first or pass correct path.
- PyYAML not installed: overrides load is skipped; scoring still runs.
- CSV schema change: adapt ns_ingest_score.py column names (name, mission, baseLocations, tags, discord, application, id).
