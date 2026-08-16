---
name: data-sync
owner: Solution Architecture
version: 0.1.0
last-reviewed: 2026-08-09
description: "Use when data must be synchronized between bank systems without a full ETL rebuild — produces a data-sync design (CDC vs event-driven vs dual-write-avoidance, reconciliation, idempotency) keeping the systems honest."
required-inputs:
  - The systems to keep in sync & the data domain
  - Freshness/latency requirement (near-real-time vs eventual)
  - Which system is the system of record for each element
  - Reconciliation gates already in place (if any)
expected-deliverables:
  - Data-sync design (CDC / event / outbox; one-way vs two-way)
  - Reconciliation model (business key, cadence, drift handling)
  - Idempotency + business-key UPSERT model
---

# /data-sync

## When to apply
Use when two (or more) systems must each have a current view of the same data — the core's customer record feeding channels, a master-data feed to services, a real-time ledger snapshot — without a heavyweight nightly ETL. The domain where silent data-drift lives: a sync done badly produces two systems that quietly disagree until reconciliation (or a customer) catches it. Pairs with `/messaging` (transport) and `/etl` (the heavier cousin).

## Inputs
- **Systems & the data domain** — what data, between which systems, one-way or two-way.
- **Freshness/latency** — near-real-time (≤seconds) vs eventual (minutes/hours); this drives CDC vs batch-event vs scheduled sync.
- **System of record per element** — for each field/element, *one* system owns truth; the others hold a copy. Multi-source-of-truth is a design smell, not a feature.
- **Reconciliation gates in place** — any existing recon (camt-style statements vs ledger) and its cadence.

## Process

1. **Designate the system of record per data element, and make copies copies.** Two systems both authoritative for the same element = two values eventually differing. For each element one owns truth; the others hold a derived/cached copy with a clear refresh contract.

2. **Pick the sync mechanism by latency & coupling.** **CDC** (change-data-capture via Debezium-style log mining) for near-real-time mirror of a source's changes — low coupling, the source doesn't even know it's being mirrored. **Event-driven domain events** when the *business fact* of the change should drive consumers (not the raw row change). **Scheduled batch sync** when freshness in minutes/hours suffices and the cost of CDC/event isn't earned. Use the **transactional-outbox** to avoid dual-write when the source must both commit and publish.

3. **Model reconciliation as a design, not an afterthought.** Every sync drifts; reconciliation is how you catch it. Define the **business key** that reconciles (account-id, UETR, customer-id — never a synthetic row id), the **cadence** (nightly vs continuous), and the **drift-handling** (alert + repair + audit-trail). A bank sync without a reconciliation plane is a silent disagreement waiting to surface as a customer complaint.
   > Reconciliation isn't regulatory-only. It's the only way a sync design keeps itself honest over time; without it, drift compounds.

4. **Design idempotent UPSERT on the business key.** The consumer of a sync must be safe to re-process the same change (CDC redelivery, event replay, sync re-run) — so its write is an UPSERT keyed by the business key, not an INSERT. Duplicate sync delivery that produces duplicate rows is the canonical sync defect.

5. **Handle ordering for state-bearing sequences.** A status sequence (pending → authorized → settled) consumed out-of-order makes the consumer's *view* go backwards. Either force ordering by partition key (UETR/account-id) or use a version/sequence-per-record so the consumer takes the "latest known" and rejects old-arriving.

6. **Decide one-way vs two-way honestly.** Two-way sync of the same element across two systems is rarely safe (conflict resolution becomes the system). Most bank syncs are one-way (system of record → copies). If you genuinely need two-way, design the conflict policy explicitly (last-writer-wins is usually wrong for bank data).

7. **Treat money & regulated values with integer-minor-units and provenance.** Money is never a float (rounding errors compound into a reconciliation breach); integers in minor units. Provenance per value — which system authored it, when — so reconciliation disputes resolve to a source, not "both systems disagree, pick one."

## Banking pitfalls
- **Two-way sync of the same element** — conflict resolution becomes the system; prefer one-way system-of-record→copy; if two-way is unavoidable, conflict policy explicit (and last-writer-wins is wrong for regulated data).
- **No reconciliation plane** — silent drift compounds until a customer notices; design the recon from day one, on the business key.
- **Reconciliation on a synthetic row id** — keys that differ across systems (a core PK vs a channel surrogate) can't reconcile; reconcile on the shared business key.
- **Non-idempotent consumer writes** — CDC redelivery / event replay creates duplicate rows; UPSERT-on-business-key, never raw INSERT.
- **Out-of-order status updating backwards** — consumer's view descends (settled→authorized) because a late-arriving event overwrote; version-per-record or partition ordering, take latest-known.
- **Money as float** — rounding drift compounds; integer minor units with explicit scale.
- **Multiple sources of truth for one element** — "the channel and the core both can update balance" = two values eventually; one system of record per element.
- **Provenance absent** — recon disputes resolve to "both disagree, pick arbitrarily"; proveance per value (who/when/why authored) resolves them to a source.

## Bulletproofing against Rationalization
To prevent silent data corruption and residency violations, you MUST:

1. **Mandatory Residency Mapping:** Target migration schemas MUST confirm explicit physical locality aligning with CBUAE (Onshore/DIFC).
2. **Data Consistency Check:** The sync/migration methodology MUST explicitly state whether it is eventually consistent or immediately consistent. Hand-waving consistency is an instant failure.
3. **Rollout Fallback Data Scripting:** You MUST include concrete scripting for reversing the data synchronization back to the legacy state.
4. **Mandatory Idempotency and Rollback:**
   a. Every synchronization action MUST use the business `idempotency-key` (UUID v4) to ensure duplicate avoidance.
   b. Consumers MUST implement a conflict-resolution strategy (first-wins, last-wins, merge).
   c. A formal rollback procedure must be documented for idempotency verification failure.

**Violating these rules invalidates the Data Integration plan.**

## Outputs
- **Data-sync design** — CDC vs event vs batch per domain; one-way vs two-way; system-of-record per element.
- **Reconciliation model** — business key, cadence, drift handling + audit trail.
- **Idempotent-UPSERT + ordering model** — on the business key; take-latest-known via version.

## Related skills
- [messaging](../messaging/SKILL.md) — the transport CDC/events ride on.
- [event-driven](../event-driven/SKILL.md) — the event-model sibling (domain events vs CDC distinction).
- [etl](../etl/SKILL.md) — the heavier-batch sibling.
- [observability](../../devops/observability/SKILL.md) — drift detection + alerting.
- [sre-review](../../devops/sre-review/SKILL.md) — owns the SLO that the freshness latency shapes.
