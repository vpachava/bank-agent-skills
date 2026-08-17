import yaml
import os
from pathlib import Path
from core_parser import parse_frontmatter

def load_taxonomy_artifacts():
    """Reads allowed artifacts list from docs/architecture/BANKING_WORKFLOWS_TAXONOMY.md"""
    taxonomy_file = Path("docs/architecture/BANKING_WORKFLOWS_TAXONOMY.md")
    if not taxonomy_file.exists():
        return set()

    content = taxonomy_file.read_text(encoding="utf-8")
    artifacts = set()
    for line in content.splitlines():
        line = line.strip()
        if line.startswith("- `") and line.endswith("`"):
            artifacts.add(line[3:-1])
    return artifacts

def validate_workflow_lineage(workflow_path, taxonomy_artifacts):
    """
    Validates step dependencies, existing skill folders, and artifacts schemas.
    """
    errors = []

    try:
        with open(workflow_path, 'r', encoding='utf-8') as f:
            workflow = yaml.safe_load(f)
    except Exception as e:
        return [f"Failed to read/parse YAML: {e}"]

    # Validate high level properties
    if not isinstance(workflow, dict):
        return ["Workflow file top-level element is not an object/dictionary"]
    if "name" not in workflow:
        errors.append("Missing Workflow 'name'")
    if "sequence" not in workflow or not isinstance(workflow["sequence"], list):
        return errors + ["Missing or invalid 'sequence' list"]

    available_artifacts = {"Requirements_Baseline"}
    w_name = workflow.get("name", "Unnamed")

    for i, step in enumerate(workflow["sequence"]):
        step_num = i + 1
        skill_id = step.get("skill_id")
        inputs = step.get("inputs", [])
        outputs = step.get("outputs", [])

        if not skill_id:
            errors.append(f"Step {step_num} is missing 'skill_id'")
            continue

        # Check local folder/skill existence
        skill_path = Path(skill_id) / "SKILL.md"
        if not skill_path.exists():
            errors.append(f"Referenced skill ID folder block not found on disk: '{skill_id}'")
        else:
            # Parse custom frontmatter details for the referenced skill
            sf_content = skill_path.read_text(encoding="utf-8")
            meta, fm_errs = parse_frontmatter(sf_content)
            for err in fm_errs:
                errors.append(f"Skill '{skill_id}' contains invalid frontmatter: {err}")

        # Check inputs exist in taxonomy
        for inp in inputs:
            if inp not in taxonomy_artifacts:
                errors.append(f"Step {step_num} Input '{inp}' is not defined in BANKING_WORKFLOWS_TAXONOMY.md")
            if inp not in available_artifacts:
                errors.append(f"Lineage Failure: Step {step_num} Input '{inp}' is missing from previous outputs in {w_name}")

        # Check outputs exist in taxonomy
        for outp in outputs:
            if outp not in taxonomy_artifacts:
                errors.append(f"Step {step_num} Output '{outp}' is not defined in BANKING_WORKFLOWS_TAXONOMY.md")
            available_artifacts.add(outp)

    return errors
