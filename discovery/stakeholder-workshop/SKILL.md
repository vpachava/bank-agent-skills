---
name: stakeholder-workshop
owner: Solution Architecture
version: 0.1.0
last-reviewed: 2026-08-08
description: "Use when eliciting requirements or decisions from a banking initiative's stakeholders â€” produces a workshop design (agenda, exercises) and a structured outcomes/decisions log with owners."
required-inputs:
  - Initiative goal & scope
  - Stakeholder map with roles & decision rights
  - Known regulatory constraints in scope
  - Time/attendee bounds of the session
expected-deliverables:
  - Workshop design (agenda, exercises, inputs to send ahead)
  - Run plan (facilitation, outputs per exercise)
  - Outcomes & decisions log (owner, decision, rationale, follow-up)
togaf-phases: [Phase A]
togaf-artifacts: [Architecture Vision]
bian-service-domains: [Customer Account.Origination]
---

# /stakeholder-workshop

## When to apply
Use when a banking initiative needs *collective* elicitation â€” requirements, a target-state decision, a prioritization call â€” and the right answer lives across business + IT + Risk + Compliance heads who won't converge by email. Pairs with `/requirements-analysis` (workshop elicits, requirements-analysis baselines) and `/solution-options` (workshop can evaluate options).

## Inputs
- **Initiative goal & scope** â€” the one- or two-line outcome and what's explicitly out of scope.
- **Stakeholder map with decision rights** â€” who must attend, who's consulted, who's informed; name the decision-maker upfront so the workshop doesn't end in "we'll take it offline."
- **Known regulatory constraints** â€” bring CBUAE/residency/KYC bounds into the room, not as a surprise.
- **Time & attendee bounds** â€” half-day, full-day, remote, async; the format is dictated by the constraints, not the other way round.

## Process
1. **Define the workshop's decision question.** A workshop without a single decision or a tight set of decisions becomes a status meeting. State it before anything else and pin who decides.

2. **Design the stakeholder room honestly.** A bank initiative needs business, IT, Risk, Compliance, Security, and Operations voices â€” not all as deciders, but all as lenses. If Risk/Compliance are absent, the outputs aren't bank-buildable.
   > Attendee list *is* a design decision. An architect-run-only workshop on a regulated journey produces gaps the compliance review later weaponizes.

3. **Pre-circulate inputs, not surprises.** Send the goal, the known constraints, and one-page context ahead. Workshop time is for *synthesis and decisions*, not first exposure.

4. **Sequence exercises from framing â†’ elicitation â†’ decision.** Start with goal/scope alignment, elicit per-stakeholder-lens (capability/requirement/constraint), then converge on the decision(s). Avoid jumping to solutioning before elicitation is done.

5. **Run structured elicitation techniques.** Capability canvassing (BIAN areas), pain-point mapping, current-state journey walkthroughs, "what would have to be true" framing for contentious decisions. Capture each contribution against the stakeholder + lens that produced it.

6. **Record decisions live, with rationale and owner.** Every decision needs a decider, a rationale ("we chose X *because* Y"), and any follow-up. A decision with no owner is an open question.

7. **Convert open threads to tickets / follow-ups.** Workshop ends â‰  work over. Each unresolved thread becomes a follow-up (and often feeds the RAID log or a research/decision ticket on the map).

## Bulletproofing against Rationalization
To prevent decisions without accountability and architectural drifting in a silo, you MUST:

1. **Mandatory Gatekeeper Alignment:** Solutioning architecture exercises CANNOT begin until strict constraints (Security, CBUAE) are presented by and aligned with the designated Compliance representatives in the room. 
2. **Decision Accountability Rule:** Documented decisions from the workshop MUST trace to a single, named decider. "The Committee" or "The Team" are invalid owners.
3. **Asymmetric Knowledge Prohibition:** Inputs and known constraints MUST be mandated as Pre-Read; workshop time diverted to presenting new foundational constraints indicates a failed workshop preparation.
4. **Actionable Unresolved Thread Tracking:** Open threads MUST be translated into defined follow-up tasks with an owner.

**Violating these rules invalidates the Stakeholder Workshop outcomes.**

## Banking pitfalls
- **No Risk/Compliance in the room** â€” a discovery workshop without these voices ships decisions that fail the architecture-board / production-readiness gates. Fix the room before the agenda.
- **Designing the solution instead of eliciting the problem** â€” architects love solutioning; a workshop that jumps to "Kafka + a new microservice" before the journey and constraints are mapped produces the wrong right answer.
- **"Decisions" with no decider** â€” group discussions that defer to "the business owner will decide later" aren't decisions; they're items you'll re-litigate.
- **Ignoring the regulatory ceiling in-room** â€” designing a target state that assumes free data movement, then discovering the onshoreâ†”DIFC SCC obligation *after* sign-off, wastes the workshop.
- **No async path for the long-tail stakeholders** â€” regional Ops, branch ops, and some 3rd-party partners can't all attend live; build in an async contribution window or their inputs surface too late.
- **Outcomes log that loses rationale** â€” capturing "we decided X" without *because Y* means six months later nobody can defend the decision at the architecture board.

## Outputs
- **Workshop design** â€” decision question, stakeholder map, agenda, exercises, pre-read materials.
- **Run plan** â€” facilitation approach, per-exercise inputs & outputs, decision co-pilot notes.
- **Outcomes & decisions log** â€” every decision with decider, rationale, owner, and follow-up; unresolved threads as follow-up items (feed RAID / gap-analysis).

## Related skills
- [requirements-analysis](../requirements-analysis/SKILL.md) â€” turns workshop outputs into the requirements baseline.
- [solution-options](../solution-options/SKILL.md) â€” when the workshop's job is to evaluate 2â€“4 options.
- [gap-analysis](../gap-analysis/SKILL.md) â€” when the workshop surfaces current-state capability gaps.
- [raid-log](../../documentation/raid-log/SKILL.md) â€” where the workshop's open threads live as the initiative runs.

### Regulatory References
1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/
2. **PDPL:** Personal Data Protection Law (Federal Decree-Law No. 45 of 2021)
3. **CBUAE Cybersecurity Framework:** Domain 1: Governance & Risk Management

## Anti-patterns
- **Running workshops without a designated and empowered decision owner**
  - **Consequence:** Endless debates that finish without consensus, delaying project progress.
  - **Correct Approach:** Identify the final decision maker before the workshop, and design exercises to align choices.
- **Proceeding with solutions before aligning on underlying problems**
  - **Consequence:** Building elegant solutions to the wrong problems, wasting time and resources.
  - **Correct Approach:** Dedicate the first half of the workshop to mapping pain points and journey constraints.
- **Excluding critical Risk, Compliance, and Security roles from initial workshops**
  - **Consequence:** Designed solutions are rejected at the board gate, requiring complete rework.
  - **Correct Approach:** Ensure representation from Risk, Compliance, and Security as key contributors in design sessions.
