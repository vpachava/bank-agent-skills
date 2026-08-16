---
name: roadmap
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when creating a delivery roadmap for a banking initiative — produces a roadmap (phases, milestones, dependencies, banking gates) grounded in the modernization-roadmap."
required-inputs:
  - Banking initiative goals & scope
  - Deliverable dependencies
  - Regulatory release gating requirements (e.g. CBUAE/DIFC/ADGM)
  - Business-value/customer-impact phasing
expected-deliverables:
  - Delivery roadmap document
  - Milestone & dependency map
  - Regulatory-gating timeline
---

# /roadmap

## When to apply
Use to define the delivery trajectory for complex banking initiatives, ensuring that phases, dependencies, and regulatory gates are sequenced logically. Bridges the high-level business vision with the actual delivery pipeline, forcing explicit acknowledgement of banking constraints (regulatory approval, security gates) as first-class milestones.

## Inputs
- **Goals & Scope** — business value / customer impact.
- **Dependencies** — technical, cross-team, vendor-integration.
- **Release gating** — what approvals are needed? (e.g. CBUAE/DIFC/ADGM compliance-gates, platform-security gate, architecture-review board).
- **Phasing** — functional / value-based prioritization.

## Process
1. **Define the phases (Value Horizons).** Map milestones to value/impact goals: e.g. "Core-modernization Foundation", "Payments- modernization", "Mobile-UX parity", "AI-native features".
2. **Anchor with banking gates.** Insert the mandatory regulatory and security gates as milestones:
   - Compliance review (e.g. CBUAE compliance / DIFC notification).
   - Security-architecture-review verdict before go-live.
   - Integration-gate approvals (oracle-core connectivity).
   - Infrastructure/Landing-zone readiness gate.
3. **Map dependencies.** Sequence phases according to strict technical/regulatory constraints, ensuring the platform foundation is live *before* functional applications ship.
4. **Define milestones.** Specific outcomes (artifacts/go-live) per phase.
5. **Draft the delivery roadmap.** Visualize the sequence (timeline, releases, and the regulating gates that bound them).

## Banking pitfalls
- **Regulatory-gating invisibility** — treating compliance reviews as things that happen "concurrently" (or late in the process) rather than as hard blocking milestones that can push go-live dates significantly if gates fail.
- **Ignoring the foundation-dependency** — planning application-feature releases before the platform landing-zone / identity-fabric is ready.
- **"All-at-once" delivery** — attempting a massive transformation instead of the `modernization-roadmap` "wedge-first / strangler-fig" sequencing.
- **Regulatory debt accumulation** — treating "we'll fix the compliance gap in the next phase" as a valid milestone, rather than declaring it as a **Residual Risk** in the RAAD-log and risk-register.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of roadmap meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the roadmap process.**

## Outputs
- **Delivery roadmap document** — the phased delivery plan, including banking-specific gates.
- **Milestone & dependency map** — visualizing the sequencing and blockages.
- **Regulatory-gating timeline** — dedicated view showing the regulatory approval points required for the initiative.

## Related skills
- [modernization-roadmap](../../modernization/modernization-roadmap/SKILL.md) — where this roadmap inherits its sequencing context.
- [security-architecture-review](../../security/security-architecture-review/SKILL.md) — the capstone gate this roadmap tracks.
- [production-readiness](../../governance/production-readiness/SKILL.md) — the milestone this roadmap ultimately targets.
