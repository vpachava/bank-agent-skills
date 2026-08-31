# MCP Server Setup & Integration Guide

Welcome to the Model Context Protocol (MCP) integration guide for `bank-agent-skills`. This guide allows your local AI agents to perform real-world actions in Jira, Confluence, Azure DevOps, GitHub, and Slack securely.

## 1. Prerequisites
- **API Tokens/PATs:** Generate valid tokens for each platform (Jira/Confluence API tokens, Azure DevOps PAT, GitHub PAT, Slack Bot Token).
- **Node.js:** `npx` must be in your system path.
- **Service Account:** Always use service accounts with the **least privilege** required for the task.

## 2. Configuration
Place your configuration files in the `mcp-servers/` directory. Each file follows the standard MCP JSON schema:

```json
{
  "mcpServers": {
    "server-name": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-..."],
      "env": {
        "API_TOKEN": "YOUR_TOKEN"
      }
    }
  }
}
```

## 3. Security Best Practices
- **Never hardcode tokens:** Pass them via environment variables or secret management tools.
- **Rotate Credentials:** Rotate tokens every 90 days.
- **Audit Logging:** Enable audit logging on your enterprise JIRA, Confluence, and Azure DevOps instances.

## 4. Testing Connection
Verify connections using the health-check utility:
```bash
python scripts/mcp-health-check.py
```
