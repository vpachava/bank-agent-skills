# Observability Design: CLI Automation Platform

## 1. Goal
Ensure 99.95% availability and auditability for regulated CLI journeys through structured, compliant telemetry.

## 2. Telemetry Strategy
- **Metrics (Prometheus/Grafana):** Focus on SLI tracking (API Latency, RPA Queue Depth, Success/Failure Rates).
- **Logs:** Structured logs, correlated via `correlationId` (UETR), NO PII/Card Data.
- **Traces (OTel):** Distributed tracing across AWS-Azure-Onprem boundaries.

## 3. Compliance & Security (Critical)
- **PII Scrubbing:** Telemetry pipeline will redact all sensitive information (card numbers, customer names) *before* ingestion into the central observability tool.
- **Residency:** Telemetry must be aggregated locally within the permitted zones unless otherwise authorized by compliance.

## 4. Key Metrics (SLIs)
| Metric | Source | Purpose |
| :--- | :--- | :--- |
| CLI Acceptance Latency | DEngage | UX monitoring |
| Final Credit Decision Time | RPA | Process efficiency |
| Fiserv Update Success | Middleware | Core/Reconciliation |
| DLQ Depth | MQ/Event Hub | Operational Resiliency |
