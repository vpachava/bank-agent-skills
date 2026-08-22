# Skills Registry Indexing Tool Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Implement a registry system that indexes all available skills in the repository into a searchable JSON format (`skills-index.json`).

**Architecture:** A Python scraper (`scripts/generate_index.py`) that parses `SKILL.md` frontmatter.

**Tech Stack:** Python, PyYAML.

**Spec:** `docs/superpowers/specs/2026-08-18-skills-registry-spec.md`

## Global Constraints
- `scripts/generate_index.py` must use UTF-8 encoding for file operations.
- `skills-index.json` must include: name, category, description, tags, togaf-phases, bian-domains, regulatory-references, related-skills, usage-count (placeholder).

---

### Task 1: Initialize Generator Script

**Files:**
- Create: `scripts/generate_index.py`

- [ ] **Step 1: Write `scripts/generate_index.py` (scaffold)**

```python
import os
import json
import yaml
from pathlib import Path

SKILLS_DIR = "." # Adjust if needed

def generate_index():
    index = []
    # Implementation logic ...
    print("Registry generation complete.")
    with open("skills-index.json", "w") as f:
        json.dump(index, f, indent=2)

if __name__ == "__main__":
    generate_index()
```

- [ ] **Step 2: Commit**

```bash
git add scripts/generate_index.py
git commit -m "feat: initialize skills registry generator"
```

### Task 2: Implement Indexing Logic

**Files:**
- Modify: `scripts/generate_index.py`

- [ ] **Step 1: Implement recursive crawler and frontmatter parser**

```python
# In scripts/generate_index.py

def parse_skill(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        # Extract YAML frontmatter
        if content.startswith('---'):
            parts = content.split('---', 2)
            metadata = yaml.safe_load(parts[1])
            return metadata
    return None

# Update generate_index to use parse_skill recursively
```

- [ ] **Step 2: Commit**

```bash
git add scripts/generate_index.py
git commit -m "feat: implement skill metadata extraction"
```

### Task 3: Finalize Generator and Documentation

**Files:**
- Modify: `scripts/generate_index.py`
- Create: `docs/reference/skills-registry.md`

- [ ] **Step 1: Complete `generate_index` and create JSON**

- [ ] **Step 2: Create query documentation**

- [ ] **Step 3: Commit**

```bash
git add scripts/generate_index.py docs/reference/skills-registry.md
git commit -m "feat: finalize skill registry and documentation"
```
