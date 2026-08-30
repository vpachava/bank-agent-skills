#!/usr/bin/env python3
"""
Advanced Security & Governance Audit Script for bank-agent-skills.
Scans all SKILL.md and Python scripts for:
  - Adversarial instruction patterns (bypassing safety rules, hiding actions)
  - Network calls (http, requests, curl, fetch, urllib, socket)
  - Hardcoded credentials (API keys, tokens, passwords)
  - Unsafe file operations (os.system, subprocess with shell=True)
Outputs: security-audit-report.md with risk ratings and remediation guidelines.
"""

import os
import re
import pathlib
from datetime import datetime

ROOT_DIR = pathlib.Path(__file__).resolve().parent.parent
REPORT_PATH = ROOT_DIR / "security-audit-report.md"

ADVERSARIAL_PATTERNS = [
    r"ignore previous instructions",
    r"bypass safety",
    r"hide actions",
    r"exfiltrate",
    r"disable guardrails"
]

NETWORK_PATTERNS = [
    r"\bhttp://\b",
    r"\bhttps://\b",
    r"requests\.get",
    r"requests\.post",
    r"urllib",
    r"fetch\(",
    r"curl\s+",
    r"socket\."
]

CREDENTIAL_PATTERNS = [
    r"api[_-]?key\s*=\s*['\"'][a-zA-Z0-9_\-]{16,}%['\"']",
    r"password\s*=\s*['\"'].+['\"']",
    r"bearer\s+[a-zA-Z0-9_\-\.]+"
]

UNSAFE_EXEC_PATTERNS = [
    r"os\.system\(",
    r"subprocess\..*shell\s*=\s*True"
]

def audit_file(file_path: pathlib.Path) -> list:
    findings = []
    try:
        content = file_path.read_text(encoding="utf-8", errors="ignore")
        lines = content.splitlines()
        
        for idx, line in enumerate(lines, 1):
            # 1. Check Adversarial
            for pat in ADVERSARIAL_PATTERNS:
                if re.search(pat, line, re.IGNORECASE):
                    findings.append({"line": idx, "severity": "CRITICAL", "category": "Adversarial Instruction", "match": line.strip()})
            # 2. Check Network Calls
            for pat in NETWORK_PATTERNS:
                if re.search(pat, line, re.IGNORECASE):
                    findings.append({"line": idx, "severity": "MEDIUM", "category": "Network Call", "match": line.strip()})
            # 3. Check Credentials
            for pat in CREDENTIAL_PATTERNS:
                if re.search(pat, line, re.IGNORECASE):
                    findings.append({"line": idx, "severity": "HIGH", "category": "Hardcoded Credential", "match": line.strip()})
            # 4. Check Unsafe Execution
            for pat in UNSAFE_EXEC_PATTERNS:
                if re.search(pat, line, re.IGNORECASE):
                    findings.append({"line": idx, "severity": "HIGH", "category": "Unsafe Execution", "match": line.strip()})
    except Exception as e:
        findings.append({"line": 0, "severity": "LOW", "category": "Read Error", "match": str(e)})
        
    return findings

def run_audit():
    print("[+] Starting Advanced Security & Governance Audit...")
    report_data = []
    total_findings = 0
    
    for path in ROOT_DIR.rglob("*"):
        if path.is_file() and not any(p.startswith(".") or p in ["venv", "__pycache__", "tests"] for p in path.parts):
            if path.suffix in [".md", ".py", ".json", ".yaml", ".yml"]:
                findings = audit_file(path)
                if findings:
                    total_findings += len(findings)
                    report_data.append({"file": path.relative_to(ROOT_DIR), "findings": findings})

    # Generate Markdown Report
    md = f"# Security Audit Report\n\nGenerated: {datetime.now().isoformat()}\n\n"
    md += f"Total Files Scanned: Checked across root directories.\n"
    md += f"Total Findings: {total_findings}\n\n"
    
    if not report_data:
        md += "### Status: PASSED ✅\nNo security vulnerabilities, unmasked credentials, or adversarial directives detected.\n"
    else:
        for item in report_data:
            md += f"### File: `{item['file']}`\n"
            for f in item["findings"]:
                md += f"- **[{f['severity']}]** Category: `{f['category']}` (Line {f['line']})\n"
                md += f"  - `Match: {f['match']}`\n"
            md += "\n"

    REPORT_PATH.write_text(md, encoding="utf-8")
    print(f"[✓] Security audit report generated at {REPORT_PATH}")

if __name__ == "__main__":
    run_audit()
