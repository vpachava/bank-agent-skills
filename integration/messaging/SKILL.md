---
name: messaging
owner: Solution Architecture
version: 0.1.0
last-reviewed: 2026-08-09
description: "Use when designing the message transport for a banking flow â€” produces a messaging design (queues/topics, delivery semantics, SLAs, payload standards) with idempotency and ordering handled at the transport."
required-inputs:
  - The flows & their producers/consumers
  - Delivery requirements (at-least-once / at-most-once / exactly-once-in-broker)
  - Payload standards in scope (ISO 20022, IFX, BIAN)
  - Operational constraints (peak rate, retention, residency)
expected-deliverables:
  - Messaging topology (queues/topics, subscriptions, partitioning)
  - Delivery-semantics + idempotency + ordering model per flow
  - Payload-standards alignment + residency note
togaf-phases: [Phase C]
togaf-artifacts: [HLD]
bian-service-domains: [Integration.API]
---

# /messaging

## When to apply
Use when the message *transport* itself is the design question â€” queue vs topic vs streaming, delivery semantics, ordering, retention. Distinct from `/event-driven` (which asks whether and how the flow *is* reactive) â€” messaging is the pipe; event-driven is the use of it. Pairs with `/event-driven` and feeds `/data-sync` and `/etl`.

> ISO 20022 message families (`pain.`/`pacs.`/`camt.`) and the IFX Business Message Spec are the payload-grounding for banking messages; BIAN's published semantic payloads describe the capability-aligned shape.

## Inputs
- **The flows & producers/consumers** â€” what travels the bus; one producerâ†’one consumer (queue) vs oneâ†’many (topic/stream with subscriptions).
- **Delivery requirements** â€” at-least-once (publish-then-dedupe at consumer), at-most-once (fire-and-forget), exactly-once *within the broker* (Kafka EOS) â€” but see the pitfall: real end-to-end is always at-least-once unless the consumer is idempotent.
- **Payload standards in scope** â€” ISO 20022 where payments/inter-bank; IFX where the bank uses it; BIAN semantic payloads where aligned.
- **Operational constraints** â€” peak rate, retention window, residency of the messages' content.

## Process

1. **Pick the model â€” queue vs topic/streaming â€” by consumer topology.** One-producer-to-one-consumer (work queue, competing consumers) for load-distribution and decoupling; one-producer-to-many (pub/sub topic/stream) for fan-out where multiple consumers each react. Mis-picking (a queue when multiple consumers need each-a-copy, or a topic when only one should act) is a foundational mistake.

2. **Set delivery semantics per flow, and own the gap to end-to-end.** Broker "exactly-once" is within the broker; once the consumer side-effects (HTTP/DB), the end-to-end guarantee is at-least-once unless the consumer dedupes. State the *broker* guarantee and the *consumer* obligation separately â€” and bake idempotency-key acceptance into the message envelope.

3. **Handle ordering at the transport, by partition key.** Within-partition ordering only; pick the partition key for the ordering invariant per flow (UETR for payments, account-id for account flows, customer-id for KYC). "Ordered per-consumer" usually means "keyed by the invariant"; document the key per topic.

4. **Align payloads to ISO 20022 / IFX / BIAN where the flow crosses those standards.** Don't invent a parallel canonical envelope that then translates forever; payload shape on the payment boundary should be ISO 20022 message families, with `UETR` as the canonical correlation id. Capability-aligned payloads lean on BIAN's semantic payloads where the bank decomposes.

5. **Design the envelope â€” idempotency key, correlation id, trace id, timestamp, schema version.** The envelope is the durable cross-cut; the idempotency key makes consumers safe on retry, the correlation id ties the message through the flow, the trace id feeds `/observability` distributed tracing.

6. **Set retention, DLQ, and replay policy.** Retention window sized to the reconciliation / reprocessing SLA; DLQ + bounded retry + alerting for poison messages; replay semantics stated (idempotent consumers only are safe under replay).

7. **Address residency & PII at the message level.** Where messages carry PII/payment data, the topic's region/residency is itself a compliance decision; cross-zone (onshoreâ†”DIFC/ADGM) message transport inherits the SCC/BCR obligation â€” design the topic's region and the message's PII minimization together.

## Banking pitfalls
- **Topic vs queue confused** â€” fan-out topic where a work queue was needed (multiple consumers each acting on the same message = double-action); or queue where each consumer needed its own copy. Topology decides correctness here.
- **Assuming broker exactly-once is end-to-end** â€” Kafka EOS is within-broker; the consumer's side-effect drops to at-least-once â€” bake idempotency keys + consumer dedupe, don't rely on the broker.
- **Ordering without the right partition key** â€” round-robin / random key for throughput loses the ordering invariant; key by the flow's ordering invariant.
- **Inventing a canonical envelope parallel to ISO 20022** â€” a permanent translation surface at the payments boundary; align to the standard there.
- **Envelope without correlation/trace/idempotency keys** â€” consumers can't dedupe; traces break across the bus; debugging becomes archaeology.
- **Replay assumed safe** â€” re-delivering messages to side-effecting consumers duplicates the side-effect; only idempotent consumers are safely replayable, and that's a consumer-design constraint, not a transport one.
- **Residency forgotten at the message level** â€” topic region not treated as compliance decision, PII ridden on a cross-region topic that violates residency; treat topic region + PII minimization as one design.

## Bulletproofing
- **Governance Policy:** Enforce [CBUAE Rulebook](governance/policy/regulations.yaml#CBUAE), [PDPL](governance/policy/regulations.yaml#PDPL), and [PCI-DSS](governance/policy/regulations.yaml#PCI-DSS) where applicable.

## Outputs
- **Messaging topology** â€” queues vs topics/streams, subscriptions, partitioning-per-flow with the ordering-invariant key.
- **Delivery-semantics + idempotency + ordering model** â€” broker guarantee vs consumer obligation stated separately; keys per flow.
- **Envelope spec** â€” idempotency key, correlation id, trace id, timestamp, schema version.
- **Payload-standards alignment + residency note** â€” ISO 20022/IFX/BIAN where applicable; topic-region compliance decision + cross-zone SCC note where relevant.

## Related skills
- [event-driven](../event-driven/SKILL.md) â€” the *use* of this transport.
- [data-sync](../data-sync/SKILL.md) â€” CDC sits on this transport.
- [etl](../etl/SKILL.md) â€” batch/stream data movement over the bus.
- [api-design](../api-design/SKILL.md) â€” the Async-API command/event cousin.
- [observability](../../devops/observability/SKILL.md) â€” trace id propagation across the bus.

### Banking Context & Examples

#### (1) Credit Card Onboarding Example
**Scenario:** Message transport for "Credit Card Approval" fan-out.
- **Architecture Lens Check:** Using a \`topic\` (not queue) with \`Exactly-Once-in-Broker\` delivery for notifying multiple channels (Mobile-App, Email-Service, Core-Banking-Ledger) of approval.
- **Sample Outcome:** \"Messaging Topology: Topic \`credit-card-approval-v1\` with four consumer subscriptions. Producer partition key: \`Application-ID\` to guarantee order.\"
- **Common Pitfall:** Using a competing-consumer \`queue\` for notification fan-out, causing only one consumer (e.g., only Mobile-App) to receive and process the approval, leaving other channels uninformed of the card status.

#### (2) Customer Profile Management Example
**Scenario:** Messaging for cross-zone (onshore â†” DIFC) data synchronization.
- **Architecture Lens Check:** Transport must comply with \`PDPL\` residency for all messages crossing the onshore/free-zone boundary, requiring a logged \`SCC/BCR\` transfer basis.
- **Sample Outcome:** \"Envelope Design: Topic \`onshore-to-difc-sync\` configured in UAE-region VPC; message envelope includes \`SCC-Transfer-ID\` for auditability.\"
- **Common Pitfall:** Transporting unmasked Emirates IDs across residency zones (e.g., onshoreâ†”DIFC) without provenance logging, failing the mandatory data residency audit trails.

#### (3) Lending/Loans Onboarding Example
**Scenario:** Message transport for Sharia-compliant loan status updates.
- **Architecture Lens Check:** Enforcing \`At-Least-Once\` delivery with idempotent consumers for status updates to ensure that even on retry, business rules for Sharia-conformant loan activation (the event) are executed only once.
- **Sample Outcome:** \"Consumer Obligation: Every status-update processor MUST verify \`event-id\` against a deduplication-table before ledger-record writing.\"
- **Common Pitfall:** Relying on broker \`At-Least-Once\` guarantees as a substitute for consumer deduplication, allowing network-retries to double-trigger the Sharia-compliant loan activation, corrupting the ledger."

### Regulatory References
1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/
2. **PDPL:** Personal Data Protection Law (Federal Decree-Law No. 45 of 2021)
3. **CBUAE Cybersecurity Framework:** Domain 1: Governance & Risk Management

## Anti-patterns
- **Using messaging queues as a persistent database store**
  - **Consequence:** Queue sizes explode, degrading message broker performance, and analytics queries become impossible.
  - **Correct Approach:** Extract and route messages to permanent sink storage (like S3 or databases) if long-term persistence is needed.
- **Designing consumers that cannot handle out-of-order message delivery**
  - **Consequence:** Incorrect state application because message 2 (update) arrives before message 1 (create) due to network routing.
  - **Correct Approach:** Design consumers to handle idempotent out-of-order arrivals, using version timestamps or state state-machine checks.
- **Ignoring poison message handling (lack of Dead Letter Queues)**
  - **Consequence:** The consumer crashes parsing a bad message, the broker requeues it, and the system enters an infinite error loop.
  - **Correct Approach:** Enforce retry limits and route perpetually failing messages explicitly into isolated Dead Letter Queues.
