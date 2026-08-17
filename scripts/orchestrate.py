import sys
import os
import re
from pathlib import Path
from core_parser import parse_frontmatter, format_skill_content
from lineage_validator import load_taxonomy_artifacts, validate_workflow_lineage

def cmd_validate():
    """Validates all skills frontmatter and workflow composition lineages."""
    success = True
    taxonomy = load_taxonomy_artifacts()

    # 1. Validate all 72 skills SKILL.md frontmatters
    skills_root = Path(".")
    print("Validating architectural skills...")
    for parent, _, filenames in os.walk(skills_root):
        # Ignore sandbox and temporary git directories
        if ".claude" in parent or ".scratch" in parent or "graphify-out" in parent:
            continue
        if "SKILL.md" in filenames:
            skill_id = Path(parent).relative_to(skills_root).as_posix()
            skill_path = Path(parent) / "SKILL.md"
            content = skill_path.read_text(encoding="utf-8")
            meta, errors = parse_frontmatter(content)

            if errors:
                print(f"Error in Skill metadata '{skill_id}':")
                for err in errors:
                    print(f"  - {err}")
                success = False

    # 2. Validate all workflows in workflows/
    workflows_root = Path("workflows")
    print("Validating workflows...")
    if workflows_root.exists():
        for wf_file in workflows_root.glob("*.yaml"):
            errors = validate_workflow_lineage(wf_file, taxonomy)
            if errors:
                print(f"Error in Workflow '{wf_file.name}':")
                for err in errors:
                    print(f"  - {err}")
                success = False

    if success:
        print("Success: All skills and workflows verified successfully against frameworks schemas.")
    return success

def cmd_report():
    """Generates the TOGAF-BIAN-Coverage.md report."""
    print("Generating TOGAF/BIAN coverage report...")
    report = "# TOGAF and BIAN Coverage Mapping Report\n\n"
    report += "| Skill | TOGAF Phase | TOGAF Artifact | BIAN Service Domain |\n"
    report += "|-------|-------------|----------------|---------------------|\n"

    skills_root = Path(".")
    skills_found = False

    # Safely scan directories
    for parent, _, filenames in os.walk(skills_root):
        if ".claude" in parent or ".scratch" in parent or "graphify-out" in parent:
            continue
        if "SKILL.md" in filenames:
            skill_name = Path(parent).name
            skill_path = Path(parent) / "SKILL.md"
            content = skill_path.read_text(encoding="utf-8")
            meta, _ = parse_frontmatter(content)

            phases = ", ".join(meta.get("togaf-phases", [])) or "N/A"
            artifacts = ", ".join(meta.get("togaf-artifacts", [])) or "N/A"
            domains = ", ".join(meta.get("bian-service-domains", [])) or "N/A"

            report += f"| {skill_name} | {phases} | {artifacts} | {domains} |\n"
            skills_found = True

    if not skills_found:
        print("Warning: No skills found for coverage mapping.")

    Path("TOGAF-BIAN-Coverage.md").write_text(report, encoding="utf-8")
    print("Report written successfully to TOGAF-BIAN-Coverage.md")
    return True

def cmd_format():
    """Formats all frontmatters for skills in the project."""
    print("Formatting and resolving metadata for skills...")
    skills_root = Path(".")
    success = True
    formatted_count = 0
    for parent, _, filenames in os.walk(skills_root):
        if ".claude" in parent or ".scratch" in parent or "graphify-out" in parent:
            continue
        if "SKILL.md" in filenames:
            skill_path = Path(parent) / "SKILL.md"
            try:
                content = skill_path.read_text(encoding="utf-8")
                new_content, modified = format_skill_content(content, str(skill_path.resolve()))
                if modified:
                    skill_path.write_text(new_content, encoding="utf-8")
                    print(f"Formatted and updated metadata in: {skill_path}")
                    formatted_count += 1
            except Exception as e:
                print(f"Error formatting {skill_path}: {e}")
                success = False

    print(f"Metadata format operation finished. Updated {formatted_count} files.")
    return success

def show_usage():
    print("Usage: python scripts/orchestrate.py <command>")
    print("Commands:")
    print("  validate    Run schema and lineage validations")
    print("  report      Generate coverage mapping mapping report")
    print("  format      Inject or fix metadata in the skill SKILL.md frontmatters")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_usage()
        sys.exit(1)

    cmd = sys.argv[1].lower()
    if cmd == "validate":
        if not cmd_validate():
            sys.exit(1)
    elif cmd == "report":
        cmd_report()
    elif cmd == "format":
        if not cmd_format():
            sys.exit(1)
    else:
        print(f"Unknown command: '{cmd}'")
        show_usage()
        sys.exit(1)
