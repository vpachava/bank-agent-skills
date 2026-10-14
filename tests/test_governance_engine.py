import unittest
import os
import sys
from pathlib import Path

# Add governance scripts to path
sys.path.append(str(Path(__file__).parents[1] / "governance" / "scripts"))
from governance_engine import GovernanceEngine

class TestGovernanceEngine(unittest.TestCase):
    def setUp(self):
        self.engine = GovernanceEngine()

    def test_engine_initialization(self):
        self.assertTrue(self.engine.repo_root.exists())
        self.assertTrue(self.engine.governance_dir.exists())

    def test_unified_audit_execution(self):
        report = self.engine.execute_unified_audit()
        self.assertIn("timestamp", report)
        self.assertIn("overall_status", report)
        self.assertEqual(report["overall_status"], "PASS")

if __name__ == "__main__":
    unittest.main()

    def test_evidence_gate_fails_on_missing_evidence(self):
        # We need to set up the engine to point to the correct repo root if necessary, 
        # but since we are running within the test environment, we should use the class instance.
        handoff_path = "tests/dummy_handoff/invalid_handoff.json"
        result = self.engine.run_evidence_gate(str(Path(self.engine.repo_root) / handoff_path))
        self.assertEqual(result["status"], "failed")
        self.assertTrue(len(result["errors"]) > 0)
        self.assertIn("Evidence path inaccessible", result["errors"][0])

    def test_evidence_gate_fails_on_empty_evidence_path(self):
        handoff_path = "tests/dummy_handoff/empty_path.json"
        result = self.engine.run_evidence_gate(str(Path(self.engine.repo_root) / handoff_path))
        # This SHOULD fail because an empty path is not valid evidence
        self.assertEqual(result["status"], "failed")
