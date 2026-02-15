# Country Runtime Config (CRC) — spec

AylluOS behaves as a **library + configuration system**. The runtime config is a first-class artifact: one file per country (or context) under `ayllu/runtime/<country>.yml`.

## Canon path

`ayllu/runtime/<country>.yml` (e.g. `venezuela.yml`).

## Must include

1. **Enabled modules**
   - COFOG baseline modules (from taxonomy; can be enabled/disabled or scoped).
   - Optional modules (e.g. from weird_revealing: diaspora, wellbeing, digital transformation, anti-corruption).

2. **CANON meta-ministries** (always present)
   - **Ministry of State Capacity (Systems & Delivery)** — delivery unit, evaluation, procurement.
   - **Ministry of Future, Risk, and Civilizational R&D** — foresight, risk register, preparedness.

3. **Resource allocation model**
   - Static baseline (e.g. default weights or caps per module).
   - Dynamic overrides (e.g. per-phase or per-program adjustments; can reference external file).

4. **Constraints / guardrails**
   - **Legal posture** — e.g. host-nation compliant, no representation claims.
   - **Comms posture** — safe terminology; no disallowed phrasing.
   - **Privacy posture** — data minimization; no sensitive personal data without policy.

5. **Metrics requirements per module**
   - Minimum viable measurement (what each enabled module must report or expose).
   - Can reference practice standards (delivery, evaluation, foresight).

## Template

Use `ayllu/runtime/templates/country.template.yml` as the starting point. Copy to `ayllu/runtime/<country>.yml` and fill.

## Relation to Venezuela

For Venezuela application: `ayllu/runtime/venezuela.yml` references ayllu modules and overlays `venezuela/blueprint/venezuela_overrides.yml` for positioning and constraints (diaspora civic infrastructure, complementary posture).
