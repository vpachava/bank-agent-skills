---
name: legacy-assessment
owner: Solution Architecture
version: 0.1.0
last-reviewed: 2026-08-09
description: "Use when deciding the fate of a legacy system in a bank — produces a legacy-assessment report (health, coupling, regulatory exposure, business value) with a reuse-wrap-replace-retire verdict and its rationale."
required-inputs:
  - The legacy system in scope & its business purpose
  - Its integrations & dependents (who calls it, who it calls)
  - Known pain points, incidents, and change-cost history
  - Regulatory constraints it carries (KYC/AML/residency/audit)
expected-deliverables:
  - Legacy-assessment report (health axis, coupling axis, risk axis, value axis)
  - Reuse / Wrap / Replace / Retire verdict with rationale
  - Modernization-potential score & what blocks it
---

# /legacy-assessment

## When to apply
Use before any modernization decision — to decide a legacy system's fate on evidence, not nostalgia. Feeds `/gap-analysis` (legacy capabilities as gaps), `/solution-options` (the verdict drives options), and `/refactoring-plan` / `/modernization-roadmap`. Especially load-bearing in a bank where the core is load-bearing, heavily coupled, and regulated — "replace it" is rarely the honest answer.

## Inputs
- **The legacy system & its business purpose** — what capability it delivers and to whom.
- **Integrations & dependents** — what calls it, what it calls, the data it owns, the events it emits. This is the coupling that decides feasibility.
- **Pain points, incidents, change-cost** — how often it breaks, how long changes take, the defect rate.
- **Regulatory constraints it carries** — KYC/AML verdict logic, residency of the data it holds, audit/posting obligations.

## Process
1. **Establish business value & criticality.** What it does that matters; how visible to customers; the revenue/operations depending on it; the criticality tier (regulated path? payment rail? back office?). Criticality gates the appetite for change.

2. **Assess health on multiple axes.** Operational health (incident rate, MTTR), code health (maintainability, test coverage, language/runtime currency), vendor/roadmap health (end-of-life status, supported?), skills health (does anyone still know it?), data health (integrity, residency, accessibility). Score each, not just "it works."

3. **Map the coupling — the real feasibility brake.** Inbound integrations (who depends on it), outbound (what it depends on), shared data ownership, shared identity, synchronous-call vs event-vs-batch. The coupling density decides whether wrap/strangler/replace is viable; a tightly-coupled synchronous core strangles any naive replacement.
   > In a bank the core is usually the densest coupling hub. Measure it before you propose anything.

4. **Surface the regulatory exposure it carries.** KYC verdict logic, AML screening, residency of PII/payment data, audit of postings, dual-control. Modernizing a system that *holds* regulatory logic is materially different from modernizing one that merely *calls* such a system.

5. **Score modernization potential.** Value vs. coupling vs. health vs. regulatory-exposure — a composite that says how worthwhile modernization is and what blocks it. A high-value, unhealthy, low-coupling, low-regulatory system scores high; the inverse scores low. Make the trade visible.

6. **Render the verdict — Reuse / Wrap / Replace / Retire — with rationale.** Reuse-as-is (healthy, low-value-churn); Reuse-with-enhance (healthy, needs a capability); Wrap (legacy intact behind a new API/adapter — the *strangler seam*); Replace (only with phased plan, never big-bang); Retire (no longer needed — fold its function elsewhere). Reference the assessment axes; cite what drove the call.

7. **Carry forward as a decision artifact.** The verdict is a candidate ADR (`/architecture-decision-records`); the assessment feeds the gap-analysis and the roadmap. Don't let it sit unread — the judgment outlasts the people who made it.

## Banking pitfalls
- **"Replace it" as a reflex** — a tightly-coupled core-banking system can't be big-bang-replaced without gutting the bank; reuse-and-wrap is almost always the honest answer; reflexive replace undercosts the migration by an order of magnitude.
- **Coupling unmeasured before the verdict** — "we'll replace the core" without a coupling map ships a roadmap the modernization plan can't honor; measure the inbound/outbound density first.
- **Regulatory logic underweighted** — treating a system that *holds* KYC/AML verdicts as interchangeable with one that just *calls* them; the regulatory exposure changes the verdict dramatically.
- **Health scored on "it works"** — operational continuity ≠ maintainability; a system that runs fine but nobody can change is a slow-burn problem the assessment must catch (skills/age/EOL).
- **Retire overlooked** — systems kept alive because nobody dare question them; a "retire / fold elsewhere" verdict is sometimes the highest-value finding and easiest to miss.
- **Verdict without rationale / owning ADR** — a Reuse/Wrap/Replace call with no rationale is reversed in six months because the reasoning left with the team.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of legacy-assessment meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the legacy-assessment process.**

## Outputs
- **Legacy-assessment report** — multi-axis health, coupling map, regulatory exposure, value & criticality, modernization-potential score.
- **Reuse/Wrap/Replace/Retire verdict** with rationale (candidate ADR).
- **What blocks modernization** — the specific coupling/regulatory/skills brakes feeding the roadmap.

## Related skills
- [gap-analysis](../../discovery/gap-analysis/SKILL.md) — legacy capabilities as gaps against the target.
- [solution-options](../../discovery/solution-options/SKILL.md) — the verdict motivates the options analysis.
- [refactoring-plan](../refactoring-plan/SKILL.md) — for Wrap/strangler-seam verdicts, the plan that enacts it.
- [modernization-roadmap](../modernization-roadmap/SKILL.md) — phases the verdict across waves.
- [impact-analysis](../impact-analysis/SKILL.md) — the change-blast view of the verdict's consequences.
- [architecture-decision-records](../../architecture/architecture-decision-records/SKILL.md) — durable record of the verdict.
- [technical-debt](../technical-debt/SKILL.md) — the code/skills debt surfaced by the assessment.
