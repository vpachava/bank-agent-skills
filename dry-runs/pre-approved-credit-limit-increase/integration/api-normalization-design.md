# API Normalization Design: T24 R24

## 1. Goal
Consolidate fragmented channel OFS interactions into a unified Domain API layer while exposing data changes as events.

## 2. API Contract (Domain Layer)
- **Standardized Payload:** All requests normalized to a Domain-specific JSON contract. 
- **Mapping Engine (Middleware):** The middleware is responsible for taking the standardized request and mapping it to the specific T24 R24 API command (REST or OFS-facade).

## 3. Event-Driven Emission (T24 Data Changes)
- **Mechanism:** T24 R24 natively emits events on data changes (e.g., account balance update, product change).
- **Architecture:** T24 -> Event Bus (e.g., Kafka) -> Event-Driven Middleware -> Subscribers (Channels).
- **Constraints:** 
    - No direct T24 database access.
    - All data changes must be emitted as domain events.

## 4. Normalization Strategy (Middleware Proxy)
The middleware acts as the translation layer:
1. Receives normalized request from Domain API.
2. Identifies legacy channel request type.
3. Translates to T24 R24 API command.
4. Performs AA to AC product translation (if applicable).
