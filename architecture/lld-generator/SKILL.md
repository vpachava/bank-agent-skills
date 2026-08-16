---
name: lld-generator
owner: Solution Architecture
version: 0.1.0
last-reviewed: 2026-08-08
description: "Use when an HLD is approved and the build needs detail — produces a Low-Level Design (component APIs, data, sequences, deployment) that an engineering team can implement against."
required-inputs:
  - Approved High-Level Design (/hld-generator)
  - Open-questions register from the HLD
  - Current-system API/schema inventory (legacy core, channels, partners)
  - NFR checklist (/nfr-checklist) at completion
expected-deliverables:
  - Low-Level Design document (component + API + data + sequence + deployment detail)
  - API contracts (sketches) per component
  - Deployment view (delegates to /deployment-diagrams)
  - Resolved open-questions register (reflected back to the HLD if they change shape)
---

# /lld-generator

## When to apply
Use after the HLD is reviewed and tentatively approved — the LLD commits the *detail*: component APIs, data structures, the sequence-level interactions, and deployment. This is the altitude the build team works to. Feeds the build, the design review (`/design-review`), and release readiness.

## Inputs
- **Approved HLD** — the shape that the LLD deepens; if the HLD is shaky, the LLD inherits the shakiness — fix the HLD first.
- **Open-questions register** — the decisions suspended at HLD altitude; resolve them here.
- **Current-system API/schema inventory** — legacy core operations, channel APIs, partner contracts; the LLD designs *against* and *around* these, not over them.
- **NFR checklist** — at completion level so the LLD commits perf, residency, audit, security specifics.

## Process
1. **Decompose containers into components.** Each HLD container becomes its components with clear responsibilities (orchestrator, adapter, validator, gateway). Name each component, its responsibility, the container it lives in — and the BIAN Service Domain if relevant.

2. **Define each component's API contract.** Operation, inputs, outputs, errors, idempotency (critical for payments/KYC steps), authz. Use a contract-first sketch (OpenAPI/Async), at LLD altitude — not a code-gen file necessarily. Mark regulated operations distinctly.

3. **Specify the data model & persistence.** Per store: schema sketch, ownership, residency (onshore/free-zone), retention, the integrity guarantees (ACID, eventual, reconciliation-backed). Mark PII/biometric/payment data and its residency explicitly.

4. **Detail the key flows to sequence depth.** Take the HLD's key flows and produce real sequence diagrams (delegate to `/sequence-diagrams` rendered by `/archify`): every actor, every call, every regulated gate, every fallback/exception path. The sequence diagram is where hidden assumptions surface (retry, timeout, reconcile, escalate).

5. **Resolve the HLD's open questions — or escalate.** Each suspended decision in the open-questions register resolves with a concrete answer *or* escalates to a new decision (ADR / `/solution-options`). Don't carry open questions silently into the build.

6. **Commit the deployment view.** Regions, AZ pairing, HA/DR, the landing-zone topology (delegate to `/deployment-diagrams`). Capture cross-region and the cross-zone (onshore ↔ DIFC/ADGM) data-residency implications — the SCC/BCR point from the UAE research if it applies.

7. **Map NFRs to design decisions.** Each completed NFR traces to a design decision in the LLD (a retry policy, a residency choice, a cache tier). NFRs with no design backing are aspirations.

8. **Cross-check against current-system contracts.** The LLD must fit the legacy core's actual interfaces, the partner contracts, the channel SDKs — not a wished-for version. Any seam that needs a new adapter or a strangler cut is flagged for `/application-migration`.

## Bulletproofing against Rationalization
To prevent leaky LLDs that ignore idempotency, error states, and data residence constraints, you MUST:

1. **Mandatory Idempotency Constraint:** All APIs that execute state changes (payments, issuance, originations) MUST explicitly define an idempotency header/key. Without this, the LLD fails the design gate.
2. **Mandatory Exception Path Modeling:** Sequence layouts MUST include the negative paths (`alt` blocks for timeout, reject, rollback, escalate). Happy-path-only sequences are strictly prohibited.
3. **Mandatory Data Residency Tagging:** Each data physical store defined in the LLD MUST explicitly state its residency classification (e.g., Onshore, DIFC). "Deferred to deployment" is an invalid response.
4. **Mandatory Legacy Interface Contract Mapping:** Do not hallucinate generic REST/JSON APIs for legacy systems. Explicitly map how the LLD integrates with the actual legacy interfaces (e.g., T24 OFS strings, SOAP).
5. **Mandatory Reconciliation Rules:** Financial and ledger-affecting components MUST explicitly define reconciliation and DLQ handling paths.

**Violating these rules invalidates the Low-Level Design.**
---

## Outputs
- **LLD document** — components + responsibilities + APIs + data + sequences + deployment + NFR-to-design mapping + resolved open questions.
- **API contract sketches** — per component, with idempotency, authz, and regulated-op markers.
- **Deployment view** — via `/deployment-diagrams`, with residency/cross-zone implications.
- **Sequence diagrams** — via `/sequence-diagrams` rendered by `/archify`, incl. exception paths.
- **Resolved open-questions register** — and any escalations to ADR / `/solution-options`.

## Related skills
- [hld-generator](../hld-generator/SKILL.md) — the altitude this deepens.
- [c4-model](../c4-model/SKILL.md) — the component-level (Level 3) C4 view.
- [sequence-diagrams](../sequence-diagrams/SKILL.md) — the sequence detail this commits.
- [deployment-diagrams](../deployment-diagrams/SKILL.md) — the deployment view.
- [api-design](../../integration/api-design/SKILL.md) — the contract-design discipline this leans on.
- [design-review](../../governance/design-review/SKILL.md) — the gate this LLD passes through.
- [application-migration](../../migration/application-migration/SKILL.md) — where legacy-core seams get migrated.
