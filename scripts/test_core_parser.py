import unittest
from core_parser import parse_frontmatter

class TestCoreParser(unittest.TestCase):
    def assert_parsed_metadata(self, content, expected_meta, expected_errors):
        meta, errs = parse_frontmatter(content)
        for key, val in expected_meta.items():
            self.assertEqual(meta.get(key), val)
        self.assertEqual(len(errs), len(expected_errors))
        for err in expected_errors:
            self.assertIn(err, errs)

    def test_valid_parsing(self):
        content = """togaf-phases: [Phase C]
togaf-artifacts: [HLD]
bian-service-domains: [Integration.API]
---
# Skill test content"""
        self.assert_parsed_metadata(
            content,
            {
                "togaf-phases": ["Phase C"],
                "togaf-artifacts": ["HLD"],
                "bian-service-domains": ["Integration.API"]
            },
            []
        )

    def test_invalid_domains(self):
        content = """togaf-phases: [Phase Unknown]
togaf-artifacts: [HLD]
bian-service-domains: [Invalid.Domain]
---
# Content"""
        self.assert_parsed_metadata(
            content,
            {
                "togaf-phases": ["Phase Unknown"],
                "togaf-artifacts": ["HLD"],
                "bian-service-domains": ["Invalid.Domain"]
            },
            [
                "Invalid TOGAF Phase: 'Phase Unknown'",
                "Invalid BIAN Domain: 'Invalid.Domain'"
            ]
        )

    def test_format_missing_metadata(self):
        from core_parser import format_skill_content
        content = """---
name: threat-model
---
# Content"""
        new_content, modified = format_skill_content(content, "skills/security/threat-model/SKILL.md")
        self.assertTrue(modified)
        self.assertIn("togaf-phases: [Phase D]", new_content)
        self.assertIn("togaf-artifacts: [Security Baseline]", new_content)
        self.assertIn("bian-service-domains: [Security.Auth]", new_content)

    def test_format_no_frontmatter(self):
        from core_parser import format_skill_content
        content = "# No frontmatter at all"
        new_content, modified = format_skill_content(content, "skills/architecture/c4-model/SKILL.md")
        self.assertTrue(modified)
        self.assertTrue(new_content.startswith("---"))
        self.assertIn("togaf-phases: [Phase C]", new_content)
        self.assertIn("togaf-artifacts: [HLD]", new_content)
        self.assertIn("bian-service-domains: [Integration.API]", new_content)
        self.assertIn("# No frontmatter at all", new_content)

    def test_format_no_change_needed(self):
        from core_parser import format_skill_content
        content = """---
togaf-phases: [Phase C]
togaf-artifacts: [HLD]
bian-service-domains: [Integration.API]
---
# Content"""
        new_content, modified = format_skill_content(content, "skills/architecture/c4-model/SKILL.md")
        self.assertFalse(modified)
        self.assertEqual(content, new_content)

if __name__ == '__main__':
    unittest.main()
