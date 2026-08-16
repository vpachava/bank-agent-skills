---
name: api-design
description: Use when designing a new API component—internal, channel, or partner—to ensure banking-grade contract boundaries and standard vocabulary.
---

﻿---
name: api-design
description: Design standard for REST, gRPC, and AsyncAPI/Event-Driven patterns.
metadata:
  type: reference
---

# /api-design

## Overview
Design standard for Synchronous and Asynchronous API patterns in banking. Requires API-First exposure; no file/DB access.

## When to apply
Use when designing a new API component—internal, channel, or partner—to ensure banking-grade contract boundaries and standard vocabulary.

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


