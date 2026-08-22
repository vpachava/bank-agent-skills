import os
import json
import yaml
from pathlib import Path

# Base directory for skills
SKILLS_DIR = "."

def parse_skill(file_path):
    print(f"Reading: {file_path}")
    # Use utf-8-sig to handle optional BOM
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        content = f.read()
        # Extract YAML frontmatter
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 2:
                try:
                    metadata = yaml.safe_load(parts[1])
                    return metadata
                except yaml.YAMLError as exc:
                    print(f"Error parsing YAML in {file_path}: {exc}")
        else:
            print(f"No frontmatter found in {file_path}")
    return None

def generate_index():
    index = []
    print("Starting registry generation...")
    # Recursively find all SKILL.md files
    print(f"Walking SKILLS_DIR: {SKILLS_DIR}")
    for root, dirs, files in os.walk(SKILLS_DIR):
        # Exclude directories
        if '.git' in dirs:
            dirs.remove('.git')
        if '.claude' in dirs:
            dirs.remove('.claude')

        for file in files:
            if file == "SKILL.md":
                file_path = os.path.join(root, file)
                metadata = parse_skill(file_path)
                if metadata:
                    # Enrich metadata
                    skill_entry = {
                        "name": metadata.get("name", "Unknown"),
                        "category": metadata.get("category", "Uncategorized"),
                        "description": metadata.get("description", ""),
                        "tags": metadata.get("tags", []),
                        "togaf-phases": metadata.get("togaf-phases", []),
                        "bian-domains": metadata.get("bian-domains", []),
                        "regulatory-references": metadata.get("regulatory-references", []),
                        "related-skills": metadata.get("related-skills", []),
                        "usage-count": 0 # Placeholder
                    }
                    index.append(skill_entry)
                    print(f"Index created for {skill_entry['name']}")

    print(f"Registry generation complete. Indexed {len(index)} skills.")
    with open("skills-index.json", "w", encoding='utf-8') as f:
        json.dump(index, f, indent=2)

if __name__ == "__main__":
    generate_index()
