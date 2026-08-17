---
name: sre-review
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when running an SRE review for a banking service â€” produces an SRE review report (SLOs/SLIs, error-budgets, toil, incident-mgmt)."
required-inputs:
  - Service SLO/SLI definitions
  - Incident-management operational-history
  - Toil-reduction automation-map
  - On-call/support team-structure
expected-deliverables:
  - SRE service-review report
  - Error-budget compliance-assessment
  - Toil-reduction strategy-map
togaf-phases: [Phase G]
togaf-artifacts: [Compliance Checklist]
bian-service-domains: [Security.Auth]
---

# /sre-review

## When to apply
Use to professionalize the support and reliability posture of a banking service. Moves teams from "reactive firefighting" to codified reliability management (SRE) by grounding reliability in quantified SLOs and budgetary control.

## Inputs
- **SLO definition** â€” Targets for availability/latency.
- **Incident report** â€” Recent post-incident reviews (PIRs).
- **Toil measurement** â€” How much time is spent on manual operational tasks?

## Process
1. **SLO/SLI Audit.** Are these goals actually tethered to business-outcomes (e.g., payments-processed/sec)?
2. **Error-Budget Assessment.** If the budget is *gone*, is the team following the formal feature-freeze-protocol?
3. **PIR Review.** Are incident-response processes efficient, audited, and compliant with banking operational-resiliency rules?
4. **Toil Audit.** Identify manual work that is blocking scaling or creating reliability risks.
5. **Issue SRE Report.** Document maturity and gaps.

## Banking pitfalls
- **Silent SLO-descoping** â€” Reducing SLO-targets just to "meet" the budget, rather than improving the system-architecture.
- **Incident-management-secrecy** â€” Managing incidents privately without the audit-trail/reporting required for banking regulators (e.g. CBUAE/DIFC).
- **"Toil-as-feature-work"** â€” Allowing operators to spend all time on manual tasks, ignoring the need for SRE-led engineering fixes that make the system more resilient.
- **Ignoring the "Shared-on-call-responsibility"** â€” Creating silos where devs "ship features" but never face the reliability-consequences that Ops-teams face.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of sre-review meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the sre-review process.**

## Outputs
- **SRE service-review report** â€” Maturity, maturity-assessment, reliability-gaps.
- **Error-budget compliance-assessment** â€” Is the budget being respected?
- **Toil-reduction strategy-map** â€” Prioritized roadmap of toil-elimination work.

## Related skills
- [observability](../observability/SKILL.md)
- [release-readiness](../release-readiness/SKILL.md)
- [operational-readiness](../../governance/operational-readiness/SKILL.md)

### Banking Context & Examples

#### (1) Error Budget and Feature Freeze Example
**Scenario:** Managing the error budget for a high-traffic retail payment service.
- **Architecture Lens Check:** Verification that the service entered a formal `Feature-Freeze` once the `Error-Budget` hit 0% following a `CBUAE` reporting incident.
- **Sample Outcome:** "Error-Budget Compliance-Assessment: Budget exhausted during incident #INC-2026-PAY-88. Formal `Feature-Freeze` initiated 2026-08-15."
- **Common Pitfall:** Treating 'Error-Budget' as advisory. In banking, if you don't enforce the `Feature-Freeze` when the budget is spent, you are prioritizing 'new features' over the 'operational stability' mandated by regulators as part of the bank's license to operate.

#### (2) Post-Incident Governance Example
**Scenario:** Conducting a Post-Incident Review (PIR) for an unexpected service outage on the digital banking portal.
- **Architecture Lens Check:** Documentation of the incident in compliance with internal `Operational-Resiliency` governance and `CBUAE` reporting requirements.
- **Sample Outcome:** "PIR Documentation: Incident #INC-2026-MOB-12. Root-cause verified; `Regulator-Reporting-Required`=True; `Regulatory-Report-Ref`: #CB/2026/08/INC-MOB-12."
- **Common Pitfall:** Sanitizing incident reports to hide the truth from the 'business' or 'regulators'. Banking incidents require *full audit trails*. If you don't formally record the root cause and the regulatory reporting status in your SRE tool, the bank is exposed to major fines for non-disclosure.

#### (3) Toil Reduction in Reconciliation Example
**Scenario:** Reducing operational toil in the end-of-day treasury reconciliation service.
- **Architecture Lens Check:** Prioritization of SRE engineering work (automating recons) over manual data-patching.
- **Sample Outcome:** "Toil-Reduction Strategy-Map: Priority #1: Automated reconciler for `UAEFTS` clearing data (estimated saving: 30 hours/week of manual toil)."
- **Common Pitfall:** Accepting manual toil (e.g., Ops staff manually patching reconciliation files every night) as a 'standard procedure'. This scale-bottleneck is a major reliability risk; if the manual staff gets it wrong, the ledger becomes unbalancedâ€”unacceptable for any banking institution.

### Banking Context & Examples

#### (1) Retail Banking Scenario
**Scenario:** Applying this skill in a retail bank core-modernization effort.
- **Architecture Lens Check:** Verification of compliance with CBUAE data-residency rules (e.g. [[compliance]]).
- **Sample Outcome:** "Design: Automated workflow integration; [[observability]] logs scrubbed of PII."
- **Common Pitfall:** Ignoring the Sharia-governance impact on the product-schema.

#### (2) Corporate Banking Scenario
**Scenario:** Using this skill for a corporate digital-onboarding integration.
- **Architecture Lens Check:** Alignment with AECB credit-reporting integration for legal-entity applicants.
- **Sample Outcome:** "Design: Integration-seam validated for high-assurance KYC; [[api-design]] handles large payload-signatures."
- **Common Pitfall:** Bypassing the mandatory legal-entity KYC check due to tight project timelines.

#### (3) Islamic Banking Scenario
**Scenario:** Utilizing this skill for Sharia-compliant loan product rollouts.
- **Architecture Lens Check:** Sharia-Board approval workflow documented within the [[architecture-decision-records]].
- **Sample Outcome:** "Design: Profit-distribution calculation encapsulated; [[api-design]] schema includes mandatory Sharia-compliance flag."
- **Common Pitfall:** Applying standard interest-based loan models to Islamic products, violating compliance.

### Regulatory References
1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/
2. **PDPL:** Personal Data Protection Law (Federal Decree-Law No. 45 of 2021)
3. **CBUAE Cybersecurity Framework:** Domain 1: Governance & Risk Management

## Anti-patterns
- **Defining service level agreements (SLAs) without real SLI metrics**
  - **Consequence:** Outage events happen but dashboards continue to report green (false compliance).
  - **Correct Approach:** Link target SLOs to reliable, quantifiable metrics (e.g., successful request rates) at the entry gateway.
- **Treating post-incident reviews as a process of finding someone to blame**
  - **Consequence:** Teams hide mistakes, leading to repeated incidents and lack of learning.
  - **Correct Approach:** Conduct blameless post-mortem reviews focused on system improvements and process failures.
- **Running manual operational tasks repeatedly without work automation plans**
  - **Consequence:** High engineering overhead, burnout, and frequent human-error incidents.
  - **Correct Approach:** Track toil hours and dedicate engineering cycles to automate repeated tasks.
