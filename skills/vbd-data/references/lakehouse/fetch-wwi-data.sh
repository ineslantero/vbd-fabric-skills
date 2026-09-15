#!/usr/bin/env bash
set -euo pipefail
URL="https://assetsprod.microsoft.com/en-us/wwi-sample-dataset.zip"
OUT="$(dirname "$0")/wwi-sample-dataset.zip"
if [[ -f "$OUT" ]]; then echo "Already downloaded: $OUT"; exit 0; fi
echo "Downloading WWI sample dataset (~1.9 GB)..."
curl -L --fail --output "$OUT" "$URL"
echo "Done: $OUT"
