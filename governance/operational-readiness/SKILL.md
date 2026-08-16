---
name: operational-readiness
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when evaluating a team's operational readiness to support a banking service — produces an operational-readiness report (runbooks, on-call, training, org-alignment)."
required-inputs:
  - Incident-management operational-maturity (PIRs/Toil)
  - Runbooks & procedures
  - On-call/support team-structure and training
  - Operational-resiliency requirements
expected-deliverables:
  - Operational-readiness assessment-report
  - Supportability-scorecard
  - Runbook-gap-analysis
---

# /operational-readiness

## When to apply
Use to qualify whether the *organization* is ready to support the *service*. A technically-perfect service will fail if the support team doesn't have the training, authority, or tools to keep it running.

## Inputs
- **Support-Structure.** Is there an aligned team?
- **Procedures.** Do the run-books exist and are they current?

## Process
1. **Organizational-Alignment.** Is it clear *who* owns the service in production?
2. **Support-Capability-Assessment.** Does the team have the training/access to troubleshoot?
3. **Runbook-Audit.** Review the actual-runbooks—do they just say "call-engineering," or do they contain *executable-remediation-steps*?
4. **Resiliency-Alignment.** Is the team prepared for regulated-incident-reporting-timelines (e.g., 72-hour notification)?
5. **Issue-Report.** Assessment of maturity.

## Bulletproofing against Rationalization
- **Support-team-as-a-dumping-ground** — Assigning complex, modern-service-support to a team that only has mainframe-training, without *up-skilling* them first.
- **Runbooks-as-a-static-artifact** — Maintaining "Runbooks" as static Word-docs that are never updated, and are already-obsolete when the system-incidents-occur.
- **On-call-Hero-Dependency** — Lacking a *structured* on-call rotation, relying solely on one "Hero" who is always-awake, leading to inevitable-burnout-and-stability-collapse.
- **Regulatory-Reporting-Gaps** — Not training the support-team *at all* on how to report a major-incident-compliant-with-CBUAE-operational-resiliency-regulations.

## Bulletproofing against Rationalization
To prevent systems from crashing without a recovery path on Day 2, you MUST:

1. **Mandatory Runbook Verification:** A system CANNOT pass Operational Readiness without verified, linked standard operating procedures (runbooks) for patching, scaling, and failure recovery.
2. **Mandatory Alert Routing Verification:** Monitoring cannot be "turned on." You MUST verify that high-severity alerts successfully route to a named, existing on-call rotation.
3. **Mandatory Backup Restoration Validation:** Producing backups is insufficient. You MUST possess evidence of a localized DR/Data restoration test executing successfully.
4. **Explicit Support Handover:** L1/L2 support structures MUST explicitly sign-off on the transition; undocumented "Dev-owned Ops" is rejected in a banking parameter.

**Violating these rules invalidates the Operational Readiness gate.**

## Outputs
- **Operational-readiness assessment-report** — The team-preparedness-verdict.
- **Supportability-scorecard** — Quantitative measure of operational-maturity.
- **Runbook-gap-analysis** — The identified weaknesses in documentation/process.

## Related skills
- [sre-review](../../devops/sre-review/SKILL.md)
- [production-readiness](../production-readiness/SKILL.md)
- [architecture-board](../architecture-board/SKILL.md)
