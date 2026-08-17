import os
import sys
from pathlib import Path

# Import the dictionaries
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
try:
    from dict_devops_discovery import DEVOPS_DISCOVERY
    from dict_doc_gov import DOC_GOV
    from inject_anti_patterns import ANTI_PATTERNS
except ImportError as e:
    print(f"Error importing dictionaries: {e}")
    sys.exit(1)

# Combine all dictionaries
all_anti_patterns = {}
all_anti_patterns.update(DEVOPS_DISCOVERY)
all_anti_patterns.update(DOC_GOV)
all_anti_patterns.update(ANTI_PATTERNS)

# Read workspace to list all skills
from workspace import Workspace
ws = Workspace('.')
skills = ws.list_skills()

print(f"Found {len(skills)} skills in workspace.")
print(f"Found {len(all_anti_patterns)} anti-pattern definitions.")

missing = []
applied = 0
for skill_id, skill in skills.items():
    if skill_id in all_anti_patterns:
        # Check if already applied
        skill_path = Path(skill_id) / "SKILL.md"
        content = skill_path.read_text(encoding="utf-8")
        if "## Anti-patterns" not in content:
            new_content = content.rstrip() + "\n\n" + all_anti_patterns[skill_id] + "\n"
            skill_path.write_text(new_content, encoding="utf-8")
            print(f"Applied anti-patterns to {skill_id}")
            applied += 1
        else:
            print(f"Anti-patterns already present in {skill_id}")
    else:
        missing.append(skill_id)

if missing:
    print(f"\nMissing anti-patterns for {len(missing)} skills:")
    for m in sorted(missing):
        print(f"  - {m}")
        
print(f"\nSuccessfully applied to {applied} skills.")
