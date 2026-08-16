---
name: performance-review
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when designing/running a banking performance review — produces a performance-report (load, capacity,瓶颈, NFR-anchored)."
required-inputs:
  - Banking workload/transaction-profile
  - Peak/Average load metrics
  - NFR definitions (latencies/throughput)
  - Testing infrastructure definition
expected-deliverables:
  - Performance-evaluation report
  - Capacity & bottlenecks-map
  - Performance-NFR-compliance verdict
---

# /performance-review

## When to apply
Use to mathematically prove that a banking service can handle the required business-scale without failure. In banking, performance *is* reliability; poor performance leads to missed trade-windows, rejected payments, and regulatory-penalties.

## Inputs
- **Workload Profile** — TPS(Transactions-per-second) vs concurrent-users vs data-volume profiles.
- **NFR Target** — Acceptable latency at p99-levels (e.g. "Payment-auth sub-200ms at 1000 TPS").

## Process
1. **Define Load-Test Profile.** Tailor the test to reality, not a best-case estimate (e.g. include realistic DB-contention).
2. **Execute Load/Capacity Testing.** Stress the system *beyond* peak-load to identify the breaking-point (Bottleneck-analysis).
3. **Analyze Resource Utilization.** Where are the constraints? (CPU-spikes, DB-locking, memory-leaks, I/O-saturation).
4. **Resiliency/Performance Check.** How does performance hold up during a simulated partition or partial-failure?
5. **Issue Compliance Verdict.** Does it fulfill the banking-NFRs?

## Banking pitfalls
- **Unrealistic-Load-Test** — Testing a "static-API-call" rather than an "end-to-end-authenticated-payment-flow" including the legacy-core integration.
- **Ignoring-DB-contention** — Testing high-TPS read-performance while ignoring that the shared-core-DB will lock under high-TPS writes.
- **Capacity-forecasting-blindness** — Not modeling the *growth* over 12/24 months, leaving the platform prone to early-life performance-failures.
- **Latency-as-average** — Optimizing for *average* performance while ignoring the p99-tails that cause poor user-experience for banking-customers.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of performance-review meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the performance-review process.**

## Outputs
- **Performance-evaluation report** — Analysis of load-results and test-setup.
- **Capacity & bottlenecks-map** — The identified resource-limits.
- **Performance-NFR-compliance verdict** — Final Go/No-go on performance goals.

## Related skills
- [nfr-checklist](../../architecture/nfr-checklist/SKILL.md)
- [observability](../observability/SKILL.md)
- [hld-generator](../../architecture/hld-generator/SKILL.md)
