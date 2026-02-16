# Debugging process — worktree apply/merge failures

**Use this every time Cursor apply or git merge fails.**

**Part D — Canonical script paths:** Scripts already use repo-relative paths (`Path(__file__).resolve().parent.parent` in Python; `$(dirname "$0")/..` in bash). Any file targeting `/Users/.../ayllu/...` must be rewritten to `scripts/...` or other repo-relative path before applying.

---

## A0) Classify the failure

| Type | Indicators |
|------|------------|
| **A** | Absolute path / permissions (EACCES, `mkdir /Users/…`) |
| **B** | Worktree branch conflict ("main is already used by worktree…") |
| **C** | Merge conflict (Overwrite / Merge manually / Stash) |
| **D** | Patch targets missing files (nonexistent path) |

---

## A1) Inspect patch BEFORE applying

- In the apply/review panel, scan changed file paths.
- **Hard-fail:** If ANY path begins with `/Users/`, `~/`, or escapes the repo via `../` → **do NOT apply**.
- These are hard-fail indicators.

---

## A2) Normalize paths

Discard any absolute-path file ops from the patch OR rewrite to repo-relative:

| Target type | Repo-relative path |
|-------------|--------------------|
| Scripts | `scripts/…` |
| Imported external docs | `inbox/external_docs/…` |
| Cloned repos | `references/…` |
| Ops | `ops/…` |
| Docs | `docs/…` |
| Apps | `apps/…` |
| Packages | `packages/…` |
| Countries | `countries/…` |

---

## A3) Merge conflict resolution policy

- **Agent version is source of truth** → choose **Overwrite**.
- **Local changes must be preserved** → Stash → Apply/Overwrite → selectively re-apply stash.

---

## A4) Worktree sanity (terminal)

From repo root:

```bash
git worktree list
git status
git branch --show-current
```

**Rule:** Do not try to check out `main` in more than one worktree.

---

## A5) Integrate worktree changes reliably

**Prefer terminal git operations** (avoid Cursor apply if buggy):

```bash
cd $REPO_ROOT   # e.g. ~/Documents/GitHub/ayllu or AylluOS
git cherry-pick <commit_sha>
```

---

## A6) Detect absolute paths in repo content (pre-commit)

From repo root:

```bash
grep -R --line-number "/Users/" . 2>/dev/null | grep -v ".git"
```

If anything shows up (excluding `.git`), fix it before applying/merging.

---

## A7) If errors persist after A1–A6

**Stop and report back to Hermes** with:

- Exact error message
- Which step failed
- File paths involved
- Output of: `git worktree list`

---

## Part E — Escalation rule

**Stop and report to Hermes** if you encounter:

- Cursor apply-worktree continues to generate `/Users/Documents/...` (missing username)
- Merge/worktree conflicts you can't resolve with cherry-pick
- Repeated EACCES failures after path normalization

Include: exact error text, context, and `git worktree list` output.
