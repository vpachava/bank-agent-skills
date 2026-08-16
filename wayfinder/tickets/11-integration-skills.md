---
id: "11"
slug: integration-skills
title: "Build the integration/ skills (6)"
map: wayfinder/map.md
label: wayfinder:task
type: task
status: closed
assignee: architect
blocked_by: ["01","05"]
blocks: []
---

## Question

Build the `integration/` category — **6 invoke-and-act skills**, each `integration/<name>/SKILL.md` on the locked archetype (ticket 01):

1. **api-design** — design a banking API (REST/Async, versioning, idempotency, contract-first); produce an API design / OpenAPI sketch.
2. **event-driven** — design an event-driven flow (domain events, choreography vs orchestration, Kafka-ish backbone); produce an event design.
3. **messaging** — design messaging (queues/topics, semantics, SLAs) incl. ISO 20022-aware payloads where relevant; produce a messaging design.
4. **data-sync** — design inter-system data sync (CDC, change events, reconciliation); produce a data-sync design.
5. **etl** — design an ETL/ELT pipeline (extract, load, transform, scheduling, lineage) for banking data; produce the ETL design.
6. **integration-patterns** — select & document integration patterns (gateway, adapter, strangler, sync/async, idempotency) for a banking scenario; produce an integration-patterns catalog entry/scoped design.

Each skill: frontmatter + per-skill metadata; embedded banking checklists (core-banking squeeze, heavy 3rd-party, reconciliation, idempotency, ordering, replay); Banking pitfalls; Outputs (named); Related skills cross-linked — `../migration/application-migration`, `../security/security-architecture-review`. Ground ISO 20022 + Kafka/BIAN event patterns (research 05) where they earn it.

Output = 6 skill files in `skills/integration/`. Resolution comment names files, close, Decisions-so-far pointer.

## Resolution

**Resolved 2026-08-09. 6 skills built in `skills/integration/<name>/SKILL.md` (~66–74 lines):**
- `api-design` — capability-resource modeling (NOT core tables); **idempotency-first** (UETR as canonical key) for any side-effecting op; ISO 20022/BIAN Semantic API payload alignment; versioned-from-day-one; regulated-op stronger authz+audit.
- `event-driven` — **domain vs CDC events separated** (never entangled); choreography-vs-orchestration per flow (regulated journeys = orchestration-with-events); **Kafka EOS is within-Kafka only → consumer idempotency mandatory**; partition-keyed on ordering invariant; **transactional outbox for dual-write**; DLQ + bounded retry; replay-tolerance-stated.
- `messaging` — queue-vs-topic by consumer topology; broker-vs-consumer delivery-semantics stated separately (end-to-end is always at-least-once without consumer dedupe); envelope with idempotency/correlation/trace keys; topic-region as compliance decision + cross-zone SCC for PII-bearing topics.
- `data-sync` — **system-of-record per element** (copies are copies, two-way is a smell); reconciliation as the spine (business-key, never synthetic row id); UPSERT-on-business-key for re-run safety; take-latest-known on out-of-order; **money as integer minor units + provenance**.
- `etl` — ETL-vs-ELT by where masking earns (land-raw-then-curate the bank default); **recon gates per stage** (count-only passes while sums drift); **lineage as first-class** (input-hash/logic-version/run-id — regulatory-reporting pipelines non-optional); residency at the landing layer.
- `integration-patterns` — the **picker** (hands off to detail skills); legacy-core seam = façade + ACL + strangler (never big-bang); saga-vs-orchestration; sync-vs-async per operation; **document the rejected alternative + trap avoided** (as instructive as the choice); idempotency+recon at every seam.

**On the archetype:** all 6 follow the locked template; `description` strings use the "Use when… — produces…" house style; cross-links folder-relative.

**Grounding used:** integration research (05) embedded heavily — ISO 20022 leg families (`pain/pacs/camt`) + UETR idempotency key in `api-design`/`messaging`/`etl`; Kafka EOS-within-Kafka-only + outbox + idempotent-consumers + partition-keys in `event-driven`/`messaging`; reconciliation-regulatory-non-optional in `etl`/`data-sync`; money-as-integer-minor-units throughout; FAPI2/sender-constraining referenced for open-banking seams in `api-design`. UAE-compliance (02) — cross-zone SCC at the topic/message/landing-layer residency pitfall.

**Caveat carried (from research 05 ⚠️):** UAE Open Finance rule text/dates and the UAE Aani/AEP ISO 20022 rail are **MEDIUM-verify** — the `api-design` skill cites ISO 20022/FAPI2 as the stable standard and *explicitly flags UAE-rule specifics to verify against current CBUAE publication rather than ship as fact* (named in its pitfalls + the standards-alignment note). Built accordingly.
