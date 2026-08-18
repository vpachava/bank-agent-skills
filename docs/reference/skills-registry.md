# Skills Registry Query Documentation

## Overview
The skills registry is generated as `scripts/skills-index.json`. It provides metadata for all indexed skills in the repository.

## Structure
The `skills-index.json` is an array of skill objects:
```json
[
  {
    "name": "string",
    "category": "string",
    "description": "string",
    "tags": ["string"],
    "togaf-phases": ["string"],
    "bian-domains": ["string"],
    "regulatory-references": ["string"],
    "related-skills": ["string"],
    "usage-count": 0
  }
]
```

## How to Query
Since it is a JSON file, you can use standard command-line tools like `jq` to query it.

### Example Queries
1. **List all skill names:**
   `jq -r '.[].name' skills-index.json`

2. **Find skills by tag:**
   `jq -r '.[] | select(.tags | contains(["security"])) .name' skills-index.json`

3. **Get specific skill description:**
   `jq -r '.[] | select(.name == "c4-model") .description' skills-index.json`
