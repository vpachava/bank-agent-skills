---
name: sre-review
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when running an SRE review for a banking service — produces an SRE review report (SLOs/SLIs, error-budgets, toil, incident-mgmt)."
required-inputs:
  - Service SLO/SLI definitions
  - Incident-management operational-history
  - Toil-reduction automation-map
  - On-call/support team-structure
expected-deliverables:
  - SRE service-review report
  - Error-budget compliance-assessment
  - Toil-reduction strategy-map
---

# /sre-review

## When to apply
Use to professionalize the support and reliability posture of a banking service. Moves teams from "reactive firefighting" to codified reliability management (SRE) by grounding reliability in quantified SLOs and budgetary control.

## Inputs
- **SLO definition** — Targets for availability/latency.
- **Incident report** — Recent post-incident reviews (PIRs).
- **Toil measurement** — How much time is spent on manual operational tasks?

## Process
1. **SLO/SLI Audit.** Are these goals actually tethered to business-outcomes (e.g., payments-processed/sec)?
2. **Error-Budget Assessment.** If the budget is *gone*, is the team following the formal feature-freeze-protocol?
3. **PIR Review.** Are incident-response processes efficient, audited, and compliant with banking operational-resiliency rules?
4. **Toil Audit.** Identify manual work that is blocking scaling or creating reliability risks.
5. **Issue SRE Report.** Document maturity and gaps.

## Banking pitfalls
- **Silent SLO-descoping** — Reducing SLO-targets just to "meet" the budget, rather than improving the system-architecture.
- **Incident-management-secrecy** — Managing incidents privately without the audit-trail/reporting required for banking regulators (e.g. CBUAE/DIFC).
- **"Toil-as-feature-work"** — Allowing operators to spend all time on manual tasks, ignoring the need for SRE-led engineering fixes that make the system more resilient.
- **Ignoring the "Shared-on-call-responsibility"** — Creating silos where devs "ship features" but never face the reliability-consequences that Ops-teams face.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of sre-review meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the sre-review process.**

## Outputs
- **SRE service-review report** — Maturity, maturity-assessment, reliability-gaps.
- **Error-budget compliance-assessment** — Is the budget being respected?
- **Toil-reduction strategy-map** — Prioritized roadmap of toil-elimination work.

## Related skills
- [observability](../observability/SKILL.md)
- [release-readiness](../release-readiness/SKILL.md)
- [operational-readiness](../../governance/operational-readiness/SKILL.md)
