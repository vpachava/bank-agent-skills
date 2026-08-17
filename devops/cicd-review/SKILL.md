---
name: cicd-review
owner: Architectural Governance
version: 0.1.1
last-reviewed: 2026-08-16
description: "Use when reviewing a banking CI/CD pipeline â€” produces a review report (gates, build-integrity, artifact-security, promotion, audit-trail, and automated readiness)."
togaf-phases: [Phase G]
togaf-artifacts: [Compliance Checklist]
bian-service-domains: [Security.Auth]
---

# /cicd-review

## When to apply
Use to validate that a banking team's CI/CD pipeline ensures *software supply chain integrity*, preventing unauthorized or unverified code from reaching production. It transforms pipelines from "developer productivity tools" into "regulated banking control-points."

## Inputs
- **Pipeline definition** â€” Pipeline as code (e.g. Jenkinsfile, GitHub Actions, Azure Pipelines).
- **Control strategy** â€” How are secrets/signed-artifacts handled?
- **Audit Requirement** â€” Traceability: build-ID to commit to artifact-signature.

## Process
1. **Source/Build Integrity.** Verify build-from-tag-only. Enforce code-signing at build-time.
2. **Review Security Gates.** Check for automated SAST, DAST, Container-scanning, and IaC-scanning *before* promotion-gates.
3. **Audit Trail/Traceability.** Verify that every artifact has a verifiable lineage (build-tool-version -> commit-hash -> scan-results -> approval).
4. **Automated Readiness Check.** Integrate checks ensuring pipeline artifacts pass `/production-readiness` gate criteria automatically.
5. **Promotion/Environment Control.** Ensure manual-approval-gates required for promotion to regulated environments (QA/UAT/PROD).
6. **Issue Review Verdict.** Report findings & non-negotiables.

## Banking pitfalls
- **"Bypass-pipeline" culture** â€” Allowing direct-to-PROD deployments without pipeline-orchestrated automated controls (critical compliance risk).
- **Artifact-registry-exposure** â€” Unsigned build-artifacts sitting in publicly-accessible/unauthorized registries (software supply chain risk).
- **Missing approval-audit** â€” Pipeline stages that "promote" but do not capture the identity of the human-approver for the required-audit-file.
- **Credential-management-in-pipeline** â€” Pipeline scripts with raw-credentials/secrets instead of managed-secrets + OIDC-federated-service-accounts.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of cicd-review meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the cicd-review process.**

## Outputs
- **CI/CD review report** â€” Automated-control gaps + pipeline-hardening steps.
- **Security/Audit-gap analysis** â€” Specific compliance-issues found in build/deploy logic.
- **Promotion-pipeline risk-profile** â€” Summary of residual risk in the pipeline.

## Related skills
- [release-readiness](../release-readiness/SKILL.md)
- [production-readiness](../../governance/production-readiness/SKILL.md)
- [compliance](../../security/compliance/SKILL.md)

### Banking Context & Examples

#### (1) Regulatory Pipeline Approval Example
**Scenario:** A deployment pipeline for a payment engine.
- **Architecture Lens Check:** Verification that the pipeline captures the UIDs of the two-person approval process in a tamper-proof audit log, required by `CBUAE` for payment-engine updates.
- **Sample Outcome:** "CI/CD Review: Pipeline passes; approval audit-trail captures UIDs of both approvers in internal Jira-integrated ticket, satisfying CBUAE audit requirement."
- **Common Pitfall:** Using a single-person approval gate for payment-engine releases. The pipeline technically "works" but is regulatory-non-compliant for high-risk systems.

#### (2) Software Supply Chain Security Example
**Scenario:** Artifact promotion for a core-banking module.
- **Architecture Lens Check:** Enforcing binary signed artifacts during the build process, preventing unsigned code from entering the registry.
- **Sample Outcome:** "Pipeline Hardening: Container images are automatically digitally signed post-build; Kubernetes Admission Controllers reject unsigned images."
- **Common Pitfall:** Using an unsigned container registry for production releases; an attacker could push a malicious image to the registry, and the cluster would automatically pull and deploy it since there are no verification checks.

#### (3) Sharia-Compliant Pipeline Gate Example
**Scenario:** Deployment pipeline for a Sharia product ledger.
- **Architecture Lens Check:** Injecting a pipeline gate requiring formal `Sharia-Compliant-Certificate` metadata ingestion before promotion to UAT.
- **Sample Outcome:** "Pipeline Gate: Gate-check requires valid `Sharia-Certificate-ID`. Deployment blocked if metadata is absent."
- **Common Pitfall:** Overlooking product-specific audit requirements in the pipeline. If the pipeline implicitly promotes all "successful builds" without verifying their compliance metadata, a non-Sharia-certified branch might accidentally be promoted, causing a major compliance breach.

### Regulatory References
1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/
2. **PDPL:** Personal Data Protection Law (Federal Decree-Law No. 45 of 2021)
3. **CBUAE Cybersecurity Framework:** Domain 1: Governance & Risk Management


