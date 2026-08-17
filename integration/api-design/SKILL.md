---
name: api-design
description: Use when designing a new API componentâ€”internal, channel, or partnerâ€”to ensure banking-grade contract boundaries and standard vocabulary.
togaf-phases: [Phase C]
togaf-artifacts: [HLD]
bian-service-domains: [Integration.API]
---

ï»¿---
name: api-design
description: Design standard for REST, gRPC, and AsyncAPI/Event-Driven patterns.
metadata:
  type: reference
---

# /api-design

## Overview
Design standard for Synchronous and Asynchronous API patterns in banking. Requires API-First exposure; no file/DB access.

## When to apply
Use when designing a new API componentâ€”internal, channel, or partnerâ€”to ensure banking-grade contract boundaries and standard vocabulary.

## Process
1. **Contract Sketch**: Define operations (for Sync) or Topics/Channels (for Async), inputs, outputs, errors.
2. **Pattern Selection**: Select Sync (REST/gRPC) or Async (Event-Driven via AsyncAPI for Kafka/MQ).
3. **Constraint Application**: Map idempotency (for mutating Sync), PII/Regulated tagging, versioning.
4. **Idempotency/Event Handling**:
    - **Sync**: Validate `idempotency-key` for mutations.
    - **Async**: Design idempotent event consumers tracking `event-id` in a deduplication store.
5. **Format Verification**: Validate against standardized error formats or schema registries.

## AsyncAPI Design Principles
- **Schema Registry**: All events MUST be schema-validated against a central registry.
- **Idempotency Consumer**: Event consumers MUST track `event-id` in a deduplication store to avoid processing same event twice.
- **Dead Letter Queue (DLQ)**: Failed events MUST be sent to a DLQ for investigation.
- **Traceability**: All events MUST include tracing headers (e.g., OpenTelemetry ID).

## Bulletproofing against Rationalization
To prevent leaky API boundaries that skip banking requirements, you MUST:

1. **Mandatory Idempotency (Sync):** Every mutating operation (POST/PUT/PATCH) MUST require an `idempotency-key` (UUID v4).
2. **Mandatory Deduplication (Async):** Every event consumer MUST implement `event-id` based deduplication.
3. **Explicit Data Classification:** The API/Event schema MUST explicitly tag fields containing PII or regulated financial data.
4. **Mandatory Versioning Scheme:** All Sync URLs MUST include versioning (e.g. `v1/`). Events MUST include schema versioning.
5. **Mandatory Error Standardization:** Sync APIs MUST adopt a standardized error format (e.g. RFC 7807). Async errors MUST be routed to a DLQ.
6. **Rollback/Failure Handling:** Every implementation MUST include a documented failure/rollback path.

**Violating these rules invalidates the API Design.**

## Outputs
- **API Contract** (OpenAPI or AsyncAPI schema).
- **Idempotency/Security/Versioning compliance report**.
- **Regulated Data Tagging map**.



### Banking Context & Examples

#### (1) Credit Card Onboarding Example
**Scenario:** Designing the API for "Credit Card Origination".
- **Architecture Lens Check:** Implementation of mandatory `idempotency-key` for all balance-modifying API calls to avoid double-processing AECB checks.
- **Sample Outcome:** "API Contract: `POST /v1/applications` accepts `idempotency-key` (UUID); returns HTTP 409 if idempotent-collision detected."
- **Common Pitfall:** Forgetting the idempotency-key on payment/origination APIs; network-retries cause duplicate applications or AECB queries, violating CBUAE consumer protection expectations.

#### (2) Customer Profile Management Example
**Scenario:** API design for a cross-zone customer profile update service.
- **Architecture Lens Check:** Explicit tagging of PII in the schema to ensure data residency compliance under `PDPL`.
- **Sample Outcome:** "Schema: `{ "fullname": "...", "emirates_id": "... (Tag: PII/Regulated)" }`."
- **Common Pitfall:** Exposing a monolithic profile API that returns all customer attributes without per-field tagging, violating residency limits when PII (e.g., Emirates ID) is accidentally retrieved in a restricted zone.

#### (3) Lending/Loans Onboarding Example
**Scenario:** Event-driven API for Sharia-compliant loan status updates.
- **Architecture Lens Check:** Ensuring `event-id` based deduplication for all loan-status changes triggered by Sharia governance events.
- **Sample Outcome:** "AsyncAPI: Sharia-status-update event includes `event-id`; consumer deduplicates to prevent re-issuing duplicate financial instructions."
- **Common Pitfall:** Building async event consumers that re-trigger Sharia-compliant status updates on every network retry; the system must deduplicate to ensure a loan instruction is never applied to the core ledger twice."

### Regulatory References
1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/
2. **PDPL:** Personal Data Protection Law (Federal Decree-Law No. 45 of 2021)
3. **CBUAE Cybersecurity Framework:** Domain 1: Governance & Risk Management

## Anti-patterns
- **Designing APIs directly matching the internal database schema (CRUD exposure)**
  - **Consequence:** Tight coupling between clients and the database. Changing the database breaks all external clients.
  - **Correct Approach:** Design APIs based on business aggregate boundaries and client usage scenarios, abstracting internal data models.
- **Failing to implement aggressive pagination, filtering, and rate limiting by default**
  - **Consequence:** Massive data queries crash the API gateway or database, leading to denial of service outages.
  - **Correct Approach:** Enforce mandatory pagination limits, payload size caps, and API gateway rate limits on all endpoints.
- **Releasing breaking API changes without explicit versioning**
  - **Consequence:** Sudden crashes for consumers when payload structures or URL paths change unexpectedly.
  - **Correct Approach:** Implement clear, semantic versioning (e.g., via URI path `/v1/` or headers) and maintain backwards compatibility.
