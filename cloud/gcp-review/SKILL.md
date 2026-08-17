---
name: gcp-review
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when reviewing GCP-based banking architectures â€” produces a GCP-review report (well-architected alignment, UAE-residency, security)."
required-inputs:
  - GCP architectural design/IaC
  - Data-residency requirements (UAE regions)
  - Workload criticality (BIAN-domain)
  - Security/Compliance constraints
expected-deliverables:
  - GCP Well-Architected review report
  - UAE data-residency compliance verification
  - Security/IAM risk-register entries
togaf-phases: [Phase D]
togaf-artifacts: [Deployment Diagram]
bian-service-domains: [Integration.API]
---

# /gcp-review

## When to apply
Use for reviewing Google Cloud Platform (GCP) solutions in a banking context. Ensures adherence to GCP Well-Architected Framework and, critically, strict adherence to UAE-specific data-residency and banking-security mandates.

## Inputs
- **GCP Design/Code** â€” Projects/Folders/Terraform config.
- **Residency Target** â€” `me-central1` (Doha - *Verify actual UAE coverage*) alignment (Note: check current GCC region availability).
- **Workload Profile** â€” Criticality, PII/Payment-data classification.

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
- **Region-misalignment** â€” Assuming GCP regions are interchangeable; must explicitly lock region-scope.
- **Orphaned-projects** â€” GCP projects created for PoCs without proper labeling, billing, or security-owner responsibility.
- **Over-privileged-Service-Accounts** â€” Service-accounts with broad "Editor" roles across the Organization/Folder.
- **VPC-Network-Exposure** â€” Cloud-NAT or Public-IP assignments on components that should have been purely internal.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of gcp-review meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the gcp-review process.**

## Outputs
- **GCP Review Report** â€” Well-architected gaps + bank-specific findings.
- **UAE Residency Verification** â€” Formal confirmation of compliant placement.
- **Risk-register entries** â€” Specific security/governance risks discovered.

## Related skills
- [cloud-migration](../../migration/cloud-migration/SKILL.md)
- [security-architecture-review](../../security/security-architecture-review/SKILL.md)
- [compliance](../../security/compliance/SKILL.md)

### Banking Context & Examples

#### (1) Core-Banking Read-Replica Deployment
**Scenario:** Deploying a Cloud Spanner read-replica for a legacy core.
- **Architecture Lens Check:** Verification that the replica is strictly within approved UAE-serving regions and uses `CMEK` (Customer Managed Encryption Key) in Cloud KMS.
- **Sample Outcome:** "Review Approved: Region-restriction enforced via GCP Org Policy; Cloud Spanner encrypted with project CMK."
- **Common Pitfall:** Allowing the Spanner instance to span multi-region groups that include non-UAE centers, triggering a regulatory residency violation for PII stored within the records.

#### (2) Payment-Hub API Deployment
**Scenario:** Deploying a containerized payment hub on `GKE` (Google Kubernetes Engine).
- **Architecture Lens Check:** Usage of `Workload Identity` for pod-to-GCP authentication and disabling public IP exposure for service endpoints.
- **Sample Outcome:** "Security Review Passed: GKE uses Workload Identity for all service accounts; VPC-SC (VPC Service Controls) enabled to perimeter-fence the project."
- **Common Pitfall:** Using static "Service Account Keys" JSON files inside container images; Google's scanners will quickly identify this as a critical vulnerability.

#### (3) Sharia Product Aggregator Deployment
**Scenario:** Deployment of an aggregator API accessing Sharia product rates.
- **Architecture Lens Check:** Ensuring `Cloud Logging` and `SCC` (Security Command Center) alerts are synced to the enterprise SOC/SIEM.
- **Sample Outcome:** "Governance Check Passed: Cloud Logging integrated with internal SOC; anomaly detection alerts forwarded to central security-operations."
- **Common Pitfall:** Letting logs die in Cloud Logging dashboard. If the security team isn't ingesting these logs into their primary toolchain (like Sentinel), they are functionally blind to attacks on the production API.

### Regulatory References
1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/
2. **PDPL:** Personal Data Protection Law (Federal Decree-Law No. 45 of 2021)
3. **CBUAE Cybersecurity Framework:** Domain 1: Governance & Risk Management


