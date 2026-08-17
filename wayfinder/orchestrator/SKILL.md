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
- **Raw requirement:** The unstructured business/technical ask.
- **Context/Constraint:** Geographic (UAE), Cloud/Hybrid/On-prem, Regulatory (CBUAE/PDPL/AECB).

## Process

1. **Pre-check:** Executing `/security-nfr-baseline-check` first.

2. **Scope/Stage Classification:** Is this discovery, greenfield, modernization, or governance?

3. **Mandatory Security Baseline:** Perform `/security-nfr-baseline-check` (verify RTO/RPO, data-residency, encryption, and PII-tagging constraints) as the first step before any design assessment.

4. **Skill Mapping:** Auto-select the critical path subset of the 72 skills using the updated `SKILL.md` frontmatter metadata (owner/domain).

5. **Dependency & Governance Generation:** Structure the skills into a dependency chain (e.g., Discovery â†’ HLD â†’ Security â†’ Prod Gate). Mandatory injection of `/security-architecture-review` and `/production-readiness` for all regulated-bank architectural paths.

6. **Taskify:** Generate the `TaskCreate` list for this session (`/tasks`).

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of orchestrator meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the orchestrator process.**

## Outputs
- **Skill Mapping:** The specific list of skills triggered.
- **Workflow Roadmap:** A sequential view of the required skills.
- **Task List:** Populated `TaskCreate` tickets for ready-to-run work.

## Banking pitfalls
- **Over-orchestration:** Mapping *too many* skills. The orchestrator must filter, not accumulate.
- **Ignoring non-optional governance:** Always injecting `/security-architecture-review` or `/production-readiness` for regulated paths, even if the user didn't ask.

## Automated Reinforcement
- The orchestrator now performs a mandatory `/security-architecture-review` baseline as the first sub-step in any modernization trigger.

### Regulatory References
1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/
2. **PDPL:** Personal Data Protection Law (Federal Decree-Law No. 45 of 2021)
3. **CBUAE Cybersecurity Framework:** Domain 1: Governance & Risk Management


