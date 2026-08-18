# skills-lint CLI Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a Python CLI tool that validates repository `SKILL.md` files against predefined standards.

**Architecture:** Rule-engine with `BaseRule` interface, rule registry, and YAML/Markdown parsing.

**Tech Stack:** Python 3 (standard library preferred + `PyYAML` if needed).

**Spec:** `docs/superpowers/specs/2026-08-17-skills-lint-design.md`

## Global Constraints
- Python 3 compatibility.
- Minimal dependencies (prefer standard library).
- Output format: `filename:line:message` (or JSON).
- Must run in CI/CD environment.

---

### Task 1: Scaffolding and Base Engine

**Files:**
- Create: `scripts/skills_lint/__init__.py`
- Create: `scripts/skills_lint/engine.py`
- Create: `scripts/skills_lint/rules/__init__.py`

**Interfaces:**
- Produces: `engine.py` with `ValidatorEngine` class and `BaseRule` abstract class.

- [ ] **Step 1: Define BaseRule class**

```python
import abc

class BaseRule(abc.ABC):
    @abc.abstractmethod
    def validate(self, content, path):
        pass
```

- [ ] **Step 2: Create ValidatorEngine**

```python
class ValidatorEngine:
    def __init__(self):
        self.rules = []
    
    def register_rule(self, rule):
        self.rules.append(rule)
        
    def run(self, files):
        results = []
        for file in files:
            with open(file, 'r') as f:
                content = f.read()
            for rule in self.rules:
                results.extend(rule.validate(content, file))
        return results
```

- [ ] **Step 3: Commit**

```bash
git add scripts/skills_lint/
git commit -m "feat: setup skills-lint engine scaffolding"
```

### Task 2: Implement Rules (Frontmatter and Sections)

**Files:**
- Create: `scripts/skills_lint/rules/yaml_frontmatter.py`
- Create: `scripts/skills_lint/rules/required_sections.py`

**Interfaces:**
- Consumes: `BaseRule` from `scripts/skills_lint/engine.py`.

- [ ] **Step 1: Implement YamlFrontmatterRule**

```python
from ..engine import BaseRule
import yaml

class YamlFrontmatterRule(BaseRule):
    def validate(self, content, path):
        issues = []
        if not content.startswith('---'):
            issues.append(('ERROR', 'Missing frontmatter', 1))
            return issues
        # Add simple YAML parsing and key checking here
        return issues
```

- [ ] **Step 2: Implement RequiredSectionsRule**

```python
from ..engine import BaseRule
import re

class RequiredSectionsRule(BaseRule):
    def validate(self, content, path):
        required = ['## When to apply', '## Inputs', '## Process', '## Outputs', '## Related skills']
        issues = []
        for section in required:
            if section not in content:
                issues.append(('ERROR', f'Missing section: {section}', 0))
        return issues
```

- [ ] **Step 3: Commit**

```bash
git add scripts/skills_lint/rules/
git commit -m "feat: implement initial linting rules"
```

### Task 3: CLI Entry Point and Integration

**Files:**
- Create: `scripts/skills-lint.py` (CLI entry point)

**Interfaces:**
- Consumes: `ValidatorEngine` from `scripts/skills_lint/engine.py`.

- [ ] **Step 1: Implement CLI argument parsing**

```python
import argparse
from skills_lint.engine import ValidatorEngine
# ... imports ...

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='Path to skill file or directory')
    args = parser.parse_args()
    # Engine orchestration
```

- [ ] **Step 2: Add usage instructions**

- [ ] **Step 3: Commit**

```bash
git add scripts/skills-lint.py
git commit -m "feat: complete skills-lint CLI tool"
```
