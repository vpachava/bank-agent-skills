---
name: refactoring-plan
owner: Solution Architecture
version: 0.1.0
last-reviewed: 2026-08-09
description: "Use when a legacy/wrapped system needs incremental restructuring, not a rewrite — produces a refactoring plan (seams to cut, safe steps, the strangler-sequence) that keeps the bank running at every cut."
required-inputs:
  - The system to refactor & its legacy assessment
  - Impact analysis (/impact-analysis) for the touched seams
  - The target architecture or capability target
  - Release cadence & freeze windows
expected-deliverables:
  - Refactoring plan (seams identified, the strangler sequence, each step)
  - Per-step safety assertions (still-runs, dual-run, rollback)
  - Step-to-release mapping honoring regulatory freeze windows
---

# /refactoring-plan

## When to apply
Use when the verdict from `/legacy-assessment` is Wrap or Replace-by-strangler, and the legacy system must be restructured incrementally while the bank keeps running. Pairs with `/impact-analysis` (each step's blast radius) and feeds `/modernization-roadmap`. The opposite of big-bang: every step leaves the bank runnable.

> **Strangler-fig** (Martin Fowler) is the house posture: build the new alongside the old, route traffic incrementally, let the new grow until the old withers and can be retired. **Never** a freeze-everything rewrite.

## Inputs
- **The system to refactor & its legacy assessment** — the verdict (Wrap/Replace-by-strangler), the coupling brakes, what blocks change.
- **Impact analysis** for the seams you'll cut — the blast radius of each step, the consumers whose contracts change.
- **Target architecture / capability target** — what the refactored state looks like (the new services that will strangle the old).
- **Release cadence & freeze windows** — bank calendars (regulatory freezes, statement runs) constrain when cuts can happen; plan *around* them.

## Process
1. **Identify the seams — the boundaries you can cut at.** A seam is an interface or data boundary you can wrap/intercept/replace without breaking dependents. The seam inventory is the refactoring plan's spine. If you can't find a seam, the first step is *making* one (a façade/adapter in front of the legacy).
   > In a bank the first seam is usually an API gateway or façade in front of the legacy — *nothing* gets refactored until you can route traffic around the old.

2. **Sequence the strangler — order cuts to de-risk the highest-value change.** "Wedge-first": pick the highest-value, lowest-risk thin slice to route through the new path first; that slice proves the new path end-to-end before you commit to the broader migration. Avoid sequencing from the edges inward on a dense coupling hub — you'll starve the load-bearing migration last.

3. **Make every step safe — still-runs, dual-run, rollback.** Each step must keep the bank runnable: behind a feature flag, dual-run where possible (both paths active, compare), rollback-defined (`/rollback-plan`). A refactoring step that can't be rolled back is a release, not a refactor.

4. **Honor the regulatory freeze windows.** The plan times cuts *around* statement runs, regulatory freezes, peak periods (salary-day, cut-off). Plan the *preparatory* steps in the freeze; the *irreversible* cuts outside it.

5. **Handle the event/async seams carefully.** Strangler at an event boundary is the trickiest: dual-publishing, switchable consumers, exactly-once guarantees during transition. The integration-research outbox/idempotent-consumer patterns are how to do this without dropping/duplicating events.

6. **Specify the retirement path for each strangled slice.** Each slice's old path is marked for retirement *with a dep inmedia date* once traffic is verified on the new path. Refactor-without-retirement accumulates dual-run debt forever; name the retirement date.

7. **Tie each step to a release.** A refactoring plan untied to the release cadence is a wish; pair each step with a release window and the readiness gate (`/release-readiness`).

## Banking pitfalls
- **Big-bang in disguise** — a "refactoring plan" of one giant cut is a rewrite; the whole point of strangler is incremental cuts that each leave the bank runnable. If a step touches everything, split it.
- **No seams identified first** — trying to refactor a tightly-coupled core without first inserting an interception seam; the plan can't even start. Step one is often *making* a seam.
- **Wedge-not-first** — sequencing low-value edge cuts first so the high-value load-bearing migration lands last (when energy/learning have run out); pick the highest-value thin slice first.
- **Unsafe steps (no rollback/dual-run)** — a refactoring step that can't be rolled back is a release; insist on feature-flag/dual-run/rollback per step.
- **Freeze windows ignored** — scheduling irreversible cuts inside a regulatory freeze or a statement run; the bank's calendar binds the plan or the plan fails.
- **Event seams half-handled** — dual-publishing/switching consumers at an event boundary done without idempotency/exactly-once guarantees drops or duplicates events; the integration patterns are mandatory here.
- **Retirement dates never set** — each strangled slice left dual-running forever; without a retirement date per slice, the strangler never completes and the debt only grows.
- **Refactor without the target** — refactoring without a target architecture is reshuffling; the target defines the new path you're strangling toward.

## Bulletproofing against Rationalization
To prevent endless refactoring without business value, you MUST:

1. **Mandatory Baseline Metrics:** You CANNOT propose a refactor without documenting the current performance or complexity baseline you are trying to improve.
2. **Mandatory Scope Bounding:** The refactoring plan MUST define explicit completion criteria. "Make it better" is an invalid end state.
3. **Automated Test Coverage Gate:** Refactoring touching critical paths MUST possess a defined automated test coverage baseline BEFORE work begins.

**Violating these rules invalidates the Refactoring Plan.**

## Outputs
- **Refactoring plan** — seams, strangler sequence wedge-first, each step with safety assertion.
- **Per-step safety** — dual-run / feature-flag / rollback per step.
- **Step-to-release mapping** — each step assigned a release window honoring freeze calendars.
- **Retirement dates** — per strangled slice, the old path's planned deprecation.

## Related skills
- [legacy-assessment](../legacy-assessment/SKILL.md) — the verdict feeding the plan.
- [impact-analysis](../impact-analysis/SKILL.md) — sizes each cut's blast radius.
- [modernization-roadmap](../modernization-roadmap/SKILL.md) — the broader wave sequencing this fits into.
- [event-driven](../../integration/event-driven/SKILL.md) — the async-seam patterns this leans on.
- [rollback-plan](../../migration/rollback-plan/SKILL.md) — per-step reversal.
- [release-readiness](../../devops/release-readiness/SKILL.md) — the gate each cut passes.
- [technical-debt](../technical-debt/SKILL.md) — refactoring pays down the debt register.

### Banking Context & Examples

#### (1) Core Banking API Strangler Example
**Scenario:** Moving customer account services from the `Mainframe-Core` to `Microservices-Pod`.
- **Architecture Lens Check:** Verification that the strangler-fig pattern maintains `Sharia-Compliance` of profit-calculations during the transition.
- **Sample Outcome:** "Refactoring Step 1 (Wedge): Route balance-inquiry to Microservice, but keep ledger-balancing on Mainframe. Dual-run verification confirms Sharia-rate equivalence before full cut-over."
- **Common Pitfall:** Skipping "dual-run" verification on profit-rate calculations; a discrepancy during the migration results in incorrect customer statements, a major `CBUAE` compliance violation and PR nightmare.

#### (2) Payment-Hub Transformation Example
**Scenario:** Replacing an aged payment hub.
- **Architecture Lens Check:** Ensuring `UAEFTS` connectivity is not interrupted during any strangler cut-over step.
- **Sample Outcome:** "Refactoring Step 3: Shift outbound-payment traffic to new Hub, while maintaining inbound-routing on legacy system. Step tied to post-salary-run release window."
- **Common Pitfall:** Scheduling the cut-over during the "salary-run" window; any failure here stalls all salary payments in the bank, violating service-level agreements and creating significant regulatory pressure.

#### (3) Sharia Product Migration Refactor Example
**Scenario:** Refactoring Sharia ledger integration from a monolith to a specialized `Sharia-Ledger-Service`.
- **Architecture Lens Check:** Maintaining mandatory `Sharia Governance` audit trails across the move.
- **Sample Outcome:** "Step: Dual-publish ledger entries to both monolithic-Sharia-ledger and new-Sharia-Service. Retirement of legacy ledger permitted only after 3 full months of audit-data alignment verified by Sharia Governance."
- **Common Pitfall:** Not setting a hard retirement date for the legacy ledger path; the bank ends up maintaining two conflicting ledgers indefinitely, destroying the auditability required by Sharia Board standards.
