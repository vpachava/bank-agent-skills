---
name: dr-review
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when performing a disaster-recovery (DR) architectural-review — produces a DR-assessment (RPO/RTO, failover-mechanisms, validation-strategy)."
required-inputs:
  - Disaster-recovery strategy (active/passive, active/active)
  - RPO/RTO targets for banking-services
  - Failover testing & validation results
  - DR-residency & infrastructure strategy
expected-deliverables:
  - Disaster-recovery assessment-report
  - RPO/RTO compliance-verification
  - Failover-validation roadmap
---

# /dr-review

## When to apply
Use to validate the robustness of the bank's ability to survive catastrophic failure (data-center loss, cloud-region failure, cyber-attack). In banking, DR is mandated by both CBUAE and international operational-resiliency frameworks.

## Inputs
- **Strategy & Targets.** What is the RPO/RTO requirement?
- **Failover-Artifacts.** Proof that the failover works.

## Process
1. **RPO/RTO Audit.** Are these targets *mathematically achievable* given current replication-methods?
2. **Failover-Mechanism-Analysis.** How does the failover trigger? Automaticaly? Manually? Who has the authority-to-trigger?
3. **Residency-Verification.** In DR, does the data-flow violate residency-laws (e.g., does it failover to an out-of-country cloud-region)?
4. **Validation-Testing.** Review the *evidence* of the last formal-DR-test.
5. **Issue-Report.** Clearly catalog gaps in resilience.

## Bulletproofing against Rationalization
- **RPO/RTO "Dreaming"** — Committing to an RTO of "seconds" for a mainframe-core that only supports daily-batch-sync (mathematically-impossible-goal).
- **Silent-DR-Replication-Failures** — Relying on cross-region-replication that hasn't successfully-synced in days, without *alerting* the support-team of the drift.
- **Failover-Authority-Confusion** — Having a service-failover that *can* be triggered by anyone, leading to accidental-triggers (operator-error), or conversely, requiring an executive-signoff-chain that makes the failover too-slow.
- **Data-Residency-DR-Trap** — Failing over to a DR-site in a *different country/jurisdiction*, unknowingly violating PDPL or CBUAE-data-residency-compliance-policy.

## Bulletproofing against Rationalization
To prevent theoretical Disaster Recovery architectures that collapse in production, you MUST:

1. **Mandatory RTO/RPO Empirical Evidence:** DR Reviews CANNOT accept stated capacities. You MUST demand actual test-run metrics proving RTO (Time) and RPO (Data Loss) boundaries are successfully validated.
2. **Mandatory Failback Analysis:** The DR Review MUST examine the procedure to restore operations from the secondary region BACK to the primary region, not just the initial failover.
3. **Mandatory Active/Active Edge Case Check:** Active/Active setups MUST be explicitly interrogated for cross-region data replication collision and split-brain resolution handling.
4. **Third-Party Dependency Failure Testing:** DR plans MUST document how the system behaves when external cloud services/vendors themselves experience regional degradation.

**Violating these rules invalidates the DR Review.**

## Outputs
- **Disaster-recovery assessment-report** — Findings on survival-posture.
- **RPO/RTO compliance-verification** — Can we actually meet the targets?
- **Failover-validation roadmap** — Plan-of-action for testing.

## Related skills
- [production-readiness](../production-readiness/SKILL.md)
- [observability](../../devops/observability/SKILL.md)
- [security-architecture-review](../../security/security-architecture-review/SKILL.md)

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
