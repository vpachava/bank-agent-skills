import unittest
from domain_models import Skill, Workflow

class TestDomainModels(unittest.TestCase):
    def test_skill_valid_parsing(self):
        content = """togaf-phases: [Phase C]
togaf-artifacts: [HLD]
bian-service-domains: [Integration.API]
---
# Skill content"""
        skill = Skill(content, "skills/architecture/c4-model/SKILL.md")
        self.assertEqual(skill.metadata["togaf-phases"], ["Phase C"])
        self.assertEqual(skill.metadata["togaf-artifacts"], ["HLD"])
        self.assertEqual(skill.metadata["bian-service-domains"], ["Integration.API"])
        self.assertEqual(len(skill.errors), 0)

    def test_skill_invalid_parsing(self):
        content = """togaf-phases: [Phase Unknown]
togaf-artifacts: [HLD]
bian-service-domains: [Invalid.Domain]
---
# Content"""
        skill = Skill(content, "skills/architecture/c4-model/SKILL.md")
        self.assertEqual(len(skill.errors), 2)
        self.assertIn("Invalid TOGAF Phase: 'Phase Unknown'", skill.errors)
        self.assertIn("Invalid BIAN Domain: 'Invalid.Domain'", skill.errors)

    def test_skill_format_defaults(self):
        content = """---
name: threat-model
---
# Content"""
        skill = Skill(content, "skills/security/threat-model/SKILL.md")
        new_content, modified = skill.format_content()
        self.assertTrue(modified)
        self.assertIn("togaf-phases: [Phase D]", new_content)
        self.assertIn("togaf-artifacts: [Security Baseline]", new_content)
        self.assertIn("bian-service-domains: [Security.Auth]", new_content)

    def test_skill_format_no_change(self):
        content = """---
togaf-phases: [Phase C]
togaf-artifacts: [HLD]
bian-service-domains: [Integration.API]
---
# Content"""
        skill = Skill(content, "skills/architecture/c4-model/SKILL.md")
        new_content, modified = skill.format_content()
        self.assertFalse(modified)
        self.assertEqual(content, new_content)

    def test_workflow_valid_lineage_in_memory(self):
        taxonomy = {"Requirements_Baseline", "Architecture_Vision", "HLD", "LLD"}
        skill_map = {
            "architecture/c4-model": Skill("togaf-phases: [Phase C]\ntogaf-artifacts: [HLD]\nbian-service-domains: [Integration.API]\n---"),
            "architecture/hld-generator": Skill("togaf-phases: [Phase C]\ntogaf-artifacts: [HLD]\nbian-service-domains: [Integration.API]\n---"),
        }

        wf_content = """
name: Valid In Memory Workflow
sequence:
  - skill_id: architecture/c4-model
    inputs: [Requirements_Baseline]
    outputs: [Architecture_Vision]
  - skill_id: architecture/hld-generator
    inputs: [Architecture_Vision]
    outputs: [HLD]
"""
        wf = Workflow(wf_content)
        errors = wf.validate_lineage(taxonomy, skill_resolver=lambda sid: skill_map.get(sid))
        self.assertEqual(len(errors), 0)

    def test_workflow_missing_input_lineage_in_memory(self):
        taxonomy = {"Requirements_Baseline", "Architecture_Vision", "HLD", "LLD"}
        skill_map = {
            "architecture/c4-model": Skill("togaf-phases: [Phase C]\ntogaf-artifacts: [HLD]\nbian-service-domains: [Integration.API]\n---"),
            "architecture/hld-generator": Skill("togaf-phases: [Phase C]\ntogaf-artifacts: [HLD]\nbian-service-domains: [Integration.API]\n---"),
        }

        wf_content = """
name: Invalid In Memory Workflow
sequence:
  - skill_id: architecture/c4-model
    inputs: [Requirements_Baseline]
    outputs: [Architecture_Vision]
  - skill_id: architecture/hld-generator
    inputs: [LLD]
    outputs: [HLD]
"""
        wf = Workflow(wf_content)
        errors = wf.validate_lineage(taxonomy, skill_resolver=lambda sid: skill_map.get(sid))
        self.assertTrue(any("Lineage Failure" in err for err in errors))

    def test_workflow_missing_skill_folder_in_memory(self):
        taxonomy = {"Requirements_Baseline", "Architecture_Vision"}
        wf_content = """
name: Missing Skill Workflow
sequence:
  - skill_id: nonexistent/skill
    inputs: [Requirements_Baseline]
    outputs: [Architecture_Vision]
"""
        wf = Workflow(wf_content)
        errors = wf.validate_lineage(taxonomy, skill_resolver=lambda sid: None)
        self.assertTrue(any("folder block not found on disk" in err for err in errors))

    def test_workflow_invalid_taxonomy_in_memory(self):
        taxonomy = {"Requirements_Baseline", "Architecture_Vision"}
        skill_map = {
            "architecture/c4-model": Skill("togaf-phases: [Phase C]\ntogaf-artifacts: [HLD]\nbian-service-domains: [Integration.API]\n---"),
        }

        wf_content = """
name: Invalid Taxonomy Workflow
sequence:
  - skill_id: architecture/c4-model
    inputs: [Invalid_Input_Type]
    outputs: [Architecture_Vision]
"""
        wf = Workflow(wf_content)
        errors = wf.validate_lineage(taxonomy, skill_resolver=lambda sid: skill_map.get(sid))
        self.assertTrue(any("is not defined in BANKING_WORKFLOWS_TAXONOMY.md" in err for err in errors))

if __name__ == "__main__":
    unittest.main()
