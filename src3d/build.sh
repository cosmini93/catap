#!/bin/sh
# Bundles the 3D siege game into a single self-contained HTML file.
#   npm install --no-save three@0.169.0 cannon-es@0.20.0
#   sh src3d/build.sh [out.html]
set -e
OUT="${1:-catapult3d.html}"
ESB="${ESBUILD:-npx --yes esbuild}"
$ESB src3d/main.js --bundle --minify --format=iife --target=es2020 \
  --loader:.glb=base64 --outfile=/tmp/_c3d.js
{ cat src3d/shell.html; printf '\n<script>\n'; cat /tmp/_c3d.js; printf '\n</script>\n'; } > "$OUT"
rm -f /tmp/_c3d.js
echo "built $OUT"
