# Axis Edit Prompts

Human/agent instructions when editing the rubric. Use repo axis keys: `dacc_alignment`, `governance_security`, `venezuela_similarity`.

---

## Axis Edit Prompt Template

```text
Context: We're updating the Network States scoring rubric in AylluOS. The rubric lives at `network-states/rubric/rubric.yml`. Each axis must be defined consistently and referenced wherever the rubric enumerates axes used by the scoring pipeline.

Task:
1) Open `network-states/rubric/rubric.yml`.
2) Add or update the axis key: `<axis_key>` under `axes:` (or the equivalent structure used).
3) Ensure the axis includes:
   - `name`
   - `weight` (default 1.0 unless specified)
   - `description`
   - `signals_positive` (bullets)
   - `signals_negative` (bullets)
   - `scoring_anchors` for 0–5
   - `measurement_notes` (bullets)
4) Keep style consistent with existing axes (indentation, tense, wording).
5) If there is an "axis list", "summary", or "pipeline config" section referencing axes, add `<axis_key>` there too.
6) Do not change other axis weights or scoring anchors unless explicitly instructed.

Acceptance:
- YAML remains valid.
- `<axis_key>` appears in both axis definitions and any axis index/list used by scoring.
- Any changes are minimal and localized.
```

---

## Prompts for Core Axes (paste one at a time)

### Cosmo-Localism

```text
Context: Add a dedicated Cosmo-Localism axis to the Network States scoring rubric (equal weight to d/acc). Cosmo-Localism = global coordination (knowledge/capital/networks) + locally grounded implementation + local value capture + accountability to local stakeholders, avoiding extractive remote-control dynamics.

Task:
1) Open `network-states/rubric/rubric.yml`.
2) Insert the `cosmo_localism` axis under `axes:` using the provided snippet (name, weight=1.0, description, signals, anchors 0–5, measurement notes).
3) Ensure it is referenced in any axis list/summary used by the scoring pipeline.
4) Do not modify other axis weights.

Acceptance:
- YAML validates.
- Cosmo-Localism is first-class and visible to the scoring pipeline.
```

### d/acc (use key `dacc_alignment`)

```text
Context: Standardize the d/acc axis definition in `network-states/rubric/rubric.yml`. Use axis key `dacc_alignment`. d/acc here means: defense/resilience, decentralization, and safety-by-design in both technical and social systems. It should not be "innovation hype"; it should reward robust, non-fragile systems.

Task:
1) Open `network-states/rubric/rubric.yml`.
2) Add or refine `dacc_alignment` under `axes:` to include: name, weight=1.0, clear description, positive/negative signals, anchors 0–5, and measurement notes.
3) Ensure anchors distinguish between: rhetoric-only vs demonstrable resilience/security/decentralization primitives.
4) Update any axis index/list to include the key if missing.

Acceptance:
- YAML validates.
- d/acc axis is explicit and consistent with other axes.
```

### Legitimacy path

```text
Context: Refine the "Legitimacy path" axis. It measures legal/compliance plausibility, host-nation compatibility, dispute resolution, and non-coercive posture.

Task:
1) Open `network-states/rubric/rubric.yml`.
2) Add/update `legitimacy_path` axis with: description, signals, anchors 0–5, measurement notes.
3) Ensure higher scores require evidence: legal wrapper clarity, compliance posture, dispute handling.
4) Ensure low scores penalize "cosplay sovereignty" and vague governance.

Acceptance:
- YAML validates.
- Axis anchors are concrete and evidence-based.
```

### Territory & density

```text
Context: Refine "Territory & density". It measures durable physical presence (leases/land/SEZ/recurring popups), and whether density is increasing.

Task:
1) Open `network-states/rubric/rubric.yml`.
2) Add/update `territory_density` axis with 0–5 anchors.
3) Add measurement notes: prefer evidence (leases, addresses, event history).

Acceptance:
- YAML validates.
- Anchors clearly map to physicality.
```

### Economic engine

```text
Context: Refine "Economic engine". It measures real value creation and sustainability beyond token speculation.

Task:
1) Open `network-states/rubric/rubric.yml`.
2) Add/update `economic_engine` axis with signals and 0–5 anchors.
3) Penalize speculative/token-only models; reward real services/products and transparent finances.

Acceptance:
- YAML validates.
- Anchors emphasize sustainable economics.
```

### Identity & credentials rails

```text
Context: Refine "Identity & credentials rails": onboarding clarity, verifiable credentials/attestations, privacy posture, revocation/disputes where applicable.

Task:
1) Open `network-states/rubric/rubric.yml`.
2) Add/update `identity_credentials` axis with signals and 0–5 anchors.
3) Include measurement notes: privacy-by-default, minimize data retention.

Acceptance:
- YAML validates.
- Credentialing is disciplined, not badge theater.
```

### Governance & safety (use key `governance_security`)

```text
Context: Refine "Governance & safety": decision processes, conflict handling, moderation/safety policies, dispute escalation. Use axis key `governance_security` in rubric and pipeline.

Task:
1) Open `network-states/rubric/rubric.yml`.
2) Add/update `governance_security` axis with signals and 0–5 anchors.

Acceptance:
- YAML validates.
- Anchors are operational and evidence-based.
```

### Execution capacity

```text
Context: Refine "Execution capacity": ship rate, cadence, operational stability, measurable outcomes.

Task:
1) Open `network-states/rubric/rubric.yml`.
2) Add/update `execution_capacity` axis with signals and 0–5 anchors.

Acceptance:
- YAML validates.
- Rewards delivery over hype.
```

### Venezuela fit modifier (use key `venezuela_similarity`)

```text
Context: Add/standardize a "Venezuela fit modifier" used for the Venezuela instance. Use modifier key `venezuela_similarity` (range -2 to +2). This is a modifier, not part of the base score.

Task:
1) Open `network-states/rubric/rubric.yml`.
2) Add/update `modifiers:` section with `venezuela_similarity` including description, signals, and anchor guidance for -2..+2.
3) Ensure scoring pipeline can apply this modifier optionally.

Acceptance:
- YAML validates.
- Base score and modifier are clearly separated.
```
