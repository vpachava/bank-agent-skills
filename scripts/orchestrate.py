import sys
from pathlib import Path
from workspace import Workspace

def cmd_validate():
    """Validates all skills frontmatter and workflow composition lineages."""
    success = True
    workspace = Workspace(".")
    taxonomy = workspace.load_taxonomy()

    # 1. Validate all 72 skills SKILL.md frontmatters
    print("Validating architectural skills...")
    skills = workspace.list_skills()
    for skill_id, skill in skills.items():
        if skill.errors:
            print(f"Error in Skill metadata '{skill_id}':")
            for err in skill.errors:
                print(f"  - {err}")
            success = False

    # 2. Validate all workflows in workflows/
    print("Validating workflows...")
    workflows = workspace.list_workflows()
    for wf_name, wf in workflows.items():
        errors = wf.validate_lineage(taxonomy, skill_resolver=workspace.get_skill)
        if errors:
            print(f"Error in Workflow '{wf_name}':")
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

    workspace = Workspace(".")
    skills = workspace.list_skills()
    skills_found = False

    for skill_id, skill in skills.items():
        skill_name = Path(skill_id).name
        phases = ", ".join(skill.metadata.get("togaf-phases", [])) or "N/A"
        artifacts = ", ".join(skill.metadata.get("togaf-artifacts", [])) or "N/A"
        domains = ", ".join(skill.metadata.get("bian-service-domains", [])) or "N/A"

        report += f"| {skill_name} | {phases} | {artifacts} | {domains} |\n"
        skills_found = True

    if not skills_found:
        print("Warning: No skills found for coverage mapping.")

    # Write report
    report_file = Path("TOGAF-BIAN-Coverage.md")
    report_file.write_text(report, encoding="utf-8")
    print("Report written successfully to TOGAF-BIAN-Coverage.md")
    return True

def cmd_format():
    """Formats all frontmatters for skills in the project."""
    print("Formatting and resolving metadata for skills...")
    workspace = Workspace(".")
    success = True
    formatted_count = 0
    skills = workspace.list_skills()

    for skill_id, skill in skills.items():
        try:
            new_content, modified = skill.format_content()
            if modified:
                workspace.write_skill(skill_id, new_content)
                skill_path = Path(skill_id) / "SKILL.md"
                print(f"Formatted and updated metadata in: {skill_path}")
                formatted_count += 1
        except Exception as e:
            skill_path = Path(skill_id) / "SKILL.md"
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
