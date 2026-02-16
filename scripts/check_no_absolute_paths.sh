#!/usr/bin/env bash
# Fail if staged diff contains /Users/ (absolute path). Run from repo root.
# Usage: ./scripts/check_no_absolute_paths.sh
# Use as pre-commit hook or in CI.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

# Check staged diff only (what would be committed)
if git diff --cached --name-only | grep -q .; then
  if git diff --cached | grep -qE '^\+.*/Users/'; then
    echo "ERROR: Staged diff contains /Users/ (absolute path). Use repo-relative paths only." >&2
    echo "See ops/GUARDRAILS.md and ops/DEBUG_WORKTREE_APPLY.md" >&2
    git diff --cached | grep -nE '^\+.*/Users/' || true
    exit 1
  fi
fi
exit 0
