---
name: tdd-documentation
description: Use when authoring or refactoring skills (SKILL.md) to ensure disciplined, TDD-based construction.
---

# /tdd-documentation

## Overview
**Writing skills IS Test-Driven Development applied to process documentation.**
Skills must follow the **RED-GREEN-REFACTOR** cycle. Without failing pressure scenarios (RED), you cannot prove a skill fixes a defect (GREEN).

## When to apply
Use for training, refactoring, or authoring skill-files when disciplined, TDD-based documentation is required.

## Inputs
- Failing subagent transcripts.
- Business acceptance criteria.

## Process
1. Define RED Scenario (failing pressure).
2. Execute RED (observe violation).
3. Draft SKILL.md (codify rule).
4. Execute GREEN (observe success).
5. Refactor (harden/refine).

## Outputs
- Reproducible RED scenario (log/transcript).
- Hardened SKILL.md.
- Verified GREEN result (subagent output).

## Related skills
- [[solution-arch-orchestrator]]
- [[design-review]]

## Core Principle
**NO SKILL WITHOUT A FAILING TEST FIRST.**

## RED-GREEN-REFACTOR Cycle

### 1. RED (Baseline Pressure)
Run critical-path pressure scenarios with subagents BEFORE writing or updating the skill.
Document how agents violate the intended logic *without* the skill to understand the baseline rationalization / gap.

### 2. GREEN (Apply Skill)
Write/update the SKILL.md.
Ensure it specifically addresses the failure modes captured in RED.

### 3. REFACTOR (Bulletproof)
Audit against common rationalization tropes. If agents *still* circumvent the skill, update it (or add clearer prohibitions) and re-verify.

## Testing Standards
- **Skills are NOT prose**—they are discipline, rules, and actionable patterns.
- **Agents are adversaries**—they will rationalize. Test them under strain (time pressure, sunk cost).
- **Match the Form to the Failure**—do not use prohibitions when the issue is shape; use recipes / contracts.

## Common Rationalizations Checklist
- "This is just a simple question" (Task = Task)
- "I need more context first" (Skill check = BEFORE context)
- "I'll just do this one thing first" (Check = BEFORE doing)

## Implementation Guidance
For any skill overhaul, use this harness:
1. `Bash` or `Agent` to generate a failing log/transcript (the RED).
2. `Write` or `Edit` to update `SKILL.md`.
3. `Agent` to re-run the scenario (the GREEN).
4. `ReportFindings` when complete.
## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of tdd-documentation meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the tdd-documentation process.**


### Regulatory References
1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/
2. **PDPL:** Personal Data Protection Law (Federal Decree-Law No. 45 of 2021)
3. **CBUAE Cybersecurity Framework:** Domain 1: Governance & Risk Management

## Anti-patterns
- **Skipping test failures to write more code**
  - **Consequence:** Accumulated bugs, regression loops, and unreliable codebases.
  - **Correct Approach:** Treat any test failure as a blocking event; stop and fix it before implementing new features.
- **Writing tests post-hoc to match existing implementation**
  - **Consequence:** Confirmatory bias, poor design modularity, and missing edge cases.
  - **Correct Approach:** Practice strict red-green-refactor by writing the test assertion first, watching it fail, and then implementing the minimal code to pass.
- **Isolating tests from business functional logic**
  - **Consequence:** Green tests that pass technical constraints but fail actual user stories.
  - **Correct Approach:** Align test cases directly with business acceptance criteria and functional specifications.
