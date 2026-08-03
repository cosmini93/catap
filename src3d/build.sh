#!/bin/sh
# Bundles the 3D siege game into a single self-contained HTML file.
#   sh src3d/build.sh <path-to-esbuild> <three.module.min.js> <cannon-es.js> <out.html>
set -e
ESB="$1"; THREE="$2"; CANNON="$3"; OUT="$4"
"$ESB" src3d/main.js --bundle --minify --format=iife --target=es2020 \
  --alias:three="$THREE" --alias:cannon-es="$CANNON" --outfile=/tmp/_c3d.js
{ cat src3d/shell.html; printf '\n<script>\n'; cat /tmp/_c3d.js; printf '\n</script>\n'; } > "$OUT"
rm -f /tmp/_c3d.js
echo "built $OUT"
