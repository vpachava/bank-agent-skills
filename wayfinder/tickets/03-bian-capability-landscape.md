---
id: "03"
slug: bian-capability-landscape
title: "BIAN service-domain & capability landscape for retail banking"
map: wayfinder/map.md
label: wayfinder:research
type: research
status: closed
assignee: research-agent
blocked_by: []
blocks: ["06","07","08"]
---

## Question

Gather the BIAN grounding that the **discovery**, **architecture**, and **greenfield** skills embed — banking-specific, not generic. Investigate (verify via web / BIAN published material; mark confidence; do not invent service-domain IDs):

1. **BIAN Service Landscape / service-domain model** — the canonical capability decomposition for a retail bank; how it maps a bank's business domains to service domains. Enough to ground a `business-capability-map` and `reference-architecture` skill that produces BIAN-aligned artifacts.
2. **BIAN service-domain / interaction model** — how domains expose service operations & events; how this feeds `api-design`, `event-driven`, and `integration-patterns` framing (cross-links ticket 05).
3. **BIAN vs. other reference frames** — where TOGAF capability analysis and BIAN service domains overlap vs. differ, so architecture skills cite the right frame for the right job.
4. **BIAN adoption reality** — typical fidelity banks actually implement (full service-domain decomposition vs. selective), to keep skills pragmatic, not aspirational.

Capture findings to `wayfinder/research/bian-capability-landscape.md`. Feeds `business-capability-map`, `gap-analysis`, `solution-options`, `hld-generator`, `reference-architecture`, and the `architecture-review` BIAN lens.

## Resolution

**Resolved 2026-08-07. Findings at `wayfinder/research/bian-capability-landscape.md`.** Reliable, **HIGH-confidence (primary-verified this session via WebFetch on BIAN.org + Wikipedia's BIAN-metamodel article)**: the 3-level metamodel (Business Area → Business Domain → Service Domain → Service Operation); Service Landscape **v14.0 current** ("AI-Ready Banking Architecture"); **~322 service domains / ~5,000 service definitions / ~250 Semantic APIs**; v14.0 pruned Service Operations + added an **Insurance** area + reorganized the Payment Area; **BIAN↔ISO 20022** metamodel alignment; **IFX Forum** = operational implementation; partners include **The Open Group (TOGAF)**. Interaction model: a Service Domain owns one business object, exposes Service Operations + ~250 OpenAPI Semantic APIs, sync request/response + pub/sub events, payload aligned via IFX Business Message Spec + ISO 20022 families (cross-links ticket 05). **BIAN vs TOGAF rule for skills:** TOGAF = industry-agnostic EA *method* (ADM); BIAN = banking-specific capability *catalogue* → "TOGAF for the method, BIAN for the content" (e.g. `gap-analysis` runs the TOGAF method on a BIAN map). **Adoption reality:** banks run **selective**, not full-322-domain, decomposition (BIAN's own Coreless Banking 1.0 piloted only three areas: consumer payments, customer offers, consumer loans) → keep deliverables pragmatic: cap at Area→Domain→Service Domain depth, score fit-gap not "BIAN compliance," sequence Payments-first (ISO 20022 + UAE Aani rail = live proof point), require vendors to cite specific Service Domains + Semantic API versions. Per-skill checklist blocks (§6) embedded for every consuming skill; open-verifications (§7) listed.

**Confidence note:** structure/counts/version/partners are HIGH + primary-verified. **MEDIUM** (behind the Portal login — verify before freezing a checklist): exact v14.0 post-prune operation taxonomy, any post-4.0 Coreless Banking wave, a specific UAE bank's actual current BIAN exposure via its core package. **Service-domain IDs were not invented.**

**Unblocks** build tickets **06 (discovery)**, **07 (architecture)**, and **08 (greenfield)** on the BIAN axis.
