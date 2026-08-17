---
name: c4-model
owner: Solution Architecture
version: 0.1.0
last-reviewed: 2026-08-08
description: "Use when a banking solution needs visual structure â€” produces the C4 views (context/container/component) as explorable diagrams via /archify, banking-conventions applied (legacy-core band, residency perimeter, regulated gates)."
required-inputs:
  - System or component to model
  - Known external actors & systems (core, channels, partners, UAE identity fabric)
  - Residency / trust-boundary constraints
  - Desired C4 level(s): context, container, component, (code)
expected-deliverables:
  - C4 context diagram
  - C4 container diagram (and component, if requested)
  - Banking annotations: legacy-core band, residency perimeter, regulated-gate markers
togaf-phases: [Phase C]
togaf-artifacts: [HLD]
bian-service-domains: [Integration.API]
---

# /c4-model

## When to apply
Use whenever you need *visual* structure â€” to anchor an HLD, brief a workshop, or feed a design review. C4 (Context, Container, Component, Code) is the house diagram model; it zooms from "who interacts with this" to "what's inside a container." Rendering is delegated to `/archify` for polished explorable HTML/SVG; this skill owns *what* to draw and the banking conventions per level.

## Inputs
- **System/component to model.**
- **External actors & systems** â€” customers, staff, branch tablet; core banking, channels, 3rd parties (UAE Pass/EFR/UAEKYC, payment rails, credit bureau, partner fintechs).
- **Residency / trust-boundary constraints** â€” onshore vs DIFC/ADGM, the CBUAE-regulated perimeter, the free-zone cross-zone transfer points.
- **Desired C4 levels.**

## Process
1. **Pick the level(s) the audience needs.** Sponsor/board â†’ Context. Engineering â†’ Container/Component. Don't over-produce; context alone often suffices for a workshop. C4 is two-levels-deep on demand, not all-four-every-time.

2. **Level 1 â€” Context.** System in the center; external actors (people, systems) around it; one-line relationships. <20 boxes â€” if more, the boundary is wrong. This is the diagram the sponsor reads first.

3. **Level 2 â€” Container.** Decompose into deployable units (apps, APIs, services, event backbone, data stores). Each: name, tech, responsibility, who owns it. Mark reused legacy-core containers distinctly from new ones (reuse-vs-build band).
   > Banking convention: shaded band for the **legacy core** so the reuse footpring is visible at a glance; in an AI-native solution a band for the **AI spine** (orchestrator/agents/RAG/memory/policy) too.

4. **Level 3 â€” Component (optional, on demand).** Inside a container, decompose to components with responsibilities and dependencies. Used in LLD; usually skip for board-level presentations.

5. **Level 4 â€” Code (rarely).** Classes/packages â€” almost never drawn; the model goes this deep only for a specific component of acute complexity.

6. **Apply banking annotations across levels.**
   - **Residency perimeter** â€” a dotted enclosure marking onshore vs DIFC/ADGM data zones; annotate cross-zone flows with the SCC/BCR implication.
   - **Regulated gates** â€” mark deterministic KYC / risk / AML / issuance steps on the flows (a small gate glyph).
   - **Trust boundaries** â€” internal / partner / public / CBUAE-regulated, as the security skills need.
   - **Legacy-core band** & **reuse-vs-build verdict** â€” so the diagram tells the reuse story, not just the greenfield story.

7. **Delegate rendering to `/archify`.** Hand it the structured diagram input (plain-language requirements or pasted Mermaid) and the banking annotations; it returns polished explorable HTML (light/dark, PNG/JPEG/SVG export). Keep the *content* of this skill, not the rendering.

8. **Keep annotations honest about selective depth.** If a BIAN service domain is decomposed only Areaâ†’Domain, annotate at that depth; don't imply Service-Domain granularity that doesn't exist (cross-links the BIAN skill).

## Bulletproofing against Rationalization
To prevent unreadable diagrams and the omission of critical banking context, you MUST:

1. **Strict Node Limits:** A Context diagram MUST NOT exceed 20 boxes. If the architecture exceeds this, you must collapse systems into broader domains. Overwhelming diagrams are rejected.
2. **Mandatory Banking Annotations:** Every C4 diagram MUST explicitly mark the legacy-core band (reuse vs. build) and the residency perimeter (onshore vs. DIFC/ADGM). Omitting these hides regulatory exposure.
3. **Mandatory Regulated Gates:** Any flow touching KYC, AML, credit checks, or issuance MUST feature a regulated gate marker.
4. **Level-Appropriateness:** Never generate a Component or Code (Level 3/4) diagram unless explicitly requested for Low-Level Design (LLD). Default to Context/Container for all initial architectures.

**Violating these rules invalidates the C4 model for banking governance.**
---

## Outputs
- **C4 context diagram** â€” rendered by `/archify`, with banking annotations.
- **C4 container diagram** â€” with legacy-core & AI-spine bands, ownership, reuse-vs-build.
- **C4 component diagram** (optional, on demand) â€” for LLD depth.
- **Banking annotations applied** â€” residency perimeter, regulated gates, trust boundaries, legacy-core band.

## Related skills
- [/archify](../../../../) â€” rendering engine (invoked from the Process step).
- [hld-generator](../hld-generator/SKILL.md) â€” embeds the context + container views.
- [lld-generator](../lld-generator/SKILL.md) â€” embeds the component view.
- [deployment-diagrams](../deployment-diagrams/SKILL.md) â€” the deployment/topology companion view.
- [sequence-diagrams](../sequence-diagrams/SKILL.md) â€” the flow-behavior companion view.
- [business-capability-map](../../discovery/business-capability-map/SKILL.md) â€” the capability structure the context/container often aligns to.

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


