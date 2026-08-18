# MkDocs Documentation Site Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Setup versioned MkDocs documentation site.

**Architecture:** MkDocs + Material theme + `mike` (versioning) + GenFiles (auto-generation).

**Tech Stack:** MkDocs, Python, GitHub Actions.

**Spec:** `docs/superpowers/specs/2026-08-18-mkdocs-specification.md`

## Global Constraints
- `mkdocs.yml` must include `mkdocs-gen-files`, `mkdocs-literate-nav`, `mkdocs-section-index`.
- Deployment must use `mike` for `vX.Y.Z` versioning.

---

### Task 1: MkDocs Configuration

**Files:**
- Create: `mkdocs.yml`

- [ ] **Step 1: Write `mkdocs.yml`**

```yaml
site_name: Bank Agent Skills
theme:
  name: material
plugins:
  - search
  - gen-files:
      scripts:
        - gen_nav.py # Assuming this script handles generation
  - literate-nav:
      nav_file: SUMMARY.md
  - section-index
```

- [ ] **Step 2: Commit**

```bash
git add mkdocs.yml
git commit -m "feat: initialize mkdocs configuration"
```

### Task 2: GHA Deployment

**Files:**
- Modify: `.github/workflows/ci.yml`

- [ ] **Step 1: Add deployment job**

```yaml
deploy:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4
    - uses: actions/setup-python@v5
    - run: pip install mkdocs-material mike
    - run: mike deploy --update-aliases dev latest
```

- [ ] **Step 2: Commit**

```bash
git add .github/workflows/ci.yml
git commit -m "feat: add mike deployment to CI"
```
