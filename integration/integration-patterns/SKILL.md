---
name: integration-patterns
owner: Solution Architecture
version: 0.1.0
last-reviewed: 2026-08-09
description: "Use when a banking scenario needs the right integration pattern chosen â€” produces a scoped integration-patterns selection (gateway / ACL / strangler / saga / sync-async / idempotency) with rationale per integration seam."
required-inputs:
  - The integration seam & the systems across it
  - Trust tier & regulatory posture of the seam
  - Whether it's modernization (strangler) or greenfield integration
  - Reliability & latency requirements
expected-deliverables:
  - Selected integration pattern(s) per seam with rationale
  - Pattern catalog entry (the seam, the chosen pattern, the alternatives rejected, the traps)
  - Cross-references to the deeper skills when the seam needs ETL / event / sync
togaf-phases: [Phase C]
togaf-artifacts: [HLD]
bian-service-domains: [Integration.API]
---

# /integration-patterns

## When to apply
Use when the *shaping* of an integration is the question â€” which pattern across the seam â€” rather than the detail of one (API contract â†’ `/api-design`; event model â†’ `/event-driven`; transport â†’ `/messaging`; batch pipeline â†’ `/etl`). This skill is the *picker*: it picks the surrounding pattern(s) and hands off to the detail skill. Feeds `/hld-generator` and `/solution-options`.

## Inputs
- **The integration seam** â€” what system talks to what, across what trust boundary / legacy / partner boundary.
- **Trust tier & regulatory posture** â€” internal / partner / public; whether regulated data flows across the seam.
- **Modernization vs greenfield** â€” a seam over a legacy core differs from a brand-new inter-service seam (strangler & ACL matter for legacy).
- **Reliability & latency requirements** â€” sync-required vs async-OK, ordering, idempotency.

## Process

1. **Characterize the seam.** Across a trust boundary (partner/public)? Over a legacy core? Service-to-service within one boundary? Data-flow (not call)? The seam's character rules out most patterns immediately.

2. **Overlay a legacy core â†’ reach for Anti-Corruption Layer + Strangler + Facade.** When the seam crosses a legacy core: put a faÃ§ade/API gateway in front (route traffic through one controllable boundary), an Anti-Corruption Layer behind it (translate core's grit into the consuming domain's clean model â€” your domain never inherits the core's table grudges), and phase replacement via strangler (route incrementally to the new path, retire the old).
   > Never big-bang the core. The seam design *is* the legacy migration's safety â€” faÃ§ade + ACL + strangler.

3. **Match the seam to a pattern, then to a detail skill.**
   - **Sync command over internal seam** â†’ API contract (`/api-design`).
   - **Status/recon or fire-and-react** â†’ event + Async-API (`/event-driven`, `/messaging`).
   - **Two-system current-view** â†’ CDC-based sync (`/data-sync`).
   - **Scheduled analytic/reporting movement** â†’ ETL/ELT (`/etl`).
   - **Long-running multi-step with compensations** â†’ saga (chosen here, detailed in the flow's `/lld-generator`).
   - **Partner / public** â†’ API + FAPI2/authn/authz + rate-limitation (`/api-design` + `/security-architecture-review`).

4. **Choose sync vs async per operation, not per system.** A system can expose a sync command API and an async event feed simultaneously; decide per operation whether the caller needs the result synchronously (command, sync) or can react later (event, async). Forcing everything sync chains the bottleneck; forcing everything async loses the command/response contract.

5. **Orchestrate RPA as a Microservice.** For legacy seams that lack APIs, wrap RPA agents as a microservice faÃ§ade: 
    - Expose standard Sync/Async API wrappers for the RPA process.
    - Decouple RPA agent lifecycle from API request lifecycle via persistent queuing.
    - Implement robust error handling (RPA step retry) and reconciliation.
    - **Regulatory Context:** All RPA-orchestrated flows involving regulated data MUST be tagged for Data Lineage (`/compliance`) to ensure auditability of automated actions.

6. **Where multi-step across services, choose saga vs orchestration.** A saga coordinates multi-service steps with compensating actions for failure (no distributed lock); pick choreographed saga (event-driven) for decoupled reactions; orchestrated saga (central flow) where accountability for the regulated spine matters. The bank default for regulated journeys: orchestrated-with-sagas-for-the-partials.

6. **Specify idempotency & reconciliation at every cross-seam.** No matter the pattern, the cross-seam carries an idempotency key (UETR-style) and a reconciliation path (statement-vs-ledger for money). Cross-seam interactions without these are where money goes wrong.

7. **Document the alternative rejected and the trap it avoided.** The pattern catalog entry is most valuable when it states: *we chose X (not Y), because Z, and Y's trap was W*. The rejected alternative is at least as instructive as the choice.

## Banking pitfalls
- **No seam characterization** â€” picking a pattern before understanding whether the seam crosses a trust boundary, a legacy core, or synchronous-time-critical flow; wrong seam â†’ wrong pattern.
- **Big-bang across a legacy core** â€” replacing the core's seam without faÃ§ade + ACL + strangler; the migration is unsafe, the new path can't be progressively cut, and rollback is a re-deploy everything.
- **Everything sync â†’ chained bottleneck** â€” the core is already the bottleneck; new sync calls through it compound the stall; let status/recon flow async where the caller doesn't need it synchronously.
- **Everything async â†’ no command/response contract** â€” callers who need the result treated as event-subscribers; over-async erases the call/response contract and breaks ORMs/tests.
- **Saga without compensations** â€” multi-service flow that only has forward steps; a failure mid-saga leaves inconsistent state (issued-but-not-debited); every step needs a compensating action.
- **Cross-seam without idempotency/recon** â€” where duplicated requests double-effect and where drift goes uncaught; bake UETR-style idempotency + statement-vs-ledger recon at every seam.
- **Anti-Corruption Layer skipped "for speed"** â€” letting the core's nouns (its table structure, its decades-accumulated field connotations) leak straight into a modern service; the leak is forever and locks every consumer.
- **Pattern chosen without documenting the rejected alternative** â€” six months later nobody remembers why the obvious-synchronous call is async; record it (an ADR, or the catalog entry's "rejected because" line).

## Bulletproofing against Rationalization
To prevent anti-patterns masquerading as "enterprise integration," you MUST:

1. **Mandatory Sync/Async Clear Boundary:** The pattern MUST explicitly justify why sync or async was chosen. Defaulting to sync for convenience is rejected.
2. **Mandatory Circuit Breaker Context:** All synchronous call patterns MUST explicitly define circuit breaker / timeout thresholds.
3. **Mandatory Legacy Coupling Check:** The pattern MUST explicitly document if it introduces tight coupling to a legacy core system's data model.

**Violating these rules invalidates the Integration Pattern.**

## Outputs
- **Selected integration pattern(s) per seam** â€” with rationale + the rejected alternative + trap avoided.
- **Pattern catalog entry** â€” seam description, chosen pattern, deeper-skill handoff (`/api-design`, `/event-driven`, `/etl`, `/data-sync`).
- **Idempotency & reconciliation requirements** â€” per seam, even if handed off to a detail skill.

## Related skills
- [api-design](../api-design/SKILL.md) â€” sync-command seams.
- [event-driven](../event-driven/SKILL.md) â€” async / saga-choreography seams.
- [messaging](../messaging/SKILL.md) â€” the transport.
- [data-sync](../data-sync/SKILL.md) â€” CDC / current-view seams.
- [etl](../etl/SKILL.md) â€” batch / reporting seams.
- [application-migration](../../migration/application-migration/SKILL.md) â€” strangler-figging the curated legacy seam.
- [hld-generator](../../architecture/hld-generator/SKILL.md) â€” the seam choices embed in the HLD.

### Banking Context & Examples

#### (1) Legacy Core Integration Pattern Example
**Scenario:** Modernizing the customer-facing `Mobile-App` by modernizing access to the `Legacy-Core-Banking-System`.
- **Integration Choice:** [FaÃ§ade + ACL (Anti-Corruption Layer) + Strangler-Fig]. 
- **Rationale:** Protects the new mobile architecture from the legacy core's inconsistent schema (ACL), provides a unified entry point (FaÃ§ade), and allows iterative migration (Strangler).
- **Reject Alternative:** [Direct-Database-Connect]. Rejected because it bypasses legacy business rules and creates unacceptable operational risk.
- **Trap Avoided:** Tightly coupling the new portal to legacy table structures, which would require re-modernization later.

#### (2) Sharia Payment Processing Pattern Example
**Scenario:** Coordinating a multi-step `Sharia-Compliant Payment` journey across payment, accounting, and Sharia-certification services.
- **Integration Choice:** [Orchestrated-Saga].
- **Rationale:** The journey requires strict consistency (Sharia-compliance checks + fund movement). An orchestrator holds the state and manages mandatory compensating actions if Sharia-certification fails.
- **Trap Avoided:** Choreographed saga (event-driven) which might struggle to provide the *guaranteed* finality status of the Sharia-compliant product, increasing compliance audit overhead.

#### (3) AECB Reporting Integration Pattern Example
**Scenario:** Sending transaction data for AECB reporting every 24 hours.
- **Integration Choice:** [Outbox-Pattern + ETL-Batch].
- **Rationale:** Ensures transaction atomicity by writing to an 'outbox' in the local database as part of the transaction, which is later securely harvested for batch ETL submission. This satisfies both transactional integrity (banking requirement) and batch-submission (AECB requirement).
- **Common Pitfall:** Using direct synchronous REST calls for the AECB submission, creating unnecessary latency and coupling to the availability of the AECB endpoint.

## Bulletproofing
- **Governance Policy:** Enforce [CBUAE Rulebook](governance/policy/regulations.yaml#CBUAE), [PDPL](governance/policy/regulations.yaml#PDPL), and [PCI-DSS](governance/policy/regulations.yaml#PCI-DSS) where applicable.

## Anti-patterns
- **Adopting a sprawling 'spaghetti' architecture of pure point-to-point API connections**
  - **Consequence:** Maintenance nightmares, extreme fragility during upgrades, and inability to trace transaction flows.
  - **Correct Approach:** Implement Hub & Spoke patterns, API Gateways, or Event Brokers to centralize routing, security, and logging.
- **Applying pattern architectures like Enterprise Service Buses (ESB) where simple APIs suffice**
  - **Consequence:** Over-engineering that creates a deployment bottleneck and slows developer velocity significantly.
  - **Correct Approach:** Use lightweight API Gateways or direct GraphQL aggregators instead of heavyweight middleware routing engines.
- **Failing to implement circuit breakers on synchronous downstream integrations**
  - **Consequence:** Complete cascading failure where a slow downstream partner crashes the entire internal ecosystem.
  - **Correct Approach:** Wrap synchronous calls in Circuit Breaker patterns to fast-fail when thresholds are breached.
