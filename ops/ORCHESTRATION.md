# Orchestration — parallel agents and worktrees

## Roles

- **Orchestrator (main thread):** Sets acceptance criteria, merges PRs, resolves cross-stream conflicts, maintains naming/spec standards.
- **Specialist agents (parallel):**
  1. **WS1 Corpus Agent** — Plan País + MCM corpus capture, provenance, indexing, compendium.
  2. **WS2 Landscape Agent** — NS dataset ingest, enrichment, clustering, scoring.
  3. **WS3 Civic House Agent** — kits/templates, ops playbooks, credentialing boundary, generator skill.
  4. **WS4 Brand Agent** — Must read [AGENT_REQUIRED_READING.md](AGENT_REQUIRED_READING.md) (STYLE_GUIDE, GUARDRAILS).
  5. **WS5 UI/UX Agent** — Must read [AGENT_REQUIRED_READING.md](AGENT_REQUIRED_READING.md) (MOBILE_PRINCIPLES, STYLE_GUIDE, GUARDRAILS).
  6. **OS Architect Agent** — COFOG baseline + CANON meta-ministries + runtime spec spine.

## Git worktrees (concurrency primitive)

Create isolated worktrees so agents do not collide. Run from repo root:

```bash
git worktree add ../wt-os-arch -b wt/os-arch
git worktree add ../wt-ws1-corpus -b wt/ws1-corpus
git worktree add ../wt-ws2-ns -b wt/ws2-ns
git worktree add ../wt-ws3-civic -b wt/ws3-civic
```

Each worktree runs one agent. Each agent submits PRs into `main`.

## Status

See [STATUS.md](STATUS.md) for per-agent objective, last shipped, next tasks, blockers.

## Required reading

See [AGENT_REQUIRED_READING.md](AGENT_REQUIRED_READING.md) for per-agent required reading (STYLE_GUIDE, MOBILE_PRINCIPLES, GUARDRAILS, rubric).

## Path conventions

- **No absolute paths** in code, scripts, docs, or patches (e.g. no `/Users/...`, `/home/...`).
- **External docs:** Import to `inbox/external_docs/` first via `scripts/import_external_docs.sh`; reference as `inbox/external_docs/<filename>`.
- **References:** Clone into `references/` via `scripts/clone_references.sh` (repo-relative).

## Reference

Execution plan: AylluOS leadership recommendations (Cursor plan). Guardrails: [GUARDRAILS.md](GUARDRAILS.md).
