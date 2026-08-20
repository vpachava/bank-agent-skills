---
name: migration-wave-planning
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when sequencing banking workloads for migration â€” produces a wave plan (dependencies, risk, banking gates)."
required-inputs:
  - Total migration scope (app/DB/platform inventory)
  - Inter-service & inter-domain dependencies
  - Change-window/Risk appetite constraints
  - Regulatory-approval roadmap
expected-deliverables:
  - Migration wave plan (sequenced roadmap)
  - Workload-dependency & risk-classification matrix
  - Migration-gating schedule
togaf-phases: [Phase F]
togaf-artifacts: [Migration Plan]
bian-service-domains: [Integration.Migration]
---

# /migration-wave-planning

## When to apply
Use to structure the multi-year bank transformation into manageable, risk-mitigated delivery increments (waves), ensuring that sequencing is technically sound and regulatorily compliant.

## Inputs
- **Workload Portfolio** â€” All initiatives/workloads to be migrated.
- **Dependency Map** â€” Hard technical dependencies (e.g. App A requires Database B).
- **Phasing constraints** â€” Regulatory freeze periods, peak business seasons, resource availability.

## Process
1. **Classify and Rank.** Categorize workloads by (1) Difficulty (Technical/Regulatory), (2) Value-to-Bank, (3) Risk.
2. **Dependency Mapping.** Visualize the "Dependency Graph" for the portfolios. Identify "Foundational Migrations" (landing-zone, identity-foundation, core-data-sync) that must come first.
3. **Draft Wave Sequence.**
   - *Wave 0:* Foundation & Low-risk pilots.
   - *Wave 1-N:* Sequenced by dependency + value, ensuring regulatory gates are met.
4. **Resilience-Check.** Ensure each wave is sized to survive the potential failure of that wave (e.g., bank can still process payments if Wave N fails).
5. **Author wave plan.** Document the sequencing, justification, and high-level milestones per wave.

## Banking pitfalls
- **"Foundation-as-an-afterthought"** â€” Expecting functional application-waves to succeed before the *fundamental* cloud-platform/identity-fabric-foundation is production-ready.
- **Regulatory-gating invisibility** â€” Planning migration waves without accounting for "Compliance/Audit review" windows that can block a wave for months.
- **"Migrate-only-the-easy-stuff"** â€” Sequencing low-value periphery services first, leaving the hardest core-banking/monolith risk-bottlenecks to the end (opposite of strangler-fig pattern).
- **Ignoring "resilience-capacity"** â€” Planning migration waves that consume so much team capacity/risk-budget that the bank is effectively unable to fix bugs in the core-banking system.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of migration-wave-planning meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the migration-wave-planning process.**

## Outputs
- **Migration wave plan** â€” The sequenced roadmap document.
- **Workload-dependency matrix** â€” Critical risks and sequencing logic per unit.
- **Migration-gating schedule** â€” Timeline mapped to business/compliance triggers.

## Related skills
- [modernization-roadmap](../../modernization/modernization-roadmap/SKILL.md)
- [cloud-migration](../cloud-migration/SKILL.md)
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

## Bulletproofing
- **Governance Policy:** Enforce [CBUAE Rulebook](governance/policy/regulations.yaml#CBUAE), [PDPL](governance/policy/regulations.yaml#PDPL), and [PCI-DSS](governance/policy/regulations.yaml#PCI-DSS) where applicable.

## Anti-patterns
- **Grouping applications into waves without mapping upstream integration dependencies**
  - **Consequence:** Breaking critical APIs when an upstream legacy application remains on-prem while its dependent moves to cloud.
  - **Correct Approach:** Use automated discovery tools (e.g. AppDynamics/Dynatrace) to map inter-service chattiness and group cohesive units.
- **Scheduling the most complex, mission-critical application in Wave 1**
  - **Consequence:** High risk of severe failure before the migration team has established processes and cloud foundations.
  - **Correct Approach:** Select low-risk, internal-facing applications for Wave 1 to test the Landing Zone and refine the runbook.
- **Running waves continuously without pausing for retrospective learnings**
  - **Consequence:** The team repeats the same manual mistakes across hundreds of migrations, wasting time and resources.
  - **Correct Approach:** Enforce a hardening sprint between early waves to automate scripts and fix gaps discovered in the process.
