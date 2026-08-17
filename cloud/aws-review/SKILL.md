---
name: aws-review
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when reviewing AWS-based banking architectures â€” produces an AWS-review report (well-architected alignment, UAE-residency, security)."
required-inputs:
  - AWS architectural design/IaC
  - Data-residency requirements (UAE regions)
  - Workload criticality (BIAN-domain)
  - Security/Compliance constraints
expected-deliverables:
  - AWS Well-Architected review report
  - UAE data-residency compliance verification
  - Security/IAM risk-register entries
togaf-phases: [Phase D]
togaf-artifacts: [Deployment Diagram]
bian-service-domains: [Integration.API]
---

# /aws-review

## When to apply
Use for reviewing AWS-based banking solutions. Ensures alignment with AWS Well-Architected Framework while strictly enforcing banking-specific constraints (residency, security-governance) for the UAE market.

## Inputs
- **AWS Design/Code** â€” Target VPC/account/service-configs.
- **Residency Target** â€” `me-central-1` (UAE) alignment.
- **Workload Profile** â€” Criticality, PII/Payment-data classification.

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
- **Region-misalignment** â€” Deploying to US/EU regions for "convenience" or "feature availability," violating data-residency laws.
- **Static-credential-sprawl** â€” Using IAM Users/Access-keys inside EC2/lambda; forces managed-identities/roles-everywhere.
- **Public-data-exposure** â€” S3/RDS instances configured with public-access-enabled (violation of base security sanity).
- **Ignoring "Cloud-Audit-Blindness"** â€” Failing to feed CloudTrail/Config-data into the bankâ€™s central SOC-SIEM-toolchain.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of aws-review meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the aws-review process.**

## Outputs
- **AWS Review Report** â€” Well-architected gaps + bank-specific findings.
- **UAE Residency Verification** â€” Formal confirmation of compliant placement.
- **Risk-register entries** â€” Specific security/governance risks discovered.

## Related skills
- [cloud-migration](../../migration/cloud-migration/SKILL.md)
- [security-architecture-review](../../security/security-architecture-review/SKILL.md)
- [compliance](../../security/compliance/SKILL.md)

### Banking Context & Examples

#### (1) Core-Banking Read-Replica Deployment
**Scenario:** Deploying a read-replica of the legacy core database in AWS.
- **Architecture Lens Check:** Verification that the replica is strictly within the `me-central-1` (UAE) region and follows `PII` data-masking rules.
- **Sample Outcome:** "Review Approved: Region `me-central-1` confirmed; replica encrypted with Customer Managed Key (CMK) in compliance with CBUAE guidelines."
- **Common Pitfall:** Creating a replica in `us-east-1` for performance testing, creating a cross-border regulatory breach if PII data is replicated there.

#### (2) Payment-Hub API Deployment
**Scenario:** Deploying a containerized payment hub on AWS EKS.
- **Architecture Lens Check:** Usage of `IAM OIDC` for pod-to-AWS authentication and strictly disabling public EKS-endpoint access.
- **Sample Outcome:** "Security Review Passed: No IAM user credentials used; identity fabric uses IAM Roles for Service Accounts (IRSA)."
- **Common Pitfall:** Using static AWS access keys inside the container image, which would be flagged immediately as a critical security risk by the bank's automated compliance scanners.

#### (3) Sharia Product Aggregator Deployment
**Scenario:** Deployment of a product aggregator API accessing product rates.
- **Architecture Lens Check:** Ensuring logs from `CloudWatch` are forwarded to the centralized SOC/SIEM (e.g., Azure Sentinel or on-prem SIEM used by the bank).
- **Sample Outcome:** "Governance Check Passed: Log-forwarding to internal SIEM enabled; audit compliance maintained."
- **Common Pitfall:** Deploying the API without configuring centralized log-forwarding; logs remain isolated in AWS, creating a "Cloud-Audit-Blindness" that prevents the security team from investigating unauthorized access to sensitive Sharia product rate APIs.

### Regulatory References
1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/
2. **PDPL:** Personal Data Protection Law (Federal Decree-Law No. 45 of 2021)
3. **CBUAE Cybersecurity Framework:** Domain 1: Governance & Risk Management

## Anti-patterns
- **Deploying a flat cloud VPC without clear subnet boundary isolations**
  - **Consequence:** Compromised application instances expose secure database instances directly to public network traffic.
  - **Correct Approach:** Segment infrastructure into public, private, and isolated data subnets with strict security groups.
- **Using IAM users with long-lived access keys instead of IAM Roles/STS**
  - **Consequence:** Hardcoded keys in source control, credential leakage, and high risk of unauthorized cloud manipulation.
  - **Correct Approach:** Authenticate services using AWS IAM Roles for Service Accounts (IRSA) or instance profiles.
- **Ignoring UAE-specific AWS data residency boundaries**
  - **Consequence:** Violation of CBUAE or PDPL data hosting regulations by routing PII out of country.
  - **Correct Approach:** Pin deployment resources to the UAE region and run local audits to block any cross-region data transit.
