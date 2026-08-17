---
name: observability
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when designing/reviewing observability for a banking solution â€” produces an observability design/review (metrics, logs, traces, OTel)."
required-inputs:
  - Banking domain/service context
  - Service-level objectives (SLOs)
  - Data-residency & security posture for telemetry data
  - Centralized observability-platform integration
expected-deliverables:
  - Observability design document (or audit-report)
  - Telemetry-strategy (Log/Metric/Trace-mapping)
  - Residency/Security-compliant telemetry-architecture
togaf-phases: [Phase G]
togaf-artifacts: [Compliance Checklist]
bian-service-domains: [Security.Auth]
---

# /observability

## When to apply
Use when defining *how* a banking service reports its health. Observability in banking isn't just "logging errors" â€” it's proving compliance, tracing regulated-transactions across-systems, and meeting strict operational-resiliency targets.

## Inputs
- **Architecture context** â€” API-mesh, core-banking integration, event-flow.
- **Resiliency goals** â€” Target SLO/SLI percentages.
- **Security context** â€” Is the telemetry-stream capturing PII? How is it scrubbed?

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
- **PII-telemetry-dump** â€” Logging PII/Card-data in plain-text to an observability tool that is not PII-compliant.
- **Trace-gap-on-regulated-paths** â€” Failing to trace payment-flows across legacy-interfaces, leaving un-auditable "dark-holes" in regulated transactions.
- **SLO-descoping** â€” Setting SLOs that hide reality (e.g., "Always-up" when the payment-gateway is failing 50% of the time, or the latency is ignored).
- **Cost-unwatched-scale** â€” Blindly logging every request-body to a managed observability-platform leading to catastrophic cloud-spend.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of observability meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the observability process.**

## Outputs
- **Observability design/audit-report** â€” The plan or review of the telemetry-architecture.
- **Telemetry-strategy** â€” Log/Metric/Trace mapping (what is captured where).
- **Residency/Security-compliant architecture** â€” Confirmed-compliant telemetry-pipeline.

## Related skills
- [sre-review](../sre-review/SKILL.md)
- [security-architecture-review](../../security/security-architecture-review/SKILL.md)
- [compliance](../../security/compliance/SKILL.md)

### Banking Context & Examples

#### (1) Cross-Border Payment Tracing Example
**Scenario:** Implementing observability for tracking cross-border `UAEFTS` payment flows.
- **Architecture Lens Check:** Verification that distributed traces include the unique `UETR` (Unique End-to-End Transaction Reference) for auditability.
- **Sample Outcome:** "Trace Design: OpenTelemetry headers propagate `UETR` across legacy/SaaS boundaries; logs correlated in ELK for end-to-end reconciliation."
- **Common Pitfall:** Tracing stops at the boundary of the legacy core-banking system; this creates a "dark hole" in the audit trail, preventing the bank from proving compliance when cross-border payments stall.

#### (2) Customer Data Access Auditing Example
**Scenario:** Observability for a service accessing residency-sensitive PII.
- **Architecture Lens Check:** Scrubbing of all `Emirates ID` and PII fields from telemetry logs *before* ingestion into the central observability tool (`Datadog`/`Splunk`).
- **Sample Outcome:** "Telemetry Strategy: All PII masked by `LoggingInterceptors` using regex `[a-zA-Z]{3}-\d{9}`; SIEM alerts on any unmasked pattern detection."
- **Common Pitfall:** Relying on 'security-by-configuration' in the observability tool instead of 'PII-scrubbing-at-source'. If a developer adds a new logging statement with PII, it hits the telemetry-hub before the masking rules trigger, immediately invalidating the bank's `PDPL` compliance posture.

#### (3) High-Frequency Trading Performance Example
**Scenario:** SLO/SLI definition for a high-frequency banking interface.
- **Architecture Lens Check:** Definition of `P99` latency SLOs for critical payment-approval endpoints, aligned with `CBUAE` operational targets.
- **Sample Outcome:** "SLO: 99.9% of payment-approval requests must complete within 200ms under peak load."
- **Common Pitfall:** Setting only 'Average' latency SLOs. In banking tech, P50 (average) latency often hides the P99 performance 'hiccups' that occur during peak `UAEFTS` hours, leading to silent service degradation for the highest-value transactions.

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
- **Logging raw or unmasked customer PII data in trace files**
  - **Consequence:** Violation of PDPL regulations and CBUAE compliance rules concerning data protection.
  - **Correct Approach:** Enforce a strict log-cleansing framework at the application layer to automatically redact credit card numbers, passwords, and IDs.
- **Setting up redundant or generic alerts, causing critical alerts to be missed**
  - **Consequence:** operational alert fatigue causing real incidents to be ignored.
  - **Correct Approach:** Define alert triggers based on customer impact metrics (SLOs) rather than generic CPU/Memory limits.
- **Lacking distributed trace identifiers across microservice boundaries**
  - **Consequence:** Extremely slow incident troubleshooting because requests cannot be traced across system boundaries.
  - **Correct Approach:** Implement trace headers correlation IDs (e.g. W3C Trace Context) in all API calls.
