---
name: rollback-plan
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when authoring a rollback plan for a banking release/migration â€” produces a rollback-runbook (triggers, steps, data-consistency)."
required-inputs:
  - Subject system, version, & rollback-scope
  - Rollback-trigger criteria (KPI/service-health targets)
  - Data-consistency & integrity assurance steps
  - Stakeholder communication plan
expected-deliverables:
  - Rollback operational plan (runbook)
  - Failure/trigger-criteria table
  - Post-rollback data-reconciliation steps
togaf-phases: [Phase F]
togaf-artifacts: [Migration Plan]
bian-service-domains: [Integration.Migration]
---

# /rollback-plan

## When to apply
Use for *every* significant banking deployment, rollout, or migration. A banking rollback-plan is not "a panic step" â€” it is a codified operational procedure that must be exercised and validated *before* the operation begins to guarantee business continuity.

## Inputs
- **Rollback triggers** â€” What specific telemetry event triggers a rollback (e.g. TPS drop > X%, error rate > Y%, data-mismatch detected)?
- **Integrity profile** â€” How will we confirm data integrity after the reversal?
- **Scope** â€” Is the rollback atomic (for the app) or cross-component (app + DB + interface-adapter)?

## Process
1. **Define Rollback Scope.** Is it a partial revert, a full-version revert, or a database-data reversal (extremely complex, requires dual-write/CDC)?
2. **Define Triggers (Thresholds).** Quantifiable service-health markers that *mandatorily* activate the rollback procedure.
3. **Draft Operational Steps.** Detailed procedural steps to undo the deployment (e.g. traffic shifting, DB-connection reversal, config-map revert).
4. **Draft Post-Rollback Integrity.** Reconciliation procedures to fix data-inconsistencies introduced by the "failed-forward" attempt (crucial for payment-data integrity).
5. **Stakeholder Communication.** Define the "rollback activation" communication path (e.g. notify SOC/CRO/Compliance team of the reversal).

## Banking pitfalls
- **DB-reversal ignorance** â€” Thinking "just revert the app code" is enough after the application has already started writing new data to the DB; database-reversals must explicitly handle data-integrity correction.
- **Rollback "never practiced"** â€” The rollback plan is a theoretical document; if not dry-run in test environments, it will likely fail during a real incident when pressure is highest.
- **Lack of trigger clarity** â€” No consensus on *when* to trigger, leading to "stalling-in-failure" (fighting to fix the system while itâ€™s crashing instead of performing the safe revert).
- **Communication-gap** â€” Reversing the system without notifying compliance/monitoring teams, creating audit-risks or triggering false-positive security-alerts.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of rollback-plan meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the rollback-plan process.**

## Outputs
- **Rollback operational plan** â€” The standardized, tested runbook.
- **Failure/trigger-criteria table** â€” The codified decision matrix for triggers.
- **Post-rollback reconciliation steps** â€” Procedures ensuring data consistency post-reversion.

## Related skills
- [production-readiness](../../governance/production-readiness/SKILL.md)
- [release-readiness](../../devops/release-readiness/SKILL.md)
- [database-migration](../database-migration/SKILL.md)

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
- **Assuming code rollbacks automatically handle data structure rollbacks**
  - **Consequence:** The older code version is restored but cannot read the newly migrated database schema, leaving the system hard-down.
  - **Correct Approach:** Provide distinct, decoupled rollback plans for application binaries, environment configs, and database schema states.
- **Relying on full backup restorations as the primary rollback mechanism for large active databases**
  - **Consequence:** Restoring a multi-terabyte database takes 10 hours, violently blowing past the recovery time objective (RTO).
  - **Correct Approach:** Design bi-directional data synchronization or employ fast storage snapshots/clones for instant rollback capability.
- **Testing the rollback plan for the first time during the actual live crisis**
  - **Consequence:** Command line syntax errors or missing access permissions prevent the emergency rollback from executing.
  - **Correct Approach:** Execute mandatory 'game day' fire drills where the rollback scripts are run in Staging environments to verify them.
