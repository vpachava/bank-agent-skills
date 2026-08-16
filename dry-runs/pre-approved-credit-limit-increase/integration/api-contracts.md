# API Contract: CLI Platform

## 1. Overview
The platform exposes critical CLI functionality across multi-cloud (AWS/Azure) environments.
- **Standards:** REST for synchronous orchestration, Async-API (MQ/Event Hub) for business state transitions.

## 2. API Catalogue (Illustrative)

### API 1: Digital Engagement to RPA (Consent Callback)
- **Endpoint:** `POST /cli/v1/consent`
- **Purpose:** Notify RPA of customer acceptance and secure consent.
- **Idempotency:** Required (`correlationId`).
- **Auth:** Azure AD (OAuth2 - Client Credentials/M2M).
- **Security:** Audit-logged, scoped access.

```json
{
  "correlationId": "uetr-12345-6789-abc",
  "customerId": "CIN-001",
  "offerId": "OFFER-99a",
  "consentTimestamp": "2026-08-15T10:00:00Z",
  "signature": "..."
}
```

### API 2: RPA to Credit Engine (Credit Summary Request)
- **Endpoint:** `POST /cli/v1/credit-summary`
- **Purpose:** Request final bureau credit fields.
- **Idempotency:** Required (`rpaReferenceId`).
- **Auth:** Azure AD.

```json
{
  "rpaReferenceId": "RPA-REF-555",
  "customerId": "CIN-001",
  "productType": "CREDIT_CARD"
}
```

### API 3: Middleware to Fiserv (Limit Update)
- **Endpoint:** `POST /fiserv/v1/limit-update` (Async via MQ)
- **Purpose:** Execute credit limit change in legacy core.
- **Idempotency:** UETR/Clerk-ID.

---
## 3. Security & Idempotency Model
- **Idempotency:** Every side-effecting operation (Consent, Credit Request, Limit Update) REQUIRES a `correlationId` (UETR-style).
- **Auth:** All service-to-service calls use Azure AD M2M tokens, scoped per operation.
- **PII:** Opaque IDs (`correlationId`/`rpaReferenceId`) used in all external/async messaging.
