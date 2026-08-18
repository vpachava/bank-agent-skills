# Analytics Design: bank-agent-skills

## Goal
Implement operational monitoring for `bank-agent-skills` using the existing shared ELK stack.

## Architecture & Instrumentation
- **Mechanism:** Decorator-based instrumentation on skill entry/exit.
- **Data Shipping:** Log-based ingestion using Filebeat.
- **Configurability:** Externalized config (e.g., `.env` or `config.yaml`) for log paths, sampling rates, and ELK indices.

## Event Schema
```json
{
  "timestamp": "ISO8601",
  "skill_name": "string",
  "status": "success/failure",
  "duration_ms": "float",
  "correlation_id": "uuid",
  "metadata": "json_blob"
}
```

## Privacy
- **PII Scrubbing:** All input/output parameters are strictly excluded from logs. Only metadata (`skill_name`, `status`, `duration`) is logged.

## Dashboarding (Kibana)
- **Success Rate:** High-level gauge.
- **Latency Distribution:** Histogram of `duration_ms`.
- **Top Invocations:** Bar chart of `skill_name` frequency.
