#!/usr/bin/env python3
"""
Quality Scorer Engine for bank-agent-skills outputs.
Evaluates architectural deliverables against completeness, compliance, and evidence validity.
"""

import json
import argparse
from pathlib import Path

def score_artifact(handoff_path: str) -> dict:
    path = Path(handoff_path)
    if not path.exists():
        return {"score": 0.0, "status": "REJECTED", "reasons": ["Artifact path does not exist"]}
        
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        return {"score": 0.0, "status": "REJECTED", "reasons": [f"Invalid JSON: {e}"]}

    score = 5.0
    reasons = []

    # 1. Check Artifact ID
    if not data.get("artifact_id"):
        score -= 1.0
        reasons.append("Missing artifact_id")

    # 2. Check Evidence Links
    links = data.get("evidence_links", [])
    if not links:
        score -= 1.5
        reasons.append("Zero evidence links provided")
    else:
        for link in links:
            if not Path(link.get("path", "")).exists():
                score -= 0.5
                reasons.append(f"Inaccessible evidence link: {link.get('path')}")

    # 3. Check Timestamp
    if not data.get("timestamp"):
        score -= 0.5
        reasons.append("Missing timestamp")

    final_score = max(0.0, round(score, 2))
    
    badge = "Gold Standard Architecture" if final_score >= 4.5 else "Standard Architectural Artifact"
    if final_score < 3.0:
        badge = "Governance Revision Required"

    report = {
        "artifact_id": data.get("artifact_id", "UNKNOWN"),
        "quality_score": final_score,
        "max_score": 5.0,
        "badge": badge,
        "deductions": reasons,
        "status": "APPROVED" if final_score >= 3.0 else "REJECTED"
    }

    return report

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Quality Scorer for Handoff Artifacts")
    parser.add_argument("handoff", help="Path to handoff.json")
    
    args = parser.parse_args()
    report = score_artifact(args.handoff)
    print(json.dumps(report, indent=2))
