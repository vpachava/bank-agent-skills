---
name: architecture-decision-records
owner: Solution Architecture
version: 0.1.0
last-reviewed: 2026-08-08
description: "Use when a banking decision needs a durable, reversible-with-cost record â€” produces a versioned ADR (context, options, decision, consequences) that survives team turnover and the architecture board."
required-inputs:
  - The decision question & its constraints
  - The options considered (incl. do-nothing) â€” /solution-options
  - The chosen option & rationale
  - The owning authority (board / lead) and acceptance date
expected-deliverables:
  - ADR file (context, decision drivers, considered options, decision, consequences, status)
  - Links to the review/gate that accepted it
  - Superseded-ADR pointer if this revises a prior decision
togaf-phases: [Phase C]
togaf-artifacts: [HLD]
bian-service-domains: [Integration.API]
---

# /architecture-decision-records

## When to apply
Use whenever a decision is **hard to reverse**, **surprising without context**, and **the product of a real trade-off** â€” the three ADR criteria. In a bank that's most architecture-significant choices: platform selection, integration pattern, residency design, AI-orchestration model. Lives in a versioned ADR log; pairs with `/solution-options` (the options) and `/architecture-board` (the authority).

> The ADR is how a bank survives team turnover â€” six months later, "why did we choose X" must be answerable without re-deriving the trade-off.

## Inputs
- **Decision question & constraints** â€” precise, with the binding constraints named.
- **Options considered incl. "do nothing"** â€” from `/solution-options`; the ADR records that "do nothing" was considered, not silently skipped.
- **Chosen option & rationale** â€” *because* Y, citing the scoring.
- **Owning authority** â€” the board or lead that accepted it, and the date.

## Process
1. **Use the standard ADR template.** Header (title, status, date, deciders, tags). Body: Context â†’ Decision Drivers â†’ Considered Options â†’ Decision â†’ Consequences â†’ (Links).

2. **Context â€” make the problem and the *why-now* precise.** What forces this decision now; what's the bind. The context section that re-litigates the problem in six months is the one that defends the decision when someone tries to revert it.

3. **Decision drivers â€” the criteria as binding forces, not weights.** Restate the top constraints ("CBUAE residency requires onshore for payment data", "RTO 30min", "team hasn't run Kafka at this scale") as *drivers* that the options were judged against â€” these are what the decision hangs on.

4. **Considered options â€” include the rejected, with their appeal.** "Do nothing" and the runner-up especially. A future reader needs to see *why the obvious alternative lost*, not just that it was considered.

5. **Decision â€” state it unambiguously.** The chosen option and the *because*. No upgrade hedging; ADRs that soft-pedal the decision ("we lean towardâ€¦") aren't decisions.

6. **Consequences â€” gains, penalties, and reversibility cost honestly.** What this enables; what it costs (run-cost, lock-in, skill debt, the regulatory exposure accepted); what it would take to reverse. The consequences block is where the ADR earns or loses its honesty.

7. **Versioning â€” Superseded / Amended.** When revising a decision, mark the prior ADR **Superseded by [n]** and the new one **Amends [n]**. Never silently edit a closed ADR; the history is the audit trail.

8. **Link the acceptance gate.** The board review or design review that accepted it; the ADR with no acceptance gate is a draft.

## Bulletproofing against Rationalization
To prevent "one-option justifications" and soft-pedaling decisions, you MUST:

1. **Mandatory Considered Options:** Include at least two alternatives and "Do Nothing".
2. **Explicit Decision Drivers:** Restate top constraints (e.g., CBUAE residency) as binding forces.
3. **Unambiguous Decision:** State the chosen option, then use the word "**because**" to link to drivers.
4. **Transparent Penalties:** Consequences MUST explicitly mention run-cost, lock-in, skill debt, or accepted regulatory exposure.

**Violating these rules invalidates the ADR.**
---
### ADR skeleton (copy)
...

## Outputs
- **ADR file** â€” versioned, standard template, with links.
- **Acceptance-gate link** â€” board or design review.
- **Superseded pointer** â€” if revising a prior decision.

## Related skills
- [solution-options](../../discovery/solution-options/SKILL.md) â€” supplies the considered options.
- [architecture-board](../../governance/architecture-board/SKILL.md) â€” the authority that accepts.
- [architecture-review](../architecture-review/SKILL.md) â€” the review whose findings may cite this ADR.
- [design-review](../../governance/design-review/SKILL.md) â€” the component-depth gate.
- [risk-register](../../documentation/risk-register/SKILL.md) â€” where the accepted consequences become tracked risks.
- [raid-log](../../documentation/raid-log/SKILL.md) â€” for the smaller decisions that don't earn an ADR.

---

### ADR skeleton (copy)

```markdown
# ADR-NNNN: <title>

- **Status:** Proposed | Accepted | Deprecated | Superseded by ADR-MMMM
- **Date:** YYYY-MM-DD
- **Deciders:** <names / forum>
- **Tags:** <domain, e.g. residency, integration, platform>

## Context
<the problem & why-now â€” the bind that forces the decision>

## Decision drivers
- <driver 1 â€” e.g. CBUAE residency for payment data>
- <driver 2 â€” e.g. RTO 30 min>

## Considered options
- **Option A â€” <name>:** <one-line + appeal + why not>
- **Option B â€” <name>:** <one-line + appeal + why not>
- **Do nothing:** <cost of inaction>

## Decision
We choose Option â€” **because** <rationale citing the drivers>.

## Consequences
- **Gains:** <what this enables>
- **Penalties / costs:** <run-cost, lock-in, skill debt>
- **Legacy Coupling Impact:** <Sync-load, Data-contention, Throughput-guarantee>
- **Accepted regulatory exposure:** <any, with rationale>
- **Reversibility cost:** <what a reversal would take>

## Links
- Acceptance gate: <board/review link or date>
- Supersedes / Amends: <ADR-nnnn if any>
```

### Banking Context & Examples

#### (1) Credit Card Onboarding Example
**Scenario:** ADR for choosing a cloud provider for credit card origination.
- **Architecture Lens Check:** Decision drivers MUST list `CBUAE` data-residency as a critical driver, not just a technical preference.
- **Sample Outcome:** "Decision drivers: AECB mandated data-locality, CBUAE data-transit compliance, latency < 100ms."
- **Common Pitfall:** Selecting a provider purely on "vendor-feature-set" while missing the primary driver ("data-residency"), leading to an ADR that cannot defend the choice when regulators challenge the cloud-setup.

#### (2) Customer Profile Management Example
**Scenario:** ADR for profile-synchronization pattern (synchronous vs asynchronous).
- **Architecture Lens Check:** Consequences block MUST discuss the risk of `PDPL` audit gaps with delayed-synchronization.
- **Sample Outcome:** "Consequences: Asynchronous sync reduces core-load but increases residency-audit complexity due to event-log storage."
- **Common Pitfall:** Recommending asynchronous synchronization without analyzing the regulatory consequence (e.g., how to prove data privacy at the moment of update), which makes the architectural choice defenseless in a DPB/PDPL audit.

#### (3) Lending/Loans Onboarding Example
**Scenario:** ADR for Sharia-compliant ledger implementation.
- **Architecture Lens Check:** Evaluates 'Build-Sharia-Module-on-Core' vs 'External-Sharia-Engine'.
- **Sample Outcome:** "Decision: Choose 'External-Sharia-Engine' because it isolates product-certification from core-binary updates, easing audit."
- **Common Pitfall:** Choosing an integrated solution because it is 'fast-to-build', ignoring the high cost of re-certifying the *entire* core binary every time Sharia-product rules change, which is a major long-term maintenance penalty."

### Regulatory References
1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/
2. **PDPL:** Personal Data Protection Law (Federal Decree-Law No. 45 of 2021)
3. **CBUAE Cybersecurity Framework:** Domain 1: Governance & Risk Management


