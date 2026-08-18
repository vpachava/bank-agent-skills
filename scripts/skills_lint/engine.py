import abc

class BaseRule(abc.ABC):
    @abc.abstractmethod
    def validate(self, content, path):
        """
        Validate a file's content.
        Returns a list of tuples: (issue_type, message, line_no)
        """
        pass

class ValidatorEngine:
    def __init__(self):
        self.rules = []

    def register_rule(self, rule):
        self.rules.append(rule)

    def run(self, files):
        results = []
        for file in files:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
            for rule in self.rules:
                results.extend(rule.validate(content, file))
        return results
