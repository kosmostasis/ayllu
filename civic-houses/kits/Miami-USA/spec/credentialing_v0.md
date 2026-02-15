# Credentialing v0 — protocol boundary

Specification of the **credentialing boundary** for Civic House nodes. This is a protocol boundary (issuer, revocation, disputes, privacy); not an implementation spec.

## Scope

- **Credential primitives:** Verifiable credentials / attestations (e.g. skills verification, participation history, contributions).
- **Issuance:** Who can issue which credentials; under what conditions; format (to be defined in a later technical spec).
- **Revocation:** Under what conditions credentials are revoked; who can revoke; how revocation is published and verified.
- **Disputes:** How disputes about issuance or revocation are handled; link to node dispute_resolution (mediation, escalation).
- **Privacy:** Data minimization; retention; no sensitive personal data without explicit policy. Credential content and visibility rules (e.g. what is shown to whom).

## Governance

- **Issuer policy:** Defined per node or network; must be host-nation compliant and aligned with GUARDRAILS (no representation claims).
- **Revocation policy:** Must include appeal path and tie to dispute resolution.
- **Dispute handling:** Credential disputes follow the same tiered mediation as other node disputes; escalation to host-country law when appropriate.

## Out of scope (for later)

- Specific technical implementation (e.g. VC format, blockchain, ZK).
- Issuer infrastructure or tooling.
- Network-wide credential registry (design only when needed).
