---
name: design-document
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when drafting a technical design document (TDD/Design-Spec) for a banking solution â€” produces a design-spec (architecture, data-flow, integration, security)."
required-inputs:
  - Functional & non-functional requirements
  - Technical-stack & integration patterns
  - Security/Compliance/PII constraints
  - Performance/Scalability targets
expected-deliverables:
  - Technical design-document
  - Data-flow diagram (C4-model)
  - Security/Compliance assessment-view
togaf-phases: [Phase A]
togaf-artifacts: [Architecture Vision]
bian-service-domains: [Customer Account.Origination]
---

# /design-document

## When to apply
Use for the formal, peer-reviewed technical-specification of a solution. In a banking-architecture practice, this document replaces "informal-diagrams-on-whiteboards." It is the canonical source for what is being built, how it is secured, and how it complies with policy.

## Inputs
- **Functional Requirements** â€” What does it do?
- **NFRs** â€” How fast/reliable/secure must it be?
- **Integration Points** â€” What legacy/external-API does it talk to?

## Process
1. **Architecture/Component-Model.** Use C4-modelling (Context, Container, Component).
2. **Data-Flow.** Document every regulated-data movement (PII/Card/Trade-data).
3. **Security/Compliance-By-Design.** Explicit security-controls.
4. **Integration-Pattern.** Sync vs Async (Event-driven)? Idempotency-handling?
5. **Architectural-Review.** Formal sign-off by Architecture-Board.

## Banking pitfalls
- **Diagrams-without-Flow** â€” Drawing boxes (components) without documenting the data-payload or the security-attributes of the connections.
- **Ignoring-Legacy-Interfaces** â€” Designing elegant APIs in the new-app without defining *how* they map to the 30-year-old mainframe databases.
- **Security-as-an-afterthought** â€” Designing the data-flow and only *then* thinking about encryption and PII-masking, forcing a total architectural-redesign.
- **NFR-omission** â€” Designing a high-throughput payment-component without defining the latency-NFRs, leaving the system unusable at peak-load.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of design-document meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the design-document process.**

## Outputs
- **Technical design-document** â€” The formal TDD (Template-aligned).
- **Data-flow diagram (C4-model)** â€” The visual-truth of data-movement.
- **Security/Compliance assessment-view** â€” Identified security-controls.

## Related skills
- [hld-generator](../../architecture/hld-generator/SKILL.md)
- [security-architecture-review](../../security/security-architecture-review/SKILL.md)
- [nfr-checklist](../../architecture/nfr-checklist/SKILL.md)


### Banking Context & Examples

#### (1) Credit Card Onboarding Example
**Scenario:** Drafting a technical design document (TDD) for new credit card issuance.
- **Architecture Lens Check:** Data-flow diagram must explicitly depict `AECB` request/response payloads with PII-masking controls and residency-compliant data transit.
- **Sample Outcome:** "C4 Model (Container): Origination-Service communicates pii-data via secure, TLS-encrypted API to AECB-gateway; logs specifically exclude sensitive-PII as per CBUAE."
- **Common Pitfall:** Drawing data flows to `AECB` without noting the transit security or the necessity of clearing PII from logs, leading to immediate compliance failure.

#### (2) Customer Profile Management Example
**Scenario:** TDD for a customer dashboard cross-zone update service.
- **Architecture Lens Check:** Defining data-sync patterns for profile changes, with explicit `PDPL` data-residency compliance checks at the data-layer/persistence boundary.
- **Sample Outcome:** "Design Component: Profile-Storage-Service enforces hard-boundary at data layer; partition residency-restricted data into isolated UAE-resident database schemas."
- **Common Pitfall:** Ignoring the persistence boundary (database schema) in the design doc, allowing profile data to be replicated blindly across data centers, which violates PDPL data-residency rules.

#### (3) Lending/Loans Onboarding Example
**Scenario:** TDD for Sharia-compliant loan workflow engine.
- **Architecture Lens Check:** Detailing the `Sharia-Certification-Gate` within the automated loan origination workflow, modeling it as a deterministic gate in the C4 model.
- **Sample Outcome:** "Integration Pattern: Workflow transitions paused at `Sharia-Cert` gate, requiring non-repudiable biometric-signature to resume."
- **Common Pitfall:** Modeling Sharia certification as a 'soft-gate' (optional) or 'notification-task' (event-driven) rather than a deterministic business-rule gate, which fails the audit check for Sharia compliance.
### Regulatory References
1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/
2. **PDPL:** Personal Data Protection Law (Federal Decree-Law No. 45 of 2021)
3. **CBUAE Cybersecurity Framework:** Domain 1: Governance & Risk Management

## Anti-patterns
- **Documenting low-level implementation details that drift daily**
  - **Consequence:** High maintenance overhead; developers ignore the design doc because it is always out of date.
  - **Correct Approach:** Focus the design document on boundaries, interface contracts, data schemas, and key design patterns.
- **Neglecting to include security and regulatory compliance sections**
  - **Consequence:** Security flaws are discovered during production reviews, forcing complete code redesigns.
  - **Correct Approach:** Dedicate specific sections to data encryption at rest/in transit, IAM controls, and data localization compliance.
- **Omitting disaster recovery, backup, and failover design details**
  - **Consequence:** System outages occur without clear processes to restore database and service instances.
  - **Correct Approach:** Detail recovery steps, define RTO/RPO limits, and describe database backup policies explicitly.
