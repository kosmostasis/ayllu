# Venezuela sources — Plan País + MCM

Run `../../scripts/fetch_plan_pais_and_mcm.sh [OUT_DIR]` to download. Do not commit the ZIP to git; store in a private artifact store. Commit only this INDEX and hashes below after running.

## Table of docs

| Title | Date | Issuer | Link / file | Type |
|-------|------|--------|-------------|------|
| Propuesta Plan País — mesa administración pública | 2019 | Plan País | plan-pais/mesas/propuesta-para-el-plan-pais-mesa-administracion-publica.pdf | Plan País |
| Propuesta Plan País — mesa discapacidad | 2019 | Plan País | plan-pais/mesas/propuesta-para-el-plan-pais-mesa-discapacidad.pdf | Plan País |
| Propuesta Plan País — mesa economía energía | 2019 | Plan País | plan-pais/mesas/propuesta-para-el-plan-pais-mesa-economia-energia.pdf | Plan País |
| Propuesta Plan País — mesa medios de comunicación | 2019 | Plan País | plan-pais/mesas/propuesta-para-el-plan-pais-mesa-medios-de-comunicacion.pdf | Plan País |
| Propuesta Plan País — mesa política social | 2019 | Plan País | plan-pais/mesas/propuesta-para-el-plan-pais-mesa-politica-social.pdf | Plan País |
| Propuesta Plan País — mesa RRII | 2019 | Plan País | plan-pais/mesas/propuesta-para-el-plan-pais-mesa-rrii.pdf | Plan País |
| Propuesta Plan País — mesas educación cultura ciencia y tecnología | 2019 | Plan País | plan-pais/mesas/...educacion-cultura-ciencia-y-tecnologia.pdf | Plan País |
| Propuesta Plan País — mesa sistema electoral | 2019 | Plan País | plan-pais/mesas/...mesa-sistema-electoral.pdf | Plan País |
| Propuesta Plan País — mesa justicia | 2019 | Plan País | plan-pais/mesas/...mesa-justicia.pdf | Plan País |
| Venezuela Tierra de Gracia | 2023-10 | MCM | mcm/venezuela-tierra-de-gracia.pdf | MCM |
| Plan para VZLA (EGU + MCM) | 2025-10 | EGU + MCM | mcm/plan-para-vzla-egu-mcm.pdf | MCM |
| Se trata de la libertad | 2016 | Vente | mcm/se-trata-de-la-libertad.pdf | MCM |
| Plan de gobierno (landing) | — | MCM | mcm/plan-de-gobierno-landing.html | MCM |

## Umbrella doc

- **Plan País:** Locate any “integrator” PDF that references the mesas. If not found, build `plan-pais_compendium.md` stitching each mesa’s executive summary + key policies.
- **MCM:** Use Venezuela Tierra de Gracia + Plan para VZLA as core program docs.

## Diff map

Create `diff_map.md`: Plan País vs MCM (tone, sequencing 100 hours/100 days, institutional reforms, economic program).

## Hashes (fill after fetch)

```
# After running fetch_plan_pais_and_mcm.sh, add checksums here, e.g.:
# plan-pais/mesas/...  sha256:...
# mcm/venezuela-tierra-de-gracia.pdf  sha256:...
```
