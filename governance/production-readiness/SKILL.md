---
name: production-readiness
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when assessing if a service is ready for the production-banking environment â€” produces a production-readiness artifact (readiness-scorecard, operational-resiliency-audit, supportability-verdict)."
required-inputs:
  - Monitoring, logging, alerting readiness-definition
  - Incident-management operational-maturity (PIRs/Toil)
  - Disaster-recovery & business-continuity plan
  - Compliance/Regulatory signoff
expected-deliverables:
  - Production-readiness scorecard
  - Operational-resiliency audit-report
  - Supportability-verdict (Go/No-go)
togaf-phases: [Phase G]
togaf-artifacts: [Compliance Checklist]
bian-service-domains: [Security.Auth]
---

# /production-readiness

## When to apply
Use for the final gate before a new/updated banking service goes "Live." Production readiness is the difference between a successful release and a catastrophic production-incident. In banking, this is explicitly tied to *operational-resiliency* regulations.

## Inputs
- **Operational-Maturity.** Is it "engineered" or "hacked"?
- **Audit-Evidence.** Logs/Metrics/Alerts setup?

## Process
1. **Operational-Resiliency-Audit.** Run through the checklists: observability, alerting, automated-recovery, failover-testing.
2. **Supportability-Review.** Does the production-support-team have the run-books, access, and training?
3. **Regulatory-Gate-Verification.** Are all compliance-gates formally signed off?
4. **Issue-Scorecard.** Provide quantitative-score and Qualitative-Verdict.

## Bulletproofing against Rationalization
- **"Monitoring-Is-Enough"** â€” Thinking that having Grafana-dashboards constitutes "Production-Readiness" while failing to configure *actionable-alerts* that actually trigger support-action.
- **Support-Team-Ambush** â€” Deploying a service to production without giving the production-support-team the necessary Training/Run-books, leading to inevitable service-failure.
- **Disaster-Recovery-Paper-Tiger** â€” Having a "DR-Plan" in a Word-doc that has never been *formally-exercised* in a non-production-failover-test.
- **Ignoring-The-Business-Resiliency-Mandate** â€” Not defining *how* the service fails gracefully (e.g. "Do we fail-closed or fail-open on an-event-bus-failure?"), leading to massive business-disruption.

## Bulletproofing against Rationalization
To prevent unstable rollouts breaching regulatory thresholds, you MUST:

1. **Mandatory Rollback Execution Proof:** The deployment plan MUST contain a rollback script/process, and its methodology MUST be verified as functional, not merely theoretical.
2. **Mandatory Defect Zero-Tolerance for Security:** You CANNOT bypass critical or high InfoSec vulnerabilities via local project acceptance. Executive clearance is required.
3. **Mandatory Data Sanity Pre-Checks:** A Production launch affecting Ledger operations MUST explicitly mandate pre-flight balancing/reconciliation hooks.
4. **Explicit Outage Window Mapping:** Cutover plans MUST explicitly align against the published Operational Downtime windows of affected core banking rails.

**Violating these rules invalidates the Production Readiness gate.**

## Outputs
- **Production-readiness scorecard** â€” Objective measure-of-readiness.
- **Operational-resiliency audit-report** â€” The findings of the audit.
- **Supportability-verdict** â€” Final Go/No-go-decision.

## Related skills
- [sre-review](../../devops/sre-review/SKILL.md)
- [release-readiness](../../devops/release-readiness/SKILL.md)
- [dr-review](../dr-review/SKILL.md)

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
- **Running the review checklist as a last-minute box-ticking exercise**
  - **Consequence:** Finding critical gaps (e.g. no backup, missing audit logs) when it is too late to postpone the release.
  - **Correct Approach:** Run production readiness checks continuously across environment stages.
- **Releasing products without testing system recovery scenarios**
  - **Consequence:** Support teams cannot resolve production lockouts, extending outage times.
  - **Correct Approach:** Enforce a check requiring manual failover tests before the production gate is passed.
- **Validating system compliance checklists manually**
  - **Consequence:** Human errors lead to non-compliant deployments and security risks.
  - **Correct Approach:** Automate validation rules within the CI/CD pipeline using policy-as-code tools.
