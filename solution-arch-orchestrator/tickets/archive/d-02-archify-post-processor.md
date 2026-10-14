---
id: d-02-archify-post-processor
title: "TICKET: Archify Post-Processor Implementation"
label: wayfinder:task
status: open
blocks: ["d-04-pipeline-integration"]
blocked_by: ["d-01-canonical-mermaid"]
---

## Question
Create the `/archify` skill that takes raw `design.json` (from any other skill) and maps it to standardized templates established in earlier steps. Ensure diagram generation incorporates the mandatory `artifact_id` linking back to the precise generator skill and version.

## Resolution
Implemented `.claude/skills/archify` toolset.
- Created `archify.sh` wrapper to process `design.json` into Mermaid diagrams using defined templates and mandatory metadata injection.
- Defined `SKILL.md` for CLI triggering.
status: closed
