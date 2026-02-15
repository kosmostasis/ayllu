# Skill: civic-house-kit-generator

Generate a Civic House kit for a city/country from templates and ops.

## Inputs

- `civic-houses/templates/*.md`
- `civic-houses/ops/*.md`
- `civic-houses/spec/credentialing_v0.md`
- Parameters: city name, country name (e.g. Miami, USA)

## Outputs

- `civic-houses/kits/<city>-<country>/` (e.g. `civic-houses/kits/Miami-USA/`)
  - brand.md, node_ops.md, service_catalog_v0.md, events_playbook.md
  - ops/safety_and_conduct.md, financial_controls.md, dispute_resolution.md, metrics.md
  - spec/credentialing_v0.md
  - README.md

## Steps

1. Normalize city and country to slug (e.g. Miami -> Miami, USA -> USA).
2. Create kit dir civic-houses/kits/<city>-<country>/.
3. Copy all templates and ops into kit; add README with kit name.
4. Optionally apply overrides (future: --overrides file).

## Commands

```bash
python scripts/generate_civic_house_kit.py Miami USA
python scripts/generate_civic_house_kit.py "Panama City" Panama
```

## Quality checklist

- [ ] Kit dir does not overwrite existing (script exits with error if exists).
- [ ] All template and ops files present.
- [ ] README mentions city/country and generator script.

## Failure modes

- Kit already exists: delete or use different city/country; do not overwrite without explicit flag.
- Invalid characters in city/country: script slugs them; review output dir name.
