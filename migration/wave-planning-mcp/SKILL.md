---
name: wave-planning-mcp
owner: Migration & Cloud Architecture
version: 1.0.0
description: "Generates enterprise cloud/database migration waves and automatically synchronizes them into Azure DevOps work items, linked to migration artifacts and broadcast to Slack."
expected-deliverables:
  - Azure DevOps Epics & Work Items
  - Linked Migration Plan Artifacts
  - Slack Progress Broadcast
togaf-phases: [Phase E, Phase F]
---

# /migration/wave-planning-mcp

## Overview
Automates cloud and database migration wave planning by directly generating Azure DevOps work items and tracking progress via MCP.

## Actions
1. **Analyze Waves:** Partitions legacy system components into structured migration waves based on dependency analysis.
2. **Create Azure DevOps Epics:** Calls `azure-devops:create_work_item` to establish tracking tasks and epics for each wave.
3. **Link Documentation:** Attaches the generated migration wave markdown as an attachment or work item link.
4. **Broadcast Progress:** Calls `slack:post_message` to update the migration war room channel (`#cloud-migration-war-room`).
