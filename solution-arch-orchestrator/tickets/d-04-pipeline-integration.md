---
id: d-04-pipeline-integration
title: "TICKET: Pipeline Integration"
label: wayfinder:task
status: open
blocks: []
blocked_by: ["d-02-archify-post-processor", "d-03-template-repository"]
---

## Question
Update validation automation (e.g. `ci.yml` or relevant scripts). Ensure it fails if a skill claims to produce a structural visual design but lacks the corresponding Mermaid/PlantUML export mapping via the Archify logic. Validate the presence of the `artifact_id` metadata tag on test exports.

## Resolution

