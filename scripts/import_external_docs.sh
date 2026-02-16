#!/usr/bin/env bash
# Import external docs into inbox/external_docs/. Run from repo root.
# No absolute paths in this script; use $HOME or env vars only.
#
# Usage:
#   ./scripts/import_external_docs.sh                    # uses SOURCES or EXTERNAL_DOCS_DIR
#   ./scripts/import_external_docs.sh /path/to/file.md  # copies given file(s)
#   EXTERNAL_DOCS_DIR=~/Desktop/OS ./scripts/import_external_docs.sh
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
INBOX="$REPO_ROOT/inbox/external_docs"
mkdir -p "$INBOX"

# Sources: add paths here. Use $HOME or env vars; no hardcoded /Users/... paths.
SOURCES=()

# Optional: read from env if set (e.g. EXTERNAL_DOCS_DIR=~/Desktop/Venezuelan\ Affairs/OS)
if [ -n "${EXTERNAL_DOCS_DIR:-}" ]; then
  for f in "$EXTERNAL_DOCS_DIR"/*.md "$EXTERNAL_DOCS_DIR"/*.yml 2>/dev/null; do
    [ -f "$f" ] && SOURCES+=("$f")
  done
fi

# If args given, use those as sources
if [ $# -gt 0 ]; then
  SOURCES=("$@")
fi

for src in "${SOURCES[@]}"; do
  if [ -f "$src" ]; then
    name=$(basename "$src")
    cp "$src" "$INBOX/$name"
    echo "[imported] $name"
  else
    echo "[skip] $src (not found)" >&2
  fi
done

echo "Done → inbox/external_docs/"
