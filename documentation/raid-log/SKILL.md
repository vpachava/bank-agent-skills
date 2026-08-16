---
name: raid-log
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when maintaining a project RAID log — (Risks, Assumptions, Issues, Dependencies) for banking projects."
required-inputs:
  - List of risks, assumptions, issues, and dependencies
  - Impact assessments and mitigation/owner mapping
expected-deliverables:
  - RAID log artifact
  - Risk-priority heat-map
  - Dependency-blocker trajectory
---

# /raid-log

## When to apply
Use for the continuous lifecycle-management of banking-projects. RAID logs (Risks, Assumptions, Issues, Dependencies) are the primary tool for Banking PMOs to track if a project is going to hit its regulatory milestones or derail due to internal/external blockers.

## Inputs
- **Risks** — Known unknowns (e.g. key dev leaving).
- **Assumptions** — Things we treat as true (e.g. legacy-API will be available).
- **Issues** — Known knowns requiring action (e.g. project budget frozen).
- **Dependencies** — External teams/services we rely on.

## Process
1. **Categorize.** Place items into R, A, I, or D.
2. **Quantify.** For Risks/Issues: Assign Likelihood (1-5) x Impact (1-5) = Severity score.
3. **Cross-Link Dependencies.** All dependency items (D) MUST contain a UUID-based link to the internal repository or external Core-system ticket being depended upon.
4. **Assign Owner/Deadline.** Never have an "unowned" risk or issue in a banking environment.
5. **Mitigation/Resolution Plan.** Map to actual tickets.
6. **Review Rhythm.** Every RAID item must be reviewed weekly in the project-governance-forum.

## Banking pitfalls
- **Turning Risks into "Ghosts"** — Setting a risk (e.g. "Vendor might miss deadline") and then forgetting to track it until it turns into a catastrophic Issue on the morning of deployment.
- **Ignoring Dependency-Deadlines** — Assuming the "Core-Banking Team" will deliver their API by Date X, without a formal signed-dependency-agreement.
- **Assumption-Creep** — Not auditing your "assumptions" when the project-landscape changes (e.g. "We assumed we could use global cloud, but CBUAE-rules-changed").
- **No-PII-in-RAID** — Accidentally putting PII or sensitive-bank-internal-data into a project-RAID that might be visible to 3rd-party-consultants.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of raid-log meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the raid-log process.**

## Outputs
- **RAID log artifact** — Central register.
- **Risk-priority heat-map** — Visual view for leadership.
- **Dependency-blocker trajectory** — Are we unblocking on time?

## Related skills
- [risk-register](../risk-register/SKILL.md)
- [project-charter](../project-charter/SKILL.md)
- [release-readiness](../../devops/release-readiness/SKILL.md)
