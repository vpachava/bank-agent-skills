---
name: executive-summary
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when drafting an executive summary for a banking initiative — produces an exec summary (business-case, outcomes, risk-headlines)."
required-inputs:
  - Initiative goals & scope
  - Key business/customer outcomes
  - High-level cost & timeline
  - Critical risks & regulatory gating
expected-deliverables:
  - Executive summary document (brief)
  - Key-outcome bullet-list
  - Headline risk-register summary
---

# /executive-summary

## When to apply
Use to distill a massive technical initiative into a dense, rapid-read, risk-focused summary for senior Banking executives (CIO, CRO, CISO). Banking executives prioritize: (1) Does this impact our regulatory standing? (2) How much money/effort? (3) Does it move our strategic capability goal?

## Inputs
- **Business case** — Why now?
- **Outcomes** — What changes for the customer/bank?
- **Risks** — Top 3 items keeping leadership awake (residency/compliance focus).

## Process
1. **The "Bottom Line Up Front" (BLUF).** State the recommendation and the primary risk immediately.
2. **Business Impact.** Business capability / BIAN domain impact.
3. **Regulatory Context.** Explicitly state the residency/compliance gating (e.g. CBUAE/PDPL/Freezone transfer status).
4. **Headline Risks.** Keep it to 3–4 items; link directly to the risk-register.
5. **Call to Action.** Clear request to the senior stakeholders (e.g. approval, budget-signoff, committee-notification).

## Banking pitfalls
- **Over-technicality** — Discussing "Kubernetes-infra-details" instead of business-outcomes; focus on capability (e.g. "Payments-Engine-modernization" vs "AKS-node-pool-scaling").
- **Regulatory-gating invisibility** — Hiding a hard regulatory-enforcement-deadline inside a "technical roadmap" rather than as a primary-Business-Risk.
- **Ignoring "The-Legacy-Integration"** — Fearing to mention that modern work depends on "Oracle-Core" fragility; executives need to know the integration-risk.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of executive-summary meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the executive-summary process.**

## Outputs
- **Executive summary document** — One-page dense BLUF text.
- **Key-outcome list** — Quantifiable business deliverables.
- **Headline risk-register summary** — Top-3 banking/regulatory risks.

## Related skills
- [proposal](../proposal/SKILL.md)
- [project-charter](../project-charter/SKILL.md)
- [risk-register](../risk-register/SKILL.md)
