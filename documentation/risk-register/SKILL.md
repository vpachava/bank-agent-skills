---
name: risk-register
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when drafting a risk register for a banking initiative — produces a risk-register (severity-scores, mitigation, regulatory-impact)."
required-inputs:
  - Inventory of potential threats
  - Likelihood/Impact ratings
  - Mitigation strategies
  - Regulatory compliance impact (e.g. data residency)
expected-deliverables:
  - Comprehensive risk-register table
  - Mitigation-action roadmap
  - Regulatory risk-exposure dashboard
---

# /risk-register

## When to apply
Use for the formal, auditable risk-landscape for a project. In banking, this is NOT optional; it is required by the CRO (Chief Risk Officer) and internal-audit. If it isn't in the risk-register and mitigated, it's a "finding."

## Inputs
- **Threat source** — e.g. Technical, Operational, Regulatory, Third-party.
- **Rating** — Likelihood x Impact.
- **Regulatory Gating** — Does this threat violate a bank-policy or local regulation?

## Process
1. **Identify.** Document the risk clearly (e.g. "Cloud-provider service-outage leads to 4-hour settlement-breach").
2. **Rate.** Assign Likelihood(1-5) and Impact(1-5).
3. **Mitigate.** Define the *preventative* control vs the *detective* control.
4. **Assign.** Owner is accountable.
5. **Report.** Weekly status of mitigation-progress for the Board/Executive-Committee.

## Banking pitfalls
- **Under-rating Operational-Resiliency-Risks** — Rating "System-Down-Time" as Impact-3 when in a *Payment-System*, it is Impact-5 (immediate regulatory-breach).
- **Ignoring Cumulative-Risk** — Treating 5 "Medium-severity-security-gaps" as separate, rather than documenting that their combination constitutes a "Major-Compliance-Failure."
- **Ghost-Mitigation** — Defining a mitigation strategy (e.g. "We will have a failover test") but never *formally-executing* that test as evidence for audit.
- **Data-Residency-Gaps** — Identifying "using-global-cloud" as a risk without explicitly mapping it to the bank's CBUAE-data-residency-compliance-policy.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of risk-register meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the risk-register process.**

## Outputs
- **Comprehensive risk-register table** — The canonical document.
- **Mitigation-action roadmap** — Tasks linked in Jira/ADO.
- **Regulatory risk-exposure dashboard** — The report for Compliance/CRO.

## Related skills
- [raid-log](../raid-log/SKILL.md)
- [security-architecture-review](../../security/security-architecture-review/SKILL.md)
- [compliance](../../security/compliance/SKILL.md)


### Banking Context & Examples

#### (1) Credit Card Onboarding Example
**Scenario:** Risk register for a new digital credit-card product.
- **Architecture Lens Check:** High-severity regulatory risk if the credit-scoring engine fails to feed `AECB` data accurately.
- **Sample Outcome:** "Risk [R-001]: Failure to report AECB data leads to CBUAE regulatory fine. Impact: 5. Mitigation: Automated reconciliation between origination-core and AECB-reporting engine. Owner: Origination-Lead."
- **Common Pitfall:** Rating AECB-integration failures as 'Operational' risk rather than 'Compliance-Regulatory' risk, thus missing the CBUAE-mandated escalation path.

#### (2) Customer Profile Management Example
**Scenario:** Risk registry for profile dashboard PII exposure.
- **Architecture Lens Check:** Risk of unauthorized access to PII due to logic-errors in cross-border profile dashboard updates (PDPL violation).
- **Sample Outcome:** "Risk [R-005]: Unintended PII disclosure to non-resident-zone dashboard users. Mitigation: Hard separation of residency-restricted data-stores. Owner: Security-Lead."
- **Common Pitfall:** Listing profile data leakage as 'Minor' because the customer has 'already provided data', ignoring the legal severity of a `PDPL` data-sovereignty breach.

#### (3) Lending/Loans Onboarding Example
**Scenario:** Risk register for a Sharia-compliant loan project.
- **Architecture Lens Check:** Operational risk of using a non-`Sharia` compliant amortization logic.
- **Sample Outcome:** "Risk [R-009]: Use of interest-based amortization logic in Sharia product. Impact: 5. Mitigation: Formal Sharia Governance Board certification for product-workflow logic. Owner: Product-Owner."
- **Common Pitfall:** Rating 'Sharia-non-compliance' risk as 'Technical Debt' which allows it to be deferred, instead of 'Major Regulatory Breach' which requires immediate production-stop.
### Regulatory References
1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/
2. **PDPL:** Personal Data Protection Law (Federal Decree-Law No. 45 of 2021)
3. **CBUAE Cybersecurity Framework:** Domain 1: Governance & Risk Management

