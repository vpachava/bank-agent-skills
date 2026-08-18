---
name: cross-domain-impact-assessment
description: Evaluates proposed architectural changes across business, data, application, and technology domains to identify cascading dependencies and risks.
owner: governance
version: 1.0.0
last-reviewed: 2026-08-18
togaf-phases: [G, H]
bian-domains: [Cross-Domain]
related-skills:
  - architecture-review
  - security-architecture-review
---

## When to apply
When a proposed solution or change spans multiple architectural domains or modifies core shared services with widespread dependencies.

## Inputs
- Proposed solution architecture document
- Current state enterprise architecture models
- Dependency maps

## Process
1. Discover current constraints in affected domains.
2. Analyze domain gaps and cross-domain ripple effects.
3. Propose target design with mitigation strategies for cascading risks.

## Outputs
- Standardized architectural artifact documenting cross-domain impacts and mitigations.

## Related skills
- [[architecture-review]]
- [[security-architecture-review]]

## Anti-patterns
- Siloed assessment focusing only on the primary domain delivering the project.
- Ignoring downstream data consumer applications during schema changes.

## Bulletproofing
- UAE Banking regulatory standards (CBUAE/PDPL/PCI-DSS where applicable).
- Assess impact on cross-border data flows and local data residency (CBUAE).

## Banking Examples
- Core banking system upgrade impacting channel applications and data warehouse.
- Introduction of a new payment gateway requiring changes to fraud detection and reconciliation systems.
