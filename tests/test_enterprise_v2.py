import sys
import json
from pathlib import Path

# Add root directory to python path for package imports
root = Path(__file__).resolve().parent.parent
if str(root) not in sys.path:
    sys.path.insert(0, str(root))

from quality_scorer.scorer import score_artifact
from multi_agent.orchestrator_agent import orchestrate
from analytics.usage_tracker import log_invocation, generate_report

def test_quality_scorer(tmp_path):
    handoff_file = tmp_path / "handoff.json"
    dummy_evidence = tmp_path / "evidence.tf"
    dummy_evidence.write_text("resource aws_s3_bucket test {}")
    
    payload = {
        "artifact_id": "TEST-ART-001",
        "timestamp": "2026-08-22T10:00:00Z",
        "evidence_links": [
            {"path": str(dummy_evidence), "type": "iac", "description": "Terraform S3"}
        ]
    }
    handoff_file.write_text(json.dumps(payload))
    
    report = score_artifact(str(handoff_file))
    assert report["quality_score"] == 5.0
    assert report["status"] == "APPROVED"
    assert report["badge"] == "Gold Standard Architecture"

def test_multi_agent_orchestrator():
    plan = orchestrate("Build Instant Payment Gateway", "UAE")
    assert plan["jurisdiction"] == "UAE"
    assert len(plan["assigned_agents"]) == 4

def test_analytics_tracker():
    log_invocation("test_skill", 150.0, True, 5)
    report = generate_report()
    assert report["total_invocations"] >= 1
    assert "success_rate" in report
