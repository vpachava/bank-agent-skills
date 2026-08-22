#!/usr/bin/env python3
"""
Interactive Installation Wizard for bank-agent-skills.
Detects OS, runtime environment, configures user profiles, and installs skills.
"""

import os
import sys
import json
import shutil
import platform
from pathlib import Path

def print_banner():
    print("=" * 60)
    print("  BANK-AGENT-SKILLS: Interactive Installation Wizard (v1.2.0)")
    print("=" * 60)

def detect_environment():
    system = platform.system()
    home = Path.home()
    
    claude_dir = home / ".claude" / "skills"
    hermes_dir = home / ".hermes" / "skills"
    
    print(f"[+] Detected OS: {system} ({platform.release()})")
    print(f"[+] User Home Directory: {home}")
    
    env_info = {
        "system": system,
        "home": str(home),
        "claude_installed": claude_dir.parent.exists(),
        "hermes_installed": hermes_dir.parent.exists()
    }
    return env_info

def prompt_installation_mode(env):
    print("\nSelect Installation Mode:")
    print("  1) Global (Install to ~/.claude/skills/bank-agent-skills)")
    print("  2) Hermes Agent (Install to ~/.hermes/skills/bank-agent-skills)")
    print("  3) Project-Local (Install to current working directory)")
    
    choice = input("Enter choice [1-3] (default: 1): ").strip() or "1"
    
    home = Path(env["home"])
    if choice == "2":
        return home / ".hermes" / "skills" / "bank-agent-skills"
    elif choice == "3":
        return Path.cwd() / "bank-agent-skills"
    else:
        return home / ".claude" / "skills" / "bank-agent-skills"

def configure_user_profile(config_dir: Path):
    print("\n--- User Profile & Jurisdiction Setup ---")
    print("Select Default Regulatory Jurisdiction:")
    print("  1) UAE (CBUAE + PDPL)")
    print("  2) KSA (SAMA + NDMO)")
    print("  3) EU (DORA + GDPR)")
    print("  4) Global Baseline (Basel III / ISO 20022)")
    
    j_choice = input("Enter choice [1-4] (default: 1): ").strip() or "1"
    jurisdictions = { "1": "UAE", "2": "KSA", "3": "EU", "4": "Global" }
    selected_jurisdiction = jurisdictions.get(j_choice, "UAE")
    
    profile = {
        "jurisdiction": selected_jurisdiction,
        "preferred_frameworks": ["TOGAF", "BIAN", "C4"],
        "auto_evidence_gate": True
    }
    
    config_dir.mkdir(parents=True, exist_ok=True)
    profile_path = config_dir / "profile.json"
    with open(profile_path, "w", encoding="utf-8") as f:
        json.dump(profile, f, indent=4)
        
    print(f"[+] Profile saved to {profile_path} (Jurisdiction: {selected_jurisdiction})")

def main():
    print_banner()
    env = detect_environment()
    
    target_dir = prompt_installation_mode(env)
    print(f"\n[+] Target Installation Directory: {target_dir}")
    
    # Copy files
    source_dir = Path(__file__).resolve().parent
    print("[+] Copying skills library...")
    
    target_dir.mkdir(parents=True, exist_ok=True)
    
    # Exclude unwanted directories during install
    excludes = {".git", ".scratch", ".superpowers", ".pytest_cache", "__pycache__"}
    
    for item in source_dir.iterdir():
        if item.name in excludes:
            continue
        dest = target_dir / item.name
        if item.is_dir():
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(item, dest)
        else:
            shutil.copy2(item, dest)
            
    print(f"[✓] Successfully installed bank-agent-skills to {target_dir}")
    
    # Post-install config
    home = Path(env["home"])
    config_dir = home / ".bank-agent-skills"
    configure_user_profile(config_dir)
    
    print("\n" + "=" * 60)
    print("  Installation Complete! Entry point: /solution-arch-orchestrator")
    print("=" * 60)

if __name__ == "__main__":
    main()
