---
name: deployment-diagrams
owner: Solution Architecture
version: 0.1.0
last-reviewed: 2026-08-08
description: "Use when a banking solution needs its deployment/topology committed — produces deployment diagrams (via /archify) with regions, HA/DR pairing, landing-zone topology, and the UAE residency perimeter."
required-inputs:
  - Current landing-zone / cloud estate (AWS, Azure, Oracle/private)
  - NFRs: availability (RTO/RPO), residency, scale targets
  - The containers from the HLD (/hld-generator)
  - Residency obligations (UAE: onshore vs DIFC/ADGM)
expected-deliverables:
  - Deployment/topology diagram(s) rendered via /archify
  - Residency-perimeter annotation (onshore / DIFC / ADGM, incl. cross-zone transfer points)
  - HA/DR pairing and data-store placement notes
  - Cloud / landing-zone alignment notes (delegates to /landing-zone-review)
---

# /deployment-diagrams

## When to apply
Use when the deployment shape needs to be committed — the HLD lands topology at altitude, the LLD commits it, and any governance / production-readiness review will ask "where does it run, how is it redundant, where does the data live." Rendering delegates to `/archify`. This skill owns *what* to depict and the banking topology conventions.

## Inputs
- **Current landing-zone / cloud estate** — AWS, Azure, Oracle/private; the subscriptions/accounts, hub-spoke, network segmentation in place (cross-link `/landing-zone-review`).
- **NFRs** — availability (RTO/RPO), residency, scale (latency/throughput) — these drive the topology (paired regions, multi-AZ, data-store placement).
- **Containers from the HLD** — the deployable units this diagram places.
- **Residency obligations** — onshore UAE vs DIFC/ADGM, the CBUAE sectoral in-country-residency rules, the free-zone cross-zone SCC/BCR obligation.

## Process
1. **Choose the abstraction — infrastructure topology, not container layout.** A deployment diagram is where things *run* (regions, zones, clusters, store placement, network) with the containers placed on them. Don't conflate with the C4 container diagram; this is the substrate under it.

2. **Place regions/availability zones per residency rule.** For a UAE bank, onshore region(s) for the CBUAE-residency data; free-zone landing zones for DIFC/ADGM activity if applicable. Mark the **residency perimeter** explicitly as a dotted boundary.
   > Where the cross-zone (onshore ↔ DIFC/ADGM) transfer happens, annotate it with the SCC/BCR implication surfaced by the UAE-compliance research — this is the diagram that either honors or violates that obligation.

3. **Lay the landing-zone topology.** Hub-spoke, management/landing/online-offline subscriptions, network segmentation, the egress/ingress gates. Delegate finer governance review to `/landing-zone-review`; here show the broad topology the HLD/LLD commits to.

4. **Place the HA/DR pairing.** Paired regions or AZs for availability; DR topology (warm/warm-standby/active-active) per the RTO/RPO NFR; the failover runbook reference (cross-link `/dr-review`). Show the data-store replication topology supporting that pairing.

5. **Place data stores with residency & retention.** Which region/zone each store lives in; PII/biometric/payment data residency explicitly; retention marking. Residency on the deployment diagram is what makes a compliance review pass.

6. **Show the multi-cloud seams honestly.** Where AWS meets Oracle/private; where Azure hosts the AI hub; the inter-cloud connection points (peering, egress, the data-sync seams). Bank estates are multi-cloud; hide the seams and the integration design assumes away the hard part.
   > Don't draw a single-cloud diagram of a multi-cloud estate; the inter-cloud seam is where the architectural risk concentrates.

7. **Annotate scale anchors.** Where auto-scaling / fixed capacity / queue-based load leveling sit; the choke points (a single ingress to the legacy core, a real-time payment gateway) marked so the perf review knows where to focus.

8. **Delegate rendering to `/archify`.** Hand it the structured topology input; it returns polished explorable diagrams. This skill owns the *topology + banking conventions*, `/archify` the rendering.

## Bulletproofing against Rationalization
- **No residency perimeter** — a deployment diagram without the onshore/DIFC/ADGM perimeter conceals the cross-border residency obligation; the very review this feeds (production-readiness) will fail it. Mark the perimeter.
- **Single-cloud assumption for a multi-cloud estate** — drawing AWS-only when the estate runs AWS+Azure+Oracle/private hides the inter-cloud seams where migration, latency, and cost risks cluster.
- **HA/DR shown without data-replication** — paired regions drawn as boxes without the replication topology that makes failover real (and without the DR runbook reference) oversells availability.
- **Residency left to "it's all in-region"** — when the estate in fact straddles onshore and a free zone, the residency diagram must show both and the transfer point; "all in-region" is often a lie.
- **Topology without the legacy-core ingress choke point** — the bottleneck for many bank flows is the single ingress to the core; if the diagram hides it, the perf review is blindsided.
- **Conflating with C4** — deployment is the *substrate* (regions/zones/network); C4 is the *software structure* placed on top. Keep them separate but linked (each C4 container placed on a deployment node).
- **Rendering-obsessed** — the pretty topology that misplaces the residency boundary or omits the DR pairing is worse than a rough correct one; own the content.

## Bulletproofing against Rationalization
To prevent abstracted topology masking systemic fragility, you MUST:

1. **Mandatory AZ/Region Explicit Placement:** Every deployed component MUST explicitly exist within a named Region and Availability Zone. Floating components are rejected.
2. **Mandatory Data Residency Perimeter:** The diagram MUST explicitly demarcate CBUAE/Data-Residency bounds (Onshore vs DIFC).
3. **Mandatory Interconnectivity Boundaries:** Subnets, VPC borders, and Firewalls MUST be drawn as explicit boundary contexts for the components they encase.
4. **Mandatory Redundancy Mapping:** HA/DR capabilities MUST be visually represented. If an application is Active/Passive, the Passive zone and replication link must exist on the page.

**Violating these rules invalidates the Deployment Diagram.**

## Outputs
- **Deployment/topology diagram(s)** — rendered by `/archify`.
- **Residency-perimeter annotation** — onshore / DIFC / ADGM zones, cross-zone transfer points with SCC/BCR implication.
- **HA/DR pairing** — regions, replication, failover mode, DR-runbook reference.
- **Data-store placement** — per store, residency + retention.
- **Multi-cloud-seam** + **scale-anchor** notes.

## Related skills
- [/archify](../../../../) — rendering engine.
- [landing-zone-review](../../cloud/landing-zone-review/SKILL.md) — the governance review of the topology this depicts.
- [c4-model](../c4-model/SKILL.md) — the software structure placed on this substrate.
- [hld-generator](../hld-generator/SKILL.md) — commits topology at altitude.
- [lld-generator](../lld-generator/SKILL.md) — commits the detailed topology.
- [dr-review](../../governance/dr-review/SKILL.md) — the DR posture this topology implies.
- [performance-review](../../devops/performance-review/SKILL.md) — reads this for scale anchors and choke points.

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
