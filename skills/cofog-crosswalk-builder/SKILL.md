# Skill: cofog-crosswalk-builder

Update ministry_crosswalk.yml from COFOG source or new mapping requirements.

## Inputs

- `ayllu/taxonomy/cofog.yml`
- UN COFOG reference (https://unstats.un.org/unsd/classifications/cofog/revision) or internal spec
- Current `ayllu/taxonomy/ministry_crosswalk.yml`

## Outputs

- `ayllu/taxonomy/ministry_crosswalk.yml` (updated)

## Steps

1. Read cofog.yml for function codes and names.
2. For each COFOG code, define or update the list of ministry/module ids in mapping.
3. Update meta_capabilities section if CANON or optional modules change.
4. Preserve YAML structure and version.

## Commands

- Manual edit or script: no dedicated script; edit ministry_crosswalk.yml directly.

## Quality checklist

- [ ] Every COFOG code in cofog.yml has an entry in mapping (or explicit empty list).
- [ ] meta_capabilities lists state_capacity and future_risk_rd sub-units.
- [ ] YAML valid.

## Failure modes

- Breaking existing runtime: ensure any id renames are reflected in runtime/*.yml that reference modules.
