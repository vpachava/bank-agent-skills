---
name: proposal
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when drafting a project proposal for a banking initiative — produces a proposal (value-prop, strategy, budget, timeline)."
required-inputs:
  - Initiative vision & scope
  - Value proposition (Why do it?)
  - High-level cost/benefit analysis
  - Resource/team requirements
expected-deliverables:
  - Project proposal document
  - Strategic alignment-map
  - Cost/Benefit/Risk summary
---

# /proposal

## When to apply
Use when you have a nascent idea or mandated initiative and need to formally pitch it to banking stakeholders. This is a "pre-charter" stage aimed at getting budget-approval for the discovery or build phase.

## Inputs
- **Vision** — What is the future state?
- **Business Value** — What is the quantifiable gain (e.g., reduction in settlement-time, new customer-acquisition)?
- **Costs** — Initial budget estimate.

## Process
1. **The "Elevator Pitch" (Value Prop).** Why this, why us, why now?
2. **Current vs. Future State.** Gap analysis (e.g., Manual reconciliation vs. Automated real-time netting).
3. **Strategic Alignment.** How does this feed into the bank's 3-year strategic-map?
4. **Residency/Regulatory Strategy.** Where will this live (Cloud/On-prem)? What regulations gate it?
5. **High-level Costs/Resources.** Order-of-magnitude budget (OOM) and core-team composition.

## Banking pitfalls
- **Ignoring residency-costs** — Proposing a "Cloud-only" model for a core-banking app without accounting for the massive costs of the mandatory-sovereign-cloud-setup.
- **Vague business-value** — Defining value as "better user experience" instead of "reduction in 20% call-centre overhead" or "30% faster loan-processing."
- **Regulatory blindness** — Proposing an initiative that is blocked by CBUAE/DIFC policy that isn't highlighted as a constraint.
- **Underestimating integration-depth** — Assuming the "new" app integrates easily with 20-year-old mainframe legacy codebases.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of proposal meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the proposal process.**

## Outputs
- **Project proposal document** — The pitch-deck or document for executive-approval.
- **Strategic alignment-map** — Visual/tabular representation of how it benefits the bank long-term.
- **Cost/Benefit/Risk summary** — The executive decision-matrix.

## Related skills
- [executive-summary](../executive-summary/SKILL.md)
- [project-charter](../project-charter/SKILL.md)
- [hld-generator](../../architecture/hld-generator/SKILL.md)
