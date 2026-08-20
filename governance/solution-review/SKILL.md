---
name: solution-review
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when performing a formal solution-architecture review â€” produces a review-report (lens-compliance, architectural-fit, integration-risk)."
required-inputs:
  - Solution-design document (TDD/HLD)
  - Business requirements & NFRs
  - Security/Regulatory threat-profile
  - Architectural-landscape context (BIAN/Legacy/Cloud)
expected-deliverables:
  - Formal review-report (verdict-anchored)
  - Architectural-fit assessment
  - Integration/Security-risk log
togaf-phases: [Phase G]
togaf-artifacts: [Compliance Checklist]
bian-service-domains: [Security.Auth]
---

# /solution-review

## When to apply
Use for the formal, peer-reviewed evaluation of a proposed banking solution *before* it moves to design-review or implementation. Ensures the architectural-intent aligns with bank-standards, BIAN-capability-models, and regulatory-fences (e.g. data residency).

## Inputs
- **Solution Document.** The HLD/TDD.
- **Banking-Constraint-Checklist.** The NFRs/Compliance-gates.

## Process
1. **Architectural-Lens-Analysis.** Run the review-lens: (1) Business-Strategy, (2) Security-&-Data-Residency, (3) Operational-Resiliency, (4) Integration-Complexity (Legacy/Modern/Event-Mesh).
2. **Identify-Gaps.** Where does the solution violate banking-principles (e.g. "Too-tightly-coupled" or "Breaches-Data-Sovereignty")?
3. **Draft-Review-Report.** Document findings clearly, including mandatory-revisions.
4. **Issue-Verdict.** Pass, Conditional-Pass, or Fail.

## Bulletproofing
- **Governance Policy:** Enforce [CBUAE Rulebook](governance/policy/regulations.yaml#CBUAE), [PDPL](governance/policy/regulations.yaml#PDPL), and [PCI-DSS](governance/policy/regulations.yaml#PCI-DSS) where applicable.

## Bulletproofing
- **Governance Policy:** Enforce [CBUAE Rulebook](governance/policy/regulations.yaml#CBUAE), [PDPL](governance/policy/regulations.yaml#PDPL), and [PCI-DSS](governance/policy/regulations.yaml#PCI-DSS) where applicable.

## Outputs
- **Formal review-report (verdict-anchored)** â€” The "go/no-go" for the design.
- **Architectural-fit assessment** â€” Evaluation against bank-principles.
- **Integration/Security-risk log** â€” Specific actions for the design-team.

## Related skills
- [architecture-board](../architecture-board/SKILL.md)
- [design-review](../design-review/SKILL.md)
- [compliance](../../security/compliance/SKILL.md)

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

## Bulletproofing
- **Governance Policy:** Enforce [CBUAE Rulebook](governance/policy/regulations.yaml#CBUAE), [PDPL](governance/policy/regulations.yaml#PDPL), and [PCI-DSS](governance/policy/regulations.yaml#PCI-DSS) where applicable.

## Anti-patterns
- **Approving solutions without verifying the core team's capability**
  - **Consequence:** Development teams fail to build or support the solution due to lack of skills.
  - **Correct Approach:** Include resourcing, skills assessment, and training plans in the solution review criteria.
- **Selecting vendor software without analyzing version upgrade strategies**
  - **Consequence:** The bank runs legacy, unsupported versions, incurring high upgrade maintenance costs.
  - **Correct Approach:** Score vendor proposals based on their ease of deployment, backward compatibility, and upgrade support.
- **Failing to align vendor solutions with regional regulations**
  - **Consequence:** Deployment blocks due to data residency violations or audit gaps inside the package.
  - **Correct Approach:** Assess solution architecture for residency isolation and CBUAE compliance first.
