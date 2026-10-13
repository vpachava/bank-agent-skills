---
name: ai-native-mobile-workflow
description: "End-to-end workflow for transforming legacy mobile banking applications into AI-native mobile apps featuring conversational UX, on-device/edge SLM models, secure local caching, and strict PCI-DSS 4.0 / UAE PDPL / SAMA compliance."
---

# AI-Native Mobile App Transformation Workflow

## Overview
This workflow guides delivery teams through modernizing legacy monolithic mobile banking applications into **AI-Native Mobile Platforms**. It integrates conversational assistant interfaces (LLM/SLM edge inference), instant financial insights, and automated straight-through processing (STP), while maintaining enterprise banking compliance.

## Execution Sequence

### Step 1: Capability Mapping & Discovery (`discovery/business-capability-map`)
- Identify legacy banking journeys targeted for AI enhancement (e.g., Credit Limit Increase, Loan Origination, Expense Insights, Smart Search).
- Map user intents to BIAN financial service domains.

### Step 2: AI-ML Architecture &amp; Guardrails (`ai-ml-architecture/rag-patterns`, `governance/ai-governance`)
- Define dual-layer architecture: Edge SLM for instant client-side intent parsing + Server-side RAG for secure core banking data retrieval.
- Implement jailbreak prevention, PII redaction filters, and EU AI Act / SAMA AI risk classification guardrails.

### Step 2.5: Mobile UI Architecture (`architecture/mobile-microfrontends`)
- Implement a **Flutter-based modularized architecture** (e.g., using `flutter_modular` or `get_it` for dependency injection) to support Microfrontend-like feature isolation.
- Separate UI features into independent packages (e.g., `feature_login`, `feature_payments`, `feature_ai_assistant`) to enable independent development, testing, and deployment cycles for product teams.
- Use a **host application (Shell)** to dynamically load and integrate these features, ensuring a unified design system and consistent banking UX while keeping domain boundaries clean.


### Step 3: API & BFF Design (`integration/api-design`, `integration/idempotent-api`)
- Design low-latency GraphQL / REST BFF (Backend-for-Frontend) contracts optimized for mobile bandwidth constraints.
- Enforce strict idempotency headers for conversational transactional triggers (e.g., transfers, limit increases).

### Step 4: Security & Compliance Overlay (`security/zero-trust`, `security/compliance`)
- Implement device attestation, biometric binding, and FAPI 2.0 (PAR/DPoP) authentication tokens.
- Ensure strict compliance with local data residency laws (CBUAE / SAMA) and PCI-DSS v4 tokenization for card data.

### Step 5: Effort Sizing & Delivery Planning (`discovery/effort-estimation`)
- Apply the AI-Native Transformation sizing archetype (89-144+ pts) with regulatory overhead factors.
- Establish sprint milestones for PO, Scrum Master, and Head of IT tracking.
