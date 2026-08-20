---
name: terraform
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when reviewing banking Terraform/IaC codebase â€” produces an IaC-review (threats, state-mgt, drift, modularization, secrets)."
required-inputs:
  - Banking Terraform source-code
  - Infrastructure scope & target environment
  - Security/Compliance constraints
expected-deliverables:
  - Terraform code-quality report
  - State-management & drift-detection risks
  - Security/Compliance IaC-scan findings
togaf-phases: [Phase D]
togaf-artifacts: [Deployment Diagram]
bian-service-domains: [Integration.API]
---

# /terraform

## When to apply
Use for reviewing banking Terraform/IaC to prevent "IaC-rot," drift, and catastrophic infrastructure-misconfigurations in production. Essential gate for any banking deployment.

## Inputs
- **IaC Code** â€” Terraform/Bicep/ARM code.
- **Environment** â€” DEV/QA/PROD targets.

## Process
1. **Security Scan.** Run IaC tools (e.g., Checkov, tfsec) to catch public-buckets, open-security-groups, or unencrypted-storage defined in code.
2. **State Management Analysis.** Check for secure remote state (S3/Blob w/ locking, encryption, versioning).
3. **Drift & Modularization review.** Are critical systems modularized for consistency? Does a drift-detection process exist?
4. **Secret Handling Audit.** Terraform must NEVER contain raw secrets; must reference CMK/SecretsManager-ARNs.
5. **Issue Verdict.** Review-findings + veto-conditions.

## Banking pitfalls
- **State-file exposure** â€” State files containing sensitive infra-keys/secret-ARNs stored in unsecured buckets.
- **"Copy-Paste" Modularization** â€” Copy-pasting instead of referencing shared modules, leading to divergence and massive security debt across environments.
- **Ignoring "Default-provider-is-non-compliant"** â€” Terraform defaults (e.g., S3-bucket-encryption:false) that must be overridden for banking compliance.
- **Manual-change-drift** â€” Infrastructure being manually updated via UI/CLI after Terraform-deployment, rendering IaC stale.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of terraform meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the terraform process.**

## Outputs
- **IaC review report** â€” Scan results, security-findings, state-risks.
- **Infrastructure-drift status** â€” Drift-detection maturity-assessment.

## Related skills
- [aws-review](../aws-review/SKILL.md)
- [azure-review](../azure-review/SKILL.md)
- [security-architecture-review](../../security/security-architecture-review/SKILL.md)

### Banking Context & Examples

#### (1) Terraform State Security
**Scenario:** Storing state files for core banking infrastructure.
- **Architecture Lens Check:** Verification that state-file buckets have `Versioned=true`, `Encryption=AES-256`, and `Access=Private`.
- **Sample Outcome:** "State Management: Verified backend remote-state uses dedicated, encrypted, and private S3 bucket with versioning."
- **Common Pitfall:** Saving state files in a generic unencrypted bucket. If a developer accidentally logs the raw state to a log file, the entire cloud infrastructure's internal structure (including secret references) is exposed.

#### (2) Compliance-as-Code Enforced
**Scenario:** Defining S3/Blob storage in Terraform.
- **Architecture Lens Check:** Terraform snippet must override provider defaults to explicitly enforce `Encryption=true`.
- **Sample Outcome:** "Terraform Scan: Confirmed bucket `encryption_configuration` blocks unencrypted uploads."
- **Common Pitfall:** Relying on provider/module defaults; many modules default to *unencrypted* storage for backwards compatibility, resulting in an automated deployment of non-compliant infrastructure.

#### (3) Sharia Product IaC Audit
**Scenario:** Creating IaC modules for Sharia ledger environments.
- **Architecture Lens Check:** Ensuring infrastructure tags enforce `Sharia-Compliant-Status` for audit compliance.
- **Sample Outcome:** "IaC Standard: Verified that all ledger modules inject `Sharia-Compliant-Status` tag into all resources."
- **Common Pitfall:** Neglecting to inject regulatory tags in IaC modules. As the infrastructure scales, the bank loses the ability to distinguish Sharia assets from conventional ones at an infrastructure level, failing external regulatory/Sharia Governance audits.

## Bulletproofing
- **Governance Policy:** Enforce [CBUAE Rulebook](governance/policy/regulations.yaml#CBUAE), [PDPL](governance/policy/regulations.yaml#PDPL), and [PCI-DSS](governance/policy/regulations.yaml#PCI-DSS) where applicable.

## Anti-patterns
- **Committing local terraform.tfstate files or sensitive secrets to git**
  - **Consequence:** Credentials exposure, state locking issues, and resource overwrites during parallel executions.
  - **Correct Approach:** Store terraform state in a secure remote backend (e.g., S3/GCS) with DynamoDB/Firestore locking.
- **Hardcoding cloud resource variables inside Terraform modules**
  - **Consequence:** Code repetition, lack of reusability, and deployment errors across environments (dev/prod).
  - **Correct Approach:** Use tfvars files and modularize code to accept input parameters dynamically.
- **Skipping strict static analysis or validation tools (tflint, tfsec, checkov) in pipeline**
  - **Consequence:** Deployment of insecure infrastructure (e.g., open security groups, unencrypted databases).
  - **Correct Approach:** Integrate automated compliance check gates inside CI/CD linting phases before applying Terraform plans.
