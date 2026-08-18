### Task 1: Initialize Generator Script

**Files:**
- Create: `scripts/generate_index.py`

- [ ] **Step 1: Write `scripts/generate_index.py` (scaffold)**

```python
import os
import json
import yaml
from pathlib import Path

# Base directory for skills
SKILLS_DIR = "C:/code/ai/BrainStorming/skills"

def generate_index():
    index = []
    print("Starting registry generation...")
    # Implementation logic will be added here in next task
    print("Registry generation complete.")
    with open("skills-index.json", "w", encoding='utf-8') as f:
        json.dump(index, f, indent=2)

if __name__ == "__main__":
    generate_index()
```

- [ ] **Step 2: Commit**

```bash
git add scripts/generate_index.py
git commit -m "feat: initialize skills registry generator"
```
