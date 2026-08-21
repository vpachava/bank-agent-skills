---
name: dashboard
owner: Architectural Governance
version: 0.1.0
description: "Generates an automated executive dashboard (dashboard.json) summarizing RAID risks, staleness, and architectural compliance health across the banking project."
expected-deliverables:
  - dashboard.json: Aggregated metrics on system health, staleness, and risk.
togaf-phases: [Phase G]
---

# /governance/dashboard

## Overview
Aggregates telemetry from the entire architectural repository to surface governance bottlenecks for Lead Architects and ARB (Architecture Review Board) stakeholders.

## Process
1. **Aggregate RAID logs:** Reads global `raid-log.json` to identify systemic architectural risks.
2. **Scan Staleness:** Crawls repository for `handoff.json` files to calculate the staleness ratio.
3. **Health Score Calculation:** Computes a composite health score based on risk exposure and artifact freshness.

## Outputs
- **dashboard.json:** Machine-readable report.
- **Console Summary:** Immediate visibility on current project health.

## Related Skills
- [raid-log](../../documentation/raid-log/SKILL.md)
- [solution-arch-orchestrator](../solution-arch-orchestrator/SKILL.md)
