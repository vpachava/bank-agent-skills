# Governance Engine ADR

## Status
Proposed

## Context
Governance scripts (`evidence-gate.py`, `staleness-detector.py`, `generate_dashboard.py`) currently operate as independent, disconnected utilities. This creates maintenance friction and makes it difficult for agents to orchestrate a full compliance check.

## Decision
Create a unified `GovernanceEngine` adapter in `governance/scripts/governance_engine.py` that exposes a single `ComplianceProofVector` interface. This module encapsulates all script execution, schema validation, and staleness detection logic.

## Consequences
- **Leverage**: Future governance tools (e.g., automated cost audits) can plug into the existing engine.
- **Locality**: All compliance checking logic is centralized, reducing scatter across the `governance/` directory.
- **Testability**: The engine can be unit-tested via the unified interface, rather than needing to orchestrate shell executions of separate scripts.
