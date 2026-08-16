---
name: reference-architecture
owner: Architectural Governance
version: 1.0.0
last-reviewed: 2026-08-15
description: "Use when authoring a reference architecture for a banking domain — produces a BIAN-grounded C4-aligned reference architecture document."
required-inputs:
  - Banking domain scope (BIAN-domain)
  - Architectural constraints & NFRs
  - Selected platform (cross-link to platform-selection)
  - Regulatory-residency context (UAE onshore/freezone)
expected-deliverables:
  - Reference architecture document (HLD)
  - Capability alignment & domain mapping (BIAN-grounded)
  - Diagram set (delegated to /archify)
  - Tradeoff rationale per-pillar
---

# /reference-architecture

## When to apply
Use to establish the authoritative "blueprint" for a specific banking business domain (e.g. Payments, Lending, Customer Onboarding, Savings). Provides a canonical, BIAN-grounded standard that product teams reuse, ensuring consistency, regulatory-compliance (residency/transfer), and architectural parity across the bank.

## Inputs
- **Banking domain scope** — align to BIAN service domains.
- **Constraints/NFRs** — availability/resiliency pattern, residency rule, latency requirements.
- **Platform** — cross-link to the chosen cloud, K8s, Terraform/IaC posture.
- **Regulatory context** — residency (PDPL/CBUAE) + transfer (Freezone SCC/BCR).

## Process
1. **Define the domain context (BIAN grounding).** Map the initiative to BIAN v14.0 service domains. Adopt the "BIAN content, TOGAF-method" approach.
2. **Author the architectural blueprint.** Define the canonical HLD:
   - Functional domains (front-office, core-integration, integration-tier, event-mesh).
   - Component topology (what lives in which Azure/AWS landing zone / OCI/Private-DC location).
   - Integration patterns (API contracts, event-topics, ISO 20022 message flows).
3. **Embed the residency/resilience posture.** Explicitly document:
   - Data residency per-element (payment-data = in-country, analytics-data = in-country etc.).
   - Disaster-recovery strategy (primary ↔ secondary pair per CBUAE expectation).
   - Cross-zone transfer basis (SCC/BCR for freezone data).
4. **Author the Pillar-Tradeoff matrix.** For the major architecture decisions (reliability vs cost vs latency), document why the chosen pattern is the "best-fit" for the bank.
5. **Diagraming.** Use `/c4-model` and `/deployment-diagrams` to produce the standard views (Context, Container, Component, Deployment).
6. **Regulatory-gate check.** Confirm the design satisfies the platform-selection and landing-zone pre-flight gates.

## Banking pitfalls
- **Over-engineering without BIAN-alignment** — inventing banking domains that don't map to industry standard taxonomy (BIAN), leading to poor integration and interoperability.
- **Hyperscaler-native-only blindspot** — assuming it's AWS-native only and ignoring the Oracle-core integration-tax or the OCI-proximity requirements.
- **Compliance-as-afterthought** — architectural blueprints that ignore the CBUAE/PDPL/DIFC/ADGM residency/transfer realities — retrofitting compliance is catastrophic.
- **Ignoring the "Multi-cloud tax"** — presenting a multi-cloud design without accounting for the cost, management overhead, and skill-sprawl of running AWS/Azure/Oracle concurrently.
- **Static blueprint** — Failing to include the evolutionary path for the design (e.g., how the Oracle core is strangled over time).

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of reference-architecture meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the reference-architecture process.**

## Outputs
- **Reference architecture document** — the authoritative HLD.
- **Capability alignment & domain mapping** — tied to BIAN.
- **Diagram set** — via `/archify` delegation.
- **Tradeoff rationale** — per-pillar analysis.

## Related skills
- [platform-selection](../platform-selection/SKILL.md) — where the foundational platform decision flows from.
- [c4-model](../../architecture/c4-model/SKILL.md) — the modeling standard used.
- [deployment-diagrams](../../architecture/deployment-diagrams/SKILL.md) — the deployment view of the RA.
- [compliance](../../security/compliance/SKILL.md) — residency/compliance as the design's constraints.
- [modernization-roadmap](../../modernization/modernization-roadmap/SKILL.md) — how to reach this blueprint from the current state.
