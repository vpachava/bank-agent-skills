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
