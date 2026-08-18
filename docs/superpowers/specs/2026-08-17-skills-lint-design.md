# Design Doc: skills-lint CLI Tool

## Overview
A Python-based CLI tool to lint and validate architectural skill definitions (`SKILL.md`) in the repository.

## Architecture (Rule-Engine)
- **Engine (`skills-lint`)**: Walks the filesystem, parses target files, runs registered validator rules.
- **Rules (`rules/`)**: Plug-and-play modules inheriting from `BaseRule`.
- **Validation Pipeline**: 
    1. Parsing (YAML frontmatter + Content).
    2. Rule Execution (Independent validators).
    3. Aggregation (Collect errors).
    4. Reporting (Console/JSON).

## Validator Rules
1. **YAML Frontmatter**: Checks for presence and mandatory `name`, `description` keys.
2. **Required Sections**: Ensures presence of specific markdown headers (`## When to apply`, `## Inputs`, etc.).
3. **Bulletproofing**: Scans for predefined mandatory checklist items.
4. **Internal Link Validity**: Ensures `[[name]]` references exist locally.
5. **Markdown Integrity**: Basic syntax check (broken headers/links).

## Implementation Plan
1. Define `BaseRule` class.
2. Implement frontmatter and section rules.
3. Build CLI interface (`argparse`).
4. Implement rule registry.
5. Add CI/CD usage instructions.

**Reviewing complete. Ready for implementation.**
