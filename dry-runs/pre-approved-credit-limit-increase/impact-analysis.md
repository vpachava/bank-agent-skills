# T24 Modernization Impact Analysis (R18 -> R24)

## Overview
This assessment evaluates the architectural shift from legacy file-based and multiple-OFS interface integration to a unified Domain API layer with event-driven data emission in T24 R24.

## Key Impacts

### 1. Integration Paradigm Shift
- **Legacy:** File sharing (flat files) and multiple, channel-specific OFS versions used for T24 interactions.
- **Modern:** API-first approach. All interaction must occur via a single Domain API.
- **Impact:** High. Channel adapters must be refactored to support the new API contract. Legacy file parsers will be deprecated.

### 2. Module Re-platforming (AA to AC)
- **Legacy:** Product codes managed under the older AA module.
- **Modern:** Migration to the AC module environment.
- **Impact:** Critical. All product definitions, interest calculations, and account lifecycle management routines must be reviewed for compatibility. AA-to-AC migration scripts and state mapping are mandatory.

### 3. Event-Driven Evolution
- **Modern:** T24 now emits events upon data changes.
- **Impact:** Positive. Enables decoupling of downstream systems. Middleware must support event subscription models, potentially requiring a broker layer (e.g., Kafka/ActiveMQ) which was not previously needed.

## Risk Assessment
- **Integration Risk:** High. Concurrent support of legacy file processing and new APIs during the transient period.
- **AA-to-AC Migration Risk:** Critical. Potential for data integrity issues or misalignment of account product behaviors during the transition.
- **Middleware Complexity:** Moderate. Tasked with mapping multiple legacy version formats into a single R24-compatible version and managing AC-module transitions.

## Recommended Next Steps
- Define and publish Domain API specifications earliest possible to allow channel adapter development parallel to T24 upgrade.
- Conduct a dry-run migration of AA to AC product codes in an isolated environment.
- Architect the event-driven middleware to handle the new emission pattern securely and reliably.
