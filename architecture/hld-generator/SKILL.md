---
name: hld-generator
owner: Solution Architecture
version: 0.1.0
last-reviewed: 2026-08-08
description: "Use when a banking initiative needs a High-Level Design â€” produces an HLD (context, containers, key flows, headline NFRs, risks) at the altitude a sponsor and architecture board can review."
required-inputs:
  - Requirements baseline (/requirements-analysis)
  - Solution option chosen (/solution-options, optional)
  - Current-state context (legacy core, channels, partners)
  - NFR framing (/nfr-checklist or baseline)
expected-deliverables:
  - High-Level Design document (context + containers + key flows + headline NFRs + risks)
  - C4 container-diagram sketch (delegates to /c4-model)
  - Open questions & assumptions carried to the LLD
togaf-phases: [Phase C]
togaf-artifacts: [HLD]
bian-service-domains: [Integration.API]
---

# /hld-generator

## When to apply
Use after requirements are baselined and an option is tentatively chosen, before the detailed Low-Level Design and before the board submission. The HLD is the altitude where the *shape* of the solution is decided â€” not the API contracts. Pairs with `/lld-generator` (which deepens it) and feeds `/architecture-board`.

> TOGAF Phase B target-architecture lives here, *at* Level 1/2. BIAN supplies the capability vocabulary; the HLD says which Service Domains the solution touches.

## Inputs
- **Requirements baseline** â€” from `/requirements-analysis`; especially the regulatory constraints (CBUAE residency, KYC/AML, free-zone cross-border).
- **Chosen solution option** â€” from `/solution-options` (may be tentative; the HLD articulates it).
- **Current-state context** â€” legacy core modules touched, channels, 3rd-party integrations; the HLD reuses, not reimagines.
- **NFR framing** â€” headline NFRs (RTO/RPO, residency, perf targets, audit posture) at the altitude the HLD commits.

## Process
1. **State the context â€” system scope, external actors, the systems it touches.** A C4 context diagram (delegate to `/c4-model`) names the users, the external systems (core banking, UAE Pass/EFR, partners), and the boundary. The HLD must make clear what is *out of scope*.

2. **List the containers â€” deployable units with their tech and responsibility.** Apps (mobile/web/branch), APIs, services, the AI spine components, the event backbone, data stores. Each container gets one line: *what it does*, *its tech*, *who owns it*. Keep the "reuse vs build" verdict visible per container â€” call out which are reused core-banking systems.
   > BIAN lens: where containers map to service domains, tag them.

3. **Sketch the 2â€“4 key flows at altitude.** The journeys that define success â€” onboarding, payment, account-opening, etc. â€” end-to-end across containers. Sequence-level detail belongs to `/lld-generator`; here it's the narrative + a sequence-diagram stub (delegate to `/sequence-diagrams`). Each key flow must surface where it crosses the legacy core and where regulated steps live.

4. **Pin headline NFRs at commitment level.** Availability (RTO/RPO), residency (which data lives where â€” onshore/DIFC/ADGM), performance (latency/throughput targets), audit/logging posture, security baseline. These are the NFRs the HLD *commits*; `/nfr-checklist` later enumerates them.

5. **Surface the reuse-vs-replace verdict per touched component.** Direct from `/gap-analysis`/`/solution-options`. The HLD should show which legacy modules are reused, wrapped, replaced, slimmed â€” no silent big-bang-replace assumptions. Use the strangler-fig / wedge-first posture if modernizing.

6. **Name the major risks & dependencies.** Regulatory risk (incl. the cross-zone SCC obligation if free-zone), vendor lock-in, legacy-core coupling, team capacity. Each risk links to a mitigation or an ADR.

7. **Carry open questions to the LLD.** An HLD that "resolves" everything hides the decisions still pending. The open-questions register is the handoff to `/lld-generator`.

## Bulletproofing against Rationalization
To prevent Greenfield Amnesia, vague NFRs, and LLD creep, you MUST:

1. **Mandatory Altitude Lock:** The HLD MUST NOT contain API endpoints, payload schemas, or database tables. Any proposed HLD diving to Level 3/4 detail is rejected.
2. **Mandatory Quantitative NFRs:** NFRs like "highly available" or "secure" without precise SLA metrics (e.g., "RTO 30m, RPO 0", "99.99% availability") are strictly prohibited.
3. **Mandatory Ownership Map:** Every single container identified MUST have an explicitly declared owner/team.
4. **Mandatory Reuse vs. Replace Declaration:** The document MUST explicitly call out which legacy core modules are reused, wrapped, or retired.
5. **Mandatory Open Questions Register:** You MUST include a non-empty list of open questions to be routed to Low-Level Design (LLD); an HLD that assumes everything is perfectly resolved is a hallucination.

**Violating these rules invalidates the High-Level Design.**
---

## Outputs
- **HLD document** â€” context, containers, key flows, headline NFRs, reuse-vs-replace, major risks & dependencies, the open questions carried to LLD.
- **C4 container-diagram sketch** (via `/c4-model`, rendered by `/archify`).
- **Key-flow sequence stubs** (via `/sequence-diagrams`, rendered by `/archify`).
- **Open-questions register** â€” handoff to `/lld-generator` and the RAID log.

## Related skills
- [lld-generator](../lld-generator/SKILL.md) â€” deepens the HLD into detail.
- [requirements-analysis](../../discovery/requirements-analysis/SKILL.md) â€” supplies the baseline the HLD articulates.
- [nfr-checklist](../nfr-checklist/SKILL.md) â€” takes headline NFRs to completion.
- [c4-model](../c4-model/SKILL.md) â€” the container/context views this HLD embeds.
- [sequence-diagrams](../sequence-diagrams/SKILL.md) â€” the key-flow stubs.
- [deployment-diagrams](../deployment-diagrams/SKILL.md) â€” the topology view, if the HLD commits deployment topology.
- [architecture-board](../../governance/architecture-board/SKILL.md) â€” the forum that reviews this HLD.

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

## Anti-patterns
- **Including low-level implementation details and specific code snippets**
  - **Consequence:** Fast obsolescence of the High-Level Design (HLD) document and developer micro-management.
  - **Correct Approach:** Focus on container boundaries, integration patterns, data schemas, and non-functional requirements.
- **Designing the system without linking to specific NFRs (RTO/RPO)**
  - **Consequence:** Failure to achieve business SLA metrics when disaster recovery is executed in production.
  - **Correct Approach:** Include dedicated sections mapping structural design choices directly to RTO, RPO, and security metrics.
- **Oversimplifying the integration boundary between legacy systems and new cloud systems**
  - **Consequence:** Underestimating sync requirements, resulting in data inconsistency, lag, or API exhaustion.
  - **Correct Approach:** Detail data format mappings, sync/async styles, latency boundaries, and failover pathways for all legacy links.
