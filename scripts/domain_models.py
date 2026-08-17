import re
import yaml

# Supported Framework Domains
VALID_TOGAF_PHASES = {
    "Architecture Vision", "Phase A", "Phase B", "Phase C", "Phase D",
    "Opportunities & Solutions", "Phase E", "Phase F", "Phase G", "Phase H"
}

VALID_BIAN_DOMAINS = {
    "Customer Account.Origination", "Payment.Clearing", "Credit.LoanProcessing",
    "Trade.Settlement", "Identity.Management", "Integration.API", "Security.Auth",
    "Integration.Migration"
}

class Skill:
    def __init__(self, content: str, path: str = ""):
        self.content = content
        self.path = path.replace('\\', '/')
        self.has_bom = content.startswith('﻿') or content.startswith('﻿')
        self.metadata = {
            "togaf-phases": [],
            "togaf-artifacts": [],
            "bian-service-domains": []
        }
        self.errors = []
        self._parse()

    def _parse(self):
        normalized = self.content.lstrip('﻿').lstrip('﻿').strip()
        if normalized.startswith('---'):
            parts = normalized.split('---', 2)
            if len(parts) < 3:
                self.errors.append("Missing frontmatter delimiters (---)")
                return
            header = parts[1]
        else:
            if '---' in normalized:
                parts = normalized.split('---', 1)
                header = parts[0]
            else:
                self.errors.append("Missing frontmatter delimiters (---)")
                return

        # Process YAML fields
        for line in header.splitlines():
            line = line.strip()
            if not line or ':' not in line:
                continue

            key, val = line.split(':', 1)
            key = key.strip()
            val = val.strip()

            # Matches lists e.g. [A, B]
            list_match = re.match(r'^\[(.*?)\]$', val)
            if list_match:
                values = [v.strip().strip("'").strip('"') for v in list_match.group(1).split(',')]
                values = [v for v in values if v]
            else:
                values = [val.strip("'").strip('"')] if val else []

            if key in self.metadata:
                self.metadata[key] = values

        # Validate domains
        for phase in self.metadata["togaf-phases"]:
            if phase not in VALID_TOGAF_PHASES:
                self.errors.append(f"Invalid TOGAF Phase: '{phase}'")

        for domain in self.metadata["bian-service-domains"]:
            if domain not in VALID_BIAN_DOMAINS:
                self.errors.append(f"Invalid BIAN Domain: '{domain}'")

    def get_defaults(self) -> tuple[str, str, str]:
        path_lower = self.path.lower()
        if "architecture" in path_lower:
            return "Phase C", "HLD", "Integration.API"
        elif "cloud" in path_lower:
            return "Phase D", "Deployment Diagram", "Integration.API"
        elif "devops" in path_lower:
            return "Phase G", "Compliance Checklist", "Security.Auth"
        elif any(k in path_lower for k in ["discovery", "documentation", "greenfield", "wayfinder"]):
            return "Phase A", "Architecture Vision", "Customer Account.Origination"
        elif "integration" in path_lower:
            return "Phase C", "HLD", "Integration.API"
        elif any(k in path_lower for k in ["migration", "modernization"]):
            return "Phase F", "Migration Plan", "Integration.Migration"
        elif "security" in path_lower:
            return "Phase D", "Security Baseline", "Security.Auth"
        elif "governance" in path_lower:
            return "Phase G", "Compliance Checklist", "Security.Auth"
        else:
            return "Phase A", "Architecture Vision", "Customer Account.Origination"

    def format_content(self) -> tuple[str, bool]:
        """
        Checks if togaf-phases, togaf-artifacts, and bian-service-domains exist in content.
        If missing, injects correct default properties based on the path.
        Returns (new_content, was_modified)
        """
        normalized = self.content.lstrip('﻿').lstrip('﻿')
        phase, artifact, domain = self.get_defaults()
        modified = False

        if normalized.strip().startswith('---'):
            parts = normalized.split('---', 2)
            if len(parts) >= 3:
                header = parts[1]
                body = parts[2]

                lines = header.splitlines()
                keys = set()
                for line in lines:
                    if ':' in line:
                        key = line.split(':', 1)[0].strip().lower()
                        keys.add(key)

                new_lines = list(lines)

                if 'togaf-phases' not in keys:
                    new_lines.append(f"togaf-phases: [{phase}]")
                    modified = True
                if 'togaf-artifacts' not in keys:
                    new_lines.append(f"togaf-artifacts: [{artifact}]")
                    modified = True
                if 'bian-service-domains' not in keys:
                    new_lines.append(f"bian-service-domains: [{domain}]")
                    modified = True

                if modified:
                    new_header = "\n".join(new_lines)
                    if not new_header.endswith('\n') and len(new_lines) > 0:
                        new_header += '\n'
                    normalized = "---" + new_header + "---" + body
            else:
                new_header = (
                    "---\n"
                    f"togaf-phases: [{phase}]\n"
                    f"togaf-artifacts: [{artifact}]\n"
                    f"bian-service-domains: [{domain}]\n"
                    "---\n"
                )
                normalized = new_header + normalized
                modified = True
        else:
            new_header = (
                "---\n"
                f"togaf-phases: [{phase}]\n"
                f"togaf-artifacts: [{artifact}]\n"
                f"bian-service-domains: [{domain}]\n"
                "---\n"
            )
            normalized = new_header + normalized
            modified = True

        bom_prefix = '﻿' if self.has_bom else ''
        if modified:
            return bom_prefix + normalized, True
        return self.content, False


class Workflow:
    def __init__(self, content: str, name: str = ""):
        self.content = content
        self.name = name
        self.sequence = []
        self.errors = []
        self._parse()

    def _parse(self):
        try:
            data = yaml.safe_load(self.content)
        except Exception as e:
            self.errors.append(f"YAML Parse Error: {e}")
            return

        if not data or not isinstance(data, dict):
            self.errors.append("Malformed workflow data")
            return

        if "name" in data:
            self.name = data["name"]

        if "sequence" not in data:
            self.errors.append("Malformed workflow (missing sequence key)")
            return

        self.sequence = data["sequence"]

    def validate_lineage(self, taxonomy_artifacts: set, skill_resolver=None) -> list[str]:
        """
        Validates sequential outputs -> inputs lineage for this workflow.
        """
        errors = list(self.errors)
        if errors:
            return errors

        available_artifacts = set()
        for idx, step in enumerate(self.sequence):
            step_num = idx + 1
            if not isinstance(step, dict):
                errors.append(f"Step {step_num}: Malformed step definition")
                continue

            skill_id = step.get("skill_id", "")
            inputs = step.get("inputs", [])
            outputs = step.get("outputs", [])

            if not skill_id:
                errors.append(f"Step {step_num}: Missing 'skill_id'")
                continue

            if skill_resolver:
                try:
                    skill = skill_resolver(skill_id)
                    if not skill:
                        errors.append(f"Step {step_num} ({skill_id}): Referenced skill ID folder block not found on disk: '{skill_id}'")
                    else:
                        if skill.errors:
                            for err in skill.errors:
                                errors.append(f"Step {step_num} ({skill_id}): invalid frontmatter: {err}")
                except Exception as e:
                    errors.append(f"Step {step_num} ({skill_id}): Could not read skill frontmatter: {e}")

            # Validate artifacts against permitted taxonomy
            for inp in inputs:
                if inp not in taxonomy_artifacts:
                    errors.append(f"Step {step_num} ({skill_id}): Input '{inp}' is not defined in BANKING_WORKFLOWS_TAXONOMY.md")
            for out in outputs:
                if out not in taxonomy_artifacts:
                    errors.append(f"Step {step_num} ({skill_id}): Output '{out}' is not defined in BANKING_WORKFLOWS_TAXONOMY.md")

            # Lineage check: seed baseline on first step
            if idx == 0:
                available_artifacts.add("Requirements_Baseline")

            missing_inputs = [inp for inp in inputs if inp not in available_artifacts]
            if missing_inputs:
                errors.append(
                    f"Step {step_num} ({skill_id}): Lineage Failure. "
                    f"Requires inputs {missing_inputs} but not yet produced in workflow sequence."
                )

            for out in outputs:
                available_artifacts.add(out)

        return errors
