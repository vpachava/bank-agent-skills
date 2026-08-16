# NFR Baseline: CLI Automation Platform
Status: Must vs Should as indicated. Measured targets provided for all.

| Category | Requirement | Measured Target | Source | Owner | M/S | Design Trace |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Availability** | Platform Availability | 99.95% | Business | SRE | Must | Multi-zone/Cloud + Orchestrator |
| **Performance** | API Latency (p95) | < 500ms | UX/Ops | Architect | Should | Caching / Lightweight API |
| **Performance** | Throughput | 3,000 offers/week | Business | Ops | Must | Batch ingestion / MQ |
| **Residency** | Data Residency | UAE Onshore | Reg | Compliance| Must | Secure Connectivity |
| **Residency** | AECB 30-day Reuse | AECB Data Usage | Reg/AECB | Risk | Must | Decisioning Service |
| **Security** | Auth | OAuth2/mTLS | Security | Security | Must | Azure AD + Certs |
| **Auditability**| Consent Audit | 7-year Retention | Reg/Audit | Audit | Must | DB/DMS Storage |
| **Capacity** | Scalability | 10k offers/week (headroom) | Ops | Architect | Should | Kafka/Event Hub |

## NFR Tensions (Resolving to ADRs)
- **Latency vs. Consistency:** High consistency requirement (limit update must be final) takes precedence over low-latency UI.
- **Residency vs. Cross-Cloud Complexity:** Strictly enforced UAE residency adds network overhead (connectivity/firewalling) between AWS/Azure components.
