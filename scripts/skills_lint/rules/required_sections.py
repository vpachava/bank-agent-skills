from ..engine import BaseRule

class RequiredSectionsRule(BaseRule):
    def validate(self, content, path):
        required = [
            '## When to apply',
            '## Inputs',
            '## Process',
            '## Outputs',
            '## Related skills'
        ]
        issues = []
        for section in required:
            if section not in content:
                issues.append(('ERROR', f'Missing required section: {section}', 0))
        return issues
