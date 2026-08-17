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

## Bulletproofing against Rationalization
- **Compliance-Blindness** â€” Analyzing *only* the technical-design (e.g. "Kubernetes-config") while ignoring that the *data-flow* violates CBUAE-data-residency-policy.
- **"The-Integration-Black-Box"** â€” Reviewing a modern-app design while ignoring the *massive-integration-risk* into the legacy-core-mainframe.
- **Omitting-NFRs** â€” Reviewing functionality while forgetting to ask: "Does this scale to the 300% peak-load required for Salary-Cycles?"
- **Reviewer-Groupthink** â€” Not ensuring the review includes representatives from Security, Data-Governance, and Infrastructure, creating a false sense of architectural-soundness.

## Bulletproofing against Rationalization
To prevent broken architectures from being forced into production, you MUST:

1. **Mandatory LLD vs Code Traversal:** A Solution Review doesn't evaluate if the solution "looks okay"; it strictly evaluates if the built code/configuration matches the approved LLD. Implementations that diverge from LLD without an ADR are failed.
2. **NFR Completion Evidence:** You CANNOT accept "it passed testing" as proof for NFRs. Solutions MUST provide the actual performance/load reporting metrics matched against the initial NFR requirements.
3. **Mandatory Security/Compliance Review Gate:** Solutions MUST possess explicit sign-off from InfoSec and Compliance before Solution Review concludes.
4. **Defect Tolerance Limits:** "Go Live with Critical/High defects" is strictly forbidden unless authorized by formal executive risk acceptance.

**Violating these rules invalidates the Solution Review.**

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

### Regulatory References
1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/
2. **PDPL:** Personal Data Protection Law (Federal Decree-Law No. 45 of 2021)
3. **CBUAE Cybersecurity Framework:** Domain 1: Governance & Risk Management


