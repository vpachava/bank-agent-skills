#!/usr/bin/env bash
# scripts/quick-diff.sh
# Fast diff scoped to a specific folder to reduce token load on agents.
# Usage:
#   ./scripts/quick-diff.sh                  # diff tickets/ folder against HEAD
#   ./scripts/quick-diff.sh architecture/    # diff any folder against HEAD
#   ./scripts/quick-diff.sh tickets/ main    # diff tickets/ against a specific branch

set -euo pipefail

FOLDER="${1:-solution-arch-orchestrator/tickets/}"
BASE="${2:-HEAD}"

echo "=== diff: $FOLDER vs $BASE ==="
git diff "$BASE" -- "$FOLDER"
