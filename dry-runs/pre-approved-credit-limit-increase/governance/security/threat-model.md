# Threat Model: CLI Platform

## 1. Scope
Cross-cloud (AWS/Azure) credit limit increase journey for thick-file customers.

## 2. Boundaries & Flows (Sketch)
- **Trust Boundary A (Azure/RPA):** Orchestrates decisioning.
- **Trust Boundary B (AWS/Engagement):** API Gateway ↔ Internal Apps.
- **Data Flow:** Customer -> API GW -> Queue -> RPA -> Core(Fiserv).

## 3. STRIDE Threat Analysis

| Threat (STRIDE) | Finding | Severity | Mitigation |
| :--- | :--- | :--- | :--- |
| **Tampering** | API request modification (CLI amount) | High | Signatures / Azure AD tokens |
| **Info Disclosure**| PII/Card detail leakage in logs | Medium | Masking/Opaque IDs |
| **Elevation** | RPA identity escalation to Core | High | Least Privilege API Gateway |
| **Information** | Data residency leak across clouds | High | Network Segmentation / TLS |
| **Repudiation** | Consent log tampering | High | Immutable DB / Audit Logging |

## 4. Key Security Recommendations
1. **Azure AD:** Enforce short-lived, narrow-scope M2M tokens.
2. **Deep-links:** Must be signed and opaque; no PII in URL.
3. **Observability:** Telemetry path must not exfiltrate PII to AWS/Azure monitoring if restricted.
