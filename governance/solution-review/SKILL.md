---
name: solution-review
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when performing a formal solution-architecture review — produces a review-report (lens-compliance, architectural-fit, integration-risk)."
required-inputs:
  - Solution-design document (TDD/HLD)
  - Business requirements & NFRs
  - Security/Regulatory threat-profile
  - Architectural-landscape context (BIAN/Legacy/Cloud)
expected-deliverables:
  - Formal review-report (verdict-anchored)
  - Architectural-fit assessment
  - Integration/Security-risk log
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
- **Compliance-Blindness** — Analyzing *only* the technical-design (e.g. "Kubernetes-config") while ignoring that the *data-flow* violates CBUAE-data-residency-policy.
- **"The-Integration-Black-Box"** — Reviewing a modern-app design while ignoring the *massive-integration-risk* into the legacy-core-mainframe.
- **Omitting-NFRs** — Reviewing functionality while forgetting to ask: "Does this scale to the 300% peak-load required for Salary-Cycles?"
- **Reviewer-Groupthink** — Not ensuring the review includes representatives from Security, Data-Governance, and Infrastructure, creating a false sense of architectural-soundness.

## Bulletproofing against Rationalization
To prevent broken architectures from being forced into production, you MUST:

1. **Mandatory LLD vs Code Traversal:** A Solution Review doesn't evaluate if the solution "looks okay"; it strictly evaluates if the built code/configuration matches the approved LLD. Implementations that diverge from LLD without an ADR are failed.
2. **NFR Completion Evidence:** You CANNOT accept "it passed testing" as proof for NFRs. Solutions MUST provide the actual performance/load reporting metrics matched against the initial NFR requirements.
3. **Mandatory Security/Compliance Review Gate:** Solutions MUST possess explicit sign-off from InfoSec and Compliance before Solution Review concludes.
4. **Defect Tolerance Limits:** "Go Live with Critical/High defects" is strictly forbidden unless authorized by formal executive risk acceptance.

**Violating these rules invalidates the Solution Review.**

## Outputs
- **Formal review-report (verdict-anchored)** — The "go/no-go" for the design.
- **Architectural-fit assessment** — Evaluation against bank-principles.
- **Integration/Security-risk log** — Specific actions for the design-team.

## Related skills
- [architecture-board](../architecture-board/SKILL.md)
- [design-review](../design-review/SKILL.md)
- [compliance](../../security/compliance/SKILL.md)
