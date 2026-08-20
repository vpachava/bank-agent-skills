---
name: azure-review
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when reviewing Azure-based banking architectures â€” produces an Azure-review report (well-architected alignment, UAE-residency, security)."
required-inputs:
  - Azure architectural design/IaC
  - Data-residency requirements (UAE regions)
  - Workload criticality (BIAN-domain)
  - Security/Compliance constraints
expected-deliverables:
  - Azure Well-Architected review report
  - UAE data-residency compliance verification
  - Security/IAM risk-register entries
togaf-phases: [Phase D]
togaf-artifacts: [Deployment Diagram]
bian-service-domains: [Integration.API]
---

# /azure-review

## When to apply
Use for reviewing Azure-based banking solutions. Ensures alignment with Microsoft Azure Well-Architected / CAF, while strictly enforcing banking-specific constraints (residency, security-governance) for the UAE market.

## Inputs
- **Azure Design/Code** â€” ARM/Bicep/Terraform targeting Resource-groups/subscriptions.
- **Residency Target** â€” `uaenorth` / `uaecentral` alignment.
- **Workload Profile** â€” Criticality, PII/Payment-data classification.

## Process
1. **Verify UAE-Region Alignment.** Confirm all resources exclusively reside in `uaenorth` (Dubai) / `uaecentral` (Abu Dhabi).
2. **Well-Architected/CAF Alignment.** Review against: Security (Defender-for-Cloud), Reliability (Availability-sets/Zones), Ops (Azure-Policy/Blueprints).
3. **Banking-Specific Security Check.** 
   - IAM: RBAC-roles, Entra-ID federation, Privileged-Identity-Management (PIM) for infra-admin.
   - Guardrails: Azure Policy/Blueprints enforcing region-locks and service-restrictions.
   - Encryption: Azure Key-vault with Customer-managed keys (CMK) mandatory for regulated data.
4. **Data Residency Audit.** Cross-reference all storage-paths against the residency-register.
5. **Issue Review Verdict.** Approve, Conditional-approve, Veto.

## Banking pitfalls
- **Region-misalignment** â€” Accidentally deploying resources into non-UAE regions (e.g. `westeurope` dev-default).
- **Public-endpoint-exposure** â€” Azure App-services/Storage-accounts with "Allow Public Access" for ease-of-testing (critical vulnerability).
- **RBAC-overpermissioning** â€” "Contributor" roles granted to entire resource-group scopes (instead of least-privilege).
- **Ignoring "Azure-Security-Center-as-a-Silo"** â€” Not integrating Azure-security-alerts into the bank's enterprise-SIEM.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of azure-review meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the azure-review process.**

## Outputs
- **Azure Review Report** â€” Well-architected gaps + bank-specific findings.
- **UAE Residency Verification** â€” Formal confirmation of compliant placement.
- **Risk-register entries** â€” Specific security/governance risks discovered.

## Related skills
- [cloud-migration](../../migration/cloud-migration/SKILL.md)
- [security-architecture-review](../../security/security-architecture-review/SKILL.md)
- [compliance](../../security/compliance/SKILL.md)

### Banking Context & Examples

#### (1) Core-Banking Read-Replica Deployment
**Scenario:** Deploying a read-replica of the legacy core database in Azure Sql.
- **Architecture Lens Check:** Verification that the replica is strictly within `uaenorth` and adheres to `CMK` (Customer Managed Key) encryption requirements.
- **Sample Outcome:** "Review Approved: Resources scoped to `uaenorth` subscription. Azure SQL encrypted with Key-vault CMK."
- **Common Pitfall:** Deploying read-replicas in `northeurope` for test workloads. This is a direct `PDPL` residency violation if those databases contain customer PII.

#### (2) Payment-Hub API Deployment
**Scenario:** Deploying a containerized payment hub on `Azure Kubernetes Service` (AKS).
- **Architecture Lens Check:** Usage of `Entra-ID` managed identities for pod authentication and strictly disabling public IP exposure for service endpoints.
- **Sample Outcome:** "Security Review Passed: AKS nodes utilize Private Endpoint networking; authentication locked to Entra-ID federation."
- **Common Pitfall:** Leaving AKS public API endpoints enabled for easier vendor debugging, exposing the internal payment-hub to public scanner attacks.

#### (3) Sharia Product Aggregator Deployment
**Scenario:** Deployment of an aggregator API accessing Sharia product rates.
- **Architecture Lens Check:** Ensuring `Azure Defender for Cloud` alerts are forwarded to the bank's central SOC SIEM.
- **Sample Outcome:** "Governance Check Passed: Defender for Cloud integrated with central SIEM; audit logs secured."
- **Common Pitfall:** Treating Defender as a standalone portal; if alerts are not pushed to the enterprise SOC, security analysts may miss targeted attacks on the rates-API, bypassing the bank's central security-operations capability.


## Bulletproofing
- **Governance Policy:** Enforce [CBUAE Rulebook](governance/policy/regulations.yaml#CBUAE), [PDPL](governance/policy/regulations.yaml#PDPL), and [PCI-DSS](governance/policy/regulations.yaml#PCI-DSS) where applicable.
