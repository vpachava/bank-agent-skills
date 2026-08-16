---
name: cloud-migration
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when planning a cloud migration (6Rs) for a banking workload — produces a cloud-migration plan grounded in landing-zone constraints."
required-inputs:
  - Banking workload inventory & criticality
  - Target cloud landing-zone architecture (cross-link to cloud-well-architected)
  - Data-residency & UAE-regulatory constraints
  - Migration risk & dependency profile
expected-deliverables:
  - Cloud migration plan document
  - 6Rs workload mapping (Rehost/Replatform/Refactor/Rearchitect/Retain/Retire)
  - Pre-migration readiness assessment
---

# /cloud-migration

## When to apply
Use during the planning phase for shifting banking workloads to cloud. Ensures the move respects strict CBUAE data-residency, security governance, and operational-continuity rules before a single workload moves.

## Inputs
- **Workload Inventory** — BIAN-mapped domain, data-sensitivity, peak/average load.
- **Landing Zone Architecture** — Defined cloud-well-architected foundation (from [cloud-well-architected](../../research/cloud-well-architected-banking.md)).
- **Residency/Regulatory constraints** — PDPL, CBUAE data-placement rules.
- **Migration profile** — Risk appetite, technical dependency graph (from [modernization-roadmap](../../modernization/modernization-roadmap/SKILL.md)).

## Process
1. **Inventory & 6Rs mapping.** Catalog all components in scope. Assign a 6Rs strategy to each: Rehost (Lift-and-shift), Replatform (e.g., containerize), Refactor (Modernize API), Rearchitect, Retain, Retire.
2. **Landing-zone validation.** Verify target landing-zone supports data-residency, network-isolations, and identity-federation needs for this workload.
3. **Banking-gate sequence.** Plan migration in alignment with regulatory-approval windows.
4. **Resiliency/DR mapping.** Define the target-state resiliency posture (must meet CBUAE ↔ geo-redundant requirement).
5. **Author the migration plan.** Document the plan, transition-state architecture, and go/no-go criteria.

## Banking pitfalls
- **Ignoring "Silent Data Drift"** — During long migration windows, failing to detect inconsistencies between source and target databases.
- **"Lift-and-Shift" compliance trap** — Rehosting a monolith to the cloud often ignores the need to modernize IAM/logging to meet cloud-native governance standards.
- **Integration-seam breakage** — Failing to account for how the migrated workload integrates with non-migrated core-banking systems (latency, security barriers).
- **Hard-coding residency** — Assuming cloud-region availability means residency compliance without validating the specific Azure/AWS/OCI region meets in-country residency rules.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of cloud-migration meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the cloud-migration process.**

## Outputs
- **Cloud migration plan** — Phased plan including transition architecture.
- **6Rs workload mapping** — Documented strategy per component.
- **Pre-migration readiness assessment** — Sign-off that the landing-zone and workload are migration-ready.

## Related skills
- [modernization-roadmap](../../modernization/modernization-roadmap/SKILL.md)
- [release-readiness](../../devops/release-readiness/SKILL.md)
- [production-readiness](../../governance/production-readiness/SKILL.md)
