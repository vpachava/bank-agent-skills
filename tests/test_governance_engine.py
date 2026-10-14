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
