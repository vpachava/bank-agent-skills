---
name: design-review
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when performing a detailed technical-design review (TDD/Design-Spec) — produces a design-review report (clash-detection, implementation-path, security-controls, performance-suitability)."
required-inputs:
  - Technical-design document (TDD/Spec)
  - Data-flow diagrams/C4-views
  - Security-control definitions
  - Implementation/deployment-plan
expected-deliverables:
  - Technical design-review report
  - Clash-detection log
  - Implementation go/no-go recommendation
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

## Bulletproofing against Rationalization
To prevent superficial box-ticking masquerading as a Design Review, you MUST:

1. **Mandatory Artifact Grounding:** A Design Review CANNOT be executed against abstract concepts, slideware, or verbal descriptions. You MUST validate against a formalized HLD or LLD.
2. **Explicit Constraint Verification:** Validation MUST force explicit checking of Regulatory (CBUAE Residency, KYC Depth) and NFR boundaries. Silence is failure; compliance must be affirmatively documented.
3. **No Conditional Go-Lives on Critical Path:** If a Design Review surfaces a flaw in data-handling or security postures, you CANNOT issue a "Passed with exception". The review fails.
4. **Accountability Sign-Off:** Each review element MUST have an identified reviewer.

**Violating these rules invalidates the Design Review.**

## Outputs
- **Technical design-review report** — Formal-feedback on the spec.
- **Clash-detection log** — Specific technical-defects to be resolved.
- **Implementation go/no-go recommendation** — Is it time to build?

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
