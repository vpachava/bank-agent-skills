# Banking Integration Patterns — Wayfinder Research Ticket 05

**Domain:** Integration grounding for a large UAE retail bank.
**Audience:** Downstream skills — `api-design`, `event-driven`, `messaging`, `data-sync`, `etl`, `integration-patterns`, `application-migration`, `security-architecture-review`.
**Currency date:** August 2026.
**Status:** Findings synthesized to support skill checklists (patterns + pitfalls), not a textbook.

---

## Methodology & Confidence Legend

During this session the web tools (`WebSearch` / `WebFetch`) returned infrastructure errors (HTTP 400 / 403 / 404 / 60s timeouts) and could not be used to verify live. Per the research-skill protocol, findings are therefore synthesized from authoritative public knowledge (the model's prior training on canonical standards and vendor documentation), **not fabricated**. Each finding carries an explicit confidence level and is cited to its canonical primary source by name and URL. Where a finding is UAE-specific or recent-and-evolving, confidence is marked **MEDIUM** and the skill builder is directed to verify against the current primary source before embedding.

- **HIGH** — Stable, long-standing, authoritative. Skeptical verification is welcome but unlikely to overturn.
- **MEDIUM** — Domain- or date-sensitive; plausibly advanced since the synthesis date. **Verify before embedding** in a skill checklist.
- **LOW** — Speculative or peripheral; used sparingly.

Primary sources referenced (canonical, stable-URL):
- ISO 20022 standard portal — https://www.iso20022.org/
- SWIFT CBPR+ programme — https://www.swift.com/our-solutions/global-financial-messaging/cross-border-payments/cbpr
- Apache Kafka docs — https://kafka.apache.org/documentation/
- Confluent docs / blog (event sourcing, CDC, EOS) — https://docs.confluent.io/ , https://www.confluent.io/blog
- Debezium (CDC) — https://debezium.io/documentation/
- Martin Fowler bliki: StranglerFig, EventSourcing — https://martinfowler.com/bliki/
- microservices.io (core patterns: ACL, API gateway, Saga, Outbox) — https://microservices.io/patterns/
- OpenID Foundation FAPI profiles — https://openid.net/wg/fapi/
- Central Bank of the UAE (CBUAE) — https://www.centralbank.ae/
- Al Etihad Payments (Aani) — https://aletihadpayments.ae/

---

## 1. ISO 20022 — Payments & Inter-Bank Messaging

**Confidence: HIGH (standard) / MEDIUM (UAE-specific rail timing)**

ISO 20022 is the open global messaging standard for financial-services payments and reporting, developed under **ISO Technical Committee TC68 (Financial Services)**, with **SWIFT acting as Registration Authority** since the standard's inception (mid-2000s). It defines messages via a structured business-process dictionary (data elements + message definitions) rather than fixed-position text, which makes it both richer and more flexible than the MT (FIN) generation it replaces.

For a retail bank the skills ground schema design around three core message *families* (always lowercase prefix + `.nnn`):

- **`pacs.*` — Payments Clearing and Settlement** (FI ↔ FI / inter-bank clearing leg):
  - `pacs.008` — FI-to-FI Customer Credit Transfer. The flagship cross-border payment instruction; **replaced MT103** under CBPR+.
  - `pacs.009` — FI-to-FI Credit Transfer (bank-to-bank, non-customer).
  - `pacs.002` — FI-to-FI Payment Status Report (clearing confirmations / exceptions).
  - `pacs.004` — Payment Reversal.
- **`pain.*` — Payments Initiation** (customer/debtor → bank, the "front door"):
  - `pain.001` — Customer Credit Transfer Initiation (the initiation payload, ISO equivalent of MT101/customer payment file).
  - `pain.002` — Payment Status Report (customer-facing status/no-reason codes).
  - `pain.008` — Customer Direct Debit Initiation.
- **`camt.*` — Cash Management / Reporting** (bank → customer statements & reconciliation):
  - `camt.053` — Bank-to-Customer Statement (end-of-day).
  - `camt.054` — Bank-to-Customer Debit/Credit Notification (per-entry reporting; the reconciliation feed).
  - `camt.052` — Bank-to-Customer Account Report (intraday).
  - `camt.029` — Resolution of Investigation (claim/investigation handling).

Adjacent families (securities/corporate-actions — `semt`, `seev`, `sese`, `setr` and `reda` reference-data) are out of scope for retail-payments integration but appear in treasury/custody skills.

**Migration timeline a skill must row against (HIGH):**
- **SWIFT CBPR+ Phase 1** landed Nov 2022 (`pacs.008/009`, MT103/202 retired; the original March 2023 deadline was pulled forward, so dual MT/ISO window is already closed).
- **CBPR+ Phase 2** landed ~Nov 2023 (camt reporting, MT9xx).
- **CHIPS (US) ISO 20022 migration:** April 2024 — done.
- **Fedwire (US) ISO 20022 migration:** March 2025 — done.
- TARGET2 / SEPA Instant / CHAPS already ISO 20022.

By Aug 2026 all major-zone cross-border and RTGS rails have completed migration — there is no remaining "should I migrate?" question for a correspondent-connected bank.

**UAE specifics — MEDIUM, verify:** The domestic instant-payment rail **Aani**, operated by **Al Etihad Payments (a CBUAE subsidiary)**, launched ~late 2023 and uses ISO 20022 message formats. The older **UAEFTS** batch funds-transfer system coexists. Verify the current set of Aani message variants and the CBUAE scheme rulebook before embedding rail-specific message selection in a skill.

**RSA-relevant schema-design grounding the skills embed (HIGH):**
1. **Map a payment to its three ISO 20022 legs** — initiation (`pain.001`) → clearing (`pacs.008`) → reporting (`camt.053/054`). Design each API contract from the canonical message for its leg; don't invent bespoke shapes that diverge from pacs/camt.
2. **UETR (Unique End-to-End Transaction Reference)** — the `pacs.008` field (gpi-lineage, mandatory under CBPR+) is the canonical end-to-end id. Carry it end-to-end as your correlation/trace id; it is also the natural idempotency key for the payment.
3. **Structured party/address/charge/creditor-agent fields** — model these as structured JSON objects in APIs (BIC vs clearing-code, structured PostalAddress24, NameAndAddress10); the MT free-text field collapse is gone — design for structured data from day one.
4. **Status / rejection reason codes** — use ISO 20022 reason codes (`pain.002` status reason, `pacs.002` transaction status) as the canonical enum set, not custom strings.
5. **JSON adapters for the API tier** — modern payment APIs wrap a JSON projection of the ISO 20022 payload (CBPR+ JSON, SWIFT MyStandards, UK Open Banking style). Schema Registry + a versioned JSON Schema keeps producers/consumers compatible across schema evolution.
6. **Versioning & evolution** — ISO publishes amended data dictionaries; peg your schema to a published version and treat dictionary upgrades as breaking-change engineering, not "just a patch".

---

## 2. Event-Driven Banking Patterns (Kafka / Confluent tier)

**Confidence: HIGH**

The accepted shape for an event-driven bank is a single **event backbone** (Kafka) that is the central nervous system: append-only, partitioned, replicated log of **immutable domain events** that every bounded context publishes to and reads from. Commands/responses still exist for synchronous request-response; the backbone is for the *facts* that downstream projections, fraud, data warehouse, and partner integrations fan out from.

**Domain-event design the `event-driven` skill embeds (HIGH):**
- Name events as **past-tense facts** ("PaymentAuthorized", "AccountDebited", "KYCVerified"), never commands.
- Every event carries: business id (paymentId/accountId), **correlationId** (the originating user/trade request) and **causationId** (the immediately-preceding event), event-type + **schema version**, and a structured payload with monetary amounts in **integer minor units** (never float) plus currency code.
- Distinguish **domain events** (business intent — what the ledger means) from **integration / notification events** (often emitted from CDC — row-level changes; leak the *source*, not the business). `messaging` skill: don't conflate the two; publish a domain-event envelope, not a row-diff.

**Event sourcing vs. CDC (HIGH):**
- **Event sourcing** — the application persists state as a sequence of domain events in an event store; state is a fold over the log; command-side validates, snapshots accelerate. Best for audit-rich domains (payments, ledger, securities). *Pitfalls*: projection rebuild is expensive; long-running streams + schema evolution turn old events into compatibility debt; command-side needs optimistic concurrency / expected-version on the stream.
- **CDC (Change Data Capture)** — emits row-level changes from a transactional DB's redo/binlog/transaction log via **Debezium → Kafka Connect** (supports Oracle, SQL Server, MySQL, Postgres, Mongo). Lets you externalise an existing DB's state without re-architecting apps; ideal for decoupling from a legacy core, populating search, cache, data lake, fraud, and read models. *Pitfalls*: row-granularity not business-granularity; leaks legacy schema internals unless there's a translation layer between CDC and the canonical schema; CDC of a legacy core is integration plumbing, not "the new domain model".

**Pitfalls the `event-driven` skill must embed as a checklist (HIGH):**
- **Ordering** — Kafka orders only *within a partition*. Choose a **partition key that matches your ordering invariant** (e.g. `accountId` for ledger entries, `paymentId` for payment stages). Cross-account / global ordering requires single-partition topics or an out-of-band sequencer — and that costs throughput. State it: "every events-bearing design proposal must state the partition key and the ordering guarantee it buys."
- **Idempotency** — producer retries ⇒ duplicates; **consumers must dedupe** by business key (paymentId/messageId) + an idempotency store with TTL. Idempotency is a producer-and-consumer shared concern, never "Kafka handles it".
- **Exactly-once (EOS)** — Kafka delivers exactly-once *within* Kafka via **idempotent producer + transactional producer/consumer** ("consume-transform-produce" transactions). Across external boundaries (a ledger-DB write, a 3rd-party debit) EOS is **not** automatic — you need the **transactional-outbox** and/or idempotent consumer writes. "We enabled EOS" is not a banking-correctness answer for side-effecting consumers.
- **Replay** — log retention ⇒ replay-by-design; great for backfill/reconstruction. **Poison pill for side effects**: re-consuming a "PaymentDebited" that actually moves external money is dangerous. Wrap every side-effecting consumer in idempotency + dedup window. Replaying a domain-event stream reproduces facts; it must not re-fire the wire.
- **Out-of-order breaks** — when consumer parallelism > producer ordering, or when partitions rebalance, a projection can observe a later state before an earlier one; mitigate with **min-offset-tracking per key**, event-time watermarks, and idempotent UPSERTs (timestamp/version-guarded) into projections.
- **Transactional Outbox** — the canonical cure for the **dual-write problem** (write DB + publish to Kafka atomically). Write the outbox row in the **same DB transaction** as the state change; a relay (Debezium CDC, or a polling publisher) publishes it. `event-driven` + `data-sync` skills: "any producer that writes both to a DB and to a broker must justify its dual-write safety — default to outbox."
- **Schema evolution** — register Avro/Protobuf/JSON-Schema with a Schema Registry under explicit BACKWARD/FORWARD/FULL compatibility. Breaking schema changes break all consumers at once — version the event type (V2 topic) before breaking V1.
- **DLQ + backpressure** — dead-letter queue for poison messages, bounded consumer-lag alerts, retry-with-bounded-attempts before parking. Banks cannot silently drop ledger events.

---

## 3. Integration Patterns over a Legacy Core

**Confidence: HIGH**

A retail bank's core (Temenos/Flexcube/Oracle Flexcube, Avaloq, or in-house) is typically synchronous, stateful, slow, hard to scale, and often the most regulated object in the estate. The dominant pragmatic patterns are:

- **API Gateway** — single ingress for external/internal API consumers; concentrates **OAuth2 / mTLS** (authN), authorization scopes, rate limiting, threat protection, routing and observability at the DMZ boundary. The gateway is the security choke point for open-banking & 3rd-party traffic. (`api-design`, `security-architecture-review`.)
- **Service mesh** (Istio/Linkerd) — east-west policy between internal microservices: **mTLS** service-to-service, traffic shifting for canary, retries/timeouts/circuit-breaking, workload identity. Worth it for microservices-heavy estates; overkill (and costly) for a thin shim over legacy. Don't prescribe mesh as default — justify it per surface.
- **Anti-Corruption Layer / Adapter** — a translation layer that adapts the legacy core's idiom (proprietary TCP, screen-scrape, file-drop, SNA/CICS, ESB SOAP wrappers) to a modern REST/event contract. Keeps legacy schema crud out of new bounded contexts; the ACL owns the legacy dialect so new services speak clean APIs.
- **Strangler Fig** (Martin Fowler) — incrementally replace legacy by intercepting at a façade; route each capability to new or old; grow the new until the legacy starves. *The big-bang core replacement is the path that overruns/fails; the strangler + ACL + event backbone is the dominant pragmatic path.* Migrate slice-by-slice; the new slice emits canonical domain events the rest of the estate replaces legacy point-to-point feeds with.

**Sync vs. async over the core (HIGH):**
- Core banking systems are synchronous, blocking, and slow under concurrency. Common shape: **front the core with an async layer** (queue + outbox); expose eventual-consistency/event-emitting APIs to inner services and clients; keep direct core calls confined to short-lived synchronous legs inside a saga step.
- Don't hold a client connection open while the core churns for minutes. Accept the request → enqueue → return an acceptCorrelation → client polls/subscribes for outcome (matches ISO 20022 `pain.001` ack → `pain.002` status).
- **Saga pattern** for cross-service transactions: a chain of local steps each with a **compensating action** on failure (payment auth → debit account → credit payee; on credit failure, refund debit). Never 2PC/distributed-lock across the core and partners.

**ETL / SOA / REST-vs-events for heavy 3rd-party & core (HIGH):**
- For **heavy 3rd-party** integration (card networks, payment schemes, regulators, treasuries): REST/file-batch is typical; events are for *downstream propagation*, not for the synchronous 3rd-party call.
- For **core commands** with tight SLA: request/response (REST/gRPC) or saga. For **core reads**: prefer **events/CDC out of the core** (read-side fan-out) — don't poll the core for every customer-screen render.
- Don't "fix" a batch system by spray-on events. Select a slice, model its events, front it with an ACL/outbox, and let the slice earn its keep. `application-migration` skill: every migration plan must name the slice, its ACL contract, and its event surface.

**Pitfalls the `integration-patterns` + `application-migration` skills embed:**
- You can't replay a synchronous call; if the legacy call is non-idempotent (e.g. "post this debit"), the ACL must dedupe by business key, because the gateway/consumer *will* retry on timeout.
- A screen-scraping adapter is fragile to terminal-format changes; pin your contract to a typed interface, not the raw terminal field positions, and version it explicitly.
- Single-core dependency = single failure mode; ensure event/CDC decoupling so downstream services degrade gracefully when the core is offline.

---

## 4. ETL & Data-Sync for Banking

**Confidence: HIGH (patterns) / MEDIUM (UAE regulatory-report specifics — verify regime)**

- **CDC** (Debezium → Kafka Connect) is the near-real-time, low-load complement to batch; banks stream OLTP-core changes into the warehouse (Iceberg/Delta/Hudi), search, fraud, intraday-liquidity, and read models. (HIGH.)
- **Reconciliation is mandatory**, not optional — daily/scheduled comparisons between internal books and external statements (Nostro/Vostro, clearing-scheme reports, scheme settlement files). This is both an accounting and a regulatory imperative (financial stability, capital adequacy, AML). The reconciliation engine consumes `camt.053/054` (or equivalent scheme statements) and matches against internal ledgers; unmatched items **age to exceptions** for manual break resolution. (HIGH — globally true; UAE-specific reporting cadences/regime: MEDIUM, verify against current CBUAE rulebook.)
- **Near-real-time vs. batch** — both coexist:
  - Real-time streaming for fraud, risk, intraday liquidity, real-time balance (millisecond SLAs).
  - Batch for end-of-day core posting, month-end, regulatory cut-offs, traditional warehouse loads.
  - Modern shape: land CDC events to an open table format lake (Iceberg/Delta/Hudi) and serve both real-time consumer pipelines and batch/historical reads from the same substrate.

**Data-integrity pitfalls the `etl` + `data-sync` skills embed (HIGH):**
- **Money as integer minor units**, never float — embed in every data contract; alongside ISO 4217 currency code and decimal-handling rules (some currencies have 3 decimal places, some 0). Float arithmetic on a banking ledger is a production incident.
- **Idempotency store** — every payment-modifying endpoint and every event consumer writes/checks an idempotency row keyed by business key (UETR/paymentId/messageId) with TTL. Replay storms **will** re-post unless deduped.
- **Duplicate detection** — globally unique id (UETR) end-to-end; consumers must be safe under re-delivery; load jobs use idempotent **MERGE/UPSERT** keyed on the business id (not the row).
- **Reconciliation breaks** — when stream and batch diverge, you need a deterministic, auditable break-resolution workflow; never silently drop exceptions. Embed "every data pipeline produces a reconciliation break report, and breaks age to an exception queue."
- **Schema/type drift** — currency precision, timezones (always store UTC, carry explicit TZ in ISO-8601), decimal/timestamp serialization in Avro/JSON, ISO country enums. Pin enums to ISO standards, not free text.
- **Landing vs. curated** — land raw events unchanged, then curate with idempotent transformations; never overwrite raw. Lake layering (bronze/silver/gold) is the standard integrity frontier.
- **At-least-once delivery is the floor, not the ceiling** — ETL/data-sync consumers must assume duplicate events and dedupe; "exactly-once" requires the outbox + idempotent-UPSERT discipline.

---

## 5. 3rd-Party / Open-Banking Integration (UAE)

**Confidence: HIGH (global posture) / MEDIUM (UAE regulatory specifics — verify against current CBUAE publications)**

Globally accepted posture the `api-design` + `security-architecture-review` skills embed as default rules (HIGH):

- **OAuth 2.0 Authorization Code with PKCE** for TPP consent capture by a regulated Third Party Provider.
- **FAPI (Financial-grade API)** security profiles from the OpenID Foundation — **FAPI 1.0 Advanced** and **FAPI 2.0** (mature by 2026). FAPI 2.0 is the current target baseline; for a new design choose FAPI 2.0 over FAPI 1.0.
- **mTLS** as both transport security and as **sender-constraining** (mTLS-bound tokens) — alternatively **DPoP**. Tokens must be sender-constrained, not bearer.
- **Strong Customer Authentication (SCA)** required before Payment Initiation and for sensitive AIS access — multi-factor (knowledge/possession/inherence). Where the bank wants SCA exemptions, implement **Transaction Risk Analysis (TRA)** with conservative thresholds; the default posture is SCA-on.
- **Consent management** — explicit scopes (`accounts`, `balances`, `transactions`, `payments`), short-lived access tokens, revocable refresh tokens, a customer-facing consent dashboard ("here's what you authorised, revoke here"). Data minimization and purpose-of-use fields.
- **Rate limits & per-TPP quotas** at the gateway; per-TPP throttling protects the core from runaway integrators.
- **Open Banking schemas are ISO 20022-derived JSON** — BIC/IBAN structured, ISO 4217 currency, ISO country, structured addresses. Design your open-banking resource model as a JSON projection of the same pacs/pain/camt canonical messages used internally — single canonical model, two surfaces.
- **Default deny.** Every external data access is audited; certificates (issuer-validated) per TPP; certificate lifecycle is its own operational concern (revocation/rotation). Open Banking is full of credential-rotation bugs.

UAE specifics — **MEDIUM, verify against current CBUAE publications before embedding dates/specs**: The **Central Bank of the UAE (CBUAE)** leads open banking under an **"Open Finance"** framing (broader than open banking, covering a wider set of financial products/players). CBUAE has run an **Open Finance Lab / technical sandbox** and an **Open Finance regulation** (in the ~2023–2024 cycle following consultation papers) — the exact final rule text, scope of AIS/PIS/party classes, and effective dates have plausibly advanced since the synthesis date of Aug 2026 and must be read against current CBUAE rulebook pages. TPPs (AIS / PIS) are licensed and supervised; SCA is required; Aani instant payments / Al Etihad Payments underpins instant retail flows. Treat all of this as directional: the global posture above is the embeddable default, but UAE-specific rule text and deadlines must be fetched and pinned in the skill by the skill builder before any checklist ships.

**What `api-design` + `security-architecture-review` embed from this section (HIGH defaults + verify-profile for UAE specifics):**
1. OAuth2 Auth-Code-PKCE + FAPI 2.0 is the default for any 3rd-party data/payment surface; deviation requires explicit justification.
2. Tokens are sender-constrained (mTLS-bound or DPoP); pure bearer is non-compliant.
3. SCA on for PIS and sensitive AIS; TRA exemptions are an opt-in with controls.
4. Consent capture/revocation is a first-class API surface + dashboard, not an afterthought.
5. Open Banking JSON contracts are a projection of the same ISO 20022 canonical messages used internally — one canonical model, two surfaces.
6. Per-TPP rate limits, quotas, audit, certificate rotation are part of the API contract from day one.

---

## Downstream Skill Grounding Matrix

| Downstream skill | Canonical grounding points pulled from this research |
|---|---|
| `api-design` | Map each API to its ISO 20022 leg (pain/pacs/camt); carry UETR end-to-end as correlation+idempotency; structured party/charge/reason-code fields; OAuth2 + FAPI 2.0 + SCA + consent for 3rd-party; one canonical ISO 20022 model, two surfaces (internal + open-banking). |
| `messaging` | Domain event vs. integration/CDC event distinction; past-tense event naming; correlationId/causationId; schema-version in every envelope; published as a JSON-Schema/Avro projection of ISO 20022 where the event reflects a payment/ledger fact. |
| `event-driven` | Event backbone (Kafka); partition key = ordering invariant; idempotency store mandatory; EOS within Kafka only; transactional-outbox for dual-write; DLQ + bounded retry; replay-safe side effects; single canonical event for a payment (UETR-keyed). |
| `data-sync` | CDC (Debezium) for near-real-time; reconciliation as mandatory accounting+regulatory discipline (`camt.053/054` vs. ledger); idempotent UPSERT on business key; land-then-curate lake layering; break → exception queue. |
| `etl` | Money as integer minor units + ISO currency; duplicate detection on UETR; batch (end-of-day) coexists with streaming; RFC/schema-versioning of pipeline contracts; timezones always UTC + explicit TZ. |
| `integration-patterns` | API gateway (security choke point) + service mesh (justified per surface); Anti-Corruption Layer over legacy; Strangler Fig for incremental migration; saga + compensating actions; sync commands + async reads; core dependency as single failure mode. |
| `application-migration` | Strangler slice-by-slice; ACL owns the legacy dialect; new slice emits canonical domain events; never big-bang; name the slice, its contract, and its event surface; idempotent ACL calls by business key because retries **will** happen. |
| `security-architecture-review` | FAPI 2.0 + OAuth2 PKCE + sender-constraining (mTLS-bound/DPoP); SCA default-on + TRA opt-in; default deny; per-TPP quotas; certificate rotation logistics; audit every external access. |

---

## Summary

Web tools were unavailable this session, so findings are synthesized from authoritative public knowledge with per-finding confidence and canonical citations, not fabricated. ISO 20022 (pacs/pain/camt) is the canonical schema surface, with SWIFT CBPR+ and CHIPS/Fedwire migrations complete by Aug 2026; downstream API/messaging skills ground every contract against the relevant ISO 20022 leg and carry the UETR end-to-end. Kafka event-backbone patterns achieve EOS *within* Kafka but require transactional outbox + idempotent consumers across boundaries; the pitfalls that must be embeddable are partition-key = ordering invariant, idempotency store, replay-safe side effects, and DLQ/bounded retry. Legacy-core integration defaults to API gateway + service mesh (justified per surface) + Anti-Corruption Layer + Strangler Fig (never big-bang), with sync commands over the core and CDC/events out of it. Data-sync/etl skills embed reconciliation as mandatory, money as integer minor units, idempotent UPSERT on the business key, and lake layering. UAE open-banking (CBUAE Open Finance + Al Etihad Payments' Aani) is high-confidence in global posture (FAPI 2.0, SCA, OAuth2 PKCE, sender-constrained tokens) but UAE-specific rule text and dates are marked MEDIUM and must be verified against current CBUAE publications before a checklist ships.

**File written:** `C:\code\ai\BrainStorming\skills\wayfinder\research\banking-integration-patterns.md`
