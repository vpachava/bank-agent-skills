import json
import os
import pytest
from scripts.export_to_tracker import export_handoff
from pathlib import Path

def test_export_to_linear():
    test_handoff = {
        "artifact_id": "BANK-101",
        "timestamp": "2026-08-21T10:00:00Z",
        "skill_name": "hld-generator",
        "evidence_links": [
            {"type": "iac", "path": "/infra/prod.tf", "description": "Terraform prod config"}
        ],
        "bian_domain": "Integration.API",
        "compliance_posture": "CBUAE / PDPL Aligned"
    }
    
    handoff_path = Path("test_handoff.json")
    with open(handoff_path, "w") as f:
        json.dump(test_handoff, f)

    try:
        output = export_handoff(handoff_path, "linear")
        assert "# [ARCH] BANK-101: Implementation from /hld-generator" in output
        assert "| `iac` | `/infra/prod.tf` | Terraform prod config |" in output
    finally:
        if handoff_path.exists():
            handoff_path.unlink()
