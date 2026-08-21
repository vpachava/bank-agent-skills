#!/usr/bin/env python3
"""
Bridge utility to export architectural handoff.json artifacts to Jira / Linear / GitHub Markdown tickets.
"""

import argparse
import json
import os
import sys
from pathlib import Path

def format_for_jira(data: dict) -> str:
    artifact_id = data.get("artifact_id", "UNKNOWN-ARTIFACT")
    skill_name = data.get("skill_name", "Architecture Skill")
    timestamp = data.get("timestamp", "N/A")
    evidence_links = data.get("evidence_links", [])
    bian_domain = data.get("bian_domain", "CoreBanking.Generic")
    compliance_posture = data.get("compliance_posture", "CBUAE / PDPL Aligned")

    lines = []
    lines.append(f"h1. [ARCH-DELIVERABLE] {artifact_id} - Generated via /{skill_name}")
    lines.append("")
    lines.append(f"*Produced By:* `/{skill_name}`")
    lines.append(f"*Timestamp:* {timestamp}")
    lines.append(f"*BIAN Service Domain:* {bian_domain}")
    lines.append(f"*Compliance Posture:* {compliance_posture}")
    lines.append("")
    lines.append("h2. Acceptance Criteria (Architecture Baseline)")
    lines.append("# All functional integration points must match the baseline C4 container specification.")
    lines.append("# Security & NFR controls must enforce TLS 1.3, mTLS for internal services, and UAE data residency.")
    lines.append("# Observability logging must scrub PII before persisting to storage.")
    lines.append("")
    lines.append("h2. Evidence Links & Artifact Verification")
    lines.append("|| Type || Path || Description ||")
    if evidence_links:
        for link in evidence_links:
            l_type = link.get("type", "doc")
            l_path = link.get("path", "")
            l_desc = link.get("description", "")
            lines.append(f"| {l_type} | {{noformat}}{l_path}{{noformat}} | {l_desc} |")
    else:
        lines.append("| doc | N/A | No explicit evidence links declared |")
    lines.append("")
    lines.append("h2. Implementation Checklist for Squad")
    lines.append("* [ ] Validate API schemas against OpenAPI/AsyncAPI specification")
    lines.append("* [ ] Verify data residency compliance (onshore/DIFC/ADGM)")
    lines.append("* [ ] Execute pre-deployment evidence-gate check")

    return "\n".join(lines)

def format_for_linear(data: dict) -> str:
    artifact_id = data.get("artifact_id", "UNKNOWN-ARTIFACT")
    skill_name = data.get("skill_name", "Architecture Skill")
    timestamp = data.get("timestamp", "N/A")
    evidence_links = data.get("evidence_links", [])
    bian_domain = data.get("bian_domain", "CoreBanking.Generic")
    compliance_posture = data.get("compliance_posture", "CBUAE / PDPL Aligned")

    lines = []
    lines.append(f"# [ARCH] {artifact_id}: Implementation from /{skill_name}")
    lines.append("")
    lines.append(f"> **Origin Skill:** `/{skill_name}` | **BIAN Domain:** `{bian_domain}` | **Compliance:** `{compliance_posture}`")
    lines.append(f"> **Generated at:** `{timestamp}`")
    lines.append("")
    lines.append("## 📋 Acceptance Criteria")
    lines.append("- [ ] **Container Contracts:** Adhere to C4 container boundaries and data flows defined in the architecture artifact.")
    lines.append("- [ ] **Security & NFRs:** Strict enforcement of zero-trust boundaries, mTLS, and zero PII leakage in observability.")
    lines.append("- [ ] **Data Sovereignty:** Ensure data persistence remains within designated sovereign zones (CBUAE/PDPL).")
    lines.append("")
    lines.append("## 🔍 Evidence Verification Links")
    lines.append("| Type | Path | Description |")
    lines.append("| :--- | :--- | :--- |")
    if evidence_links:
        for link in evidence_links:
            l_type = link.get("type", "doc")
            l_path = link.get("path", "")
            l_desc = link.get("description", "")
            lines.append(f"| `{l_type}` | `{l_path}` | {l_desc} |")
    else:
        lines.append("| `doc` | `N/A` | No explicit evidence links attached |")
    lines.append("")
    lines.append("## 🛠️ Squad Action Items")
    lines.append("- [ ] Verify Infrastructure as Code (Terraform / K8s manifests)")
    lines.append("- [ ] Run automated `/governance/evidence-gate` prior to ARB review")
    lines.append("- [ ] Complete unit/integration tests according to TDD baseline")

    return "\n".join(lines)

def export_handoff(input_path: str, output_format: str = "linear", output_path: str = None) -> str:
    path = Path(input_path)
    if not path.exists():
        raise FileNotFoundError(f"Handoff file not found at: {input_path}")

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if output_format.lower() == "jira":
        rendered = format_for_jira(data)
    else:
        rendered = format_for_linear(data)

    if output_path:
        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            f.write(rendered)

    return rendered

def main():
    parser = argparse.ArgumentParser(description="Export handoff.json to Jira or Linear/Markdown tickets.")
    parser.add_argument("input", help="Path to handoff.json")
    parser.add_argument("--format", "-f", choices=["jira", "linear", "markdown"], default="linear", help="Target tracker format")
    parser.add_argument("--output", "-o", help="Optional output file path")

    args = parser.parse_args()
    try:
        fmt = "linear" if args.format in ["linear", "markdown"] else "jira"
        result = export_handoff(args.input, fmt, args.output)
        if not args.output:
            print(result)
        else:
            print(f"Successfully exported ticket to {args.output}")
    except Exception as e:
        print(f"Export failed: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
