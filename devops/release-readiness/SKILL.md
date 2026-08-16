---
name: release-readiness
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when gating a release for go/no-go — produces a release-readiness checklist/verdict (change-advisory, test-evidence, rollback-plan, compliance)."
required-inputs:
  - Initiative/system-service-context
  - Test evidence & verification reports
  - Rollback-plan readiness check
  - Compliance gate-approvals (e.g. CBUAE/DIFC)
expected-deliverables:
  - Release-readiness scorecard
  - Go/No-Go decision-verdict
  - Regulatory release-traceability record
---

# /release-readiness

## When to apply
Use for the mandatory "go/no-go" gate before *any* release. Ensures that releases are not just technically sound, but fully compliant, audited, and rollback-ready before hitting the banking production domain.

## Inputs
- **Release-context** — Release-ID, impacted services, business-impact analysis.
- **Evidence-pack** — Test logs, SAST reports, approval sign-offs.
- **Contingency Status** — Rollback-plan validated?

## Process
1. **Change-Advisory Gate.** Verify the CAB/Change-board-approval (or equivalent automated-gate data).
2. **Evidence Audit.** Quantifiable proof: Test-suite pass, automated scan status, compliance-gate-verdict.
3. **Rollback Review.** Is the [rollback-plan](../../migration/rollback-plan/SKILL.md) currently verified for this exact version?
4. **Residency/Compliance Review.** Has the "Compliance/Regulatory gate" been formally signed off for this release?
5. **Issue Verdict.** Go, No-go, or Conditional-go (with-risks-accepted).

## Banking pitfalls
- **Evidence-fabrication/omission** — Assuming "it ran through the pipeline" is sufficient evidence without auditing the actual test-exit-criteria log.
- **Rollback "assumed"** — Believing the app can be rolled-back without practicing the DB-data-reversal-step in a non-production environment.
- **Failing to notify Stakeholders** — Releasing without the documented communication-plan for Compliance/SOC, or missing a regulatory-reporting trigger.
- **Regulatory-gating invisibility** — Approving a release that requires a specific CBUAE approval-letter that hasn't actually arrived yet.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of release-readiness meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the release-readiness process.**

## Outputs
- **Release-readiness scorecard** — The objective measure of gates vs targets.
- **Go/No-Go decision-verdict** — Executable command to release.
- **Regulatory release-traceability record** — Snapshot of release-compliance for the audit-trail.

## Related skills
- [cicd-review](../cicd-review/SKILL.md)
- [production-readiness](../../governance/production-readiness/SKILL.md)
- [rollback-plan](../../migration/rollback-plan/SKILL.md)
