---
name: technology-evaluation
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when evaluating a specific tech/component for a banking initiative — produces an evaluation report (build/buy/use, fit, risk, support) and architectural verdict."
required-inputs:
  - Component/tech candidate
  - Evaluation criteria & use cases
  - Banking domain architectural context
  - Regulatory & security requirements
expected-deliverables:
  - Technology evaluation report
  - Banking-fit and risk assessment
  - Architectural veto/approval verdict
---

# /technology-evaluation

## When to apply
Use when a delivery team wants to introduce a new technology, service, or component (e.g. new integration library, data-streaming engine, specific AI/ML model, new database SKU). Prevents uncontrolled tech-stack sprawl by enforcing a documented, scored, and regulatory-aware evaluation for every new introduction into the bank's production environment.

## Inputs
- **Technology candidate** — what is it and why do we need it?
- **Use case / Context** — exactly where in the banking journey does this fit?
- **Evaluation criteria** — fit-for-purpose (banking capability mapping), cost, risk, supportability (does the bank have the skills?), licensing, compliance.
- **Regulatory/Security** — PDPL/CBUAE/Freezone considerations.

## Process
1. **Define the assessment lens.**
   - Functional fit (BIAN-grounded domain capability).
   - Non-functional fit (performance, scalability, reliability, observability).
   - Regulatory fit (data residency, AI-processing regulations).
   - Operational fit (skill availability, licensing, vendor support/exit-plan).
2. **Conduct the build vs buy vs reuse evaluation.**
   - **Reuse-over-rewrite:** Does the bank *already* have a vetted component (e.g. existing Kafka cluster, existing API gateway, existing secrets manager) that handles this?
   - **Buy vs Build:** Does this solve a competitive banking differentiation (e.g. proprietary AI-engine or unique payments-switch logic) or commodity banking capability (e.g. log-parsing or generic queue-worker)?
3. **Review risks.**
   - Vendor risk (e.g. SaaS bank-dependency, financial stability).
   - Compatibility/Lock-in (can we swap it if we need to?).
   - Compliance risk (does it process PII/payment data? Is it a compliant vendor?).
4. **Issue verdict.** Recommendation: Approved, Approved-with-conditions, Vetoed, or Resubmit-with-modifications.

## Banking pitfalls
- **"New & shiny" bias** — adopting a cutting-edge engine for a commodity banking use case (e.g. niche streaming tech for a simple nightly-batch report).
- **Ignoring the integration-tax** — cost of wrapping, logging, monitoring, and IAM-federating a new component into the banking estate.
- **Vendor-lock-in without an exit plan** — adopting a SaaS-only component without clear data-export/portability plans for regulators (like CBUAE operational resilience requirements).
- **Security-blind evaluation** — component is functional, but lacks the bank-appropriate IAM integration, auditability, or data-protection compliance.
- **Skill-gap failure** — introducing a tech the bank ops/dev team cannot actually operate.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of technology-evaluation meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the technology-evaluation process.**

## Outputs
- **Technology evaluation report** — summary of the evaluation, candidate, decision rationale, risk-register items.
- **Architectural verdict** — explicit Approved or Vetoed stance.
- **Banking-fit/risk assessment** — specific banking-capability/regulatory fit.

## Related skills
- [reference-architecture](../reference-architecture/SKILL.md) — where the vetted technology lands.
- [platform-selection](../platform-selection/SKILL.md) — higher-level decision than a single component.
- [technical-debt](../../modernization/technical-debt/SKILL.md) — how to manage the lifecycle of technologies after they are introduced.

### Regulatory References
1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/
2. **PDPL:** Personal Data Protection Law (Federal Decree-Law No. 45 of 2021)
3. **CBUAE Cybersecurity Framework:** Domain 1: Governance & Risk Management

