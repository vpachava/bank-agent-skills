from ..engine import BaseRule
import yaml

class YamlFrontmatterRule(BaseRule):
    def validate(self, content, path):
        issues = []
        if not content.startswith('---'):
            issues.append(('ERROR', 'Missing frontmatter', 1))
            return issues

        # Simple frontmatter extraction
        try:
            parts = content.split('---', 2)
            if len(parts) < 3:
                return [('ERROR', 'Malformed frontmatter', 1)]

            data = yaml.safe_load(parts[1])
            if not data or 'name' not in data or 'description' not in data:
                issues.append(('ERROR', 'Frontmatter missing name or description', 1))
        except yaml.YAMLError:
            issues.append(('ERROR', 'Invalid YAML in frontmatter', 1))

        return issues
