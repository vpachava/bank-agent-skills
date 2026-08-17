---
name: poc-planning
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when scoping a proof-of-concept for a potential banking technology investment — produces a PoC plan (hypothesis, success criteria, timeline, deliverables)."
required-inputs:
  - PoC hypothesis & scope
  - Success criteria/indicators (success metrics)
  - Resources available (dev/cloud/budget)
  - Timeboxed delivery constraints
  - Regulatory-exposure class
expected-deliverables:
  - PoC delivery plan
  - Formal PoC scorecard/success-criteria table
  - Banking-specific risk register for the PoC
---

# /poc-planning

## When to apply
Use when a team wants to spend time testing a new technology or approach *before* committing to a full-scale investment. Protects bank budget and focus by timeboxing investments and ensuring they are designed to either definitively prove-out or reliably fail the investment hypothesis.

## Inputs
- **PoC Hypothesis & scope** — what are we testing, and what specifically *isn't* in scope?
- **Success criteria** — quantifiable measures of success.
- **Resource constraints** — who, what infra, how much budget.
- **Delivery constraints** — total timeboxed duration (e.g. 2–4 weeks max).

## Process
1. **Define the hypothesis.** State the specific bank problem the PoC solves. (e.g. "Can we integrate Oracle FLEXCUBE with Azure Event Hubs within [latency N] without custom query load?")
2. **Set success criteria.** *Quantifiable indicators.* e.g., "Max latency N ms", "Zero data loss under load", "API call response < 200ms", "Successfully passes compliance-gate check X". If it doesn't have a quantified metric, it's not a PoC — it's a research project (use `/platform-selection` or `/technology-evaluation` instead).
3. **Draft the delivery plan.** Timeboxed (max 4 weeks): Phase 1 setup/integrations, Phase 2 test-cases, Phase 3 scorecard report.
4. **Identify "PoC Regulatory Sandbox" constraints.** Is the PoC infrastructure separate from production? Does it connect to real core-banking data? Ensure it runs in a development/PoC landing-zone, not within the regulated production trust domain.
5. **Scorecard build.** Define the scorecard the PoC delivers: a yes/no on the success criteria and the documented findings.

## Banking pitfalls
- **Success criteria that are hand-wavy** — e.g. "The PoC is successful if it feels fast enough" (not quantifiable/defensible to stakeholders).
- **PoC expands into "pilot" / "limited-production" without re-evaluation** — PoC deliverables often get reused in production, inheriting its PoC-quality security/compliance; explicitly block PoC code from production without transformation.
- **Ignoring the platform-selection gate** — testing a technology that is non-compliant with the platform standards (`/platform-selection`) is a waste of time.
- **Data-privacy violations** — testing with production PII data in an insecure PoC environment — must use synthetic or anonymised/masked data for banking PoCs under PDPL.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of poc-planning meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the poc-planning process.**

## Outputs
- **PoC delivery plan** — timeline, tasks, success assessment.
- **Formal PoC scorecard/success-criteria table** — the quantifiable measure vs outcome.
- **Banking-specific risk register for the PoC** — data-handling risk, security compliance of the PoC environment.

## Related skills
- [technology-evaluation](../technology-evaluation/SKILL.md) — where the PoC results feed heavily.
- [roadmap](../roadmap/SKILL.md) — where the Post-PoC decision feeds.
- [reference-architecture](../reference-architecture/SKILL.md) — the candidate solution architecture tested by the PoC.

### Regulatory References
1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/
2. **PDPL:** Personal Data Protection Law (Federal Decree-Law No. 45 of 2021)
3. **CBUAE Cybersecurity Framework:** Domain 1: Governance & Risk Management

