---
name: project-charter
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when creating a project charter for a banking project — produces a project-charter (purpose, scope, authority, key-roles)."
required-inputs:
  - Project purpose & objectives
  - High-level scope & constraints
  - Key personnel/governance (PM, Product-Owner, Sponsor)
  - Authority level (Budget/Decision-rights)
expected-deliverables:
  - Formal project-charter document
  - Governance/decision-matrix
  - Scope-bound constraints-map
---

# /project-charter

## When to apply
Use for the formal start of a project. The charter provides the PM/Sponsor authority to spend budget, deploy resources, and make decisions. Without a signed charter, a banking project is "unauthorized-work" and vulnerable to being killed at any moment.

## Inputs
- **Objectives** — What business outcome are we delivering?
- **Scope** — What are we *definitely not* doing?
- **Governance** — Who decides if the project is authorized/stopped?

## Process
1. **Purpose.** Why are we doing this project? (Strategic-link).
2. **Scope.** Clear definition-of-boundaries.
3. **Roles.** Sponsor, Project-Manager, Product-Owner, Risk-Owner.
4. **Authority.** Budget-limit (before-needing-further-signoff) and decision-rights.
5. **Regulatory-Gating.** Document any regulatory-signoff that must occur before go-live.

## Banking pitfalls
- **Unbounded-Scope** — Assuming the "Modernization-Project" will include "AI-chatbot-implementation" just because it sounds fancy, causing massive budget-slippage.
- **Empty-Roles** — No assigned Risk-Owner, meaning technical-debts accrue without accountability.
- **Decision-Rights-Ambiguity** — Leaving it unclear if the "Architectural-Governing-Board" or the "Local-Product-Owner" has the final say on architectural-decisions.
- **Assuming Authorization** — Believing the project is "authorized" just because a VP mentioned it in a meeting, without a signed charter for the PM.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of project-charter meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the project-charter process.**

## Outputs
- **Formal project-charter document** — The authorization-document.
- **Governance/decision-matrix** — RACI chart for key-decisions.
- **Scope-bound constraints-map** — Clearly defines what is "In-Scope" vs "Out-of-Scope."

## Related skills
- [proposal](../proposal/SKILL.md)
- [executive-summary](../executive-summary/SKILL.md)
- [raid-log](../raid-log/SKILL.md)


### Banking Context & Examples

#### (1) Credit Card Onboarding Example
**Scenario:** Drafting a charter for a new credit-card issuance initiative.
- **Architecture Lens Check:** High-level project goal must explicitly state compliance with `CBUAE` requirements for credit card product issuance (e.g., DBR/AECB checks).
- **Sample Outcome:** "Project Charter: Authorized to deliver virtual-card features compliant with CBUAE consumer-protection regulations for retail banking."
- **Common Pitfall:** Drafting a generic 'Digital-Card-Project' charter, thereby failing to capture the project's regulatory 'compliance-as-code' obligations which can stall go-live.

#### (2) Customer Profile Management Example
**Scenario:** Project charter for cross-border dashboard rationalization.
- **Architecture Lens Check:** Documentation of `PDPL` residency-compliance as a foundational project boundary.
- **Sample Outcome:** "Constraints: All customer PII management must strictly comply with UAE Data Residency policies (PDPL)."
- **Common Pitfall:** Omitting residency-compliance as a project constraint, encouraging developers to use cloud services that may later be found in violation of local CBUAE/PDPL rules.

#### (3) Lending/Loans Onboarding Example
**Scenario:** Project charter for Sharia-compliant personal loan product.
- **Architecture Lens Check:** Explicit requirement for `Sharia Board` approval as part of the project's critical governance path.
- **Sample Outcome:** "Governance Path: Project cannot proceed to go-live without formal certification from the Internal Sharia Governance Board."
- **Common Pitfall:** Defining project goals only by revenue/technical metrics, ignoring the 'Sharia-Governance' gate, making the project's Go-Live readiness unattainable.
### Regulatory References
1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/
2. **PDPL:** Personal Data Protection Law (Federal Decree-Law No. 45 of 2021)
3. **CBUAE Cybersecurity Framework:** Domain 1: Governance & Risk Management

