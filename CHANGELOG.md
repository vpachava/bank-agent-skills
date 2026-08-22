# Changelog

## [1.0.1] - 2026-08-22

### What's New
- **Library Expansion:** Total reach expanded to **100 invoke-and-act skills** across **16 structured categories**.
- **Global Portability:** Fully OS-agnostic repository; removed all hardcoded system/user-specific paths (e.g., C:/Users/...). Now runs on Windows (Git Bash), macOS, and Linux without modification.
- **Enterprise-Grade Governance:** 
  - **Evidence-Gating:** New `evidence-gate` skill ensures designs link to real repo IaC/Config.
  - **Multi-Jurisdictional Overlays:** Regional policy definitions for UAE, KSA, EU, UK, USA, Singapore, India, and Australia.
  - **Industry Packs:** New compliance overlays for Healthcare, Insurance, Retail, Government, and Energy.
- **Developer Experience:** 
  - `install-wizard.py` for automated multi-mode setup (Global/Hermes/Local).
  - Pre-commit git hooks for automated linting/testing.
- **Observability & CI/CD:** 
  - Automated RAID risk registry, staleness detection, and analytics dashboard.
  - Native `.gitlab-ci.yml` pipeline alongside GitHub Actions.
- **Diagram-as-Code:** New `/archify` engine to generate Mermaid diagrams directly from `design.json`.

### Breaking Changes
- None: This release is fully backward compatible with v1.0.0.

### Known Limitations
- The `Evidence-Gate` currently relies on standard Unix-like utilities (`grep`, `ls`); Windows users must ensure `git-bash` tools are in their PATH.

### Upgrade Guide
1. Pull the latest: `git pull origin main`
2. Run installer: `python scripts/install-wizard.py`
3. Activate local pre-commit hooks: `python scripts/setup_hooks.py`
