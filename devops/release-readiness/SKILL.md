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

### Banking Context & Examples

#### (1) Regulatory Approval Traceability Example
**Scenario:** Readying a release for a new payment processing service.
- **Architecture Lens Check:** Verification of explicit sign-off from `CBUAE` for the new transaction-message format.
- **Sample Outcome:** "Regulatory Traceability-Record: [Release-ID: 102] linked to formal CBUAE-approval-letter ref: #CB/2026/08/PAY."
- **Common Pitfall:** Assuming the technical 'Go' is sufficient. If the `CBUAE` or `Internal Sharia Board` approval letter is missing, the release is formally illegal even if the tests all pass green.

#### (2) Automated Rollback Practice Example
**Scenario:** Planning a release for the mobile banking app's profile-update service.
- **Architecture Lens Check:** Simulation of database rollback, including potential data-corruption reversal of `Emirates ID` records.
- **Sample Outcome:** "Rollback-Plan Status: `Verified`. DB-Data-Reversal-Procedure for `Customer_Profile` table tested successfully in Pre-Prod."
- **Common Pitfall:** Relying on 're-deploying the previous binary' as a rollback strategy. In banking core-systems, a binary swap doesn't undo the corrupted database records `EMIRATES_ID` was modified to; the DB-data-reversal must be the primary test criterion.

#### (3) Go/No-Go Gate Checklist Example
**Scenario:** Releasing a Sharia-compliant loan origination improvement.
- **Architecture Lens Check:** Validating that `Sharia-Compliant-Repayment` flags were actually included in the test-data and passed validation gate.
- **Sample Outcome:** "Release-Readiness Scorecard: Gate `Sharia-Compliance-Audit` status=Pass; Evidence attached: `audit_sharia_log_v2.json`."
- **Common Pitfall:** Approving a release based only on generic functional tests. Releasing a Sharia-compliant product without verified `Sharia-Compliance` test-logs is a total regulatory failure (non-compliance with `Sharia-Governance-Standards`).

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

