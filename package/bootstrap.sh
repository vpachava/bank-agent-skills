#!/bin/bash
# Install Architectural Governance Engine
set -e

echo "Installing Architectural Governance Engine..."
mkdir -p ~/.claude/skills/

# Link skills defined in manifest
# Simplified for POC: point to local repo
REPO_ROOT=$(pwd)
ln -sf "$REPO_ROOT/skills/evidence-gate" ~/.claude/skills/evidence-gate

echo "Installation complete."
