---
name: legacy-assessment
owner: Solution Architecture
version: 0.1.0
last-reviewed: 2026-08-09
description: "Use when deciding the fate of a legacy system in a bank â€” produces a legacy-assessment report (health, coupling, regulatory exposure, business value) with a reuse-wrap-replace-retire verdict and its rationale."
required-inputs:
  - The legacy system in scope & its business purpose
  - Its integrations & dependents (who calls it, who it calls)
  - Known pain points, incidents, and change-cost history
  - Regulatory constraints it carries (KYC/AML/residency/audit)
expected-deliverables:
  - Legacy-assessment report (health axis, coupling axis, risk axis, value axis)
  - Reuse / Wrap / Replace / Retire verdict with rationale
  - Modernization-potential score & what blocks it
togaf-phases: [Phase F]
togaf-artifacts: [Migration Plan]
bian-service-domains: [Integration.Migration]
---

# /legacy-assessment

## When to apply
Use before any modernization decision â€” to decide a legacy system's fate on evidence, not nostalgia. Feeds `/gap-analysis` (legacy capabilities as gaps), `/solution-options` (the verdict drives options), and `/refactoring-plan` / `/modernization-roadmap`. Especially load-bearing in a bank where the core is load-bearing, heavily coupled, and regulated â€” "replace it" is rarely the honest answer.

## Inputs
- **The legacy system & its business purpose** â€” what capability it delivers and to whom.
- **Integrations & dependents** â€” what calls it, what it calls, the data it owns, the events it emits. This is the coupling that decides feasibility.
- **Pain points, incidents, change-cost** â€” how often it breaks, how long changes take, the defect rate.
- **Regulatory constraints it carries** â€” KYC/AML verdict logic, residency of the data it holds, audit/posting obligations.

## Process
1. **Establish business value & criticality.** What it does that matters; how visible to customers; the revenue/operations depending on it; the criticality tier (regulated path? payment rail? back office?). Criticality gates the appetite for change.

2. **Assess health on multiple axes.** Operational health (incident rate, MTTR), code health (maintainability, test coverage, language/runtime currency), vendor/roadmap health (end-of-life status, supported?), skills health (does anyone still know it?), data health (integrity, residency, accessibility). Score each, not just "it works."

3. **Map the coupling â€” the real feasibility brake.** Inbound integrations (who depends on it), outbound (what it depends on), shared data ownership, shared identity, synchronous-call vs event-vs-batch. The coupling density decides whether wrap/strangler/replace is viable; a tightly-coupled synchronous core strangles any naive replacement.
   > In a bank the core is usually the densest coupling hub. Measure it before you propose anything.

4. **Surface the regulatory exposure it carries.** KYC verdict logic, AML screening, residency of PII/payment data, audit of postings, dual-control. Modernizing a system that *holds* regulatory logic is materially different from modernizing one that merely *calls* such a system.

5. **Score modernization potential.** Value vs. coupling vs. health vs. regulatory-exposure â€” a composite that says how worthwhile modernization is and what blocks it. A high-value, unhealthy, low-coupling, low-regulatory system scores high; the inverse scores low. Make the trade visible.

6. **Render the verdict â€” Reuse / Wrap / Replace / Retire â€” with rationale.** Reuse-as-is (healthy, low-value-churn); Reuse-with-enhance (healthy, needs a capability); Wrap (legacy intact behind a new API/adapter â€” the *strangler seam*); Replace (only with phased plan, never big-bang); Retire (no longer needed â€” fold its function elsewhere). Reference the assessment axes; cite what drove the call.

7. **Carry forward as a decision artifact.** The verdict is a candidate ADR (`/architecture-decision-records`); the assessment feeds the gap-analysis and the roadmap. Don't let it sit unread â€” the judgment outlasts the people who made it.

## Banking pitfalls
- **"Replace it" as a reflex** â€” a tightly-coupled core-banking system can't be big-bang-replaced without gutting the bank; reuse-and-wrap is almost always the honest answer; reflexive replace undercosts the migration by an order of magnitude.
- **Coupling unmeasured before the verdict** â€” "we'll replace the core" without a coupling map ships a roadmap the modernization plan can't honor; measure the inbound/outbound density first.
- **Regulatory logic underweighted** â€” treating a system that *holds* KYC/AML verdicts as interchangeable with one that just *calls* them; the regulatory exposure changes the verdict dramatically.
- **Health scored on "it works"** â€” operational continuity â‰  maintainability; a system that runs fine but nobody can change is a slow-burn problem the assessment must catch (skills/age/EOL).
- **Retire overlooked** â€” systems kept alive because nobody dare question them; a "retire / fold elsewhere" verdict is sometimes the highest-value finding and easiest to miss.
- **Verdict without rationale / owning ADR** â€” a Reuse/Wrap/Replace call with no rationale is reversed in six months because the reasoning left with the team.

## Bulletproofing
- **Governance Policy:** Enforce [CBUAE Rulebook](governance/policy/regulations.yaml#CBUAE), [PDPL](governance/policy/regulations.yaml#PDPL), and [PCI-DSS](governance/policy/regulations.yaml#PCI-DSS) where applicable.

## Outputs
- **Legacy-assessment report** â€” multi-axis health, coupling map, regulatory exposure, value & criticality, modernization-potential score.
- **Reuse/Wrap/Replace/Retire verdict** with rationale (candidate ADR).
- **What blocks modernization** â€” the specific coupling/regulatory/skills brakes feeding the roadmap.

## Related skills
- [gap-analysis](../../discovery/gap-analysis/SKILL.md) â€” legacy capabilities as gaps against the target.
- [solution-options](../../discovery/solution-options/SKILL.md) â€” the verdict motivates the options analysis.
- [refactoring-plan](../refactoring-plan/SKILL.md) â€” for Wrap/strangler-seam verdicts, the plan that enacts it.
- [modernization-roadmap](../modernization-roadmap/SKILL.md) â€” phases the verdict across waves.
- [impact-analysis](../impact-analysis/SKILL.md) â€” the change-blast view of the verdict's consequences.
- [architecture-decision-records](../../architecture/architecture-decision-records/SKILL.md) â€” durable record of the verdict.
- [technical-debt](../technical-debt/SKILL.md) â€” the code/skills debt surfaced by the assessment.

### Banking Context & Examples

#### (1) Core Banking Replacement Example
**Scenario:** Assessing the 20-year-old `CORE-X` system for replacement.
- **Architecture Lens Check:** Verification of `AECB` reporting compliance dependencies and data-residency obligations of the storage data.
- **Sample Outcome:** "Verdict: Wrap. Rationale: System holds critical `KYC-Verdict` logic, making a direct Replace high-risk. Propose ACL-facade wrapper to safely strangler-fig."
- **Common Pitfall:** Proposing a direct "Replace" without accounting for the fact that `CORE-X` serves as the primary data-store for PII/regulated data, failing the `CBUAE` residency compliance audit.

#### (2) Payment Hub Replacement Example
**Scenario:** Assessing the enterprise `Payment-Hub` modernization.
- **Architecture Lens Check:** Modeling coupling density for `UAEFTS` connectivity and `Sharia-Compliant` ledger posting.
- **Sample Outcome:** "Verdict: Replace. Rationale: Moderate coupling; critical modernization needed to meet new `UAEFTS` ISO20022 mandates."
- **Common Pitfall:** Assessing health based on "uptime" rather than "maintainability." The system stays up, but code-agility to implement ISO20022 is zero, making an "Replace" verdict essential for regulatory compliance.

#### (3) Sharia Loan Ledger Assessment Example
**Scenario:** Assessing a legacy ledger system containing both Conventional and Sharia loan records.
- **Architecture Lens Check:** Evaluating the impact of "Retail-Banking" Ledger segregation required by `Sharia-Governance` board.
- **Sample Outcome:** "Verdict: Wrap + Refactor. Rationale: System cannot easily segregate Conventional and Sharia funds at the DB level, requiring a wrapper to enforce Sharia-compliant isolation and audit trail."
- **Common Pitfall:** Ignoring the `Sharia Board` requirements for segregation; assessing the system as "Replace" without recognizing the need for logical separation from Conventional products leads to non-compliant Sharia auditing.

### Regulatory References
1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/
2. **PDPL:** Personal Data Protection Law (Federal Decree-Law No. 45 of 2021)
3. **CBUAE Cybersecurity Framework:** Domain 1: Governance & Risk Management

## Anti-patterns
- **Assuming "legacy" automatically means "needs to be rewritten"**
  - **Consequence:** Wasting millions of dollars rebuilding a stable, unchanging core system instead of just wrapping it in an API.
  - **Correct Approach:** Use the TIME framework (Tolerate, Invest, Migrate, Eliminate) to objectively score modernization strategies based on business value versus technical limits.
- **Focusing on code age rather than maintainability and vendor support risk**
  - **Consequence:** Targeting the wrong systems while ignoring modern systems with toxic technical debt and severe security vulnerabilities.
  - **Correct Approach:** Score legacy systems by measuring engineering velocity, deployment frequency, and critical vendor EOL status.
- **Conducting the assessment purely through IT metrics without business alignment**
  - **Consequence:** Producing a modernization roadmap that the business refuses to fund because it solves zero customer pain points.
  - **Correct Approach:** Align legacy pain points directly to business outcomes (e.g., "Cannot launch new deposit product due to mainframe lock").
