# Skill: compendium-synthesizer

Produce or update the Plan País compendium from corpus content; include “what’s missing relative to AylluOS”.

## Inputs

- `venezuela/corpus/plan-pais/` (mesa PDFs) or extracted text
- `venezuela/spec/plan-pais_compendium.md` (current compendium)
- AylluOS reference: ayllu/spec/COUNTRY_RUNTIME_SPEC.md, ayllu/taxonomy, ayllu/practices

## Outputs

- `venezuela/spec/plan-pais_compendium.md` (updated with executive summaries and key policies per mesa; annex “What’s missing relative to AylluOS” filled)

## Steps

1. For each mesa PDF in corpus, extract text (e.g. pdftotext or cloud extraction).
2. For each mesa section in compendium, paste or summarize: Executive summary, Key policies (bullets).
3. Fill Cross-cutting: sequencing, institutional anchor, resource/budget if mentioned.
4. Fill Annex “What’s missing relative to AylluOS”: COFOG mapping, practice standards gaps, CRC vs Plan País, credentialing/Civic House.

## Commands

- No single script; use extraction tool + manual or Cursor edit. Future: script that takes extracted text dir and compendium path.

## Quality checklist

- [ ] Every mesa (1–9) has at least placeholder or content for Executive summary and Key policies.
- [ ] Annex compares Plan País to AylluOS (COFOG, practices, runtime, credentialing).
- [ ] No representation claims; language aligns with GUARDRAILS.

## Failure modes

- PDF extraction fails: ensure pdftotext or alternative; may need manual copy-paste.
- Source URLs change: corpus may need re-download; compendium references corpus paths.
