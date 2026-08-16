---
name: architecture-board
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when running or presenting to an Architectural Governance Board — produces an board-review artifact (agenda, decisions, risks, board-governance)."
required-inputs:
  - Initiative/Project context
  - Key architectural decisions requiring approval
  - Risk-register summary
  - Strategic alignment evidence
expected-deliverables:
  - Governance-board agenda
  - Architecture-decision approval record
  - Action-item/Risk log
---

# /architecture-board

## When to apply
Use to professionalize and organize the formal Architectural Governance Board (AGB). Banking-governance is not a bureaucratic hurdle; it is the primary mechanism for preventing "architectural-drift," ensuring security adherence, and maintaining regulatory-compliance across the enterprise.

## Inputs
- **Decision-Packages** — The specific items needing AGB endorsement.
- **Compliance-Gate-Status** — Explicit confirmation that what is being proposed doesn't violate residency/CBUAE-rules.

## Process
1. **Agenda Setting.** Clearly state what items need decisions (not just "info-sharing").
2. **Standardized-Review.** Follow the "Architecture-lens" check (Security/Residency/Compatibility/NFRs).
3. **Formal-Decision-Logging.** Decisions must be documented, archived, and communicated as binding-mandates.
4. **Action-Tracking.** AGB actions are not suggestions; they are mandates that *must* be tracked in the project RAID-log or Jira-backlog.

## Bulletproofing against Rationalization
To prevent "info-sharing" sessions that avoid scrutiny and evade accountability, you MUST:

1. **Mandatory Decision Focus:** Every agenda item MUST be classified as "Info", "Decision", or "Risk". Items without a decision or risk trigger are rejected from the AGB.
2. **Mandatory Architecture Lens:** Every AGB agenda MUST include a mandatory compliance check against CBUAE residency rules and legacy system integration compatibility.
3. **Mandatory Action Tracking:** Every AGB decision MUST be tied to an action item and integrated into the project RAID log.
4. **Scrutiny Requirement:** If an item is not fully vetted, the AGB Chair MUST reject the presentation; AGB is not for sharing unvetted proposals.

**Violating these rules invalidates the AGB agenda.**
---

## Outputs
- **Governance-board agenda** — Structured list of items-for-decision.
- **Architecture-decision approval record** — The formal binding-record of the AGB.
- **Action-item/Risk log** — Follow-up tracker.

## Related skills
- [solution-review](../solution-review/SKILL.md)
- [design-review](../design-review/SKILL.md)
- [architecture-decision-records](../../architecture/architecture-decision-records/SKILL.md)
