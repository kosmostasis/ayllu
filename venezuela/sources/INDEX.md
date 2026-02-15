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

## Hashes (sha256)

Verified after running `fetch_plan_pais_and_mcm.sh`. Re-run hashes if you re-download.

| File | sha256 |
|------|--------|
| plan-pais/mesas/propuesta-para-el-plan-pais-mesa-administracion-publica.pdf | 0a63b9f003cb5a72f9122bde7302601cce6316b4f31de990ecc29cb996b8f033 |
| plan-pais/mesas/propuesta-para-el-plan-pais-mesa-discapacidad.pdf | dd94c92d4178392dadbb6c4c096d3ad6d045edec9fa8ba6deb85f42d68af59a7 |
| plan-pais/mesas/propuesta-para-el-plan-pais-mesa-economia-energia.pdf | 3c6e463f1f31f1277d37a5ad4d7874a0a9f0df05e9450dda60b678aff1e72616 |
| plan-pais/mesas/propuesta-para-el-plan-pais-mesa-justicia.pdf | fe3704fe90a781bd36c3bd9c0a566183e0f94b5071ef30490fb783d9918243e2 |
| plan-pais/mesas/propuesta-para-el-plan-pais-mesa-medios-de-comunicacion.pdf | 7afa2f4900c852e31ad1fc9847cb3cde927230449c3f7def3c992fca2d0e5bf1 |
| plan-pais/mesas/propuesta-para-el-plan-pais-mesa-politica-social.pdf | feed47293b0bf7d0f928aadaffea5c2bf002261378086bffd0c0ba800aa0d28f |
| plan-pais/mesas/propuesta-para-el-plan-pais-mesa-rrii.pdf | bf772d206986b39834982d2d36c2ffd2c3876eb48698381e41bde9b18036d4e3 |
| plan-pais/mesas/propuesta-para-el-plan-pais-mesa-sistema-electoral.pdf | 71f9c3fed057a9275a720d1a9a65ba3669feeb8c33fe8dea97b3dc05c4b238a7 |
| plan-pais/mesas/propuesta-para-el-plan-pais-mesas-educacion-cultura-ciencia-y-tecnologia.pdf | d79c5de197f8227ac8f9884a5542d896ebada47c5346d9110316c6f1b7bb9c2c |
| mcm/venezuela-tierra-de-gracia.pdf | d6d079c7a328ed5f0d42721989f13d8774650fc2354a7a149fbfbb09fc466b7c |
| mcm/plan-para-vzla-egu-mcm.pdf | 21ce7a7a3038cead49edd671677296458975ed8a6c376902a19986044767c17a |
| mcm/se-trata-de-la-libertad.pdf | 75e42560b52e93ba9b1a6baa67132ccbe62f1d6e800cf95346daf512775dca1c |
| mcm/plan-de-gobierno-landing.html | bb0a9ff8ac0019201bb8a2e70e5e36928c3df6e1119307129e0715ff419d8b8e |
