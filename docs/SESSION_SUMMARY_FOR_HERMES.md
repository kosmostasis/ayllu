# Session summary for Hermes (ChatGPT)

**Date:** Feb 16, 2026  
**Context:** AylluOS Venezuela MVP — implementation, path normalization, readiness check, and integration issues.

---

## 1. What was done

### Implementation (Leadership recs plan)
- **Phase 1:** Created `brand/STYLE_GUIDE.md`, `ux/MOBILE_PRINCIPLES.md`, `ops/AGENT_REQUIRED_READING.md`; added WS4/WS5 to ORCHESTRATION and STATUS.
- **Phase 2:** Created `network-states/rubric/AXIS_KEYS.md`, `AXIS_EDIT_PROMPTS.md`, `AXIS_SNIPPETS.yml`, `RUBRIC_SCHEMA_CHECKLIST.md`; expanded `rubric.yml` to v0.3 with full schema and `cosmo_localism` axis; updated `scripts/ns_ingest_score.py` and `scripts/score_network_states.py` to include `cosmo_localism` in Score and heuristic.
- **Phase 3:** Added Cosmo-Localism and d/acc to README, venezuela/README, venezuela/blueprint/one_liner; confirmed guardrail logging in GUARDRAILS.

### Path normalization
- Created `inbox/external_docs/` with README; `scripts/import_external_docs.sh` for importing external docs.
- Added path conventions to `ops/GUARDRAILS.md` and `ops/ORCHESTRATION.md`: no absolute paths; external docs → `inbox/external_docs/`; references → `references/` via clone script.

### Readiness check
- Created `ops/READINESS.md` with launch gates, blockers, and evidence paths for Venezuela MVP.

---

## 2. Errors encountered

### Error A: Cursor "apply worktree to current branch" — path bug
**Message:** `Failed to apply worktree to current branch: Unable to write file '/Users/Documents/GitHub/ayllu/scripts/generate_civic_house_kit.py' (EACCES: permission denied, mkdir '/Users/Documents')`

**Root cause:** Cursor IDE constructs the target path incorrectly. The path is missing the username:
- **Expected:** `/Users/knobs/Documents/GitHub/ayllu/...`
- **Actual:** `/Users/Documents/GitHub/ayllu/...`

When Cursor tries to write the file, it attempts `mkdir '/Users/Documents'`, which fails with EACCES (and is wrong — Documents lives under `/Users/<username>/`).

**Workaround:** Use Git from the terminal instead of Cursor's apply-worktree action.

---

### Error B: Git merge — worktree conflict
**Message:** `fatal: 'main' is already used by worktree at '/Users/knobs/Documents/GitHub/ayllu'`

**Context:** User committed changes in the `ccz` worktree (`/Users/knobs/.cursor/worktrees/ayllu/ccz`), then tried `git checkout main` and `git merge ccz` from that same worktree.

**Root cause:** `main` is checked out in the main repo at `/Users/knobs/Documents/GitHub/ayllu`. A branch can only be checked out in one worktree at a time. The `ccz` worktree is in detached HEAD (commit `2853c0b`).

**Workaround:** Cherry-pick from the main repo:
```bash
cd /Users/knobs/Documents/GitHub/ayllu
git cherry-pick 2853c0b
```

---

## 3. Current state

| Item | Status |
|------|--------|
| **Commit 2853c0b** | In `ccz` worktree (detached HEAD): "Path conventions, inbox, readiness" |
| **Files in commit** | `ops/GUARDRAILS.md`, `ops/ORCHESTRATION.md`, `inbox/external_docs/README.md`, `ops/READINESS.md`, `scripts/import_external_docs.sh` |
| **Integration into main** | Pending — needs `git cherry-pick 2853c0b` from main repo |
| **Earlier implementation** | May already be on main from prior sessions; verify with `git log` |

---

## 4. Next steps for Hermes

1. **Integrate commit 2853c0b into main** (from main repo):
   ```bash
   cd /Users/knobs/Documents/GitHub/ayllu
   git cherry-pick 2853c0b
   ```

2. **Report Cursor path bug** — The apply-worktree feature generates `/Users/Documents/...` instead of `/Users/<username>/Documents/...`. Worth reporting to Cursor with the error message and path comparison.

3. **Readiness follow-up** — `ops/READINESS.md` lists launch gates and blockers. Top 5: CRC not wired, compendium/diff_map empty, no CI, no trust/safety in app, no deployment pipeline.
