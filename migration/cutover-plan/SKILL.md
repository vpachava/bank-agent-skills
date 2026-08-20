---
name: cutover-plan
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when authoring a cutover plan for a banking release/migration â€” produces a cutover-runbook (pre-checks, freeze, go/no-go, hypercare)."
required-inputs:
  - Initiative/system-scope
  - Go/No-Go criteria (quantifiable)
  - Stakeholder & support-command team-lists
  - Data-integrity & validation checklist
expected-deliverables:
  - Cutover execution runbook
  - Go/No-Go decision matrix
  - Hypercare plan
togaf-phases: [Phase F]
togaf-artifacts: [Migration Plan]
bian-service-domains: [Integration.Migration]
---

# /cutover-plan

## When to apply
Use to oversee the high-risk "final switch" moment of a migration or release. Ensures the transition is methodical, audited, and possesses established, non-negotiable exit points to guarantee business-data integrity.

## Inputs
- **Business/Tech Context** â€” System criticality and expected downtime impact.
- **Go/No-go Readiness** â€” Pre-checks (e.g. data consistency confirmed, integration services online).
- **Stakeholder Registry** â€” Command center participants (Dev, Ops, Compliance, Security, Business).

## Process
1. **Define Cutover Window.** Establish the exact timing for the freeze (e.g. "Banking shutdown period").
2. **Draft Pre-Flight Checklists.** Non-negotiable readiness-gates (e.g. "Data sync lag < 100ms", "Backup successfully completed").
3. **Draft Execution Runbook.** Sequential, time-stamped commands to perform the final switch, test, and verify.
4. **Define Go/No-Go decision.** Who has final authority? What specific, quantified thresholds must be met?
5. **Hypercare plan.** Define the intense monitoring/support period immediately post-cutover (e.g. 72h continuous).

## Banking pitfalls
- **Unquantified Go/No-Go** â€” Go/No-Go based on "vibes" or "feeling good," rather than data-confirmed stability markers (e.g. "Can we process a dummy-payment end-to-end?").
- **Ignoring regulatory freeze** â€” Attempting a cutover during a sensitive regulatory period (e.g. CBUAE/DIFC reporting dates), risking compliance impact.
- **"Cutover" as a solo-tech-job** â€” Treating it as a dev task instead of a cross-functional banking operational event involving Compliance, Security, and Business teams.
- **Hidden rollback requirements** â€” Not having the [rollback-plan](../rollback-plan/SKILL.md) explicitly integrated as a contingency step *within* the cutover runbook's logic.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of cutover-plan meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the cutover-plan process.**

## Outputs
- **Cutover execution runbook** â€” Time-stamped implementation tasks.
- **Go/No-Go decision matrix** â€” The authoritative checklist for switching.
- **Hypercare plan** â€” Post-switch monitoring and escalation procedures.

## Related skills
- [rollback-plan](../rollback-plan/SKILL.md)
- [production-readiness](../../governance/production-readiness/SKILL.md)
- [release-readiness](../../devops/release-readiness/SKILL.md)

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
- **Scheduling cutovers without predefined execution timeboxes and checkpoint gates**
  - **Consequence:** Operations teams run out of time and attempt to rush critical steps, resulting in botched deployments and data loss.
  - **Correct Approach:** Write a minute-by-minute runbook with strict "Go/No-Go" decision checkpoints based on time limits.
- **Failing to define explicit criteria and commands for executing a rollback**
  - **Consequence:** The team realizes the migration is failing but has no practiced script for restoring the legacy system state safely.
  - **Correct Approach:** Document, script, and test specific rollback procedures and database restoration commands before the cutover begins.
- **Undercommunicating with business owners during the cutover window**
  - **Consequence:** Business operations are stalled in confusion, and the helpdesk is overwhelmed with identical problem reports.
  - **Correct Approach:** Establish a dedicated communication bridge and issue periodic status updates to a predefined stakeholder list.
