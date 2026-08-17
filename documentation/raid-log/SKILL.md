---
name: raid-log
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when maintaining a project RAID log â€” (Risks, Assumptions, Issues, Dependencies) for banking projects."
required-inputs:
  - List of risks, assumptions, issues, and dependencies
  - Impact assessments and mitigation/owner mapping
expected-deliverables:
  - RAID log artifact
  - Risk-priority heat-map
  - Dependency-blocker trajectory
togaf-phases: [Phase A]
togaf-artifacts: [Architecture Vision]
bian-service-domains: [Customer Account.Origination]
---

# /raid-log

## When to apply
Use for the continuous lifecycle-management of banking-projects. RAID logs (Risks, Assumptions, Issues, Dependencies) are the primary tool for Banking PMOs to track if a project is going to hit its regulatory milestones or derail due to internal/external blockers.

## Inputs
- **Risks** â€” Known unknowns (e.g. key dev leaving).
- **Assumptions** â€” Things we treat as true (e.g. legacy-API will be available).
- **Issues** â€” Known knowns requiring action (e.g. project budget frozen).
- **Dependencies** â€” External teams/services we rely on.

## Process
1. **Categorize.** Place items into R, A, I, or D.
2. **Quantify.** For Risks/Issues: Assign Likelihood (1-5) x Impact (1-5) = Severity score.
3. **Cross-Link Dependencies.** All dependency items (D) MUST contain a UUID-based link to the internal repository or external Core-system ticket being depended upon.
4. **Assign Owner/Deadline.** Never have an "unowned" risk or issue in a banking environment.
5. **Mitigation/Resolution Plan.** Map to actual tickets.
6. **Review Rhythm.** Every RAID item must be reviewed weekly in the project-governance-forum.

## Banking pitfalls
- **Turning Risks into "Ghosts"** â€” Setting a risk (e.g. "Vendor might miss deadline") and then forgetting to track it until it turns into a catastrophic Issue on the morning of deployment.
- **Ignoring Dependency-Deadlines** â€” Assuming the "Core-Banking Team" will deliver their API by Date X, without a formal signed-dependency-agreement.
- **Assumption-Creep** â€” Not auditing your "assumptions" when the project-landscape changes (e.g. "We assumed we could use global cloud, but CBUAE-rules-changed").
- **No-PII-in-RAID** â€” Accidentally putting PII or sensitive-bank-internal-data into a project-RAID that might be visible to 3rd-party-consultants.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of raid-log meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the raid-log process.**

## Outputs
- **RAID log artifact** â€” Central register.
- **Risk-priority heat-map** â€” Visual view for leadership.
- **Dependency-blocker trajectory** â€” Are we unblocking on time?

## Related skills
- [risk-register](../risk-register/SKILL.md)
- [project-charter](../project-charter/SKILL.md)
- [release-readiness](../../devops/release-readiness/SKILL.md)


### Banking Context & Examples

#### (1) Credit Card Onboarding Example
**Scenario:** RAID tracking for a digital credit card issuance project.
- **Architecture Lens Check:** High-severity risk if `AECB` connectivity API is not validated by the agreed-upon regulatory deadline.
- **Sample Outcome:** "Risk [R-001]: Failure to meet AECB reporting integration deadline. Impact: 5. Residual Risk: High. Mitigation: Proactive vendor engagement for AECB API schema validation."
- **Common Pitfall:** Listing `AECB` integration as an 'Assumption' (that it will be ready) instead of tracking it as a high-risk 'Dependency'.

#### (2) Customer Profile Management Example
**Scenario:** RAID entry for cross-zone customer data management.
- **Architecture Lens Check:** Risk of non-compliance with `PDPL` data residency during cross-border dashboard updates.
- **Sample Outcome:** "Issue [I-005]: Unclear data-residency mapping for mobile-dashboard accessed from overseas. Resolution: Immediate review via architecture board for temporary PII masking solution."
- **Common Pitfall:** Treating data residency compliance as an 'Assumption' rather than an 'Issue' that requires immediate mitigation, leading to surprise regulatory non-compliance.

#### (3) Lending/Loans Onboarding Example
**Scenario:** RAID tracking for Sharia-compliant product workflow.
- **Architecture Lens Check:** Dependency on `Internal Sharia Governance Board` sign-off for product architecture updates.
- **Sample Outcome:** "Dependency [D-002]: Sign-off from Sharia Board on product structure. Blocker: Workflow remains uncertified. Owner: Product Compliance lead."
- **Common Pitfall:** Failing to link the Sharia Board sign-off as a `Critical Dependency`, thereby failing to realize the project cannot go to production without it.
### Regulatory References
1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/
2. **PDPL:** Personal Data Protection Law (Federal Decree-Law No. 45 of 2021)
3. **CBUAE Cybersecurity Framework:** Domain 1: Governance & Risk Management

## Anti-patterns
- **Treating the RAID log as static documentation to be updated before meetings**
  - **Consequence:** Issues remain unresolved, risks escalate, and dependencies dry up.
  - **Correct Approach:** Keep the RAID document active, updating status, owner updates, and milestones continuously.
- **Documenting risks and issues without specific mitigation plans or owners**
  - **Consequence:** Risks inevitably become actual issues, and issues linger without resolution.
  - **Correct Approach:** Assign a single owner to each entry and record actionable mitigation steps with clear target dates.
- **Closing entries without capturing lessons learned or post-mortems**
  - **Consequence:** Teams repeat the same mistakes in subsequent sprints and phases.
  - **Correct Approach:** Record a summary of why the risk was closed, what mitigated it, and what needs to be changed next.
