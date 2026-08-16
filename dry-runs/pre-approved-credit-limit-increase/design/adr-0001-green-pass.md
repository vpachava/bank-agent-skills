# ADR-0001: API Gateway Facade

- **Status:** Accepted
- **Date:** 2026-08-15
- **Deciders:** Architecture Board
- **Tags:** integration, modernization

## Context
We need to modernize T24 R18 to R24. Current state is fragmented OFS interfaces. We need to standardize interface exposure.

## Decision drivers
- **Standardization:** All channels must use a single Domain API.
- **Regulatory Resiliency:** CBUAE residency rules apply.
- **Maintainability:** Middleware must manage mapping logic.

## Considered options
- **Option A — API Gateway Facade:** Fast to implement, but risk of logic accumulation in gateway.
- **Option B — Domain API Mapping in Middleware (Chosen):** Better decoupling, manageable mapping.
- **Do nothing:** Continued fragmentation, high compliance risk.

## Decision
We choose Option B — **because** it aligns with the modernization roadmap and enforces decoupling.

## Consequences
- **Gains:** Decoupled architecture, single entry point.
- **Penalties / costs:** High initial development effort for mapping logic.
- **Accepted regulatory exposure:** None beyond standard baseline.
- **Reversibility cost:** High, requires migration of all mapping logic.

## Links
- Acceptance gate: Board Review 2026-08-15
