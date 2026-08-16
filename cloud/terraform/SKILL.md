---
name: terraform
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when reviewing banking Terraform/IaC codebase — produces an IaC-review (threats, state-mgt, drift, modularization, secrets)."
required-inputs:
  - Banking Terraform source-code
  - Infrastructure scope & target environment
  - Security/Compliance constraints
expected-deliverables:
  - Terraform code-quality report
  - State-management & drift-detection risks
  - Security/Compliance IaC-scan findings
---

# /terraform

## When to apply
Use for reviewing banking Terraform/IaC to prevent "IaC-rot," drift, and catastrophic infrastructure-misconfigurations in production. Essential gate for any banking deployment.

## Inputs
- **IaC Code** — Terraform/Bicep/ARM code.
- **Environment** — DEV/QA/PROD targets.

## Process
1. **Security Scan.** Run IaC tools (e.g., Checkov, tfsec) to catch public-buckets, open-security-groups, or unencrypted-storage defined in code.
2. **State Management Analysis.** Check for secure remote state (S3/Blob w/ locking, encryption, versioning).
3. **Drift & Modularization review.** Are critical systems modularized for consistency? Does a drift-detection process exist?
4. **Secret Handling Audit.** Terraform must NEVER contain raw secrets; must reference CMK/SecretsManager-ARNs.
5. **Issue Verdict.** Review-findings + veto-conditions.

## Banking pitfalls
- **State-file exposure** — State files containing sensitive infra-keys/secret-ARNs stored in unsecured buckets.
- **"Copy-Paste" Modularization** — Copy-pasting instead of referencing shared modules, leading to divergence and massive security debt across environments.
- **Ignoring "Default-provider-is-non-compliant"** — Terraform defaults (e.g., S3-bucket-encryption:false) that must be overridden for banking compliance.
- **Manual-change-drift** — Infrastructure being manually updated via UI/CLI after Terraform-deployment, rendering IaC stale.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of terraform meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the terraform process.**

## Outputs
- **IaC review report** — Scan results, security-findings, state-risks.
- **Infrastructure-drift status** — Drift-detection maturity-assessment.

## Related skills
- [aws-review](../aws-review/SKILL.md)
- [azure-review](../azure-review/SKILL.md)
- [security-architecture-review](../../security/security-architecture-review/SKILL.md)
