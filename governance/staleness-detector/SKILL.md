---
name: staleness-detector
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-20
description: "Detects aging architectural handoff artifacts."
required-inputs:
  - Repository root path
expected-deliverables:
  - List of stale handoff artifacts
togaf-phases: [Phase C]
togaf-artifacts: [Architecture Definition]
bian-service-domains: [Operations.Governance]
---

# /staleness-detector

## When to apply
Use for identifying stale design artifacts in the repository.

## Process
1. Crawls repo for `handoff.json` files.
2. Calculates staleness (default 30 days).
3. Reports stale artifacts.
