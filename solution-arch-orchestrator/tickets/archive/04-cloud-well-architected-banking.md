---
id: "04"
slug: cloud-well-architected-banking
title: "Cloud Well-Architected × banking + multi-cloud landing zones"
map: solution-arch-orchestrator/map.md
label: wayfinder:research
type: research
status: closed
assignee: research-agent
blocked_by: []
blocks: ["08","10","13"]
---

## Question

Gather the cloud-framework grounding that the **cloud**, **migration**, and **greenfield** skills embed — covering the bank's multi-cloud reality (AWS + Azure + Oracle/private). Investigate (verify via web / vendor docs; mark confidence):

1. **AWS & Azure Well-Architected pillars** — the canonical pillars & review lenses as of ~2026, and the banking-specific overlays (data protection, regulated workload, resilience) that the `aws-review` / `azure-review` / `performance-review` skills step through. Note the GCP Well-Architected posture briefly for `gcp-review` parity.
2. **Landing zones** — CAF/landing-zone anatomy for a regulated bank (management/landing/online-vs-offline subscriptions, hub-spoke, network segmentation, guardrails/policy), AWS vs. Azure shapes, and how UAE data-residency (ticket 02) constrains region selection & landing-zone topology.
3. **Oracle/cloud-native + private-cloud coexistence** — common patterns for running a legacy core alongside cloud-natively; how the cloud skills treat a mixed estate honestly rather than AWS/Azure-only.
4. **Kubernetes & Terraform posture for banking** — the control-plane conventions (multi-tenant cluster topology, secret/secret-mgr, GitOps drift, Terraform module/landing-zone patterns, state & policy guardrails) the `kubernetes` / `terraform` skills embed.
5. **Well-Architected → migration sequencing tie-in** — which landing-zone & pillar decisions a cloud-migration or wave-planning skill must surface early (cross-links ticket 05 and the modernization track).

Capture findings to `solution-arch-orchestrator/research/cloud-well-architected-banking.md`. Feeds `aws-review`, `azure-review`, `gcp-review`, `kubernetes`, `terraform`, `landing-zone-review`, `cloud-migration`, `migration-wave-planning`, and `reference-architecture`.

## Resolution

**Research complete.** Findings synthesized to `solution-arch-orchestrator/research/cloud-well-architected-banking.md`. Covers: AWS/Azure/GCP Well-Architected pillars with banking overlays per UAE-residency; landing-zone anatomy (AWS Control Tower + Azure CAF + Oracle/private); oracle-core + cloud-native coexistence via strangler-fig/CDC/event-mesh; Kubernetes + Terraform posture for banking (state, drift, security, compliant secrets); and landing-zone pre-flight gates for migration sequencing. HIGH-confidence on all load-bearing UAE-residency/region-selection + primary-vendor fact patterns; LOW/MEDIUM flags for specific product-name currency (AWS/LZA/accelerator/region-dates) — re-pin from live docs per the follow-up list before checklist-freezing. Unblocks 08, 10, 13.
