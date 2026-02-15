# Skill: country-runtime-generator

Generate a Country Runtime Config (CRC) YAML for a given country from taxonomy and overrides.

## Inputs

- `ayllu/taxonomy/cofog.yml`, `ayllu/taxonomy/ministry_crosswalk.yml`
- Optional: country overrides (e.g. `venezuela/blueprint/venezuela_overrides.yml`)
- Parameter: country code or name (e.g. venezuela)

## Outputs

- `ayllu/runtime/<country>.yml` (e.g. `ayllu/runtime/venezuela.yml`)

## Steps

1. Copy `ayllu/runtime/templates/country.template.yml` to `ayllu/runtime/<country>.yml`.
2. Set `country` key to the country id.
3. Fill `modules.baseline` from COFOG/taxonomy; add `modules.optional` if applicable.
4. Set `canon.state_capacity` and `canon.future_risk_rd` to true.
5. Fill `constraints` (legal_posture, comms_posture, privacy_posture) from ops/GUARDRAILS and country blueprint.
6. If overrides path provided, set `blueprint_ref` or merge overrides into resources/constraints.

## Commands

- No dedicated script; use template copy + manual or Cursor edit. Future: `python scripts/generate_country_runtime.py COUNTRY [--overrides PATH]`.

## Quality checklist

- [ ] File validates as YAML.
- [ ] All required keys from ayllu/spec/COUNTRY_RUNTIME_SPEC.md present.
- [ ] Canon meta-ministries enabled.
- [ ] Constraints align with GUARDRAILS.

## Failure modes

- Missing taxonomy: ensure cofog.yml and ministry_crosswalk exist.
- Invalid blueprint_ref path: use path relative to repo root or runtime dir.
