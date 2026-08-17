import unittest
import os
import tempfile
import yaml
from pathlib import Path
from lineage_validator import validate_workflow_lineage

class TestLineageValidator(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.old_cwd = os.getcwd()
        os.chdir(self.temp_dir.name)

        # Define default taxonomy
        self.taxonomy = {"Requirements_Baseline", "Architecture_Vision", "HLD", "LLD"}

    def tearDown(self):
        os.chdir(self.old_cwd)
        self.temp_dir.cleanup()

    def create_skill(self, skill_id, togaf_phases, togaf_artifacts, bian_domains):
        skill_dir = Path(skill_id)
        skill_dir.mkdir(parents=True, exist_ok=True)
        content = f"""togaf-phases: {togaf_phases}
togaf-artifacts: {togaf_artifacts}
bian-service-domains: {bian_domains}
---
# Skill content
"""
        (skill_dir / "SKILL.md").write_text(content, encoding="utf-8")

    def create_workflow(self, name, sequence):
        wf_dir = Path("workflows")
        wf_dir.mkdir(exist_ok=True)
        wf_path = wf_dir / "test_wf.yaml"
        wf_data = {
            "name": name,
            "sequence": sequence
        }
        with open(wf_path, "w", encoding="utf-8") as f:
            yaml.dump(wf_data, f)
        return wf_path

    def test_valid_lineage(self):
        # Create skills
        self.create_skill("architecture/c4-model", "[Phase C]", "[HLD]", "[Integration.API]")
        self.create_skill("architecture/hld-generator", "[Phase C]", "[HLD]", "[Integration.API]")

        # Create workflow
        sequence = [
            {
                "skill_id": "architecture/c4-model",
                "inputs": ["Requirements_Baseline"],
                "outputs": ["Architecture_Vision"]
            },
            {
                "skill_id": "architecture/hld-generator",
                "inputs": ["Architecture_Vision"],
                "outputs": ["HLD"]
            }
        ]
        wf_path = self.create_workflow("Valid Project", sequence)

        errs = validate_workflow_lineage(wf_path, self.taxonomy)
        self.assertEqual(len(errs), 0)

    def test_missing_input_lineage(self):
        self.create_skill("architecture/c4-model", "[Phase C]", "[HLD]", "[Integration.API]")
        self.create_skill("architecture/hld-generator", "[Phase C]", "[HLD]", "[Integration.API]")

        # Step 2 requires LLD but it wasn't produced by Step 1 or baseline
        sequence = [
            {
                "skill_id": "architecture/c4-model",
                "inputs": ["Requirements_Baseline"],
                "outputs": ["Architecture_Vision"]
            },
            {
                "skill_id": "architecture/hld-generator",
                "inputs": ["LLD"],
                "outputs": ["HLD"]
            }
        ]
        wf_path = self.create_workflow("Invalid Lineage", sequence)

        errs = validate_workflow_lineage(wf_path, self.taxonomy)
        self.assertTrue(any("Lineage Failure" in err for err in errs))

    def test_missing_skill_folder(self):
        sequence = [
            {
                "skill_id": "nonexistent/skill",
                "inputs": ["Requirements_Baseline"],
                "outputs": ["Architecture_Vision"]
            }
        ]
        wf_path = self.create_workflow("Missing Folder Workflow", sequence)

        errs = validate_workflow_lineage(wf_path, self.taxonomy)
        self.assertTrue(any("folder block not found on disk" in err for err in errs))

    def test_invalid_taxonomy_artifacts(self):
        self.create_skill("architecture/c4-model", "[Phase C]", "[HLD]", "[Integration.API]")

        sequence = [
            {
                "skill_id": "architecture/c4-model",
                "inputs": ["Invalid_Input_Type"],
                "outputs": ["Architecture_Vision"]
            }
        ]
        wf_path = self.create_workflow("Invalid Taxonomy Workflow", sequence)

        errs = validate_workflow_lineage(wf_path, self.taxonomy)
        self.assertTrue(any("is not defined in BANKING_WORKFLOWS_TAXONOMY.md" in err for err in errs))

    def test_invalid_frontmatter_propagation(self):
        # Create skill with invalid TOGAF Phase in frontmatter
        self.create_skill("architecture/c4-model", "[Invalid Phase]", "[HLD]", "[Integration.API]")

        sequence = [
            {
                "skill_id": "architecture/c4-model",
                "inputs": ["Requirements_Baseline"],
                "outputs": ["Architecture_Vision"]
            }
        ]
        wf_path = self.create_workflow("Invalid Frontmatter Workflow", sequence)

        errs = validate_workflow_lineage(wf_path, self.taxonomy)
        self.assertTrue(any("invalid frontmatter: Invalid TOGAF Phase" in err for err in errs))

if __name__ == '__main__':
    unittest.main()
