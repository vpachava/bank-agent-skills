#!/bin/bash
# bank-agent-skills Installer for Hermes Agent and Claude Code

echo "Installing Banking Architectural Governance Engine (bank-agent-skills v1.2.0)..."

# Detect home paths across OS/Windows MSYS
HOME_DIR="${HOME:-$USERPROFILE}"

# Target paths
HERMES_SKILLS_DIR="$HOME_DIR/.hermes/skills/bank-agent-skills"
HERMES_WIN_DIR="$HOME_DIR/AppData/Local/hermes/skills/bank-agent-skills"
CLAUDE_SKILLS_DIR="$HOME_DIR/.claude/skills/bank-agent-skills"

INSTALLED=0

if [ -d "$HOME_DIR/.hermes" ]; then
    mkdir -p "$HERMES_SKILLS_DIR"
    cp -r ./* "$HERMES_SKILLS_DIR/"
    echo "✓ Installed to Hermes Agent ($HERMES_SKILLS_DIR)"
    INSTALLED=1
fi

if [ -d "$HOME_DIR/AppData/Local/hermes" ]; then
    mkdir -p "$HERMES_WIN_DIR"
    cp -r ./* "$HERMES_WIN_DIR/"
    echo "✓ Installed to Hermes Agent Windows ($HERMES_WIN_DIR)"
    INSTALLED=1
fi

if [ -d "$HOME_DIR/.claude" ]; then
    mkdir -p "$CLAUDE_SKILLS_DIR"
    cp -r ./* "$CLAUDE_SKILLS_DIR/"
    echo "✓ Installed to Claude Code CLI ($CLAUDE_SKILLS_DIR)"
    INSTALLED=1
fi

if [ $INSTALLED -eq 0 ]; then
    mkdir -p "$CLAUDE_SKILLS_DIR"
    cp -r ./* "$CLAUDE_SKILLS_DIR/"
    echo "✓ Default installed to $CLAUDE_SKILLS_DIR"
fi

echo "Installation complete! Entry point: /solution-arch-orchestrator"
