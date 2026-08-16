---
name: gcp-review
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when reviewing GCP-based banking architectures — produces a GCP-review report (well-architected alignment, UAE-residency, security)."
required-inputs:
  - GCP architectural design/IaC
  - Data-residency requirements (UAE regions)
  - Workload criticality (BIAN-domain)
  - Security/Compliance constraints
expected-deliverables:
  - GCP Well-Architected review report
  - UAE data-residency compliance verification
  - Security/IAM risk-register entries
---

# /gcp-review

## When to apply
Use for reviewing Google Cloud Platform (GCP) solutions in a banking context. Ensures adherence to GCP Well-Architected Framework and, critically, strict adherence to UAE-specific data-residency and banking-security mandates.

## Inputs
- **GCP Design/Code** — Projects/Folders/Terraform config.
- **Residency Target** — `me-central1` (Doha - *Verify actual UAE coverage*) alignment (Note: check current GCC region availability).
- **Workload Profile** — Criticality, PII/Payment-data classification.

## Process
1. **Verify UAE-Region Alignment.** Confirm all resources exclusively reside in regions serving the UAE (or approved GCC regions).
2. **Well-Architected Alignment.** Review against: Security (Cloud Armor/SCC), Reliability (Zonal vs Regional), Ops (Stackdriver/Cloud Logging).
3. **Banking-Specific Security Check.** 
   - IAM: Service-accounts with Workload-Identity; NO static service-account keys.
   - Guardrails: Organization Policy Service enforcing region-restrictions.
   - Encryption: Cloud KMS with CMEK for PII/Payment-data.
4. **Data Residency Audit.** Cross-reference all storage-paths against the residency-register.
5. **Issue Review Verdict.** Approve, Conditional-approve, Veto.

## Banking pitfalls
- **Region-misalignment** — Assuming GCP regions are interchangeable; must explicitly lock region-scope.
- **Orphaned-projects** — GCP projects created for PoCs without proper labeling, billing, or security-owner responsibility.
- **Over-privileged-Service-Accounts** — Service-accounts with broad "Editor" roles across the Organization/Folder.
- **VPC-Network-Exposure** — Cloud-NAT or Public-IP assignments on components that should have been purely internal.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of gcp-review meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the gcp-review process.**

## Outputs
- **GCP Review Report** — Well-architected gaps + bank-specific findings.
- **UAE Residency Verification** — Formal confirmation of compliant placement.
- **Risk-register entries** — Specific security/governance risks discovered.

## Related skills
- [cloud-migration](../../migration/cloud-migration/SKILL.md)
- [security-architecture-review](../../security/security-architecture-review/SKILL.md)
- [compliance](../../security/compliance/SKILL.md)
