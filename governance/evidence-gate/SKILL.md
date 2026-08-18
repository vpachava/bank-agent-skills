---
name: evidence-gate
description: Tests architectural claims against real project repository state to ensure compliance and prevent hallucination.
owner: Architectural Governance
version: 1.0.0
last-reviewed: 2026-08-18
togaf-phases: [Phase G]
---

# /evidence-gate

## When to apply
Use this skill immediately after any architectural or design skill (like `/hld-generator` or `/threat-model`) completes. Do NOT allow an architecture review or design to pass to the next phase without going through this gate.

## Inputs
- `handoff.json` containing the findings and `verifiable_evidence_paths`
- Current working directory repository

## Process
1. Discover the architectural claim in the conversation or `handoff.json`.
2. Extract the `verifiable_evidence_paths` linked to the claim.
3. Validate existence: Use `Read` or `Bash` tools to confirm the path points to an actual file.
4. Validate content (Optional but recommended): Use `Grep` to confirm the file actually contains the relevant architectural component (e.g. searching for a Terraform resource definition).

## Outputs
- Evidence-Gate Validation Report (Boolean Pass/Fail + Context)

## Related skills
- [[solution-arch-orchestrator]]
- [[compliance]]

## Bulletproofing
- Any claim missing a `verifiable_evidence_paths` array element is an automatic FAIL.
- Any path that 404s or is inaccessible is an automatic FAIL.
- Agent PROSE or promises do not count as evidence.

## Anti-patterns
- **Accepting PROSE over PATHS:** The agent writes "The database will be encrypted" but provides no path to `main.tf` proving KMS is used.
  - **Correction:** Reject the claim. Force the agent to link to the IaC or code.
