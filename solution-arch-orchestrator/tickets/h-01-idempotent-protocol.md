---
id: h-01-idempotent-protocol
title: "Implement Idempotent Handoff Protocol"
label: wayfinder:task
status: closed
assignee: antigravity
blocks: ["h-02-evidence-gate", "h-03-banking-raid", "h-05-packaging"]
blocked_by: []
---

## Question
Define `handoff.json` schema to pass state between decoupled skills (e.g., passing `/gap-analysis` findings into `/hld-generator`).

## Resolution
Successfully mapped and tested JSON schema at `solution-arch-orchestrator/handoff.schema.json`. Tested via Python using jsonschema testing GREEN and RED scenarios.
