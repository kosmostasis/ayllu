#!/usr/bin/env bash
set -euo pipefail

OUT_DIR=${1:-"./downloads"}
mkdir -p "$OUT_DIR/plan-pais/mesas" "$OUT_DIR/mcm" "$OUT_DIR/mcm/other"

# ---------------------------
# Plan País (Guaidó-era) — mesa annexes (WordPress corpus)
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
# María Corina Machado (PRIORITY) — core PDFs
# ---------------------------
# "Venezuela Tierra de Gracia" (government program)
curl -L --fail "https://conmariacorina.com/sites/default/files/2023-10/1-Plan-Vente-2023-10.pdf" \
  -o "$OUT_DIR/mcm/venezuela-tierra-de-gracia.pdf"

# "Plan para VZLA" (EGU + MCM) — economic launch plan
curl -L --fail "https://www.ventevenezuela.org/wp-inter/uploads/2025/10/Plan_para_VZLA_EGU_y_MCM.pdf" \
  -o "$OUT_DIR/mcm/plan-para-vzla-egu-mcm.pdf"

# "Se trata de la libertad" (Vente document)
curl -L --fail "https://www.ventevenezuela.org/wp-inter/uploads/2016/11/SE-TRATA-DE-LA-LIBERTAD.pdf" \
  -o "$OUT_DIR/mcm/se-trata-de-la-libertad.pdf"

# Program landing page (HTML) for additional linked downloads
curl -L --fail "https://conmariacorina.com/es/programa-de-gobierno" \
  -o "$OUT_DIR/mcm/plan-de-gobierno-landing.html"

# Zip it
cd "$OUT_DIR"
zip -r "venezuela_plans_bundle.zip" plan-pais mcm

echo "Done → $OUT_DIR/venezuela_plans_bundle.zip"
