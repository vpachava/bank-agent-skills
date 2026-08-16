---
name: observability
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when designing/reviewing observability for a banking solution — produces an observability design/review (metrics, logs, traces, OTel)."
required-inputs:
  - Banking domain/service context
  - Service-level objectives (SLOs)
  - Data-residency & security posture for telemetry data
  - Centralized observability-platform integration
expected-deliverables:
  - Observability design document (or audit-report)
  - Telemetry-strategy (Log/Metric/Trace-mapping)
  - Residency/Security-compliant telemetry-architecture
---

# /observability

## When to apply
Use when defining *how* a banking service reports its health. Observability in banking isn't just "logging errors" — it's proving compliance, tracing regulated-transactions across-systems, and meeting strict operational-resiliency targets.

## Inputs
- **Architecture context** — API-mesh, core-banking integration, event-flow.
- **Resiliency goals** — Target SLO/SLI percentages.
- **Security context** — Is the telemetry-stream capturing PII? How is it scrubbed?

## Process
1. **Define SLOs/SLIs.** What specifically triggers a Page-Alert in production? (e.g., latency SLIs on payment-processing threads).
2. **Telemetry Strategy (Log/Metric/Trace).**
   - Metrics: Prometheus/Grafana (SLI/throughput).
   - Logs: Structured, correlated-with-UETR (idempotency-key) + scrubbed-of-PII.
   - Traces: Distributed-tracing (OTel) across regulated-boundaries (mandatory for reconciliation).
3. **Residency/Security Audit of Streams.** Ensure the telemetry-pipeline itself doesn't violate residency laws (e.g., streaming prod-logs out-of-country).
4. **Integration with Central Platforms.** Mapping the service-telemetry into the bank's central SOC-SIEM-toolchain.
5. **Issue Design/Review.** Report on gaps or design strengths.

## Banking pitfalls
- **PII-telemetry-dump** — Logging PII/Card-data in plain-text to an observability tool that is not PII-compliant.
- **Trace-gap-on-regulated-paths** — Failing to trace payment-flows across legacy-interfaces, leaving un-auditable "dark-holes" in regulated transactions.
- **SLO-descoping** — Setting SLOs that hide reality (e.g., "Always-up" when the payment-gateway is failing 50% of the time, or the latency is ignored).
- **Cost-unwatched-scale** — Blindly logging every request-body to a managed observability-platform leading to catastrophic cloud-spend.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of observability meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the observability process.**

## Outputs
- **Observability design/audit-report** — The plan or review of the telemetry-architecture.
- **Telemetry-strategy** — Log/Metric/Trace mapping (what is captured where).
- **Residency/Security-compliant architecture** — Confirmed-compliant telemetry-pipeline.

## Related skills
- [sre-review](../sre-review/SKILL.md)
- [security-architecture-review](../../security/security-architecture-review/SKILL.md)
- [compliance](../../security/compliance/SKILL.md)
