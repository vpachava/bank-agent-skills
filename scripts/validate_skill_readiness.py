import os
from pathlib import Path
import sys

def validate_skills(repo_root):
    skills_dir = repo_root
    errors = []
    
    # Simple check: every skill dir should have a SKILL.md and tests/
    for item in skills_dir.rglob("SKILL.md"):
        skill_dir = item.parent
        if not (skill_dir / "tests").exists():
            errors.append(f"Skill missing tests/ directory: {skill_dir}")
            
    if errors:
        for err in errors:
            print(f"Validation Error: {err}")
        sys.exit(1)
    print("Skill readiness validation passed.")

if __name__ == "__main__":
    validate_skills(Path("C:/code/ai/BrainStorming/bank-agent-skills"))
