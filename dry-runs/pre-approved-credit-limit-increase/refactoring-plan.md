# Refactoring Plan: T24 R24 Upgrade

## 1. Domain API Refactoring (Channel Adapters)
- **Objective:** Normalize all channel-specific OFS interactions to 1x Domain API.
- **Approach:**
    - Standardize request/response payloads in a new Middleware Proxy.
    - Channel A -> Domain API -> Middleware Proxy -> T24 R24 API.
    - Implement correlation ID (UETR) for tracing all requests across the hop.

## 2. Product Module Migration (AA -> AC)
- **Objective:** Move account product codes/logic from AA to AC.
- **Approach:**
    - Define mapping table: AA_PRODUCT_CODE -> AC_PRODUCT_CODE.
    - Create automation script to patch existing account records in staging migration.
    - Perform shadow-calculation: Run interest/charges logic against both modules in parallel to validate accuracy.

## 3. Event-Driven Integration (T24 Emitter)
- **Objective:** Enable event emission from T24 R24 on data change.
- **Approach:**
    - Configure JMS/Event bus listeners within T24.
    - Middleware subscription model: Downstream system initiates subscription to specific event topics.
