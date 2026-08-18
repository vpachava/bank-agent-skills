---
id: hardening-map
title: "Production-Grade Hardening for Architecture-Skills Library"
label: wayfinder:map
status: open
---

## Destination
Transform the current POC banking architecture library into a production-grade 'Architectural Governance Engine' that enforces evidence-based design, automated regulatory compliance, and machine-readable handoffs between skills.

## Notes
- Enforce 'Evidence-Gate' requirements: Every skill output MUST link to concrete evidence (repo paths, IaC configs) rather than abstract prose.
- Prioritize banking-specific regulatory robustness (CBUAE, FAPI 2.0, ISO 20022).
- Use `solution-arch-orchestrator` as the primary integration entry point.
- Treat skills as software: enforce CI/CD, linting, and TDD construction.

## Decisions so far
- [Implement Idempotent Handoff Protocol](tickets/h-01-idempotent-protocol.md) - Created JSON schema.
- [Formalize Evidence-Gate Verification](tickets/h-02-evidence-gate.md) - Built /governance/evidence-gate skill.
- [Automate Banking RAID Registry](tickets/h-03-banking-raid.md) - Defined raid-log-schema.json.
- [Adversarial Compliance Testing](tickets/h-04-adversarial-compliance.md) - Wrote adversarial red-team skill.
- [Packaging for Enterprise Consumption](tickets/h-05-packaging.md) - Scaffolded manifest and installer.
- [Canonical Mermaid Definitions](tickets/d-01-canonical-mermaid.md) - Established template system.
- [Archify Post-Processor](tickets/d-02-archify-post-processor.md) - Created archify tool.
- [Template Repository Creation](tickets/d-03-template-repository.md) - Populated diagram-templates/.
- [Pipeline Integration](tickets/d-04-pipeline-integration.md) - Enforced governance in CI.

## Not yet specified

## Out of scope
- Implementation of the actual banking software; this effort is limited to the *architectural governance tooling itself*.
