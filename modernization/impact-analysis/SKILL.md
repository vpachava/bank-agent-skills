---
name: impact-analysis
owner: Solution Architecture
version: 0.1.0
last-reviewed: 2026-08-09
description: "Use when a planned change may ripple across the bank's interdependent estate â€” produces an impact-analysis report (blast radius, affected integrations/data/regulatory paths, severity) so the change is sized before it ships."
required-inputs:
  - The planned change & its scope
  - Estate inventory & integration map (inbound/outbound per system)
  - Data-flow & ownership map
  - Regulatory-bearing paths touched
expected-deliverables:
  - Impact-analysis report (direct & ripple impact, per-system severity)
  - Affected-integrations & affected-data list
  - Regulatory-path exposure call
  - Reverse-impact (who breaks downstream)
togaf-phases: [Phase F]
togaf-artifacts: [Migration Plan]
bian-service-domains: [Integration.Migration]
---

# /impact-analysis

## When to apply
Use *before* a release, migration wave, refactor cut, or deprecation â€” to size the blast radius of a change across the interdependent estate. In a bank where the core sits under dozens of callers and owns the canonical data, every change has a shadow; this skill finds it. Feeds `/refactoring-plan`, `/migration-wave-planning`, and `/cutover-plan`, and gates `/design-review`.

## Inputs
- **The planned change** â€” scope, in-scope systems, what's added/changed/removed/withdrawn.
- **Estate inventory & integration map** â€” inbound/outbound calls per system, sync vs async, the partner/rail integrations.
- **Data-flow & ownership map** â€” which system owns which data; where changes propagate via data, not just via calls.
- **Regulatory-bearing paths touched** â€” KYC verdict, payments, AML, residency-affected stores, audit postings.

## Process
1. **Bound the change precisely â€” direct impact first.** Which systems/components are directly modified. This is the trivial layer; the danger is everywhere *downstream* of it.

2. **Trace ripple impact â€” who calls the changed thing, who consumes its data/events.** Walk the inbound/integration graph: every system that calls the changed interface/consumes the changed data/events. Each ripple may break (consume behavior changes), tolerate (interface stable but semantics shift), or be null.
   > A bank's danger is the *event* ripple â€” an event schema change consumers never asked for breaks them silently, exactly-once consumers may double-process on replay. Trace data & events, not just calls.

3. **Score impact per affected system â€” Major/Minor/None.** Major = breaks the consumer or a regulatory path. Minor = tolerated surface change. None = no real effect. Per-system, with the specific failure mode if Major (breaks build; runtime behavior; data-integrity; regulatory).

4. **Surface regulatory-path exposure explicitly.** Does the change touch KYC verdict, AML screening, payment amount handling, residency of PII/payment data, audit postings, dual-control ceremonies? A change on a regulated path is severity-amplified â€” "minor" interface churn on the AML screening path is *not* minor.

5. **Identify reverse-impact â€” what breaks downstream of the changed systems' own consumers.** The blast radius isn't one hop; a payment-service change can ripple to reconciliation, to the customer statement, to the dispute path. Walk two hops minimum.

6. **Capture the compensating actions.** Per Major impact: co-deploy, version-staged, consumer-side change ticket, dual-run, or explicit "break & migrate." The impact analysis is only useful if it tells you what to *do* about each hit.

7. **Tie to the change-advisory & release gates.** The impact analysis is the input to the change board, the `/cutover-plan`, the `/migration-wave-planning`; Major impacts shape the wave and the rollback.

## Banking pitfalls
- **Direct-impact-only** â€” "we changed interface X, Y calls it, we'll tell Y" traces one hop and misses the data/event ripple two hops down; an event-schema change is the canonical silent break.
- **Async ripple ignored** â€” changes to event payloads/consumers treated as harmless; exactly-once consumers replay/double-process, ordered consumers' ordering breaks, idempotency assumptions shatter. The async path is where most bank-change incidents live.
- **Regulatory-path severity not amplified** â€” interface churn scored "Minor" because it's small, but on the AML/payment/KYC path it's Major by content; severity is consequence-weighted not size-weighted.
- **Impact without compensating action** â€” an impact analysis that lists "X breaks" without "co-deploy / version-stage / dual-run" is a finding that won't get closed; require the action.
- **No reverse-impact** â€” stopping at the direct consumer and missing the statement/dispute/reconciliation path two hops down; trace two hops minimum.
- **Change without the consumer contracts** â€” analyzing impact without the actual consumer contracts in hand means guessing; pull the contracts or the integration map before scoring.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of impact-analysis meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the impact-analysis process.**

## Outputs
- **Impact-analysis report** â€” direct + ripple impact per system with severity and specific failure mode.
- **Affected-integrations & affected-data list** â€” and the async/event consumers that ripple.
- **Regulatory-path exposure call** â€” explicit yes/no per regulated path, with severity-amplification where yes.
- **Compensating actions** â€” per Major impact, the co-deploy / version-stage / dual-run / break-and-migrate call, feeding the wave & cutover plan.

## Related skills
- [migration-wave-planning](../../migration/migration-wave-planning/SKILL.md) â€” uses the impact analysis to group/separate waves.
- [cutover-plan](../../migration/cutover-plan/SKILL.md) â€” uses the impact analysis for the go/no-go risk & compensating actions.
- [rollback-plan](../../migration/rollback-plan/SKILL.md) â€” uses the impact analysis for the reversal triggers.
- [refactoring-plan](../refactoring-plan/SKILL.md) â€” uses the impact analysis to size the safe steps.
- [design-review](../../governance/design-review/SKILL.md) â€” the gate that consumes the impact analysis.
- [event-driven](../../integration/event-driven/SKILL.md) â€” for async ripples.
- [legacy-assessment](../legacy-assessment/SKILL.md) â€” the verdict whose impact this sizes.

### Banking Context & Examples

#### (1) Core Banking Schema Change Example
**Scenario:** Adding a mandatory field `New-PII-Consent-Flag` to the `Customer-Profile` table in the legacy core.
- **Architecture Lens Check:** Verification of impact on `PDPL` compliance reporting and `downstream` synchronization ETLs.
- **Sample Outcome:** "Impact Analysis: Major. Schema change ripples to `KYC-Reporting-Engine` (broken transformation) and `Mobile-App` (Profile API validation breakage). Action: Co-deploy with ETL version-upgrade."
- **Common Pitfall:** Assessing only the immediate service dependency; missing the downstream ETL job that breaks silently because it expects a fixed schema, leading to broken regulatory reports.

#### (2) Sharia Lending API Refactor Example
**Scenario:** Changing the calculation logic for `Sharia-Compliant` profit rates in a loan-service.
- **Architecture Lens Check:** Evaluating impact on the ledger-posting service which records Sharia transactions.
- **Sample Outcome:** "Impact Analysis: Major. Change impacts ledger-posting service; must be audited to ensure calculations adhere to `Sharia-Governance-Book`."
- **Common Pitfall:** Scoring the change as "Minor" due to few code changes; missing the fact that any change here invalidates previous regulatory audits, requiring re-certification by the Sharia Board.

#### (3) AECB Reporting Pipeline Impact Example
**Scenario:** Withdrawing an event from the legacy data-pipeline that once fed AECB reporting.
- **Architecture Lens Check:** Compliance impact on bank's ability to submit accurate data to the bureau.
- **Sample Outcome:** "Impact Analysis: Critical. Withdrawal invalidates AECB submission. Action: Cannot proceed until AECB-submission logic is migrated to a new stable event-sink."
- **Common Pitfall:** Assuming the event is "unused" by the legacy system, missing its crucial business role in generating regulatory data, inevitably leading to a regulatory breach.

## Bulletproofing
- **Governance Policy:** Enforce [CBUAE Rulebook](governance/policy/regulations.yaml#CBUAE), [PDPL](governance/policy/regulations.yaml#PDPL), and [PCI-DSS](governance/policy/regulations.yaml#PCI-DSS) where applicable.

## Anti-patterns
- **Analyzing downstream dependencies while ignoring upstream consuming systems**
  - **Consequence:** Modernizing an API breaks critical legacy consumers that rely on the old protocol or payload structure.
  - **Correct Approach:** Create a comprehensive 360-degree dependency tree, incorporating both the systems it calls and the systems calling it.
- **Failing to quantify the operational impact on IT support structure workflows**
  - **Consequence:** Support teams are overwhelmed because they lack tools (or access) to monitor the new modernized architecture.
  - **Correct Approach:** Explicitly include the impact on SOC, Level 1/2 Support observability, and runbook updates in the initial analysis.
- **Using static documentation to perform the dependency impact assessment**
  - **Consequence:** Static architecture diagrams are often hopelessly out of date, omitting shadow IT or point-to-point workarounds.
  - **Correct Approach:** Leverage dynamic APM telemetry (network traffic analysis) to identify actual dependencies executing in production.
