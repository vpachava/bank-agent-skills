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
