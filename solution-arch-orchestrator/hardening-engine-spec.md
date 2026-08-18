# Production-Grade Hardening for Architecture-Skills Library

## Problem Statement

The current UAE retail-bank solution-architecture skills library acts as an excellent Proof of Concept (POC) reference model and instructional toolkit. However, it operates purely via abstract prose generation. It lacks strict, machine-enforceable rules that link generated designs to real-world code (evidence), it does not elegantly pass state between disconnected skills, and it lacks an automated red-teaming capability to ensure adherence to strict banking compliance requirements (CBUAE, FAPI 2.0). Finally, it cannot be easily distributed as an enterprise plugin payload to Hermes or Claude Code.

## Solution

Transform the library into an 'Architectural Governance Engine.' This will provide automated compliance guardrails, force physical evidence links for architectural claims, utilize a unified JSON protocol for sharing state across disjointed agent sessions, centralize risk tracking, and package the entire suite as a distributed, plug-and-play enterprise enterprise scale artifact.

## User Stories

1. As an Enterprise Architect, I want the `solution-arch-orchestrator` to emit and consume state via a `handoff.json` format, so that my sequence of agent operations retains high-fidelity context across sessions.
2. As a Security Governance Lead, I want a new `/governance/evidence-gate` skill to explicitly verify architectural claims against repository reality, so that hallucinated compliance claims are rejected immediately.
3. As a Risk Manager, I want all architectural skills to push identified constraints and mitigations directly into a centralized `raid-log.json`, so that we have a living, unified Banking RAID catalog rather than diffuse markdown documents.
4. As a Red Team Member, I want a standardized suite of adversarial prompts that attempt to break Data-Residency and CBUAE constraints, so that I can validate the robustness of our governance guardrails automatically.
5. As an Engineering Lead, I want the toolset packaged with a `manifest.json` and install scripts, so that my team can easily load the bank-agent-skills library into their local AI companions (Hermes/Claude Code) as a native plugin.

## Implementation Decisions

- **Handoff Protocol (`handoff.json`):** A JSON Schema will define the format for inter-skill state sharing. Any capability skill that generates requirements or constraints will write an intermediate object to this schema, and succeeding capabilities will fetch it.
- **Evidence Verification (`evidence-gate`):** We will create the `/governance/evidence-gate/SKILL.md` that leverages local IDE paths and regex-based or AST-based searches to ensure infrastructure (e.g., Terraform paths) referenced in solutions actually exists.
- **Central RAID registry (`raid-log.json`):** A centralized tracker schema. Updates to this log must handle sequential mutation safely (e.g., additive log patterns).
- **Adversarial Suite:** New test fixtures structured as 'Pressure Tests' aligning with the `RED-GREEN-REFACTOR` concept found in `/tdd-documentation`. It will run scenarios specifically tailored for CBUAE data sovereignty breaking.
- **Distribution Model:** A `manifest.json` will be scaffolded at the root directory following Anthropic plugin/skill manifest conventions.

## Testing Decisions

- Tests should evaluate the behavior of the rules when exposed to simulated agent transcripts. 
- Using the pattern codified in `/tdd-documentation/SKILL.md`, each feature will be tested by running a 'RED' baseline agent invocation (e.g., trying to sneak a hallucinated design past the evidence gate, observing failure), then applying the skill logic to ensure the agent correctly flags or corrects it ('GREEN').
- **Modules Tested:** 
  - The `evidence-gate` ruleset.
  - The `handoff.json` parsability across skills.
  - The `raid-log` centralization (ensuring duplicate risk logs aren't created).
- **Prior Art:** We will build on existing testing paradigms demonstrated in the `.claude/tdd-documentation/` pattern.

## Out of Scope

- Implementing actual banking backend applications (e.g., core ledgers, Swift gateways).
- Developing a custom visual frontend for the RAID log.
- Hosting the solution on the Cloud (must remain a local terminal/IDE driven toolkit).

## Further Notes
- This implementation fulfills all tracking tickets `h-01` through `h-05` mapped in the `hardening-map.md`.
