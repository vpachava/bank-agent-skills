---
name: aws-review
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when reviewing AWS-based banking architectures — produces an AWS-review report (well-architected alignment, UAE-residency, security)."
required-inputs:
  - AWS architectural design/IaC
  - Data-residency requirements (UAE regions)
  - Workload criticality (BIAN-domain)
  - Security/Compliance constraints
expected-deliverables:
  - AWS Well-Architected review report
  - UAE data-residency compliance verification
  - Security/IAM risk-register entries
---

# /aws-review

## When to apply
Use for reviewing AWS-based banking solutions. Ensures alignment with AWS Well-Architected Framework while strictly enforcing banking-specific constraints (residency, security-governance) for the UAE market.

## Inputs
- **AWS Design/Code** — Target VPC/account/service-configs.
- **Residency Target** — `me-central-1` (UAE) alignment.
- **Workload Profile** — Criticality, PII/Payment-data classification.

## Process
1. **Verify UAE-Region Alignment.** Confirm workload is exclusively deployed to `me-central-1` or appropriate CBUAE-compliant regions.
2. **Well-Architected Alignment.** Review against pillars: Reliability (multi-AZ/region), Security (IAM granularity), Operational Excellence (IaC/observability), Cost, Performance.
3. **Banking-Specific Security Check.** 
   - IAM: No static credentials; use IAM Roles/OIDC/Federation.
   - Guardrails: SCPs controlling region restrictions, service-whitelists.
   - Encryption: KMS-encryption with CMKs mandatory for PII/Payment-data.
4. **Data Residency Audit.** Cross-reference all storage-paths against the residency-register.
5. **Issue Review Verdict.** Approve, Conditional-approve, Veto.

## Banking pitfalls
- **Region-misalignment** — Deploying to US/EU regions for "convenience" or "feature availability," violating data-residency laws.
- **Static-credential-sprawl** — Using IAM Users/Access-keys inside EC2/lambda; forces managed-identities/roles-everywhere.
- **Public-data-exposure** — S3/RDS instances configured with public-access-enabled (violation of base security sanity).
- **Ignoring "Cloud-Audit-Blindness"** — Failing to feed CloudTrail/Config-data into the bank’s central SOC-SIEM-toolchain.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of aws-review meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the aws-review process.**

## Outputs
- **AWS Review Report** — Well-architected gaps + bank-specific findings.
- **UAE Residency Verification** — Formal confirmation of compliant placement.
- **Risk-register entries** — Specific security/governance risks discovered.

## Related skills
- [cloud-migration](../../migration/cloud-migration/SKILL.md)
- [security-architecture-review](../../security/security-architecture-review/SKILL.md)
- [compliance](../../security/compliance/SKILL.md)
