# Ticket: MCP Server Implementation

**ID**: mcp-server-implementation
**Priority**: P1
**Status**: Open

## Problem

`mcp-registry.json` references `mcp-servers/bank_skills_server.py` as the MCP server entry point, but that file does not exist. The current `governance/scripts/governance_engine.py` is a Python deep module, not an MCP server. Any external agent attempting to use the registry will fail silently.

## Acceptance Criteria

1. `mcp-servers/bank_skills_server.py` is a valid MCP tool-server that wraps `GovernanceEngine` and exposes at minimum:
   - `run_evidence_gate(handoff_path: str) -> dict`
   - `run_staleness_check(docs_path: str) -> dict`
   - `execute_unified_audit(handoff_path: str, docs_path: str) -> dict`
2. The server starts cleanly with `python mcp-servers/bank_skills_server.py`.
3. `mcp-registry.json` status field updated from `not-yet-implemented` to `available`.
4. A smoke test is added to `tests/test_mcp_server.py`.

## References

- `governance/scripts/governance_engine.py` — the underlying deep module to wrap
- `mcp-registry.json` — registry entry to update on completion
- MCP spec: https://modelcontextprotocol.io/
