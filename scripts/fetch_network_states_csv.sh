#!/usr/bin/env bash
set -euo pipefail
OUT_DIR=${1:-"./downloads"}
mkdir -p "$OUT_DIR/network-states"

curl -L --fail \
  "https://raw.githubusercontent.com/thenetworkstate/network-states-of-the-internet/main/societies.csv" \
  -o "$OUT_DIR/network-states/societies.csv"

echo "Saved → $OUT_DIR/network-states/societies.csv"
