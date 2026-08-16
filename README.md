# bank-agent-skills

Welcome to **bank-agent-skills** — a comprehensive, production-hardened collection of 68 agentic skills designed for solution architecture in complex enterprise banking environments. These skills empower AI agents to assist with architecture assessments, design, security reviews, governance, and modernization, all while adhering to strict banking standards.

## 1. Overview
The library provides domain-specific knowledge packaged as actionable, agent-invocable skills, covering the complete lifecycle of a solution. It is organized into 13 core domains:

- **Architecture:** Foundation models (C4, Deployment, HLD/LLD)
- **Cloud:** Provider-specific reviews and infrastructure-as-code
- **DevOps:** CI/CD, FinOps, SRE, Performance
- **Discovery:** Business capabilities, stakeholder alignment, requirements
- **Documentation:** Project artifacts, charters, RAID logs
- **Governance:** AI/ML governance, design reviews, production readiness
- **Greenfield:** Technology evaluation, roadmap development
- **Integration:** API design, events, messaging, data sync
- **Migration:** Application and database cutover, wave planning
- **Modernization:** Legacy assessment, debt management, refactoring
- **Security:** Compliance, IAM, Threat Modeling, Zero Trust
- **Wayfinder:** Meta-orchestrator for initiative scoping
- **Utilities:** Supporting tools for agentic productivity

## 2. Installation

You can install and use these skills in a few different ways depending on your workflow.

### Via 
px skills add (Recommended for Cursor/Copilot)
If you are using the skills CLI tool:
\\\ash
npx skills add github.com/username/bank-agent-skills
\\\

### Via Git Clone
Clone the repository directly into your local agent's skill directory:
\\\ash
git clone https://github.com/username/bank-agent-skills.git ~/.claude/skills/bank-agent-skills
\\\
*(Adjust the path based on your specific IDE or agent configuration).*

### Manual Copy
Simply download the ZIP or copy the specific domain folders you need directly into your project's .claude/skills directory or your IDE's custom instructions path.

## 3. Invocation

Once installed, you can invoke these skills within your AI assistant.

### Claude Code
Type the skill name with a forward slash:
\\\	ext
/orchestrator
/security-architecture-review
\\\

### Cursor
Reference the specific skill file using the @ symbol:
\\\	ext
@skills/security/security-architecture-review/SKILL.md Help me review this implementation.
\\\

### GitHub Copilot Workspace / CLI
Include the skill context in your prompt or use configured slash commands if your environment supports them:
\\\	ext
#consult skills/architecture/api-design Draft the OpenAPI spec for our new payments endpoint.
\\\

## 4. Quick Start: 5 Common Scenarios

Here are exactly how to run 5 common scenarios using these skills.

### Scenario 1: Greenfield Project Initiation
Start a brand new project right by establishing the foundation and security baseline early.
**Commands:**
1. \/orchestrator\ - *Map the initiative and required skills.*
2. \/reference-architecture\ - *Establish the base patterns.*
3. \/api-design\ - *Draft the initial API contracts.*
4. \/security-architecture-review\ - *Ensure the initial design meets banking constraints.*

### Scenario 2: Legacy Modernization
Assess and plan the modernization of a legacy banking core or system.
**Commands:**
1. \/legacy-assessment\ - *Analyze the current debt and coupling.*
2. \/impact-analysis\ - *Determine the blast radius of changes.*
3. \/integration-patterns\ - *Design the anti-corruption layers.*
4. \/modernization-roadmap\ - *Generate the phased execution plan.*

### Scenario 3: Cloud Migration
Plan a compliance-heavy move to the cloud.
**Commands:**
1. \/cloud-migration\ - *Assess general cloud readiness.*
2. \/landing-zone-review\ - *Validate the target cloud environment.*
3. \/database-migration\ - *Plan data transfer ensuring sovereignty rules.*
4. \/cutover-plan\ - *Detail the weekend cutover events.*

### Scenario 4: API Design & Validation
Design a new enterprise API.
**Commands:**
1. \/api-design\ - *Structure the endpoints, payloads, and idempotency.*
2. \/security-architecture-review\ - *Validate authz/authn layers.*
3. \/compliance\ - *Check data exposure against PDPL/GDPR.*

### Scenario 5: Security & CI/CD Review
Perform a full audit before production promotion.
**Commands:**
1. \/threat-modeling\ - *Identify potential attack vectors.*
2. \/cicd-review\ - *Validate software supply chain integrity and gates.*
3. \/compliance\ - *Final check against banking regulations.*

## 5. Troubleshooting FAQ

* **Q: The agent isn't loading the skill.**
    * **A:** Ensure the library root directory is correctly added to your agent's configuration (.claude/CLAUDE.md or equivalent IDE settings).
* **Q: The output doesn't comply with banking standards.**
    * **A:** Ensure you run the security-architecture-review AND compliance skills as high-priority gates early in your process.
* **Q: Skill output feels generic.**
    * **A:** Increase the context by providing local ADR (Architecture Decision Records) or NFR documentation to the agent before invoking the skill.

## 6. License
MIT License. See [LICENSE](LICENSE) for details.
