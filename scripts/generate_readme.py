import os
import yaml
from pathlib import Path

def extract_frontmatter(content):
    if content.startswith("---"):
        end_idx = content.find("---", 3)
        if end_idx != -1:
            try:
                fm_text = content[3:end_idx]
                return yaml.safe_load(fm_text)
            except:
                pass
    return {}

root_dir = Path(".")
categories = {
    "discovery": "Discovery",
    "architecture": "Architecture",
    "greenfield": "Greenfield",
    "modernization": "Modernization",
    "migration": "Migration",
    "integration": "Integration",
    "security": "Security",
    "cloud": "Cloud",
    "devops": "DevOps",
    "documentation": "Documentation",
    "governance": "Governance",
    "wayfinder": "Wayfinder (Orchestration)",
}

# Collect all skills
skills_by_category = {k: [] for k in categories.keys()}
skills_by_category["other"] = []

for skill_file in root_dir.rglob("SKILL.md"):
    # Skip ignored dirs
    if any(p.startswith(".") and p != ".claude" for p in skill_file.parts):
        continue
    if "node_modules" in skill_file.parts or "venv" in skill_file.parts:
        continue
        
    category = skill_file.parts[0] if len(skill_file.parts) > 1 else "other"
    if category == ".claude":
        category = "other"
        
    if category not in skills_by_category:
        skills_by_category[category] = []
        
    content = skill_file.read_text(encoding="utf-8")
    fm = extract_frontmatter(content)
    
    skill_info = {
        "path": skill_file.as_posix(),
        "name": fm.get('name', skill_file.parent.name),
        "description": fm.get('description', 'No description provided.')
    }
    skills_by_category[category].append(skill_info)

# Generate README content
readme_lines = [
    "# UAE Retail-Bank Solution-Architect Skills Library",
    "",
    "Welcome to the comprehensive skills library for UAE retail-bank solution architecture. This repository contains **invoke-and-act** Claude Code skills covering the complete solution-architecture lifecycle — from initial discovery through operational readiness.",
    "",
    "## What is this library?",
    "",
    "This library is a collection of 64+ concrete, executable skills. Unlike static reference documentation, these are **active processes**. Each skill is invoked as a slash command (e.g., `/threat-model`) which triggers an interactive assessment or generation process.",
    "",
    "Each skill features:",
    "- **Embedded Checklists & Pitfalls:** Banking-specific and UAE-specific constraints, common anti-patterns, and step-by-step checklists.",
    "- **Industry-framework Grounding:** Inline and actionable alignment with BIAN, TOGAF, C4, AWS Well-Architected, Azure CAF, OWASP, NIST, SRE, and ITIL 4 frameworks.",
    "- **Concrete Deliverables:** Every skill produces an explicit artifact (e.g., a high-level design document, a risk register, a platform evaluation report).",
    "",
    "## How to Use",
    "",
    "Skills are designed to be invoked sequentially through the structural lifecycle phases of architecture. You can invoke them using their short, unprefixed names (e.g., `/solution-options`).",
    "",
    "**The Lifecycle Throughline:**",
    "1. **Discovery & Assessment (`discovery/`, `modernization/`, `greenfield/`)** -> Understand the landscape. Map capabilities, assess legacy tech debt, and evaluate candidate target platforms.",
    "2. **Planning & Strategy (`migration/`, `architecture/`)** -> Establish the blueprints and transition roadmaps. Map high-level/low-level designs, target non-functional requirements (NFRs), and sequence migration waves.",
    "3. **Secure & Integrate Early (`security/`, `integration/`)** -> Front-load risk. Enforce enterprise zero-trust, IAM best practices, API designs, and messaging models before any coding happens.",
    "4. **Platform & Validation (`cloud/`, `devops/`)** -> Ensure continuous quality and readiness. Verify well-architected cloud footprint, CI/CD checks, and release gates.",
    "5. **Governance Gates & Tracking (`governance/`, `documentation/`)** -> Manage lifecycle status. Present to architecture boards, gate production releases, and continuously maintain RAID logs and risk registers.",
    "",
    "## Catalogue",
    ""
]

for cat_code, cat_name in categories.items():
    skills = sorted(skills_by_category.get(cat_code, []), key=lambda x: x['name'])
    if not skills:
        continue
        
    readme_lines.append(f"### {cat_name}")
    for skill in skills:
        path_link = f"[{skill['name']}]({skill['path']})"
        readme_lines.append(f"- **{path_link}** — `{skill['description']}` Invoke with: `/{skill['name']}`")
    readme_lines.append("")

# Add 'other' category if present
other_skills = skills_by_category.get("other", [])
if other_skills:
    readme_lines.append("### Tooling & CI/CD")
    for skill in other_skills:
        path_link = f"[{skill['name']}]({skill['path']})"
        readme_lines.append(f"- **{path_link}** — `{skill['description']}` Invoke with: `/{skill['name']}`")
    readme_lines.append("")

readme_lines.extend([
    "## Cross-Link Navigation",
    "",
    "Each `.md` document includes a \"Related Skills\" or \"Inputs/Outputs\" section in its frontmatter metadata enabling navigation across the graph. ",
    "For example, you might flow from `/gap-analysis` -> `/solution-options` -> `/architecture-board`.",
    "",
    "**Core Orchestration:** Use `/orchestrator` located in `wayfinder/` to orchestrate agents automatically executing these sequences.",
    ""
])

Path("skills/README.md").parent.mkdir(exist_ok=True)
Path("skills/README.md").write_text("\n".join(readme_lines), encoding="utf-8")
print(f"Generated README.md at skills/README.md")
