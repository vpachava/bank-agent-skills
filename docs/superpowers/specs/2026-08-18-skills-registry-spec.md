# Specification: Skills Registry Indexing Tool

## Goal
Implement a registry system that indexes all available skills in the repository into a searchable JSON format.

## Architecture
- A Python script (`scripts/generate_index.py`) will crawl the directory structure, locate `SKILL.md` files, parse their YAML frontmatter, and aggregate the metadata.
- Output: `skills-index.json`.

## Requirements
- Metadata to extract: name, category, description, tags, togaf-phases, bian-domains, regulatory-references, related-skills.
- Field `usage-count` initialized to 0.
- Documentation: `docs/reference/skills-registry.md` detailing index structure and how to query the generated JSON.

## Process
1. Create `scripts/generate_index.py`.
2. Implement frontmatter parsing logic using `pyyaml` (consistent with `skills-lint`).
3. Define the data model for the index.
4. Execute generator to produce `skills-index.json`.
5. Create query documentation.

## Outputs
- `scripts/generate_index.py`
- `skills-index.json`
- `docs/reference/skills-registry.md`
