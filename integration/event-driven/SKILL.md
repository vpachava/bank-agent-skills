---
name: event-driven
owner: Solution Architecture
version: 0.1.0
last-reviewed: 2026-08-09
description: "Use when designing an event-driven flow over a legacy core — produces an event design (domain events vs CDC, choreography vs orchestration, the backbone topology) with idempotency, ordering, and replay handled."
required-inputs:
  - The flow & its producers/consumers
  - Whether events are domain-business or change-data-capture
  - Reliability requirements (ordering, exactly-once, replay tolerance)
  - Consumers' side-effect nature (idempotent-safe?)
expected-deliverables:
  - Event design (event types/schemas, choreography vs orchestration choice)
  - Reliability model (ordering, idempotency, replay, DLQ)
  - Backbone topology note (domain-topic layout, partitioning keys)
---

# /event-driven

## When to apply
Use when a flow should be *reactive* — the legacy core emits, services react — rather than a chain of synchronous calls. High-leverage in a bank where the core is the bottleneck and extending it with new sync calls starves the core. The home of much modernization risk: event systems done badly drop, duplicate, and reorder — done well they decouple and scale. Pairs with `/messaging` (the transport) and `/data-sync` (the CDC side).

## Inputs
- **The flow & its producers/consumers** — who emits, who reacts, what state each owns.
- **Domain-events vs CDC-events** — the crucial first call: domain events express a business fact (PaymentInitiated) and are publish-deliberate; CDC events mechanically mirror a data change and are publish-implicit. Mixing them in the same stream is the most common event architecture bug.
- **Reliability requirements** — ordering (per-stream? globally?), delivery (at-least-once / exactly-once-in-kafka / exactly-once-application), replay tolerance.
- **Consumers' side-effect nature** — are they safe to re-run (idempotent) or do they charge/issue/notify?

## Process
1. **Distinguish domain events from CDC events — and keep them separate.** Domain events = deliberate business signals published by the producer; CDC events = a stream of row-changes captured mechanically (Debezium) from the core. Mixing carries the legacy core's table grit into the event surface. Separate streams per category; the system of record owns domain events.

2. **Choose choreography vs orchestration per flow.** Choreography (services react to events, no central director) for genuinely decoupled cross-domain reactions; orchestration (a central flow drives calls/commands + listens) where the journey has a regulated deterministic spine. A bank's regulated journeys usually need *orchestration with events*, not pure choreography, because somebody must be accountable for the KYC/issuance decision.

3. **Design event schemas versioned + additive-only.** Events are forever-once-published; consumers you don't know about depend on them. Version in the schema + envelope; within a version, additive-only; breaking change = new event type + a deprecation runway, never a silent schema change.

4. **Model partitioning keys to preserve ordering where it matters.** Ordering is per-partition, not global. Pick the partition key that matches your ordering invariant — per account, per transaction (UETR), per customer — not "round-robin for throughput." The wrong key means a consumer sees out-of-order events and makes wrong decisions (status-of-payment consumed before initiation).
   > Kafka ordering guarantee is within-partition only, not global. A partition keyed by account-id preserves order for that account; keyed at random for throughput preserves no order at all.

5. **Make consumers idempotent by construction — at-least-once is your real guarantee.** Kafka's "exactly-once" is within-Kafka only; the moment a consumer side-effects (HTTP call, DB write), the end-to-end delivery guarantee drops to at-least-once unless the consumer is idempotent. Design an idempotency key per event (UETR-style) and dedupe at the consumer; **don't rely on the broker's exactly-once to make your consumer safe.**

6. **Handle poison messages with a DLQ + bounded retries.** A malformed event retried forever blocks its partition (and everything behind it in that partition — ordering). Use a dead-letter queue + a bounded retry count; alert on DLQ growth; define whether DLQ'd events are order-suspended or skipped.

7. **Define replay semantics explicitly.** Replay re-feeds past events to consumers. For idempotent consumers replays are safe; for side-effecting consumers replays duplicate the side-effects unless idempotent/dedupe holds. State replay tolerance per consumer; many bank consumers (notification, charge) are *not* safely replayable without dedupe.

8. **Use the transactional-outbox to avoid the dual-write problem.** Publishing to a broker + writing your own DB in one transaction needs the outbox: write the event to an outbox table in the same DB transaction, a relay publishes it. Otherwise you get "DB committed, event never published" or the inverse — exactly the silent data-loss banks suffer under naive event designs.

## Banking pitfalls
- **Domain events entangled with CDC events** — row-change grit from the core pollutes the business event stream; consumers depend on the core's table structure (locked forever). Keep them separate streams.
- **Pure choreography on a regulated journey** — no accountable director for the KYC/issuance decision; regulated journeys need orchestration-with-events, not free-floating reaction.
- **Consumers assumed exactly-once because Kafka says so** — Kafka's exactly-once is within-Kafka; the consumer's HTTP call / DB write drops to at-least-once end-to-end. Design consumer idempotency + dedupe, always.
- **Wrong partition keys** — partitioned for throughput (random) not for ordering invariants; out-of-order consuming produces wrong decisions. Key by the ordering-invariant (account/UETR/customer).
- **Naive dual-write** — DB commit + broker publish in two separate operations → silent publish-loss or ghost publish; use the transactional outbox.
- **Poison-message without DLQ** — a malformed event retried forever stalls the partition (and everything behind it, ordering); bounded-retry + DLQ + alerting or the legacy core's grit stops the stream.
- **Replay assumed safe** — re-running events against side-effecting consumers (charge, notify) duplicates the side-effects unless idempotency-keyed/deduped; state replay tolerance per consumer.
- **Event schema breaking-versioned silently** — a quiet schema change breaks unknown consumers; additive-only within a version, breaking = new type + deprecation runway.

## Bulletproofing against Rationalization
To prevent async chaotic messaging that loses financial events, you MUST:

1. **Mandatory Dead Letter Strategy:** Every consumer MUST have an explicitly documented Dead Letter Queue and retry policy.
2. **Mandatory Schema Registry:** Event payloads MUST be governed by a schema registry. Ad-hoc JSON blobs on the bus are rejected.
3. **Guaranteed Ordering Analysis:** The design MUST explicitly analyze whether event processing order matters and how out-of-order deliveries are handled.
4. **Mandatory Idempotency and Rollback:**
   a. Every event MUST carry a unique `idempotency-key` (UUID v4).
   b. Consumers MUST implement a conflict-resolution strategy (first-wins, last-wins, merge).
   c. A formal rollback procedure must be documented for idempotency verification failure.

**Violating these rules invalidates the Event-Driven Design.**

## Outputs
- **Event design** — domain vs CDC separated, event types/schemas (versioned + additive), choreography-vs-orchestration call per flow.
- **Reliability model** — partition keys (ordering invariants), idempotency keys (dedupe at consumer), DLQ + bounded retry, replay tolerance per consumer.
- **Transactional-outbox decision** — where needed to avoid dual-write loss.
- **Backbone topology note** — domain-topic layout, partitioning strategy, the bridge to any enterprise hub.

## Related skills
- [messaging](../messaging/SKILL.md) — the transport this runs over.
- [data-sync](../data-sync/SKILL.md) — the CDC sibling for the data-synchronization side.
- [api-design](../api-design/SKILL.md) — the command-API half of an orchestrated event flow.
- [integration-patterns](../integration-patterns/SKILL.md) — picks the surrounding integration pattern.
- [application-migration](../../migration/application-migration/SKILL.md) — for strangler-fig the event seam out of the core.
- [observability](../../devops/observability/SKILL.md) — distributed tracing across the event chain.

### Banking Context & Examples

#### (1) Credit Card Onboarding Example
**Scenario:** Event-driven design for an "Instant Credit Card" fulfillment.
- **Architecture Lens Check:** Separation of \`Domain-Event\` (\`CardApprovalRequested\`) from \`CDC-Event\` (table-row change in \`Origination-Core\`).
- **Sample Outcome:** \"Event Design: \`CardApprovalRequested\` emitted by Service; \`Core-Ledger-Update\` emitted by separate CDC-process.\"
- **Common Pitfall:** Emitting row-changes from the \`Origination-Core\` database directly to the \`Email-Service\` consumer; this couples the consumer permanently to the database schema, which will break instantly when the core system upgrades.

#### (2) Customer Profile Management Example
**Scenario:** Reacting to customer profile updates.
- **Architecture Lens Check:** Choreography-with-an-orchestrator spine for sensitive data changes to ensure \`PDPL\` compliance audit logging.
- **Sample Outcome:** \"Backbone Topology: Orchestrator captures \`ProfileChanged\` domain-event, triggers sync-event to residency-zone-databases with provenance headers for audit.\"
- **Common Pitfall:** Using pure event-choreography for PII updates, allowing profile changes to flow unchecked through distributed systems without accountable orchestration, making \`PDPL\` compliance audits impossible.

#### (3) Lending/Loans Onboarding Example
**Scenario:** Event backbone for Sharia-compliant loan activation.
- **Architecture Lens Check:** Enforcing \`Idempotency\` via consumer-side deduplication for the \`ShariaLoanActivated\` domain event.
- **Sample Outcome:** \"Reliability Model: Consumer implements \`event-id\` based dedupe; only processes first \`ShariaLoanActivated\` fact.\"
- **Common Pitfall:** Assuming event-broker's \`at-least-once\` delivery is sufficient for ledger updates. Network-retry causes consumers to double-process activate events, resulting in loan funds being double-charged or double-activated."

### Banking Context & Examples

#### (1) Credit Card Onboarding Example
**Scenario:** Event-driven design for an "Instant Credit Card" fulfillment.
- **Architecture Lens Check:** Separation of `Domain-Event` (`CardApprovalRequested`) from `CDC-Event` (table-row change in `Origination-Core`).
- **Sample Outcome:** "Event Design: `CardApprovalRequested` emitted by Service; `Core-Ledger-Update` emitted by separate CDC-process."
- **Common Pitfall:** Emitting row-changes from the `Origination-Core` database directly to the `Email-Service` consumer; this couples the consumer permanently to the database schema, which will break instantly when the core system upgrades.

#### (2) Customer Profile Management Example
**Scenario:** Reacting to customer profile updates.
- **Architecture Lens Check:** Choreography-with-an-orchestrator spine for sensitive data changes to ensure `PDPL` compliance audit logging.
- **Sample Outcome:** "Backbone Topology: Orchestrator captures `ProfileChanged` domain-event, triggers sync-event to residency-zone-databases with provenance headers for audit."
- **Common Pitfall:** Using pure event-choreography for PII updates, allowing profile changes to flow unchecked through distributed systems without accountable orchestration, making `PDPL` compliance audits impossible.

#### (3) Lending/Loans Onboarding Example
**Scenario:** Event backbone for Sharia-compliant loan activation.
- **Architecture Lens Check:** Enforcing `Idempotency` via consumer-side deduplication for the `ShariaLoanActivated` domain event.
- **Sample Outcome:** "Reliability Model: Consumer implements `event-id` based dedupe; only processes first `ShariaLoanActivated` fact."
- **Common Pitfall:** Assuming event-broker's `at-least-once` delivery is sufficient for ledger updates. Network-retry causes consumers to double-process activate events, resulting in loan funds being double-charged or double-activated."
