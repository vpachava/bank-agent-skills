---
name: cutover-plan
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when authoring a cutover plan for a banking release/migration — produces a cutover-runbook (pre-checks, freeze, go/no-go, hypercare)."
required-inputs:
  - Initiative/system-scope
  - Go/No-Go criteria (quantifiable)
  - Stakeholder & support-command team-lists
  - Data-integrity & validation checklist
expected-deliverables:
  - Cutover execution runbook
  - Go/No-Go decision matrix
  - Hypercare plan
---

# /cutover-plan

## When to apply
Use to oversee the high-risk "final switch" moment of a migration or release. Ensures the transition is methodical, audited, and possesses established, non-negotiable exit points to guarantee business-data integrity.

## Inputs
- **Business/Tech Context** — System criticality and expected downtime impact.
- **Go/No-go Readiness** — Pre-checks (e.g. data consistency confirmed, integration services online).
- **Stakeholder Registry** — Command center participants (Dev, Ops, Compliance, Security, Business).

## Process
1. **Define Cutover Window.** Establish the exact timing for the freeze (e.g. "Banking shutdown period").
2. **Draft Pre-Flight Checklists.** Non-negotiable readiness-gates (e.g. "Data sync lag < 100ms", "Backup successfully completed").
3. **Draft Execution Runbook.** Sequential, time-stamped commands to perform the final switch, test, and verify.
4. **Define Go/No-Go decision.** Who has final authority? What specific, quantified thresholds must be met?
5. **Hypercare plan.** Define the intense monitoring/support period immediately post-cutover (e.g. 72h continuous).

## Banking pitfalls
- **Unquantified Go/No-Go** — Go/No-Go based on "vibes" or "feeling good," rather than data-confirmed stability markers (e.g. "Can we process a dummy-payment end-to-end?").
- **Ignoring regulatory freeze** — Attempting a cutover during a sensitive regulatory period (e.g. CBUAE/DIFC reporting dates), risking compliance impact.
- **"Cutover" as a solo-tech-job** — Treating it as a dev task instead of a cross-functional banking operational event involving Compliance, Security, and Business teams.
- **Hidden rollback requirements** — Not having the [rollback-plan](../rollback-plan/SKILL.md) explicitly integrated as a contingency step *within* the cutover runbook's logic.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of cutover-plan meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the cutover-plan process.**

## Outputs
- **Cutover execution runbook** — Time-stamped implementation tasks.
- **Go/No-Go decision matrix** — The authoritative checklist for switching.
- **Hypercare plan** — Post-switch monitoring and escalation procedures.

## Related skills
- [rollback-plan](../rollback-plan/SKILL.md)
- [production-readiness](../../governance/production-readiness/SKILL.md)
- [release-readiness](../../devops/release-readiness/SKILL.md)
