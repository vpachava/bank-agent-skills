# ADR-0001: Orchestration Strategy for CLI Automation

- **Status:** Accepted
- **Date:** 2026-08-15
- **Deciders:** Solution Architecture Team
- **Tags:** orchestration, rpa, migration

## Context
The Credit Limit Increase (CLI) automation platform must be delivered quickly to meet business goals. The existing credit decision rules are already implemented within UiPath RPA, which is currently orchestrating the end-to-end journey. While the target architecture seeks to move decision logic into an enterprise Credit Engine (CE) for better manageability and reduced RPA dependency, doing so immediately would delay delivery and increase technical debt due to rule migration complexity.

## Decision drivers
- **Time-to-market:** Pre-approved CLI MVP is urgent.
- **Rule Consistency:** Existing rules are proven in RPA; migrating them now risks discrepancies.
- **Future-proofing:** The architectural design must allow for the eventual migration of rules logic from RPA to a dedicated Credit Engine without major changes to the customer journey or integration contracts.

## Considered options
- **Option A — Full Orchestration & Rules in RPA:** Keep all orchestration and decision rules in UiPath RPA (Current Proposal). *Pros: Fast delivery, leverages existing rules. Cons: RPA as long-term system of record/decisioning.*
- **Option B — Immediate Migration to Credit Engine:** Migrate all rule logic to a new Credit Engine immediately in Phase 1. *Pros: Cleaner architecture. Cons: High risk of delay and rule mismatch.*
- **Option C — Hybrid Orchestration (Adopted):** Keep orchestration and current rules in RPA for Phase 1, but standardize API contracts to ensure Credit Engine integration and eventual rule migration are modular.

## Decision
We choose **Option C — Hybrid Orchestration**. RPA will remain responsible for orchestration and credit-rule execution for Phase 1. However, APIs between RPA, Digital Engagement, and Credit Engine will be designed as enterprise-grade REST services. This modularity ensures we can replace RPA's rule-execution role with the Credit Engine in future phases using the established API contracts.

## Consequences
- **Gains:** Faster delivery of MVP; clear path to target architecture (Credit Engine).
- **Penalties / costs:** Continued dependency on RPA; maintenance of two "decision" environments during the migration window.
- **Accepted regulatory exposure:** The current reliance on RPA for decision-logic auditability must be compensated by rigorous RPA logging and reconciliation between RPA's state and system-of-record entities (Fiserv/DWH).
- **Reversibility cost:** Medium; depends on the stability of the API contracts defined in Phase 1.

## Links
- Acceptance gate: Enterprise Architecture Review - 2026-08-15
