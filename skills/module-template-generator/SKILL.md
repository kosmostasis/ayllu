# Skill: module-template-generator

Create a new ministry or meta-capability module stub under ayllu/modules.

## Inputs

- Module type: core (COFOG-aligned), meta_capability (CANON), or weird_revealing (optional)
- Module id and name (e.g. diaspora, wellbeing)
- `ayllu/schemas/ministry_module.schema.json` (reference)
- `ayllu/modules/meta_capabilities/README.md` or existing module as template

## Outputs

- `ayllu/modules/<type>/<module_id>/` with README.md or module definition (e.g. YAML or JSON matching ministry_module schema)

## Steps

1. Choose parent dir: ayllu/modules/core, ayllu/modules/meta_capabilities, or ayllu/modules/weird_revealing.
2. Create subdir <module_id>.
3. Add README.md with: purpose, sub-units (if any), outputs (if any), link to COFOG or CANON.
4. Optionally add a module definition file (e.g. module.yml) with id, name, purpose, cofog_code or canon, sub_units, outputs.

## Commands

- No dedicated script. Manual: mkdir ayllu/modules/weird_revealing/diaspora; add README and optional module.yml.

## Quality checklist

- [ ] Module id is lowercase, no spaces.
- [ ] Purpose and outputs (if any) stated.
- [ ] If COFOG-aligned, cofog_code or crosswalk reference; if CANON, state which meta-ministry.

## Failure modes

- Duplicate id: check existing dirs under core, meta_capabilities, weird_revealing.
- Invalid schema: if module.yml used, validate against ministry_module.schema.json.
