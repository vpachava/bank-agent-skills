---
name: performance-review
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when designing/running a banking performance review â€” produces a performance-report (load, capacity,ç“¶é¢ˆ, NFR-anchored)."
required-inputs:
  - Banking workload/transaction-profile
  - Peak/Average load metrics
  - NFR definitions (latencies/throughput)
  - Testing infrastructure definition
expected-deliverables:
  - Performance-evaluation report
  - Capacity & bottlenecks-map
  - Performance-NFR-compliance verdict
togaf-phases: [Phase G]
togaf-artifacts: [Compliance Checklist]
bian-service-domains: [Security.Auth]
---

# /performance-review

## When to apply
Use to mathematically prove that a banking service can handle the required business-scale without failure. In banking, performance *is* reliability; poor performance leads to missed trade-windows, rejected payments, and regulatory-penalties.

## Inputs
- **Workload Profile** â€” TPS(Transactions-per-second) vs concurrent-users vs data-volume profiles.
- **NFR Target** â€” Acceptable latency at p99-levels (e.g. "Payment-auth sub-200ms at 1000 TPS").

## Process
1. **Define Load-Test Profile.** Tailor the test to reality, not a best-case estimate (e.g. include realistic DB-contention).
2. **Execute Load/Capacity Testing.** Stress the system *beyond* peak-load to identify the breaking-point (Bottleneck-analysis).
3. **Analyze Resource Utilization.** Where are the constraints? (CPU-spikes, DB-locking, memory-leaks, I/O-saturation).
4. **Resiliency/Performance Check.** How does performance hold up during a simulated partition or partial-failure?
5. **Issue Compliance Verdict.** Does it fulfill the banking-NFRs?

## Banking pitfalls
- **Unrealistic-Load-Test** â€” Testing a "static-API-call" rather than an "end-to-end-authenticated-payment-flow" including the legacy-core integration.
- **Ignoring-DB-contention** â€” Testing high-TPS read-performance while ignoring that the shared-core-DB will lock under high-TPS writes.
- **Capacity-forecasting-blindness** â€” Not modeling the *growth* over 12/24 months, leaving the platform prone to early-life performance-failures.
- **Latency-as-average** â€” Optimizing for *average* performance while ignoring the p99-tails that cause poor user-experience for banking-customers.

## Bulletproofing
- **Governance Policy:** Enforce [CBUAE Rulebook](governance/policy/regulations.yaml#CBUAE), [PDPL](governance/policy/regulations.yaml#PDPL), and [PCI-DSS](governance/policy/regulations.yaml#PCI-DSS) where applicable.

## Outputs
- **Performance-evaluation report** â€” Analysis of load-results and test-setup.
- **Capacity & bottlenecks-map** â€” The identified resource-limits.
- **Performance-NFR-compliance verdict** â€” Final Go/No-go on performance goals.

## Related skills
- [nfr-checklist](../../architecture/nfr-checklist/SKILL.md)
- [observability](../observability/SKILL.md)
- [hld-generator](../../architecture/hld-generator/SKILL.md)

### Banking Context & Examples

#### (1) Retail Payment Flow Performance Example
**Scenario:** Performance testing for high-volume retail payment processing.
- **Architecture Lens Check:** Simulation of realistic locking contention on the shared ledger database during peak `UAEFTS` operational hours.
- **Sample Outcome:** "Performance-Evaluation Report: p99 latency increased to 450ms at 2x peak load due to row-level locking on the `Transaction_Ledger` table."
- **Common Pitfall:** Testing against a 'clean' development database. This fails to surface the locking/concurrency issues that arise in the production ledger when 50+ services attempt simultaneous payment-record commits.

#### (2) AECB Credit Query Load Example
**Scenario:** Performance review for a real-time credit card origination service.
- **Architecture Lens Check:** Validating system response times when an `AECB` inquiry latency spikes to >5 seconds.
- **Sample Outcome:** "Capacity & Bottleneck-Map: Service relies on synchronous `AECB` call; 5s spike causes thread-pool exhaustion."
- **Common Pitfall:** Assuming `AECB` API is always fast. Performance reviews must explicitly test (and handle) third-party provider latency spikes, or the mobile banking app stops responding for all users.

#### (3) Sharia-Compliant Amortization Calculation Example
**Scenario:** Stress testing for a new Sharia loan product origination.
- **Architecture Lens Check:** Evaluating the performance of the complex `Amortization Schedule` logic during batch processing.
- **Sample Outcome:** "Performance-Evaluation Report: Calculation engine scales linearly (CPU-bound) for 10k concurrent loan origination requests."
- **Common Pitfall:** Underestimating the computational load of Sharia-compliant financial calculations (often iterative `Profit-Calculation-Algorithms`) in batch, leading to missed execution-windows in core processing hours.

### Banking Context & Examples

#### (1) Retail Banking Scenario
**Scenario:** Applying this skill in a retail bank core-modernization effort.
- **Architecture Lens Check:** Verification of compliance with CBUAE data-residency rules (e.g. [[compliance]]).
- **Sample Outcome:** "Design: Automated workflow integration; [[observability]] logs scrubbed of PII."
- **Common Pitfall:** Ignoring the Sharia-governance impact on the product-schema.

#### (2) Corporate Banking Scenario
**Scenario:** Using this skill for a corporate digital-onboarding integration.
- **Architecture Lens Check:** Alignment with AECB credit-reporting integration for legal-entity applicants.
- **Sample Outcome:** "Design: Integration-seam validated for high-assurance KYC; [[api-design]] handles large payload-signatures."
- **Common Pitfall:** Bypassing the mandatory legal-entity KYC check due to tight project timelines.

#### (3) Islamic Banking Scenario
**Scenario:** Utilizing this skill for Sharia-compliant loan product rollouts.
- **Architecture Lens Check:** Sharia-Board approval workflow documented within the [[architecture-decision-records]].
- **Sample Outcome:** "Design: Profit-distribution calculation encapsulated; [[api-design]] schema includes mandatory Sharia-compliance flag."
- **Common Pitfall:** Applying standard interest-based loan models to Islamic products, violating compliance.

### Regulatory References
1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/
2. **PDPL:** Personal Data Protection Law (Federal Decree-Law No. 45 of 2021)
3. **CBUAE Cybersecurity Framework:** Domain 1: Governance & Risk Management

## Anti-patterns
- **Running performance tests using simple, hot mock databases**
  - **Consequence:** Under-predicting latency by ignoring database locks and disk IO barriers.
  - **Correct Approach:** Test using realistic data distributions, mock latency on dependencies, and actual production scale databases.
- **Testing transaction performance purely at 100% capacity without spike simulation**
  - **Consequence:** Server crashes during unpredictable traffic spikes.
  - **Correct Approach:** Run stress tests, endurance runs, and sudden step-up spike workloads to identify bottleneck points.
- **Ignoring performance metrics and thread locks on legacy integration points**
  - **Consequence:** System failure because legacy systems freeze under load.
  - **Correct Approach:** Put down strict thread limits, queues, and connection timeouts on legacy system integrations.
