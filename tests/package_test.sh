#!/bin/bash
set -e

# Run bootstrap
./package/bootstrap.sh

# Verify skills installed (expand tilde)
TARGET_DIR="$HOME/.claude/skills/evidence-gate"
if [ -L "$TARGET_DIR" ] || [ -d "$TARGET_DIR" ]; then
    echo "Validation Successful"
else
    echo "Validation directory: $(ls -ld $HOME/.claude/skills/evidence-gate 2>&1)"
    echo "Validation Failed"
    exit 1
fi
