#!/usr/bin/env bash
# Download Venezuela corpus (Plan País + MCM) into corpus dir; record provenance.
# Usage: from repo root, ./scripts/download_corpus.sh [OUT_DIR]
# Default OUT_DIR: ./venezuela/corpus (writes plan-pais/mesas, mcm under it)
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT_DIR="${1:-$REPO_ROOT/venezuela/corpus}"
mkdir -p "$OUT_DIR/plan-pais/mesas" "$OUT_DIR/mcm" "$OUT_DIR/mcm/other"

capture_time="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

# ---------------------------
# Plan País (Guaidó-era) — mesa annexes
# ---------------------------
PLAN_PAIS_MESAS=(
  "https://propuestasparaelplanpais.wordpress.com/wp-content/uploads/2019/05/propuesta-para-el-plan-pais-mesa-administracion-publica.pdf"
  "https://propuestasparaelplanpais.wordpress.com/wp-content/uploads/2019/05/propuesta-para-el-plan-pais-mesa-discapacidad.pdf"
  "https://propuestasparaelplanpais.wordpress.com/wp-content/uploads/2019/05/propuesta-para-el-plan-pais-mesa-economia-energia.pdf"
  "https://propuestasparaelplanpais.wordpress.com/wp-content/uploads/2019/05/propuesta-para-el-plan-pais-mesa-medios-de-comunicacion.pdf"
  "https://propuestasparaelplanpais.wordpress.com/wp-content/uploads/2019/05/propuesta-para-el-plan-pais-mesa-politica-social.pdf"
  "https://propuestasparaelplanpais.wordpress.com/wp-content/uploads/2019/05/propuesta-para-el-plan-pais-mesa-rrii.pdf"
  "https://propuestasparaelplanpais.wordpress.com/wp-content/uploads/2019/05/propuesta-para-el-plan-pais-mesas-educacion-cultura-ciencia-y-tecnologia.pdf"
  "https://propuestasparaelplanpais.wordpress.com/wp-content/uploads/2019/05/propuesta-para-el-plan-pais-mesa-sistema-electoral.pdf"
  "https://propuestasparaelplanpais.wordpress.com/wp-content/uploads/2019/05/propuesta-para-el-plan-pais-mesa-justicia.pdf"
)

for url in "${PLAN_PAIS_MESAS[@]}"; do
  fname=$(basename "$url")
  echo "[Plan País mesa] $fname"
  curl -L --fail "$url" -o "$OUT_DIR/plan-pais/mesas/$fname"
done

# ---------------------------
# MCM (PRIORITY)
# ---------------------------
curl -L --fail "https://conmariacorina.com/sites/default/files/2023-10/1-Plan-Vente-2023-10.pdf" \
  -o "$OUT_DIR/mcm/venezuela-tierra-de-gracia.pdf"
curl -L --fail "https://www.ventevenezuela.org/wp-inter/uploads/2025/10/Plan_para_VZLA_EGU_y_MCM.pdf" \
  -o "$OUT_DIR/mcm/plan-para-vzla-egu-mcm.pdf"
curl -L --fail "https://www.ventevenezuela.org/wp-inter/uploads/2016/11/SE-TRATA-DE-LA-LIBERTAD.pdf" \
  -o "$OUT_DIR/mcm/se-trata-de-la-libertad.pdf"
curl -L --fail "https://conmariacorina.com/es/programa-de-gobierno" \
  -o "$OUT_DIR/mcm/plan-de-gobierno-landing.html"

# ---------------------------
# Provenance: compute sha256 and write provenance.yml per folder
# ---------------------------
_provenance_file() {
  local dir="$1"
  local classification="$2"
  echo "version: 0.1
classification: $classification
capture_time: $capture_time
files:" > "$dir/provenance.yml"
  for f in "$dir"/*.pdf "$dir"/*.html 2>/dev/null; do
    [ -f "$f" ] || continue
    b="$(basename "$f")"
    h="$(shasum -a 256 "$f" | cut -d' ' -f1)"
    echo "  - file: $b" >> "$dir/provenance.yml"
    echo "    sha256: $h" >> "$dir/provenance.yml"
  done
}

_provenance_file "$OUT_DIR/mcm" "MCM"
# Plan País: mesas are in plan-pais/mesas/
echo "version: 0.1
classification: Plan País
capture_time: $capture_time
files:" > "$OUT_DIR/plan-pais/provenance.yml"
for f in "$OUT_DIR/plan-pais/mesas"/*.pdf 2>/dev/null; do
  [ -f "$f" ] || continue
  b="$(basename "$f")"
  h="$(shasum -a 256 "$f" | cut -d' ' -f1)"
  echo "  - file: mesas/$b" >> "$OUT_DIR/plan-pais/provenance.yml"
  echo "    sha256: $h" >> "$OUT_DIR/plan-pais/provenance.yml"
done

echo "Done → $OUT_DIR (provenance written in plan-pais/provenance.yml and mcm/provenance.yml)"
