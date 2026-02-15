# ux/MOBILE_PRINCIPLES.md (Required reading for WS5 UI/UX Agent)

## 0) Product posture
Venezuela AylluOS instance is **serious civic infrastructure**: credibility-first, minimal, intuitive.

Primary job: help people contribute **knowledge, capital, and network** into national areas (COFOG-like), grounded through **Civic Houses**.

## 1) Mobile-first commandments
1) **One next action per screen**  
2) **Progressive disclosure** (basic view calm; advanced controls hidden)  
3) **Fast comprehension** (scan in 3 seconds; act in 10)  
4) **Trust cues always visible** for claims/rankings (source, confidence, method)  
5) **Low-friction contribution**: capture now, structure later  
6) **No critical-path poetry**: critical flows are plain language

## 2) Information Architecture (IA) — minimum viable
### Top navigation (3 primary modes)
- **Contribute**
- **Areas**
- **Civic Houses**

### Home (default)
Prompt: **"Where can you help today?"**
Three tiles:
- Contribute Knowledge
- Contribute Capital
- Contribute Network

Below: National Areas cards (Education, Health, Justice, Infrastructure, etc.)

## 3) The "Area" page pattern (repeatable template)
Every Area page shows:
- A short description (1–2 lines)
- **Three contribution tabs**: Knowledge / Capital / Network
- Current initiatives (small list)
- Related Civic Houses (nearby or relevant)
- Latest outcomes / evidence (if any)

## 4) Contribution flows (v0)
### Knowledge
- Add note / link / dataset / translation
- Tag to Area + subtopic
- Optional: attach sources
- Output: a contribution object with provenance metadata

### Capital
- Pick a micro-fund or initiative
- Show budget transparency (what's needed, what's funded)
- Confirm payment flow (keep minimal; avoid holding sensitive info)
- Output: transaction record + earmark

### Network
- Structured intro form (who/why/what offered)
- Consent checkbox + visibility selection
- Output: intro request + status tracking (met / in progress / shipped)

## 5) Civic Houses: the hyperlocal bridge
Civic House page shows:
- Location + host partner
- Services offered (directory)
- Upcoming events
- Active pilots and outcomes
- "Start a Civic House" CTA (kit generator)

## 6) Trust & verification UX
For anything "ranked", "verified", or "computed":
- **Source** (link or captured artifact reference)
- **Confidence** (A/B/C) based on completeness
- **Method** ("scored by rubric vX", "validated by attestations", etc.)
- "Dispute / report" path for corrections

## 7) Design system constraints
- Typography-first hierarchy
- No hidden navigation gimmicks
- Use subtle motion only for orientation and state change
- Accessibility: readable contrast, tap targets, predictable layouts

## 8) Required reading for WS5
- This file
- `brand/STYLE_GUIDE.md`
- `ops/GUARDRAILS.md`
- `ayllu/runtime/templates/country.template.yml`
- `network-states/rubric/rubric.yml`
