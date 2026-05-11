#!/usr/bin/env bash
set -euo pipefail
PORT="${1:-8080}"
echo "Starting Mobile Web Runner on http://0.0.0.0:${PORT}"
python3 -m http.server "$PORT" --bind 0.0.0.0
