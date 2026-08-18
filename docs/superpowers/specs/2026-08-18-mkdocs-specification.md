# Design Doc: MkDocs Documentation Site for bank-agent-skills

## Destination
A fully autonomous, versioned MkDocs documentation site deployed to GitHub Pages, automatically generated from the repository structure.

## Architecture
- **Engine**: `mkdocs` + `mkdocs-material`主题.
- **Auto-generator**: 
    - `mkdocs-gen-files`: Dynamically scans `architecture/`, `cloud/`, etc., to ingest `SKILL.md` files at build time.
    - `mkdocs-literate-nav`: Generates structured navigation from repository folders.
    - `mkdocs-section-index`: Enables top-level category pages.
- **Deployment**: `mike` for `gh-pages` versioned deployment.

## Features
- **Search**: `mkdocs-material` (in-memory client-side).
- **Navigation**: Folder-based hierarchical categorization.
- **Cross-References**: Standard markdown links automatically resolved.
- **Versioning**: `mike` CLI for `latest`, `vX.Y.Z` aliases.

## Implementation Plan
1. Configure `mkdocs.yml`.
2. Generate `docs/` structure.
3. Configure `mike` for deployment.
4. Integrate with CI/CD pipeline (automatically build/deploy on push to `main`?).
