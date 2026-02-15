# Rubric consistency checklist

For each axis under `axes:`:

- [ ] has `name`, `weight`, `description`
- [ ] has `signals_positive` and `signals_negative` lists
- [ ] has `scoring_anchors` with keys 0..5
- [ ] has `measurement_notes` list
- [ ] wording is evidence-based; avoid hype language
- [ ] if data is sparse, include a conservative scoring note (cap at 3)

Modifiers live under `modifiers:` and must not be mixed into base axes.
