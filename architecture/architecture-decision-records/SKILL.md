---
name: architecture-decision-records
owner: Solution Architecture
version: 0.1.0
last-reviewed: 2026-08-08
description: "Use when a banking decision needs a durable, reversible-with-cost record — produces a versioned ADR (context, options, decision, consequences) that survives team turnover and the architecture board."
required-inputs:
  - The decision question & its constraints
  - The options considered (incl. do-nothing) — /solution-options
  - The chosen option & rationale
  - The owning authority (board / lead) and acceptance date
expected-deliverables:
  - ADR file (context, decision drivers, considered options, decision, consequences, status)
  - Links to the review/gate that accepted it
  - Superseded-ADR pointer if this revises a prior decision
---

# /architecture-decision-records

## When to apply
Use whenever a decision is **hard to reverse**, **surprising without context**, and **the product of a real trade-off** — the three ADR criteria. In a bank that's most architecture-significant choices: platform selection, integration pattern, residency design, AI-orchestration model. Lives in a versioned ADR log; pairs with `/solution-options` (the options) and `/architecture-board` (the authority).

> The ADR is how a bank survives team turnover — six months later, "why did we choose X" must be answerable without re-deriving the trade-off.

## Inputs
- **Decision question & constraints** — precise, with the binding constraints named.
- **Options considered incl. "do nothing"** — from `/solution-options`; the ADR records that "do nothing" was considered, not silently skipped.
- **Chosen option & rationale** — *because* Y, citing the scoring.
- **Owning authority** — the board or lead that accepted it, and the date.

## Process
1. **Use the standard ADR template.** Header (title, status, date, deciders, tags). Body: Context → Decision Drivers → Considered Options → Decision → Consequences → (Links).

2. **Context — make the problem and the *why-now* precise.** What forces this decision now; what's the bind. The context section that re-litigates the problem in six months is the one that defends the decision when someone tries to revert it.

3. **Decision drivers — the criteria as binding forces, not weights.** Restate the top constraints ("CBUAE residency requires onshore for payment data", "RTO 30min", "team hasn't run Kafka at this scale") as *drivers* that the options were judged against — these are what the decision hangs on.

4. **Considered options — include the rejected, with their appeal.** "Do nothing" and the runner-up especially. A future reader needs to see *why the obvious alternative lost*, not just that it was considered.

5. **Decision — state it unambiguously.** The chosen option and the *because*. No upgrade hedging; ADRs that soft-pedal the decision ("we lean toward…") aren't decisions.

6. **Consequences — gains, penalties, and reversibility cost honestly.** What this enables; what it costs (run-cost, lock-in, skill debt, the regulatory exposure accepted); what it would take to reverse. The consequences block is where the ADR earns or loses its honesty.

7. **Versioning — Superseded / Amended.** When revising a decision, mark the prior ADR **Superseded by [n]** and the new one **Amends [n]**. Never silently edit a closed ADR; the history is the audit trail.

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
- **ADR file** — versioned, standard template, with links.
- **Acceptance-gate link** — board or design review.
- **Superseded pointer** — if revising a prior decision.

## Related skills
- [solution-options](../../discovery/solution-options/SKILL.md) — supplies the considered options.
- [architecture-board](../../governance/architecture-board/SKILL.md) — the authority that accepts.
- [architecture-review](../architecture-review/SKILL.md) — the review whose findings may cite this ADR.
- [design-review](../../governance/design-review/SKILL.md) — the component-depth gate.
- [risk-register](../../documentation/risk-register/SKILL.md) — where the accepted consequences become tracked risks.
- [raid-log](../../documentation/raid-log/SKILL.md) — for the smaller decisions that don't earn an ADR.

---

### ADR skeleton (copy)

```markdown
# ADR-NNNN: <title>

- **Status:** Proposed | Accepted | Deprecated | Superseded by ADR-MMMM
- **Date:** YYYY-MM-DD
- **Deciders:** <names / forum>
- **Tags:** <domain, e.g. residency, integration, platform>

## Context
<the problem & why-now — the bind that forces the decision>

## Decision drivers
- <driver 1 — e.g. CBUAE residency for payment data>
- <driver 2 — e.g. RTO 30 min>

## Considered options
- **Option A — <name>:** <one-line + appeal + why not>
- **Option B — <name>:** <one-line + appeal + why not>
- **Do nothing:** <cost of inaction>

## Decision
We choose Option — **because** <rationale citing the drivers>.

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
