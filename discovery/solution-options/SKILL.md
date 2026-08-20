---
name: solution-options
owner: Solution Architecture
version: 0.1.0
last-reviewed: 2026-08-08
description: "Use when a banking decision needs 2â€“4 candidate solutions surfaced and compared â€” produces an options matrix with weighted scoring, risks, and a recommendation (including 'do nothing')."
required-inputs:
  - The decision question & its constraints (regulatory, cost, time)
  - Current-state context (capability map, gap register, systems)
  - Decision criteria & their relative weights
  - The authority that will own the call
expected-deliverables:
  - 2â€“4 candidate solution options (buy / build / modernize / replatform / do-nothing)
  - Weighted scoring matrix (criteria Ã— options)
  - Risks & dependencies per option
  - Recommendation with rationale & a path to the decision
togaf-phases: [Phase A]
togaf-artifacts: [Architecture Vision]
bian-service-domains: [Customer Account.Origination]
---

# /solution-options

## When to apply
Use when a real fork needs a decision â€” build vs. buy, modernize vs. replace, platform A vs. platform B, one integration pattern vs. another â€” and the call shouldn't be made in one head. Especially load-bearing before an ADR (`/architecture-decision-records`) or a board submission (`/architecture-board`). Pairs with `/gap-analysis` (the gap begs the options) and feeds the ADR.

## Inputs
- **Decision question & constraints** â€” the precise question, plus the binding constraints: regulatory (CBUAE/residency/KYC), cost ceiling, timeline, organizational / skills, existing-system.
- **Current-state context** â€” what exists already (capability map, systems, the gap register) so options are designed *from* the present, not in a vacuum.
- **Decision criteria & weights** â€” what actually matters for this call (cost, time-to-value, risk, strategic fit, compliance, total-cost-of-ownership) and their relative weight; agree the rubric before scoring the options.
- **The owning authority** â€” who/what forum decides, so the options are framed for that decision path (ADR vs. architecture board vs. exec).

## Process
1. **State the decision question precisely and the constraints that bind it.** "How do we do X, given constraint Y, by date Z" â€” and name the forum that will own the call. An imprecise question produces options that miss the constraint.

2. **Agree the criteria & weights before generating options.** If criteria are negotiated after options exist, the rubric bends to whichever option someone already wanted. Cost, time-to-value, risk, strategic fit, compliance, run-cost (TCO not just build-cost); weight them.

3. **Generate 2â€“4 genuine options.** Always include **"do nothing / defer"** as an option â€” it surfaces whether the decision is forced or discretionary, and exposes the cost of inaction. Cover the realistic space: buy, build, modernize-in-place, replatform, wrap/integrate.
   > In bank contexts, **reuse-and-wrap over a legacy core** is usually a real option; **big-bang replace** rarely is. Don't let "greenfield rebuild" sneak in as the default without honest cost.

4. **Sketch each option at the same fidelity.** Asymmetry hides the trade-off; if one option is a paragraph and another is three pages, the short one loses on framing not merits. Cover: approach, what it touches (and reuses), what it adds, timeline ballpark, run-cost.

5. **Score each option against the weighted criteria.** Show the matrix; let the recommendation emerge from the scoring, not the other way round. Where scores are close, that itself is a finding (the decision is sensitive to the weighting â€” surface it).

6. **Capture risk & dependency per option.** Each option carries risks (execution, regulatory, vendor lock-in, team-skill) and dependencies (on a team, vendor, regulatory shift, or another initiative). These are decision inputs, not afterthoughts.

7. **Recommend, with rationale and a path to the decision.** State the recommendation, *why* (citing the scoring + constraints), the key risk accepted, and the next step (ADR draft, board submission, or a prototype to de-risk a close call).

8. **Note what would change the recommendation.** A good options analysis names its sensitivities â€” "if criterion X reweights higher, option A wins; if vendor Y's cost held, it'd be a 2 not a 3." Next time the call is revisited, those are your re-decision triggers.

## Bulletproofing against Rationalization
To prevent skewed analysis masking pre-ordained choices, you MUST:

1. **Mandatory Deferral Baseline:** Every options matrix MUST actively include 'Do Nothing / Defer' to act as the baseline cost of operational continuity.
2. **Comprehensive TCO Mandate:** Cost metrics CANNOT be isolated to "Build Expense". They MUST document Total Cost of Ownership (TCO) extending to ongoing licensing, specialized skill acquisition, and maintenance support.
3. **Criterion Lockdown:** Evaluation weights and constraint criteria MUST be documented and frozen BEFORE option formulation begins to prevent subjective manipulation toward a preferred path.
4. **Mandatory Rationale Tracing:** The recommendation MUST trace directly to constrained logic. 

**Violating these rules invalidates the Solution Options recommendation.**

## Banking pitfalls
- **No "do nothing" option** â€” forcing a binary choice among build/buy when defer-with-tactic is the real answer; the cost of action is invisible without a do-nothing baseline.
- **Greenfield rebuild smuggled in as the default** â€” in a bank with a legacy core, reuse-and-wrap is almost always a viable option; big-bang replace is rarely viable on cost/risk alone. Make the field honest.
- **Build-cost scored, run-cost ignored** â€” build-vs-buy often inverts once TCO (licensing, ops, skills, depreciated rewrites) is added; total-cost, not build-cost.
- **Criteria reweighted after the favorite is known** â€” the rubric bends to confirm a pre-chosen option; lock criteria and weights before scoring.
- **Regulatory/compliance treated as a tie-breaker, not a knockout** â€” in a UAE bank, an option that can't meet residency/KYC/AML is out, not a low-scoring choice; treat compliance as a gate.
- **Single-option recommendations disguised as options** â€” "here's the plan and two implausible alternatives" isn't options analysis; if two options can't really be chosen, say so and recommend the one viable path with rationale.
- **No decision path** â€” options presented with no named forum and no next step die in committee; end with "ADR draft â†’ Architecture Board on [date]."

## Outputs
- **Options matrix** â€” 2â€“4 options Ã— weighted criteria, with scores and rationale per cell.
- **Risks & dependencies** â€” per option, with severity.
- **Recommendation** â€” option chosen, rationale (citing scoring + constraints), key accepted risk, and the decision path (ADR / board / prototype).
- **Sensitivities** â€” what would change the recommendation (criteria reweighting, new facts).

## Related skills
- [gap-analysis](../gap-analysis/SKILL.md) â€” the gaps that often motivate an options analysis.
- [architecture-decision-records](../../architecture/architecture-decision-records/SKILL.md) â€” the durable record of the chosen option.
- [architecture-board](../../governance/architecture-board/SKILL.md) â€” the forum that often owns the call.
- [technology-evaluation](../../greenfield/technology-evaluation/SKILL.md) â€” for an option that needs a deeper single-tech eval.
- [risk-register](../../documentation/risk-register/SKILL.md) â€” the per-option risks land here as the initiative proceeds.

## Bulletproofing
- **Governance Policy:** Enforce [CBUAE Rulebook](governance/policy/regulations.yaml#CBUAE), [PDPL](governance/policy/regulations.yaml#PDPL), and [PCI-DSS](governance/policy/regulations.yaml#PCI-DSS) where applicable.

## Anti-patterns
- **Recommending a single solution without presenting alternative options**
  - **Consequence:** Confirmatory bias, lack of objective evaluation, and poor engineering decisions.
  - **Correct Approach:** Present at least 2 distinct alternative options alongside the "Do Nothing" baseline.
- **Structuring evaluation criteria around vendor biases rather than requirements**
  - **Consequence:** Vendor lock-in and high platform cost for features that are never used.
  - **Correct Approach:** Base criteria scoring on objective NFRs, business goals, and cost metrics.
- **Underestimating overall cost of ownership (TCO) and skill requirements**
  - **Consequence:** Projects run out of budget midway or rely on costly external consulting resource indefinitely.
  - **Correct Approach:** Include licensing, compute, operations, training, and maintenance costs in the TCO evaluation.
