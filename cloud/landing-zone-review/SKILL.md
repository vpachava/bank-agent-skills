---
name: landing-zone-review
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when reviewing banking Landing-Zones — produces a Landing-Zone review (governance, policy, network, security) against the banking foundation."
required-inputs:
  - Landing-zone design & IaC
  - Regulatory-residency constraints
  - Banking workload/connectivity patterns
  - Identity & IAM baseline
expected-deliverables:
  - Landing-zone governance assessment report
  - Network-policy & isolation risk-profile
  - Banking compliance gap-analysis
---

# /landing-zone-review

## When to apply
Use to validate the "Foundation" of the bank's cloud presence (the Landing Zone). A flawed Landing Zone makes compliant, secure banking work impossible. This governs the cross-account/subscription structure.

## Inputs
- **LZ Configuration** — VPC/VNet/Account-structure/Policy-foundation.
- **Compliance** — Banking-residency laws + cross-zone transfer rules.

## Process
1. **Goverance-structure review.** Account-structure, subscription-nesting, tag-policies (must facilitate regulatory-cost-allocation).
2. **Network-topology review.** Hub-and-spoke / Transit-Gateway models: verify segmentation between prod/non-prod zones AND between regulated/internal zones.
3. **IAM/Identity-fabric baseline.** Confirm EntraID/IAM roles map to banking-teams, not individual-users.
4. **Policy-as-Code audit.** Inspect Cloud-Policy/Blueprints (e.g., "Must-have logs in LogAnalytics," "Must-have encryption in Transit").
5. **Issue Review Verdict.** Formal assessment of the "Banking-Readiness" of the Foundation.

## Banking pitfalls
- **Over-complex account-hiring** — Creating 100+ accounts without a clear organizational hierarchy/billing-model for regulatory audit.
- **Flat-Network-Foundations** — LZ designed without clear isolation between App/DB/Interface-adapter subnets.
- **Policy-Audit-Lag** — Policies deployed but not monitored; drift not remediated within X-days.
- **Ignoring "Egress-Controls"** — LZ lacking centralized egress-firewalls for banking traffic.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of landing-zone-review meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the landing-zone-review process.**

## Outputs
- **LZ Capability Assessment** — Governance/Policy assessment report.
- **Network-Isolation profile** — Risks in hub-spoke/transit-gateway logic.
- **Banking compliance gap-analysis** — Compliance gaps (e.g. residency/logging gaps).

## Related skills
- [aws-review](../aws-review/SKILL.md)
- [azure-review](../azure-review/SKILL.md)
- [compliance](../../security/compliance/SKILL.md)

### Banking Context & Examples

#### (1) Multi-Region Landing Zone Structure
**Scenario:** Establishing a multi-account AWS/Azure LZ for a bank with UAE onshore and regional offices.
- **Architecture Lens Check:** Verification of `Data-Residency` via strict SCPs/Policies preventing deployment to non-authorized regions outside the UAE.
- **Sample Outcome:** "Governance Check: LZ policies lock all resources to `uaenorth`/`me-central-1`."
- **Common Pitfall:** A "global" LZ setup that allows developers to spin up resources in any region. This is an immediate, catastrophic regulatory failure for banking data.

#### (2) Hub-and-Spoke Network Design
**Scenario:** Network design for a bank-wide landing zone.
- **Architecture Lens Check:** Centralized firewall/ingress-filtering and explicit segmentation between `Internal-Banking` subnets and `External-Payment-Gateway` subnets using a Transit-Gateway/Firewall-Hub.
- **Sample Outcome:** "Network Design: Verified isolation between internal core-banking flows and external internet-facing traffic via centralized egress."
- **Common Pitfall:** A "Flat-VPC" network design for the sake of simplicity. This allows lateral movement if a single public-facing workload is compromised, exposing the core banking systems immediately.

#### (3) Sharia-Governance Audit Tags
**Scenario:** Implementing tag-policies in the landing zone to support Sharia-compliance audits.
- **Architecture Lens Check:** Mandatory tagging of all infrastructure resources with `Sharia-Compliant-Status`.
- **Sample Outcome:** "Governance Policy: All `Finance` resources must have `Sharia-Compliant-Status` tag enforced by Landing Zone policy."
- **Common Pitfall:** Failing to enforce tagging at the Foundation level; auditors cannot determine if resources form part of a Sharia-compliant product-line or not, making "compliance-as-code" impossible for Sharia audits."

### Regulatory References
1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/
2. **PDPL:** Personal Data Protection Law (Federal Decree-Law No. 45 of 2021)
3. **CBUAE Cybersecurity Framework:** Domain 1: Governance & Risk Management

