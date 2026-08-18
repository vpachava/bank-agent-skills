# Design Doc: CI/CD Pipeline for bank-agent-skills

## Destination
A fully autonomous GitHub Actions pipeline (`.github/workflows/ci.yml`) that validates repository integrity on every pull request and push to `main`.

## Decisions so far
- Rule-engine based `skills-lint` used as the foundation.
- Actions: GitHub Actions (GHA) chosen for repository integration.

## Not yet specified
- Specific Action names for Markdown linting.
- Internal link validation mechanism (custom script vs Action).

## Out of scope
- External web link validation.
- Complex end-to-end integration tests.

## Architecture
- **Trigger**: `push` to `main`, `pull_request` to `main`.
- **Environment**: `ubuntu-latest`.
- **Steps**:
  1. `Checkout`: `actions/checkout@v4`.
  2. `Setup Python`: `actions/setup-python@v5`.
  3. `Lint Skills`: Execution of `python scripts/skills_lint.py .`.
  4. `Validate Markdown`: `markdownlint` (via `action`).
  5. `Validate Internal Links`: Custom Python `scripts/links_lint.py`.

## Technical Trade-offs
- Using a custom script for internal link validation (`scripts/links_lint.py`) provides maximum control over the internal structure of this repo's references (`[[name]]` vs `[text](internal-link-target.md)`), avoiding over-generalized Action configuration issues.
