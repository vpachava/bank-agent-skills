---
name: cloud-migration
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when planning a cloud migration (6Rs) for a banking workload â€” produces a cloud-migration plan grounded in landing-zone constraints."
required-inputs:
  - Banking workload inventory & criticality
  - Target cloud landing-zone architecture (cross-link to cloud-well-architected)
  - Data-residency & UAE-regulatory constraints
  - Migration risk & dependency profile
expected-deliverables:
  - Cloud migration plan document
  - 6Rs workload mapping (Rehost/Replatform/Refactor/Rearchitect/Retain/Retire)
  - Pre-migration readiness assessment
togaf-phases: [Phase D]
togaf-artifacts: [Deployment Diagram]
bian-service-domains: [Integration.API]
---

# /cloud-migration

## When to apply
Use during the planning phase for shifting banking workloads to cloud. Ensures the move respects strict CBUAE data-residency, security governance, and operational-continuity rules before a single workload moves.

## Inputs
- **Workload Inventory** â€” BIAN-mapped domain, data-sensitivity, peak/average load.
- **Landing Zone Architecture** â€” Defined cloud-well-architected foundation (from [cloud-well-architected](../../research/cloud-well-architected-banking.md)).
- **Residency/Regulatory constraints** â€” PDPL, CBUAE data-placement rules.
- **Migration profile** â€” Risk appetite, technical dependency graph (from [modernization-roadmap](../../modernization/modernization-roadmap/SKILL.md)).

## Process
1. **Inventory & 6Rs mapping.** Catalog all components in scope. Assign a 6Rs strategy to each: Rehost (Lift-and-shift), Replatform (e.g., containerize), Refactor (Modernize API), Rearchitect, Retain, Retire.
2. **Landing-zone validation.** Verify target landing-zone supports data-residency, network-isolations, and identity-federation needs for this workload.
3. **Banking-gate sequence.** Plan migration in alignment with regulatory-approval windows.
4. **Resiliency/DR mapping.** Define the target-state resiliency posture (must meet CBUAE â†” geo-redundant requirement).
5. **Author the migration plan.** Document the plan, transition-state architecture, and go/no-go criteria.

## Banking pitfalls
- **Ignoring "Silent Data Drift"** â€” During long migration windows, failing to detect inconsistencies between source and target databases.
- **"Lift-and-Shift" compliance trap** â€” Rehosting a monolith to the cloud often ignores the need to modernize IAM/logging to meet cloud-native governance standards.
- **Integration-seam breakage** â€” Failing to account for how the migrated workload integrates with non-migrated core-banking systems (latency, security barriers).
- **Hard-coding residency** â€” Assuming cloud-region availability means residency compliance without validating the specific Azure/AWS/OCI region meets in-country residency rules.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of cloud-migration meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the cloud-migration process.**

## Outputs
- **Cloud migration plan** â€” Phased plan including transition architecture.
- **6Rs workload mapping** â€” Documented strategy per component.
- **Pre-migration readiness assessment** â€” Sign-off that the landing-zone and workload are migration-ready.

## Related skills
- [modernization-roadmap](../../modernization/modernization-roadmap/SKILL.md)
- [release-readiness](../../devops/release-readiness/SKILL.md)
- [production-readiness](../../governance/production-readiness/SKILL.md)

### Banking Context & Examples

#### (1) Retail Banking Scenario
**Scenario:** Applying this skill in a retail bank core-modernization effort.
- **Architecture Lens Check:** Verification of compliance with CBUAE data-residency rules (e.g. [[compliance]]).
- **Sample Outcome:** "Design: Automated workflow integration; [[observability]] logs scrubbed of PII."
- **Common Pitfall:** Ignoring the Sharia-governance impact on the product-schema.

#### (2) Corporate Banking Scenario
**Scenario:** Using this skill for a corporate digital-onboarding integration.
- **Architecture Lens Check:** Alignment with AECB credit-reporting integration for legal-entity applicants.
- **Sample Outcome:** "Design: Integration-seam validated for high-assurance KYC; [[api-design]] handles large payload-signatures."
- **Common Pitfall:** Bypassing the mandatory legal-entity KYC check due to tight project timelines.

#### (3) Islamic Banking Scenario
**Scenario:** Utilizing this skill for Sharia-compliant loan product rollouts.
- **Architecture Lens Check:** Sharia-Board approval workflow documented within the [[architecture-decision-records]].
- **Sample Outcome:** "Design: Profit-distribution calculation encapsulated; [[api-design]] schema includes mandatory Sharia-compliance flag."
- **Common Pitfall:** Applying standard interest-based loan models to Islamic products, violating compliance.

### Regulatory References
1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/
2. **PDPL:** Personal Data Protection Law (Federal Decree-Law No. 45 of 2021)
3. **CBUAE Cybersecurity Framework:** Domain 1: Governance & Risk Management


