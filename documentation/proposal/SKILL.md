---
name: proposal
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when drafting a project proposal for a banking initiative â€” produces a proposal (value-prop, strategy, budget, timeline)."
required-inputs:
  - Initiative vision & scope
  - Value proposition (Why do it?)
  - High-level cost/benefit analysis
  - Resource/team requirements
expected-deliverables:
  - Project proposal document
  - Strategic alignment-map
  - Cost/Benefit/Risk summary
togaf-phases: [Phase A]
togaf-artifacts: [Architecture Vision]
bian-service-domains: [Customer Account.Origination]
---

# /proposal

## When to apply
Use when you have a nascent idea or mandated initiative and need to formally pitch it to banking stakeholders. This is a "pre-charter" stage aimed at getting budget-approval for the discovery or build phase.

## Inputs
- **Vision** â€” What is the future state?
- **Business Value** â€” What is the quantifiable gain (e.g., reduction in settlement-time, new customer-acquisition)?
- **Costs** â€” Initial budget estimate.

## Process
1. **The "Elevator Pitch" (Value Prop).** Why this, why us, why now?
2. **Current vs. Future State.** Gap analysis (e.g., Manual reconciliation vs. Automated real-time netting).
3. **Strategic Alignment.** How does this feed into the bank's 3-year strategic-map?
4. **Residency/Regulatory Strategy.** Where will this live (Cloud/On-prem)? What regulations gate it?
5. **High-level Costs/Resources.** Order-of-magnitude budget (OOM) and core-team composition.

## Banking pitfalls
- **Ignoring residency-costs** â€” Proposing a "Cloud-only" model for a core-banking app without accounting for the massive costs of the mandatory-sovereign-cloud-setup.
- **Vague business-value** â€” Defining value as "better user experience" instead of "reduction in 20% call-centre overhead" or "30% faster loan-processing."
- **Regulatory blindness** â€” Proposing an initiative that is blocked by CBUAE/DIFC policy that isn't highlighted as a constraint.
- **Underestimating integration-depth** â€” Assuming the "new" app integrates easily with 20-year-old mainframe legacy codebases.

## Bulletproofing
- **Governance Policy:** Enforce [CBUAE Rulebook](governance/policy/regulations.yaml#CBUAE), [PDPL](governance/policy/regulations.yaml#PDPL), and [PCI-DSS](governance/policy/regulations.yaml#PCI-DSS) where applicable.

## Outputs
- **Project proposal document** â€” The pitch-deck or document for executive-approval.
- **Strategic alignment-map** â€” Visual/tabular representation of how it benefits the bank long-term.
- **Cost/Benefit/Risk summary** â€” The executive decision-matrix.

## Related skills
- [executive-summary](../executive-summary/SKILL.md)
- [project-charter](../project-charter/SKILL.md)
- [hld-generator](../../architecture/hld-generator/SKILL.md)


### Banking Context & Examples

#### (1) Credit Card Onboarding Example
**Scenario:** Proposing a new digital credit card initiative to the executive board.
- **Architecture Lens Check:** Value proposition must clearly highlight regulatory-Gating (CBUAE/AECB) as a necessary precondition, not a 'soft-constraint'.
- **Sample Outcome:** "Strategy: Leveraging cloud-native components with sovereign-cloud residency, subject to CBUAE data-sovereign audits."
- **Common Pitfall:** Ignoring the regulatory 'sovereign-cloud' requirement in OOM (Order of Magnitude) costing, which leads to budget mid-project shortfall when infrastructure is correctly scoped.

#### (2) Customer Profile Management Example
**Scenario:** Proposal for dashboard rationalization project.
- **Architecture Lens Check:** Highlighting `PDPL` compliance as a key business benefit (brand trust) rather than just an unavoidable regulatory burden.
- **Sample Outcome:** "Business Value: 20

### Banking Context & Examples

#### (1) Credit Card Onboarding Example
**Scenario:** Proposing a new digital credit card initiative to the executive board.
- **Architecture Lens Check:** Value proposition must clearly highlight regulatory-Gating (CBUAE/AECB) as a necessary precondition, not a 'soft-constraint'.
- **Sample Outcome:** "Strategy: Leveraging cloud-native components with sovereign-cloud residency, subject to CBUAE data-sovereign audits."
- **Common Pitfall:** Ignoring the regulatory 'sovereign-cloud' requirement in OOM (Order of Magnitude) costing, which leads to budget mid-project shortfall when infrastructure is correctly scoped.

#### (2) Customer Profile Management Example
**Scenario:** Proposal for dashboard rationalization project.
- **Architecture Lens Check:** Highlighting `PDPL` compliance as a key business benefit (brand trust) rather than just an unavoidable regulatory burden.
- **Sample Outcome:** "Business Value: 20
### Banking Context & Examples

#### (1) Credit Card Onboarding Example
**Scenario:** Proposing a new digital credit card initiative to the executive board.
- **Architecture Lens Check:** Value proposition must clearly highlight regulatory-Gating (CBUAE/AECB) as a necessary precondition, not a 'soft-constraint'.
- **Sample Outcome:** "Strategy: Leveraging cloud-native components with sovereign-cloud residency, subject to CBUAE data-sovereign audits."
- **Common Pitfall:** Ignoring the regulatory 'sovereign-cloud' requirement in OOM (Order of Magnitude) costing, which leads to budget mid-project shortfall when infrastructure is correctly scoped.

#### (2) Customer Profile Management Example
**Scenario:** Proposal for dashboard rationalization project.
- **Architecture Lens Check:** Highlighting `PDPL` compliance as a key business benefit (brand trust) rather than just an unavoidable regulatory burden.
- **Sample Outcome:** "Business Value: 20% reduction in profile management support calls, while strengthening customer trust through PDPL-aligned data privacy controls."
- **Common Pitfall:** Failing to pitch the 'security/residency' aspects of the design as a value-add, thus reducing the project to a 'cost-center' rather than 'trusted-platform' strategy.

#### (3) Lending/Loans Onboarding Example
**Scenario:** Pitching Sharia-compliant product workflow modernization.
- **Architecture Lens Check:** Project alignment with bank's Sharia-governance strategy. 
- **Sample Outcome:** "Strategic Alignment: Directly supports Sharia-product expansion mandate through automated Sharia-governance gates in the loan-origination API."
- **Common Pitfall:** Proposing technical efficiency (faster loan turnaround) without mentioning the `Sharia-Governance` alignment; the board might see the technical speed as secondary to the product-compliance mandate.

### Regulatory References
1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/
2. **PDPL:** Personal Data Protection Law (Federal Decree-Law No. 45 of 2021)
3. **CBUAE Cybersecurity Framework:** Domain 1: Governance & Risk Management

## Anti-patterns
- **Presenting technology stacks before identifying business outcomes**
  - **Consequence:** Business sponsors reject the proposal as a costly technical exercise with no ROI.
  - **Correct Approach:** Focus first slide on current customer pain points and how the solution meets those needs.
- **Ignoring migration, transition, and legacy system compatibility**
  - **Consequence:** Unplanned system downtime or unexpected modernization cost to bridge old and new layers.
  - **Correct Approach:** Include a clear transition roadmap showing legacy migration waves and fallback steps.
- **Understating the operational effort and ongoing maintenance costs**
  - **Consequence:** The system becomes shelf-ware because the bank cannot afford the operational run costs.
  - **Correct Approach:** Detail licensing, compute costs, SRE support teams, and yearly training budgets in the TCO section.
