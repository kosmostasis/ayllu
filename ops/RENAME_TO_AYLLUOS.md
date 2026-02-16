# Rename repo: ayllu → AylluOS

**Goal:** Eliminate ayllu/ayllu confusion. Run steps in order.

---

## C0) Confirm current remote

```bash
git remote -v
```

---

## C1) Rename on GitHub

1. Repo **Settings** → **General**
2. **Repository name** → Rename to: **AylluOS**
3. Confirm

---

## C2) Update local remote URL

From repo root (before or after folder rename):

```bash
git remote set-url origin git@github.com:<ORG_OR_USER>/AylluOS.git
git remote -v
```

Replace `<ORG_OR_USER>` with your GitHub org or username.

---

## C3) Rename local folder (recommended)

```bash
cd ~/Documents/GitHub
mv ayllu AylluOS
cd AylluOS
```

---

## C4) Re-open repo in Cursor

- Close the old repo
- Open: `~/Documents/GitHub/AylluOS`

---

## C5) Worktrees cleanup (if needed)

```bash
git worktree list
git worktree prune   # removes stale worktree refs
```

If worktrees point to old paths, remove and re-add:

```bash
git worktree remove <path>   # for each stale worktree
git worktree add ../wt-name -b wt/branch-name
```

---

## C6) Update internal references

Run the update script (dry-run first):

```bash
./scripts/update_repo_refs.sh        # dry-run: list files
./scripts/update_repo_refs.sh --apply   # apply replacements
```

Or search manually:

```bash
grep -R --line-number "Documents/GitHub/ayllu" . 2>/dev/null | grep -v ".git"
grep -R --line-number "github/ayllu" . 2>/dev/null | grep -v ".git"
```

Replace with **AylluOS** in:
- Docs that prescribe future paths (e.g. cherry-pick examples)
- Config files
- Scripts (if any hardcode the repo name)

**Note:** Historical docs (e.g. SESSION_SUMMARY_FOR_HERMES.md) that document past errors may keep the old path for accuracy; update only if they prescribe future commands.

---

## Post-rename verification

```bash
git remote -v          # should show AylluOS
git worktree list      # paths may still show ayllu until worktrees are recreated
pwd                    # should be .../AylluOS
```
