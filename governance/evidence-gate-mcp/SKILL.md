---
name: evidence-gate-mcp
owner: Architectural Governance
version: 1.0.0
description: "Executes evidence-gating with automated MCP tool integration (creates Jira tickets on failure, updates Confluence page with audit summary, and notifies Slack channels)."
expected-deliverables:
  - Jira Issue Key
  - Confluence Page URL
  - Slack Notification Receipt
togaf-phases: [Phase G]
---

# /governance/evidence-gate-mcp

## Overview
Automated bridge connecting the architectural `/governance/evidence-gate` to enterprise workflow tools via the Model Context Protocol (MCP).

## Actions
1. **Run Evidence Gate:** Scans local repository IaC and configs against `handoff.json`.
2. **On Gate Failure:**
   - Calls `jira:create_issue` to open an architectural blocking bug with defect details.
   - Calls `slack:post_message` to alert the `#architecture-review-board` channel.
3. **On Gate Success:**
   - Calls `confluence:update_page` to publish the verified architectural compliance certificate.
   - Calls `slack:post_message` to post the sign-off confirmation.
