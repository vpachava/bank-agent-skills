# Glossary

This document defines the canonical vocabulary for the **Global Banking Solution-Architect Skills Library** (`bank-agent-skills`). Use these terms consistently across all specifications, workflows, and documentation.

## Architectural Design Vocabulary (Deep Modules)

- **AI-Native**: A software architecture designed for intent-based, conversational interaction, utilizing edge LLM/SLM inference orchestrated with secure enterprise RAG data retrieval.
- **Edge SLM**: A purpose-built, quantized language model optimized for low-latency, on-device intent parsing within mobile banking clients, ensuring PII data remains local.
- **BFF (Backend-for-Frontend)**: A dedicated adaptation layer providing an interface optimized for a specific client (e.g., Mobile App). All mobile-to-core banking traffic must traverse this seam.
- **Idempotency**: The guarantee that executing the same transactional request multiple times results in exactly one state change. Required for all conversational banking transactions.
- **Module**: Anything with an interface and an implementation. Deliberately scale-agnostic: a function, class, package, or tier-spanning slice. (Prohibited terms: component, service, boundary; use \"interface\" or \"seam\" for interaction points).

- **Implementation**: What is inside a module, distinct from its external surface.
- **Depth**: Leverage at the interface. The amount of behaviour a caller or test can exercise per unit of interface they have to learn. A deep module combines a small interface with a rich implementation.
- **Seam**: A place where behaviour can be altered without editing code in that place; the location at which a module's interface lives.
- **Adapter**: A concrete component that satisfies an interface at a seam, describing a role rather than internal substance.
- **Leverage**: What callers get from depth — more capability per unit of interface learned.
- **Locality**: What maintainers get from depth — change, bugs, and verification concentrate in one place rather than spreading across callers.

## Banking & Governance Domain Vocabulary

- **Evidence Gate**: An automated or semi-automated verification checkpoint (`/governance/evidence-gate`) that inspects repository artifacts (IaC, design specs, handoffs) to prove compliance before architectural sign-off.
- **Compliance Proof Vector**: The standardized output object returned by the unified governance engine summarizing evidence validity, staleness audits, and regulatory conformance status.
- **Straight-Through Processing (STP)**: Operational execution without manual intervention or human exception queues.
- **Dual-Orchestration Pattern**: A hybrid enterprise architecture combining BPM (for complex underwriting and human exception workflows) with RPA (for bulk pre-approved batch processing).
- **Regional Regulatory Overlay**: Jurisdiction-specific compliance rules (e.g., CBUAE, SAMA, DORA, FAPI 2.0, PCI-DSS v4) bound to architectural designs during orchestration.
- **Data Residency Boundary**: Physical restriction ensuring customer PII and sensitive financial ledgers reside exclusively within domestic cloud or on-premise infrastructure.
