---
name: orchestrator
owner: Architectural Governance
version: 0.1.1
last-reviewed: 2026-08-16
description: "Meta-skill: Receives a raw requirement, maps it to the necessary subset of 72 architectural skills, and generates an actionable dependency roadmap (workflow)."
required-inputs:
  - Raw business requirement
  - Initiative stage (e.g., discovery, design, hardening)
expected-deliverables:
  - Skill-mapping report
  - Actionable dependency workflow
togaf-phases: [Phase A]
togaf-artifacts: [Architecture Vision]
bian-service-domains: [Customer Account.Origination]
---

# /orchestrator

## When to apply
Use as the entry point for *any* new initiative. It acts as the "Wayfinder" for the 72-skill library, taking the cognitive load of selecting the right subset of skills away from you and structuring the project lifecycle.

## Inputs
- Raw business requirement
- Context/Constraint

## Process
1. Discover current constraints.
2. Analyze domain gaps.
3. Propose target design.

## Outputs
- Standardized architectural artifact.

## Related skills
- [[tdd-documentation]]
- [[design-review]]
## Bulletproofing
- UAE Banking regulatory standards (CBUAE/PDPL/PCI-DSS where applicable).
- Mandatory Security Baseline: Perform `/security-nfr-baseline-check`.
- Mandatory explicit verification and accountability.


## Banking pitfalls
- **Over-orchestration:** Mapping *too many* skills. The orchestrator must filter, not accumulate.
- **Ignoring non-optional governance:** Always injecting `/security-architecture-review` or `/production-readiness` for regulated paths, even if the user didn't ask.

## Automated Reinforcement
- The orchestrator now performs a mandatory `/security-architecture-review` baseline as the first sub-step in any modernization trigger.

### Regulatory References
1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/
2. **PDPL:** Personal Data Protection Law (Federal Decree-Law No. 45 of 2021)
3. **CBUAE Cybersecurity Framework:** Domain 1: Governance & Risk Management

## Anti-patterns
- **Commanding agents without clearly defined success criteria or bounded domains**
  - **Consequence:** Agents drift into endless conversational loops, hallucinate tasks, or execute infinite web searches without yielding actionable artifacts.
  - **Correct Approach:** Define sharp, boolean completion gates ("Produce a 500-word markdown ADR", "Find the IP range") before delegating a subtask.
- **Failing to maintain conversational memory or artifact context across sequential agent handoffs**
  - **Consequence:** Each newly spawned agent starts from scratch, forcing the user to repeat instructions and resulting in disjointed, conflicting solutions.
  - **Correct Approach:** Utilize structured summary blocks, shared memory files, or centralized context repositories explicitly passed between orchestration steps.
- **Executing destructive code changes (e.g., Git pushes, database drops) without Human-In-The-Loop review**
  - **Consequence:** Agents autonomously overwrite critical production configurations based on hallucinated confidence, causing major system outages.
  - **Correct Approach:** Implement hard-stop validation gates for any mutable action, requiring manual human approval before execution algorithms proceed.
