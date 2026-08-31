---
name: executive-summary-mcp
owner: Documentation & Governance
version: 1.0.0
description: "Compiles and publishes high-impact executive architecture summaries directly to Confluence, creates GitHub tracking issues, and dispatches Slack digests via MCP."
expected-deliverables:
  - Confluence Executive Summary Page
  - GitHub Action Item Issue
  - Slack Digest Notification
togaf-phases: [Phase A, Phase H]
---

# /documentation/executive-summary-mcp

## Overview
Automates executive stakeholder communication and task dispatching by integrating architecture summaries directly into enterprise tools via MCP.

## Actions
1. **Compile Summary:** Generates executive-level architectural brief from `handoff.json` and `design.json`.
2. **Publish to Confluence:** Calls `confluence:create_page` under the target Enterprise Architecture space.
3. **Dispatch Action Items:** Calls `github:create_issue` for required follow-up engineering spikes and ADR reviews.
4. **Broadcast to Slack:** Calls `slack:post_message` to post the executive summary brief to `#leadership-updates`.
