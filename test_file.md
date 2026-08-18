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

## Outputs
- **Skill Mapping:** The specific list of skills triggered.
- **Workflow Roadmap:** A sequential view of the required skills.
- **Task List:** Populated `TaskCreate` tickets for ready-to-run work.
