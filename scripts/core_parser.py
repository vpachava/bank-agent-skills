import re

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

def parse_frontmatter(file_content):
    """
    Robust frontmatter parser parsing yaml-like formats.
    Returns: (parsed_metadata_dict, errors_list)
    """
    errors = []
    metadata = {
        "togaf-phases": [],
        "togaf-artifacts": [],
        "bian-service-domains": []
    }

    normalized = file_content.lstrip('﻿').strip()
    if normalized.startswith('---'):
        parts = normalized.split('---', 2)
        if len(parts) < 3:
            return metadata, ["Missing frontmatter delimiters (---)"]
        header = parts[1]
    else:
        if '---' in normalized:
            parts = normalized.split('---', 1)
            header = parts[0]
        else:
            return metadata, ["Missing frontmatter delimiters (---)"]

    # Process YAML fields carefully
    for line in header.splitlines():
        line = line.strip()
        if not line or ':' not in line:
            continue

        key, val = line.split(':', 1)
        key = key.strip()
        val = val.strip()

        # Matches brackets e.g. [A, B]
        list_match = re.match(r'^\[(.*?)\]$', val)
        if list_match:
            values = [v.strip().strip("'").strip('"') for v in list_match.group(1).split(',')]
            values = [v for v in values if v]
        else:
            values = [val.strip("'").strip('"')] if val else []

        if key in metadata:
            metadata[key] = values

    # Validate domains
    for phase in metadata["togaf-phases"]:
        if phase not in VALID_TOGAF_PHASES:
            errors.append(f"Invalid TOGAF Phase: '{phase}'")

    for domain in metadata["bian-service-domains"]:
        if domain not in VALID_BIAN_DOMAINS:
            errors.append(f"Invalid BIAN Domain: '{domain}'")

    return metadata, errors

def get_defaults_for_path(path_str):
    path_lower = path_str.replace('\\', '/').lower()
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

def format_skill_content(content, path_str):
    """
    Checks if togaf-phases, togaf-artifacts, and bian-service-domains exist in content.
    If missing, injects correct default properties based on the path.
    Returns (new_content, was_modified)
    """
    has_bom = content.startswith('﻿')
    normalized = content.lstrip('﻿')

    phase, artifact, domain = get_defaults_for_path(path_str)
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

    if modified:
        return ('﻿' if has_bom else '') + normalized, True
    return content, False
