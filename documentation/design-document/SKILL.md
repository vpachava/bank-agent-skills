---
name: design-document
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when drafting a technical design document (TDD/Design-Spec) for a banking solution — produces a design-spec (architecture, data-flow, integration, security)."
required-inputs:
  - Functional & non-functional requirements
  - Technical-stack & integration patterns
  - Security/Compliance/PII constraints
  - Performance/Scalability targets
expected-deliverables:
  - Technical design-document
  - Data-flow diagram (C4-model)
  - Security/Compliance assessment-view
---

# /design-document

## When to apply
Use for the formal, peer-reviewed technical-specification of a solution. In a banking-architecture practice, this document replaces "informal-diagrams-on-whiteboards." It is the canonical source for what is being built, how it is secured, and how it complies with policy.

## Inputs
- **Functional Requirements** — What does it do?
- **NFRs** — How fast/reliable/secure must it be?
- **Integration Points** — What legacy/external-API does it talk to?

## Process
1. **Architecture/Component-Model.** Use C4-modelling (Context, Container, Component).
2. **Data-Flow.** Document every regulated-data movement (PII/Card/Trade-data).
3. **Security/Compliance-By-Design.** Explicit security-controls.
4. **Integration-Pattern.** Sync vs Async (Event-driven)? Idempotency-handling?
5. **Architectural-Review.** Formal sign-off by Architecture-Board.

## Banking pitfalls
- **Diagrams-without-Flow** — Drawing boxes (components) without documenting the data-payload or the security-attributes of the connections.
- **Ignoring-Legacy-Interfaces** — Designing elegant APIs in the new-app without defining *how* they map to the 30-year-old mainframe databases.
- **Security-as-an-afterthought** — Designing the data-flow and only *then* thinking about encryption and PII-masking, forcing a total architectural-redesign.
- **NFR-omission** — Designing a high-throughput payment-component without defining the latency-NFRs, leaving the system unusable at peak-load.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of design-document meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the design-document process.**

## Outputs
- **Technical design-document** — The formal TDD (Template-aligned).
- **Data-flow diagram (C4-model)** — The visual-truth of data-movement.
- **Security/Compliance assessment-view** — Identified security-controls.

## Related skills
- [hld-generator](../../architecture/hld-generator/SKILL.md)
- [security-architecture-review](../../security/security-architecture-review/SKILL.md)
- [nfr-checklist](../../architecture/nfr-checklist/SKILL.md)
