# EACCES Report for Hermes — Cursor apply-worktree path bug

**Status:** Still occurring. Need escalation path and/or fix.

---

## 1. Exact error message

```
Failed to apply worktree to current branch:
Unable to write file '/Users/Documents/GitHub/ayllu/scripts/generate_civic_house_kit.py' 
(NoPermissions (FileSystemError): Error: EACCES: permission denied, mkdir '/Users/Documents')
```

---

## 2. Root cause (confirmed)

**Path construction bug:** Cursor generates a path **missing the username**:

| Expected (correct) | Actual (bug) |
|--------------------|--------------|
| `$REPO_ROOT/...` (e.g. `~/Documents/GitHub/ayllu`) | `/Users/Documents/...` (missing username) |

When Cursor tries to write the file, it first runs `mkdir '/Users/Documents'`, which:
- Fails with EACCES (permission denied)
- Is wrong — on macOS, Documents is under `/Users/<username>/Documents`

---

## 3. Environment

| Item | Value |
|------|-------|
| **Main repo** | `$REPO_ROOT` |
| **Worktree (ccz)** | `$REPO_ROOT` (via worktree) |
| **Main branch** | `main` @ 6dc4e30 |
| **Worktree HEAD** | 2853c0b (detached) |
| **OS** | macOS (darwin) |

```
git worktree list:
$REPO_ROOT       [main]
$REPO_ROOT/ccz   (detached HEAD)
...
```

---

## 4. What we've tried

1. **Path normalization** — All patches use repo-relative paths (`ops/...`, `scripts/...`). No absolute paths in our patch content.
2. **Terminal cherry-pick** — Works when run from main repo: `cd ~/Documents/GitHub/ayllu && git cherry-pick 2853c0b`
3. **Debugging process** — Created `ops/DEBUG_WORKTREE_APPLY.md` with A0–A7 steps.
4. **Hard path rules** — GUARDRAILS, ORCHESTRATION enforce no absolute paths in outputs.

**Conclusion:** The bug is in Cursor's apply-worktree logic, not in our patch content. Our patches are already repo-relative.

---

## 5. Hypothesis to test: doc context pollution

**Idea:** Cursor may use repo file content as context when building paths. Docs that contained literal paths (e.g. `$REPO_ROOT`) could be incorrectly normalized (e.g. strips username). We sanitized to `$REPO_ROOT` placeholders.

**Test:** Use `$REPO_ROOT` or `~/Documents/GitHub/<repo>` in examples; avoid literal `/Users/...` paths.

Then retry Cursor apply. If it still fails, the bug is purely in Cursor's internal path resolution.

---

## 6. Request for Hermes

1. **Escalate to Cursor** — Report the path bug: apply-worktree generates `/Users/Documents/...` instead of `/Users/<username>/Documents/...`. Include this error message and path comparison.

2. **Workaround** — Until fixed, always use terminal:
   ```bash
   cd $REPO_ROOT   # e.g. ~/Documents/GitHub/AylluOS (after rename) or ayllu (current)
   git cherry-pick <commit_sha>
   ```

3. **Optional: sanitize docs** — Replace literal paths in `docs/`, `ops/` with placeholders to rule out context pollution.

---

## 7. Files with literal paths (candidates for sanitization)

- `docs/SESSION_SUMMARY_FOR_HERMES.md` — cherry-pick example, error documentation
- `ops/DEBUG_WORKTREE_APPLY.md` — A5 example
- `ops/RENAME_TO_AYLLUOS.md` — C3, C4 examples

Replace with `$REPO_ROOT` or `~/Documents/GitHub/AylluOS` (after rename).
