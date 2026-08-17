import unittest
import tempfile
import sys
from pathlib import Path

# Add scripts directory to path if needed
sys.path.append(str(Path(__file__).parent))

from workspace import Workspace
from domain_models import Skill, Workflow

class TestWorkspace(unittest.TestCase):
    def setUp(self):
        # Create a temp directory to acts as mock workspace root
        self.test_dir = tempfile.TemporaryDirectory()
        self.root_path = Path(self.test_dir.name)
        self.workspace = Workspace(self.root_path)

    def tearDown(self):
        self.test_dir.cleanup()

    def test_load_taxonomy_exists(self):
        # Create taxonomy file
        tax_dir = self.root_path / "docs" / "architecture"
        tax_dir.mkdir(parents=True)
        tax_file = tax_dir / "BANKING_WORKFLOWS_TAXONOMY.md"
        tax_file.write_text(
            "# Title\n- `Requirements_Baseline`\n- `Architecture_Vision`\n- `HLD`\n",
            encoding="utf-8"
        )
        taxonomy = self.workspace.load_taxonomy()
        self.assertEqual(taxonomy, {"Requirements_Baseline", "Architecture_Vision", "HLD"})

    def test_load_taxonomy_missing(self):
        taxonomy = self.workspace.load_taxonomy()
        self.assertEqual(taxonomy, set())

    def test_list_and_get_skills(self):
        # Setup mock skills
        skill_1_dir = self.root_path / "architecture" / "c4-model"
        skill_1_dir.mkdir(parents=True)
        (skill_1_dir / "SKILL.md").write_text("togaf-phases: [Phase C]\n---", encoding="utf-8")

        skill_2_dir = self.root_path / "security" / "threat-model"
        skill_2_dir.mkdir(parents=True)
        (skill_2_dir / "SKILL.md").write_text("togaf-phases: [Phase D]\n---", encoding="utf-8")

        # Create ignored folder and a SKILL.md there
        ignored_dir = self.root_path / ".claude" / "some-skill"
        ignored_dir.mkdir(parents=True)
        (ignored_dir / "SKILL.md").write_text("togaf-phases: [Phase H]\n---", encoding="utf-8")

        skills = self.workspace.list_skills()
        self.assertEqual(len(skills), 2)
        self.assertIn("architecture/c4-model", skills)
        self.assertIn("security/threat-model", skills)
        self.assertNotIn(".claude/some-skill", skills)

        # Verify get_skill
        sk = self.workspace.get_skill("architecture/c4-model")
        self.assertIsNotNone(sk)
        self.assertEqual(sk.metadata["togaf-phases"], ["Phase C"])

        # Verify missing skill
        self.assertIsNone(self.workspace.get_skill("nonexistent"))

    def test_write_skill(self):
        self.workspace.write_skill("governance/architecture-board", "togaf-phases: [Phase G]\n---")
        skill_file = self.root_path / "governance" / "architecture-board" / "SKILL.md"
        self.assertTrue(skill_file.exists())
        self.assertEqual(skill_file.read_text(encoding="utf-8"), "togaf-phases: [Phase G]\n---")

        sk = self.workspace.get_skill("governance/architecture-board")
        self.assertIsNotNone(sk)
        self.assertEqual(sk.metadata["togaf-phases"], ["Phase G"])

    def test_list_and_get_workflows(self):
        wf_dir = self.root_path / "workflows"
        wf_dir.mkdir()
        (wf_dir / "test-wf.yaml").write_text("name: Test WF\nsequence:\n  - skill_id: architecture/c4-model\n", encoding="utf-8")
        (wf_dir / "other.yml").write_text("name: Other WF\nsequence:\n  - skill_id: security/threat-model\n", encoding="utf-8")
        (wf_dir / "not-wf.txt").write_text("some content", encoding="utf-8")

        wfs = self.workspace.list_workflows()
        self.assertEqual(len(wfs), 2)
        self.assertIn("test-wf.yaml", wfs)
        self.assertIn("other.yml", wfs)
        self.assertNotIn("not-wf.txt", wfs)

        # Verify get_workflow
        wf = self.workspace.get_workflow("test-wf.yaml")
        self.assertIsNotNone(wf)
        self.assertEqual(wf.name, "Test WF")

        # Get workflow using name without extension
        wf2 = self.workspace.get_workflow("other")
        self.assertIsNotNone(wf2)
        self.assertEqual(wf2.name, "Other WF")

        self.assertIsNone(self.workspace.get_workflow("nonexistent"))

    def test_write_workflow(self):
        self.workspace.write_workflow("test-write.yaml", "name: Written WF\nsequence: []")
        wf_file = self.root_path / "workflows" / "test-write.yaml"
        self.assertTrue(wf_file.exists())
        self.assertEqual(wf_file.read_text(encoding="utf-8"), "name: Written WF\nsequence: []")

    def test_search_skills_and_workflows(self):
        # Setup skills
        (self.root_path / "architecture" / "c4-model").mkdir(parents=True)
        (self.root_path / "architecture" / "c4-model" / "SKILL.md").write_text("---", encoding="utf-8")
        (self.root_path / "security" / "threat-model").mkdir(parents=True)
        (self.root_path / "security" / "threat-model" / "SKILL.md").write_text("---", encoding="utf-8")

        # Setup workflows
        (self.root_path / "workflows").mkdir()
        (self.root_path / "workflows" / "c4-workflow.yaml").write_text("sequence: []", encoding="utf-8")
        (self.root_path / "workflows" / "security-workflow.yaml").write_text("sequence: []", encoding="utf-8")

        # Search skills
        matched_skills = self.workspace.search_skills("*c4*")
        self.assertEqual(list(matched_skills.keys()), ["architecture/c4-model"])

        matched_skills_sub = self.workspace.search_skills("threat")
        self.assertEqual(list(matched_skills_sub.keys()), ["security/threat-model"])

        # Search workflows
        matched_wfs = self.workspace.search_workflows("*security*")
        self.assertEqual(list(matched_wfs.keys()), ["security-workflow.yaml"])

if __name__ == "__main__":
    unittest.main()
