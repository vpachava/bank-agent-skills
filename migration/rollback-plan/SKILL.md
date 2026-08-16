---
name: rollback-plan
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when authoring a rollback plan for a banking release/migration — produces a rollback-runbook (triggers, steps, data-consistency)."
required-inputs:
  - Subject system, version, & rollback-scope
  - Rollback-trigger criteria (KPI/service-health targets)
  - Data-consistency & integrity assurance steps
  - Stakeholder communication plan
expected-deliverables:
  - Rollback operational plan (runbook)
  - Failure/trigger-criteria table
  - Post-rollback data-reconciliation steps
---

# /rollback-plan

## When to apply
Use for *every* significant banking deployment, rollout, or migration. A banking rollback-plan is not "a panic step" — it is a codified operational procedure that must be exercised and validated *before* the operation begins to guarantee business continuity.

## Inputs
- **Rollback triggers** — What specific telemetry event triggers a rollback (e.g. TPS drop > X%, error rate > Y%, data-mismatch detected)?
- **Integrity profile** — How will we confirm data integrity after the reversal?
- **Scope** — Is the rollback atomic (for the app) or cross-component (app + DB + interface-adapter)?

## Process
1. **Define Rollback Scope.** Is it a partial revert, a full-version revert, or a database-data reversal (extremely complex, requires dual-write/CDC)?
2. **Define Triggers (Thresholds).** Quantifiable service-health markers that *mandatorily* activate the rollback procedure.
3. **Draft Operational Steps.** Detailed procedural steps to undo the deployment (e.g. traffic shifting, DB-connection reversal, config-map revert).
4. **Draft Post-Rollback Integrity.** Reconciliation procedures to fix data-inconsistencies introduced by the "failed-forward" attempt (crucial for payment-data integrity).
5. **Stakeholder Communication.** Define the "rollback activation" communication path (e.g. notify SOC/CRO/Compliance team of the reversal).

## Banking pitfalls
- **DB-reversal ignorance** — Thinking "just revert the app code" is enough after the application has already started writing new data to the DB; database-reversals must explicitly handle data-integrity correction.
- **Rollback "never practiced"** — The rollback plan is a theoretical document; if not dry-run in test environments, it will likely fail during a real incident when pressure is highest.
- **Lack of trigger clarity** — No consensus on *when* to trigger, leading to "stalling-in-failure" (fighting to fix the system while it’s crashing instead of performing the safe revert).
- **Communication-gap** — Reversing the system without notifying compliance/monitoring teams, creating audit-risks or triggering false-positive security-alerts.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of rollback-plan meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the rollback-plan process.**

## Outputs
- **Rollback operational plan** — The standardized, tested runbook.
- **Failure/trigger-criteria table** — The codified decision matrix for triggers.
- **Post-rollback reconciliation steps** — Procedures ensuring data consistency post-reversion.

## Related skills
- [production-readiness](../../governance/production-readiness/SKILL.md)
- [release-readiness](../../devops/release-readiness/SKILL.md)
- [database-migration](../database-migration/SKILL.md)
