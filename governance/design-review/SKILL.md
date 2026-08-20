---
name: design-review
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when performing a detailed technical-design review (TDD/Design-Spec) â€” produces a design-review report (clash-detection, implementation-path, security-controls, performance-suitability)."
required-inputs:
  - Technical-design document (TDD/Spec)
  - Data-flow diagrams/C4-views
  - Security-control definitions
  - Implementation/deployment-plan
expected-deliverables:
  - Technical design-review report
  - Clash-detection log
  - Implementation go/no-go recommendation
togaf-phases: [Phase G]
togaf-artifacts: [Compliance Checklist]
bian-service-domains: [Security.Auth]
---

# /design-review

## When to apply
Use for the final technical-assurance of a solution. This is the peer-review that occurs *after* the architectural-review (HLD), focused on "Is this design implementable, secure, performant, and maintainable?"

## Inputs
- **Design Spec.** The TDD/API-definitions.
- **Implementation-Plan.** The deployment/migration-approach.

## Process
1. **Clash-Detection.** Do the components fit together (e.g., API-contracts, data-schema)?
2. **Security-Control-Verification.** Are the specified security-controls (e.g. encryption/PII-masking) *actually implementable* within the technical-design?
3. **Performance-Verification.** Are the NFRs (latency/throughput) *realistically achievable* given the design-choice?
4. **Implementation-Viability.** Can the team actually build/deploy this using bank-standard tools (CI/CD, Landing-Zone)?
5. **Issue-Report.** Clearly documented-defects.

## Bulletproofing
- **Governance Policy:** Enforce [CBUAE Rulebook](governance/policy/regulations.yaml#CBUAE), [PDPL](governance/policy/regulations.yaml#PDPL), and [PCI-DSS](governance/policy/regulations.yaml#PCI-DSS) where applicable.

## Outputs
- **Technical design-review report** â€” Formal-feedback on the spec.
- **Clash-detection log** â€” Specific technical-defects to be resolved.
- **Implementation go/no-go recommendation** â€” Is it time to build?

## Related skills
- [design-document](../../documentation/design-document/SKILL.md)
- [architecture-board](../architecture-board/SKILL.md)
- [release-readiness](../../devops/release-readiness/SKILL.md)

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
- **Focusing reviews on detailed code implementations instead of components**
  - **Consequence:** Reviews take too long, missing high-level integration issues and missing timelines.
  - **Correct Approach:** Scope the review on APIs, database patterns, data flows, and isolation boundaries.
- **Reviewing component design without evaluating scaling limits**
  - **Consequence:** System bottleneck failures under peak production transaction throughputs.
  - **Correct Approach:** Require the design package to include latency profiles, thread limits, and cache plans.
- **Failing to track design review feedback in issue tracking tickets**
  - **Consequence:** Developers skip recommended design fixes, leading to non-compliant production releases.
  - **Correct Approach:** Log feedback as tickets inside the tracking board and verify block closures before code merges.
