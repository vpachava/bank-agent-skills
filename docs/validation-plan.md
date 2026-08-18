# Validation Plan: bank-agent-skills

## 1. Pilot Projects
| Pilot Type | Scope | Goal |
| :--- | :--- | :--- |
| **Greenfield** | Credit limit increase (existing card) | Rapid, template-driven implementation. |
| **Modernization** | Card management (monolith → microservices) | Complex architectural refactoring and API definition. |
| **Migration** | Legacy SQL onboarding table → RDS Postgres | Data structure mapping and regulatory-compliant migration. |

## 2. Success Metrics
*   **Efficiency Gain:** Time-to-resolution (baseline manual vs. agent-assisted).
*   **Quality Assurance:** Defect rate (post-implementation).
*   **Governance/Compliance:** Number of compliance gaps/policy violations proactively caught by agentic skills.
*   **Cognitive Load:** Developer confidence and ease-of-use (post-pilot survey).

## 3. Feedback Collection Mechanism
*   **Usage Logs:** Automated telemetry for all skill invocations.
*   **Developer Surveys:** Post-task survey (Accuracy, Trust, Ease-of-Use).
*   **Governance Interviews:** Deep-dive with Architecture team post-pilot.

## 4. Iteration Cadence
*   **Weekly Review:** Tactical sync (bugs, UX friction, compliance catches).
*   **Monthly Update:** Formal retrospective (case studies, documentation updates, prioritization).

## 5. Case Study Structure
Each successful pilot will result in a case study (2-pager) covering:
*   Context/Challenge.
*   Agent-assisted implementation path.
*   Metrics results.
*   Refinement captured for the library.

## Timeline & Owners
*   **Overall Owner:** Architecture Team.
*   **Pilot Execution:** Assigned Lead Architect per project.
*   **Timeline:** 3 months total (1 month per pilot type, interleaved).
