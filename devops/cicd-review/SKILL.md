---
name: cicd-review
owner: Architectural Governance
version: 0.1.1
last-reviewed: 2026-08-16
description: "Use when reviewing a banking CI/CD pipeline — produces a review report (gates, build-integrity, artifact-security, promotion, audit-trail, and automated readiness)."
---

# /cicd-review

## When to apply
Use to validate that a banking team's CI/CD pipeline ensures *software supply chain integrity*, preventing unauthorized or unverified code from reaching production. It transforms pipelines from "developer productivity tools" into "regulated banking control-points."

## Inputs
- **Pipeline definition** — Pipeline as code (e.g. Jenkinsfile, GitHub Actions, Azure Pipelines).
- **Control strategy** — How are secrets/signed-artifacts handled?
- **Audit Requirement** — Traceability: build-ID to commit to artifact-signature.

## Process
1. **Source/Build Integrity.** Verify build-from-tag-only. Enforce code-signing at build-time.
2. **Review Security Gates.** Check for automated SAST, DAST, Container-scanning, and IaC-scanning *before* promotion-gates.
3. **Audit Trail/Traceability.** Verify that every artifact has a verifiable lineage (build-tool-version -> commit-hash -> scan-results -> approval).
4. **Automated Readiness Check.** Integrate checks ensuring pipeline artifacts pass `/production-readiness` gate criteria automatically.
5. **Promotion/Environment Control.** Ensure manual-approval-gates required for promotion to regulated environments (QA/UAT/PROD).
6. **Issue Review Verdict.** Report findings & non-negotiables.

## Banking pitfalls
- **"Bypass-pipeline" culture** — Allowing direct-to-PROD deployments without pipeline-orchestrated automated controls (critical compliance risk).
- **Artifact-registry-exposure** — Unsigned build-artifacts sitting in publicly-accessible/unauthorized registries (software supply chain risk).
- **Missing approval-audit** — Pipeline stages that "promote" but do not capture the identity of the human-approver for the required-audit-file.
- **Credential-management-in-pipeline** — Pipeline scripts with raw-credentials/secrets instead of managed-secrets + OIDC-federated-service-accounts.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of cicd-review meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the cicd-review process.**

## Outputs
- **CI/CD review report** — Automated-control gaps + pipeline-hardening steps.
- **Security/Audit-gap analysis** — Specific compliance-issues found in build/deploy logic.
- **Promotion-pipeline risk-profile** — Summary of residual risk in the pipeline.

## Related skills
- [release-readiness](../release-readiness/SKILL.md)
- [production-readiness](../../governance/production-readiness/SKILL.md)
- [compliance](../../security/compliance/SKILL.md)
