---
name: data-sync
owner: Solution Architecture
version: 0.1.0
last-reviewed: 2026-08-09
description: "Use when data must be synchronized between bank systems without a full ETL rebuild â€” produces a data-sync design (CDC vs event-driven vs dual-write-avoidance, reconciliation, idempotency) keeping the systems honest."
required-inputs:
  - The systems to keep in sync & the data domain
  - Freshness/latency requirement (near-real-time vs eventual)
  - Which system is the system of record for each element
  - Reconciliation gates already in place (if any)
expected-deliverables:
  - Data-sync design (CDC / event / outbox; one-way vs two-way)
  - Reconciliation model (business key, cadence, drift handling)
  - Idempotency + business-key UPSERT model
togaf-phases: [Phase C]
togaf-artifacts: [HLD]
bian-service-domains: [Integration.API]
---

# /data-sync

## When to apply
Use when two (or more) systems must each have a current view of the same data â€” the core's customer record feeding channels, a master-data feed to services, a real-time ledger snapshot â€” without a heavyweight nightly ETL. The domain where silent data-drift lives: a sync done badly produces two systems that quietly disagree until reconciliation (or a customer) catches it. Pairs with `/messaging` (transport) and `/etl` (the heavier cousin).

## Inputs
- **Systems & the data domain** â€” what data, between which systems, one-way or two-way.
- **Freshness/latency** â€” near-real-time (â‰¤seconds) vs eventual (minutes/hours); this drives CDC vs batch-event vs scheduled sync.
- **System of record per element** â€” for each field/element, *one* system owns truth; the others hold a copy. Multi-source-of-truth is a design smell, not a feature.
- **Reconciliation gates in place** â€” any existing recon (camt-style statements vs ledger) and its cadence.

## Process

1. **Designate the system of record per data element, and make copies copies.** Two systems both authoritative for the same element = two values eventually differing. For each element one owns truth; the others hold a derived/cached copy with a clear refresh contract.

2. **Pick the sync mechanism by latency & coupling.** **CDC** (change-data-capture via Debezium-style log mining) for near-real-time mirror of a source's changes â€” low coupling, the source doesn't even know it's being mirrored. **Event-driven domain events** when the *business fact* of the change should drive consumers (not the raw row change). **Scheduled batch sync** when freshness in minutes/hours suffices and the cost of CDC/event isn't earned. Use the **transactional-outbox** to avoid dual-write when the source must both commit and publish.

3. **Model reconciliation as a design, not an afterthought.** Every sync drifts; reconciliation is how you catch it. Define the **business key** that reconciles (account-id, UETR, customer-id â€” never a synthetic row id), the **cadence** (nightly vs continuous), and the **drift-handling** (alert + repair + audit-trail). A bank sync without a reconciliation plane is a silent disagreement waiting to surface as a customer complaint.
   > Reconciliation isn't regulatory-only. It's the only way a sync design keeps itself honest over time; without it, drift compounds.

4. **Design idempotent UPSERT on the business key.** The consumer of a sync must be safe to re-process the same change (CDC redelivery, event replay, sync re-run) â€” so its write is an UPSERT keyed by the business key, not an INSERT. Duplicate sync delivery that produces duplicate rows is the canonical sync defect.

5. **Handle ordering for state-bearing sequences.** A status sequence (pending â†’ authorized â†’ settled) consumed out-of-order makes the consumer's *view* go backwards. Either force ordering by partition key (UETR/account-id) or use a version/sequence-per-record so the consumer takes the "latest known" and rejects old-arriving.

6. **Decide one-way vs two-way honestly.** Two-way sync of the same element across two systems is rarely safe (conflict resolution becomes the system). Most bank syncs are one-way (system of record â†’ copies). If you genuinely need two-way, design the conflict policy explicitly (last-writer-wins is usually wrong for bank data).

7. **Treat money & regulated values with integer-minor-units and provenance.** Money is never a float (rounding errors compound into a reconciliation breach); integers in minor units. Provenance per value â€” which system authored it, when â€” so reconciliation disputes resolve to a source, not "both systems disagree, pick one."

## Banking pitfalls
- **Two-way sync of the same element** â€” conflict resolution becomes the system; prefer one-way system-of-recordâ†’copy; if two-way is unavoidable, conflict policy explicit (and last-writer-wins is wrong for regulated data).
- **No reconciliation plane** â€” silent drift compounds until a customer notices; design the recon from day one, on the business key.
- **Reconciliation on a synthetic row id** â€” keys that differ across systems (a core PK vs a channel surrogate) can't reconcile; reconcile on the shared business key.
- **Non-idempotent consumer writes** â€” CDC redelivery / event replay creates duplicate rows; UPSERT-on-business-key, never raw INSERT.
- **Out-of-order status updating backwards** â€” consumer's view descends (settledâ†’authorized) because a late-arriving event overwrote; version-per-record or partition ordering, take latest-known.
- **Money as float** â€” rounding drift compounds; integer minor units with explicit scale.
- **Multiple sources of truth for one element** â€” "the channel and the core both can update balance" = two values eventually; one system of record per element.
- **Provenance absent** â€” recon disputes resolve to "both disagree, pick arbitrarily"; proveance per value (who/when/why authored) resolves them to a source.

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
- **Data-sync design** â€” CDC vs event vs batch per domain; one-way vs two-way; system-of-record per element.
- **Reconciliation model** â€” business key, cadence, drift handling + audit trail.
- **Idempotent-UPSERT + ordering model** â€” on the business key; take-latest-known via version.

## Related skills
- [messaging](../messaging/SKILL.md) â€” the transport CDC/events ride on.
- [event-driven](../event-driven/SKILL.md) â€” the event-model sibling (domain events vs CDC distinction).
- [etl](../etl/SKILL.md) â€” the heavier-batch sibling.
- [observability](../../devops/observability/SKILL.md) â€” drift detection + alerting.
- [sre-review](../../devops/sre-review/SKILL.md) â€” owns the SLO that the freshness latency shapes.

### Banking Context & Examples

#### (1) Customer Master Data Sync Example
**Scenario:** Synchronizing customer data between the legacy `Core-Banking-System` and a new `Digital-Onboarding-Portal`.
- **Architecture Lens Check:** Verification of `PDPL` compliance regarding data-masking during the sync, and `UAE-Data-Residency` requirements for the destination database.
- **Sample Outcome:** "Sync architecture approved with requirements for 128-bit encryption at rest and automated PII masking in non-production environments."
- **Common Pitfall:** Syncing PII data from the legacy core *without* identifying the residency perimeter, resulting in an unauthorized off-shore data leak.

#### (2) AECB Credit Report Sync Example
**Scenario:** Batch processing of credit reports from `AECB` (Al Etihad Credit Bureau) into the Credit Risk modeling engine.
- **Architecture Lens Check:** AECB mandates secure, point-to-point transfer protocols and specific file handling. 
- **Common Pitfall:** Ignoring AECB data-handling requirements, leading to potential regulatory fines due to insecure file handling in the staging area.

#### (3) Sharia Product Master Data Sync Example
**Scenario:** Syncing Sharia-product data, including `Markup-Profit` rates, to external financial aggregators.
- **Architecture Lens Check:** Sharia-governance requires proof that the transmitted rate data matches the certified-Sharia rate calculation for that product.
- **Sample Outcome:** "Sync validated with `Integrity-Checksum` ensuring distributed product-data matches the `Internal-Sharia-Governance-Book`."
- **Common Pitfall:** Exposing raw "Interest-Rate" fields for Sharia products, creating compliance violations with Sharia Board product definitions.

### Regulatory References
1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/
2. **PDPL:** Personal Data Protection Law (Federal Decree-Law No. 45 of 2021)
3. **CBUAE Cybersecurity Framework:** Domain 1: Governance & Risk Management

## Anti-patterns
- **Relying on synchronous point-to-point calls to sync data between macro-services**
  - **Consequence:** Cascading timeouts and total system failure if the receiving data service goes offline.
  - **Correct Approach:** Use asynchronous messaging or event streaming (e.g., Kafka) to buffer sync events and decouple services.
- **Lacking a defined master source of truth for synced entities**
  - **Consequence:** Multi-directional data overwrites ("split-brain") leading to deeply corrupted customer records.
  - **Correct Approach:** Define a single system of record for every entity and enforce one-way (uni-directional) master-to-replica syncs.
- **Failing to implement error/dead-letter queues for failed synchronization events**
  - **Consequence:** Transient network errors cause permanent data drift between systems, and administrators have no visibility.
  - **Correct Approach:** Route failed sync attempts to a Dead Letter Queue (DLQ) with automated retry rules and manual intervention dashboards.
