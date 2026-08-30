#!/usr/bin/env python3
"""
Evaluation Suite Generator for bank-agent-skills.
Generates 3-5 representative test queries per skill covering:
  - Trigger Case (when skill should activate)
  - Non-Trigger Case (when skill should NOT activate)
  - Edge Case (ambiguous input)
Outputs: evaluation-suites/ directory with one JSON file per skill.
"""

import json
import pathlib

ROOT_DIR = pathlib.Path(__file__).resolve().parent.parent
EVAL_DIR = ROOT_DIR / "evaluation-suites"
EVAL_DIR.mkdir(parents=True, exist_ok=True)

def generate_evaluation_suites():
    skills = list(ROOT_DIR.rglob("SKILL.md"))
    print(f"[+] Found {len(skills)} skills. Generating evaluation suites...")

    for skill in skills:
        rel = skill.relative_to(ROOT_DIR)
        category = rel.parts[0]
        skill_name = skill.parent.name
        if skill_name == "." or skill_name == category:
            skill_name = rel.stem

        suite = {
            "skill_name": f"/{skill_name}",
            "category": category,
            "path": str(rel.as_posix()),
            "evaluations": [
                {
                    "case_type": "trigger",
                    "input": f"Execute standard {skill_name} for my architecture project.",
                    "expected_activation": True,
                    "validation": f"Skill /{skill_name} activates and returns standard handoff artifact."
                },
                {
                    "case_type": "non_trigger",
                    "input": "Write a python function to print hello world.",
                    "expected_activation": False,
                    "validation": f"Skill /{skill_name} should remain inactive for generic non-architectural requests."
                },
                {
                    "case_type": "edge_case",
                    "input": f"Can you review my design and evaluate {skill_name} feasibility?",
                    "expected_activation": True,
                    "validation": f"Skill /{skill_name} activates conditionally based on intent extraction."
                }
            ]
        }

        out_file = EVAL_DIR / f"{category}_{skill_name}.json"
        out_file.write_text(json.dumps(suite, indent=2), encoding="utf-8")

    print(f"[✓] Successfully generated {len(skills)} evaluation suites in {EVAL_DIR}")

if __name__ == "__main__":
    generate_evaluation_suites()
