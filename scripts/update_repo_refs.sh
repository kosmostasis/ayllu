#!/usr/bin/env bash
# Update repo path references after rename: ayllu → AylluOS
# Run from repo root. Dry-run by default; pass --apply to actually replace.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

APPLY=false
[ "${1:-}" = "--apply" ] && APPLY=true

echo "Scanning for 'Documents/GitHub/ayllu' and 'github/ayllu'..."
grep -Rl -E "Documents/GitHub/ayllu|github/ayllu" . 2>/dev/null | grep -v ".git" | while read -r f; do
  echo "  $f"
  if [ "$APPLY" = true ]; then
    sed -i '' 's|Documents/GitHub/ayllu|Documents/GitHub/AylluOS|g' "$f"
    sed -i '' 's|github/ayllu|github/AylluOS|g' "$f"
  fi
done

if [ "$APPLY" = false ]; then
  echo ""
  echo "Dry-run. To apply: ./scripts/update_repo_refs.sh --apply"
fi
