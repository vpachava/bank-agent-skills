---
name: etl
owner: Solution Architecture
version: 0.1.0
last-reviewed: 2026-08-09
description: "Use when building a repeatable data movement & transformation pipeline for banking data — produces an ETL/ELT design (extract, load, transform, scheduling, lineage, reconciliation) that is auditable and idempotent."
required-inputs:
  - The sources, target, and the analytical/reporting purpose
  - Volume & refresh cadence (batch window vs streaming)
  - Data quality & reconciliation requirements
  - Compliance constraints (lineage/audit, residency, retention)
expected-deliverables:
  - ETL/ELT pipeline design (stages, scheduling, lineage)
  - Reconciliation & data-quality gates
  - Compliance posture (audit/lineage, residency, retention)
---

# /etl

## When to apply
Use when you're moving *and transforming* bank data on a recurring schedule — to a warehouse/lakehouse for analytics, regulatory reporting, or a downstream feed. Distinct from `/data-sync` (one system keeping a current mirror of another) — ETL is the *shaping-for-purpose* pipeline with its own scheduling, lineage, and audit. The home of regulatory-reporting feeds, where an unaudited pipeline is a compliance breach waiting.

## Inputs
- **Sources, target, and the analytical/reporting purpose** — what data, from where, to where, and for what (analytics, regulatory report, downstream feed).
- **Volume & refresh cadence** — batch window (with its deadline, e.g. pre-statement-run) vs streaming/ELT-on-arrival.
- **Data quality & reconciliation requirements** — what "correct" looks like and how it's verified (count checks, sum-reconciliation against the source, business-key completeness).
- **Compliance constraints** — audit/lineage (who/when each transformation ran and on what input), residency of the landed data, retention windows.

## Process

1. **Choose ETL vs ELT by where the transformation earns.** **ETL** (transform-then-load) when the source is sensitive and should be cleaned/masked *before* landing (e.g., PII de-scope before lakehouse). **ELT** (load-raw-then-transform) when you want the raw available for many downstream views and a powerful target (Iceberg/Delta/Hudi lakehouse) can do the transform cheaply. Land-then-curate has become the bank default for analytic estates.

2. **Model the pipeline as stages with idempotency + reconciliation gates at each.** Extract → Stage → Transform/Load → Quality-Gate → Publish. Each stage idempotent (re-run-able on a date/window without double-effect) and each gated by a reconciliation (count/sum/business-key completeness against the prior stage). An unaudited pipeline with no per-stage gates is a silent data-loss surface.

3. **Define reconciliation as the spine — not optional.** For any pipeline feeding regulatory reporting or ledgers: a sum-reconciliation per landed table against the source (`camt.053/054`-style statement vs ledger for payments) — the **regulatorily non-optional** check. For analytic pipelines: count & business-key completeness gates per stage. Reconciliation that nobody reads is theatre; alert on drift.

4. **Use idempotent UPSERT on the business key for re-runs.** A re-run of a window must not duplicate (regulatory reporting doubling every column because the pipeline re-ran — yes, this happens). UPSERT-on-business-key, never INSERT, and idempotency-keyed loads.

5. **Design lineage as a first-class output.** Every transformation logged with input hash/version, the transform logic version, the run id, the timestamp, the operator. Regulatory/reporting pipelines *must* be able to answer "what input, what logic, when, produced this figure" — that's lineage, and it's missing from most pipelines that later fail audit.

6. **Honor residency & retention at the landed layer.** Where the target sits (onshore vs free-zone) and the data's PII/payment classification dictates residency; the retention window per classification. An analytic lakehouse in a free-zone that ingests onshore medical/payment-adjacent data without the cross-zone SCC basis is a residency violation.

7. **Make money integer-minor-units through the whole pipeline.** Float arithmetic across millions of rows compounds to reconciliation-implausible drift; integers in minor units with explicit scale everywhere, with a single rounding policy at the *only* place it's permitted (e.g. display/reporting).

8. **Schedule for the deadline & the source-window.** A regulatory reporting batch that must publish pre-statement-run needs its extract window, transform window, gate window — and a failure-time catch-up policy. Schedule for the deadline; design for the catch-up.

## Banking pitfalls
- **No reconciliation gates** — a pipeline that loads whatever the extract gave with no count/sum/business-key check ships silent data loss or duplication; recon is the spine, especially for regulatory feeds.
- **Recon on count only** — "row counts match" while sums quietly drift (a row landed but truncated) passes the gate and fails the figure; sum-reconcile for money, business-key-completeness for entity data.
- **Regulatory pipeline without lineage** — when the regulator asks "what produced this figure and from what input," you need to answer; a pipeline that can't is an audit failure waiting.
- **Re-run as INSERT not UPSERT** — re-run a window without dedupe and the figure doubles; idempotent UPSERT on the business key + date/window key.
- **Float money across millions of rows** — compounding rounding drift breaks the downstream recon; integer minor units throughout, rounding only where designated.
- **Residency forgotten at the landing layer** — analytic target in a different zone than the source's data classification permits; treat the lakehouse's zone as a compliance decision.
- **ETL chosen where masking-before-land matters** — landing raw PII into a multi-tenant lakehouse then masking = a residency/PII-exposure window; transform-before-load for sensitive extracts.
- **No failure-catch-up policy** — a deadline-bearing batch that fails with only "retry manually" is an unrunnable reporting commitment; build catch-up into the schedule.

## Bulletproofing against Rationalization
To prevent data lake swamps and untraceable pipelines, you MUST:

1. **Mandatory Lineage Tracing:** The ETL design MUST show the explicit hop-by-hop lineage from Source System to Final Warehouse Table.
2. **PII Masking at Boundary:** You MUST document exactly where PII masking occurs (e.g., in-transit, at rest in the raw zone).
3. **Mandatory Failure Notifications:** ETL designs without explicit DLQ (Dead Letter Queue) or alerting paths for failed batches are rejected.
4. **Mandatory Idempotency and Rollback:**
   a. All transformation stages MUST use a business `idempotency-key` (UUID v4) on every job-run to ensure re-run safety.
   b. Consumers MUST implement a conflict-resolution strategy (first-wins, last-wins, merge).
   c. A formal rollback procedure must be documented for idempotency verification failure.

**Violating these rules invalidates the ETL Design.**

## Outputs
- **ETL/ELT pipeline design** — stages, ETL-vs-ELT call with rationale, scheduling, failure-catch-up policy.
- **Reconciliation & data-quality gates** — per stage, with alerting on drift.
- **Lineage design** — input-hash/logic-version/run-id/operator per transform.
- **Compliance posture** — residency & retention at the landed layer; cross-zone SCC basis where relevant.

## Related skills
- [data-sync](../data-sync/SKILL.md) — the near-real-time mirror cousin.
- [messaging](../messaging/SKILL.md) — when the feed crosses a bus.
- [observability](../../devops/observability/SKILL.md) — pipeline telemetry + drift alerting.
- [compliance](../../security/compliance/SKILL.md) — the regulatory-reporting obligations the pipeline feeds.
- [governance architecture-board](../../governance/architecture-board/SKILL.md) — the gate for a regulated-feed pipeline.
- [performance-review](../../devops/performance-review/SKILL.md) — for the batch-window/bottleneck design.

### Banking Context & Examples

#### (1) Regulatory Reporting ETL Example
**Scenario:** Building an ETL pipeline to aggregate transaction data for automated `CBUAE` regulatory reporting.
- **Architecture Lens Check:** Pipeline MUST guarantee data integrity ensuring no transaction record is dropped, and preserve original `UAEFTS` transaction identifiers.
- **Sample Outcome:** "Pipeline approved, supporting idempotent retry and mandatory audit-logging for all transformed records."
- **Common Pitfall:** Dropping transaction metadata during transformation, failing to meet the `CBUAE` auditable-trace requirement.

#### (2) AECB Batch Submission ETL Example
**Scenario:** Transforming local loan records into `AECB` submission formatted files.
- **Architecture Lens Check:** Validating PII data encryption and strictly enforcing the `AECB` schema definitions.
- **Common Pitfall:** ETL process introducing schema-mapping errors that lead to AECB submission rejection, requiring manual data adjustment (a high-risk compliance action).

#### (3) Sharia Product Amortization ETL Example
**Scenario:** ETL job calculating and generating the amortization schedules for Sharia-compliant personal loans.
- **Architecture Lens Check:** Sharia-compliance requires that amortization calculations use the bank's officially `Sharia-certified formula`.
- **Sample Outcome:** "ETL transformation logic validated against `Sharia-Governance-Book`."
- **Common Pitfall:** ETL pipeline applying a generic interest-accrual formula instead of the Sharia-compliant profit-rate formula, resulting in non-compliant customer repayment plans.
