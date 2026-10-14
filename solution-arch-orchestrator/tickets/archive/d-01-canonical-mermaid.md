---
id: d-01-canonical-mermaid
title: "TICKET: Canonical Mermaid Definitions"
label: wayfinder:task
status: open
blocks: ["d-02-archify-post-processor", "d-03-template-repository"]
blocked_by: []
---

## Question
Establish the standard Mermaid syntax for all banking components (Core Banking, Payment Hub, IAM, API Gateway). Include the strict Governance Rule: Every diagram must be tagged with a unique `artifact_id` in its metadata that links back to the specific architectural skill/version that generated it to prevent "orphan diagrams".

## Resolution
Canonical Mermaid components and governance rule (artifact_id metadata) established and validated in the `diagram-templates/` directory.

- Added `diagram-templates/README.md` documenting the governance policy and class definitions.
- Created `diagram-templates/canonical-mermaid.md` with base styles.
- Created example templates: `c4-context.md`, `sequence-iso20022.md`, `deployment-zones.md`.
status: closed
