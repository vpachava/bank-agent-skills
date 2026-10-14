---
id: "05"
slug: banking-integration-patterns
title: "Banking integration standards & event patterns"
map: solution-arch-orchestrator/map.md
label: wayfinder:research
type: research
status: closed
assignee: research-agent
blocked_by: []
blocks: ["10","11"]
---

## Question

Gather the integration-grounding that the **integration** and **migration** skills embed — banking-specific. Investigate (verify via web; mark confidence):

1. **ISO 20022** — the messaging standard's role in payments & inter-bank flows; how an `api-design` / `messaging` / `data-sync` skill frames schema design around it for a UAE bank.
2. **Event-driven banking patterns** — Kafka/CorBA-tier event backbones, domain event design, event sourcing vs. CDC, the BIAN event network tie (cross-links ticket 03), and the pitfalls (ordering, idempotency, exactly-once, replay) the `event-driven` skill must embed.
3. **Integration patterns over a legacy core** — API gateway / service mesh / adapter-vs-strangler, sync-vs-async over a core banking system, ETL/SOA/rest-vs-events for the bank's heavy 3rd-party & core integrations.
4. **ETL & data-sync for banking** — CDC, reconciliation, near-real-time sync vs. batch, and the data-integrity pitfalls (reconciliation, duplicate detection) the `etl` / `data-sync` skills embed.
5. **3rd-party / open-banking integration** — the API & security posture for external partners/ fintech integrations that `api-design` + `security-architecture-review` reference.

Capture findings to `solution-arch-orchestrator/research/banking-integration-patterns.md`. Feeds `api-design`, `event-driven`, `messaging`, `data-sync`, `etl`, `integration-patterns`, and `application-migration` (integration-side concerns).

## Resolution

**Resolved 2026-08-07. Findings at `solution-arch-orchestrator/research/banking-integration-patterns.md`.** HIGH-confidence grounding ready to embed: (1) ISO 20022 leg families (`pain.001`→`pacs.008`→`camt.053/054`), UETR as canonical end-to-end id + idempotency key; (2) event-driven — Kafka EOS is within-Kafka only → transactional-outbox + idempotent consumers, partition-key=ordering invariant, DLQ+bounded retry, replay poisons side-effecting consumers, domain-event vs CDC-event distinction; (3) legacy-core — API gateway + Anti-Corruption Layer + Strangler-Fig (never big-bang), sync commands in / CDC-events out, saga+compensations; (4) ETL/data-sync — reconciliation is regulatory non-optional (camt.053/054 vs ledger), money as integer minor units, idempotent UPSERT on business key, land-then-curate; (5) 3rd-party/open-banking — OAuth2+PKCE+FAPI 2.0 + sender-constraining (mTLS-bound/DPoP) + SCA + consent dashboard. Downstream-skill grounding matrix maps each section to its consuming skills.

**⚠️ CAVEAT for builders of tickets 10 & 11 (and any skill citing UAE specifics): web tools failed this session (infrastructure 400/403/404/timeout).** Findings are synthesized from authoritative public knowledge with per-finding confidence + canonical source citations — **nothing fabricated** — but **all UAE-specific items are MEDIUM and must be verified against current CBUAE/primary publications before a checklist ships.** In particular: UAE Aani/AEP ISO 20022 rail, and UAE Open Finance rule text/dates — verify before embedding. Treat the HIGH-confidence standard/tool findings (ISO 20022 structure, Kafka semantics, integration patterns) as embeddable; treat UAE regulatory specifics as draft-pending-verification.
