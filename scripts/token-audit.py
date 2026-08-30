#!/usr/bin/env python3
"""
Token Audit Script for bank-agent-skills.
Analyzes all SKILL.md files:
  - Counts approximate tokens (words * 1.33 heuristic)
  - Identifies files > 500 lines or heavy token usage
  - Outputs token-audit-report.md
"""

import pathlib
from datetime import datetime

ROOT_DIR = pathlib.Path(__file__).resolve().parent.parent
REPORT_PATH = ROOT_DIR / "token-audit-report.md"

def audit_tokens():
    skills = list(ROOT_DIR.rglob("SKILL.md"))
    print(f"[+] Auditing token counts across {len(skills)} skills...")

    audit_data = []
    total_tokens = 0

    for s in skills:
        try:
            content = s.read_text(encoding="utf-8", errors="ignore")
            lines = len(content.splitlines())
            # Heuristic: 1 token ~= 0.75 words, or words * 1.33
            words = len(content.split())
            est_tokens = int(words * 1.33)
            total_tokens += est_tokens

            audit_data.append({
                "path": str(s.relative_to(ROOT_DIR)),
                "lines": lines,
                "words": words,
                "est_tokens": est_tokens
            })
        except Exception as e:
            print(f"Error reading {s}: {e}")

    # Sort by token count descending
    audit_data.sort(key=lambda x: x["est_tokens"], reverse=True)

    # Generate Markdown Report
    md = f"# Token Audit Report\n\nGenerated: {datetime.now().isoformat()}\n\n"
    md += f"**Total Skills Audited:** {len(skills)}\n"
    md += f"**Total Estimated Token Footprint:** {total_tokens:,} tokens\n\n"
    md += "## Top 20 Token-Heavy Skills\n\n"
    md += "| Rank | Skill Path | Lines | Est. Tokens |\n| :--- | :--- | :--- | :--- |\n"

    for idx, item in enumerate(audit_data[:20], 1):
        md += f"| {idx} | `{item['path']}` | {item['lines']} | {item['est_tokens']:,} |\n"

    md += "\n## Optimization Recommendations\n"
    md += "1. **Progressive Disclosure:** Use `skills-index.json` so agents only load metadata at startup.\n"
    md += "2. **Split Large Bodies:** Any skill exceeding 500 lines should extract code templates and examples into `examples.md` or `templates.md`.\n"

    REPORT_PATH.write_text(md, encoding="utf-8")
    print(f"[✓] Token audit report generated at {REPORT_PATH}")

if __name__ == "__main__":
    audit_tokens()
