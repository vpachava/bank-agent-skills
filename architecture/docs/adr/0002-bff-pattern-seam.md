# ADR: BFF Pattern & Seam Discipline

## Status
Proposed

## Context
In large-scale banking architectures, mobile clients often attempt to call core banking systems directly, or inflate the mobile client with complex business orchestration logic. This leakage of domain logic and excessive interface exposure creates high coupling and fragile deployments.

## Decision
We adopt the **BFF (Backend-for-Frontend) Pattern** as a mandatory architectural seam for all mobile UI traffic. The BFF must act as the sole adaptation layer, enforcing domain boundaries and idempotency, ensuring that no business logic leaks into the mobile client and no core banking protocol details are exposed to the mobile interface.

## Consequences
- **Leverage**: Mobile teams gain a clean, client-optimized interface; backend teams gain freedom to evolve core APIs without mobile breakage.
- **Locality**: All client-specific orchestration (e.g., UX-driven composition, intent parsing) is concentrated within the BFF module.
- **Testability**: The BFF seam provides a perfect point for contract testing and mock injection, significantly simplifying mobile application UI testing.
- **Regulatory**: Centralized audit logging of mobile-triggered transactions at the BFF seam streamlines compliance reporting.
