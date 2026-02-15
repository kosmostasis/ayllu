#!/usr/bin/env bash
# Clone reference repos into references/ (read-only). Run from repo root.
set -euo pipefail
REF_DIR="$(cd "$(dirname "$0")/.." && pwd)/references"
mkdir -p "$REF_DIR"
cd "$REF_DIR"
for repo in \
  "https://github.com/Bit-Nation/BITNATION-Framework" \
  "https://github.com/compdemocracy/polis" \
  "https://github.com/liminalvillage/liminalvillage" \
  "https://github.com/thenetworkstate/network-states-of-the-internet" \
  "https://github.com/GSA/participation-playbook"; do
  name=$(basename "$repo")
  if [ -d "$name" ]; then
    echo "[skip] $name (already exists)"
  else
    echo "[clone] $repo"
    git clone --depth 1 "$repo" "$name" || true
  fi
done
echo "Done → $REF_DIR"
