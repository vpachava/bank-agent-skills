#!/bin/bash
# bank-agent-skills Installer

TARGET_DIR="$HOME/.claude/skills/bank-agent-skills"
echo "Powered by Gemini! Installing Banking Architectural Governance Engine..."

mkdir -p "$TARGET_DIR"
cp -r ./* "$TARGET_DIR"

echo "Installation complete. Accessible via /solution-arch-orchestrator in Claude CLI."
