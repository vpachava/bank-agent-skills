---
id: 01-data-sovereignty-tags
title: "TICKET: Data Sovereignty Tags"
label: wayfinder:task
status: in_progress
---

## Question
Inject 'Data Sovereignty Tags' into C4-model artifacts to ensure compliance and traceability for banking data.

## Injection Logic
For each file in `diagram-templates/`, append `%% data_sovereignty: onshore %%` (or relevant region).

- Files to process:
  - `c4-context.md`
  - `canonical-mermaid.md`
  - `deployment-zones.md`
  - `sequence-iso20022.md`

## Status
- [ ] Injection into `c4-context.md`
- [ ] Injection into `canonical-mermaid.md`
- [ ] Injection into `deployment-zones.md`
- [ ] Injection into `sequence-iso20022.md`
