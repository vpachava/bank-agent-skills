GREEN_INT_MIG_SEC = {
    "greenfield/platform-selection": """## Anti-patterns
- **Selecting platforms based on vendor hype or familiarity without evaluating NFRs**
  - **Consequence:** Expensive platform lock-in that fails to meet target latency or scalability requirements.
  - **Correct Approach:** Use a balanced scorecard evaluating NFRs, Total Cost of Ownership (TCO), and engineering skill availability.
- **Ignoring integration capabilities with existing legacy systems**
  - **Consequence:** Massive custom ETL or bridge coding required to make the new platform work with core banking systems.
  - **Correct Approach:** Prioritize platforms with robust API ecosystems and out-of-the-box connectors for enterprise legacy systems.
- **Failing to validate data residency and compliance certifications**
  - **Consequence:** Sudden project blocks when security audits find the chosen platform cannot host data within UAE boundaries legally.
  - **Correct Approach:** Verify ISO, SOC2, and specific UAE CBUAE/PDPL compliance as a mandatory first gate in selection.""",

    "greenfield/poc-planning": """## Anti-patterns
- **Treating a Proof of Concept (POC) as an attempt to build MVP production code**
  - **Consequence:** Project gets bogged down in edge cases and security hardening, taking months instead of weeks.
  - **Correct Approach:** Timebox the POC and strictly target only the highest-risk technical assumptions or integration points.
- **Starting a POC without predefined quantitative success metrics**
  - **Consequence:** The POC finishes but stakeholders cannot objectively decide whether the technology passed or failed.
  - **Correct Approach:** Define clear, boolean completion gates (e.g., "throughput > 1000 TPS", "latency < 50ms") before starting.
- **Failing to document architecture decisions and trade-offs discovered during the POC**
  - **Consequence:** Lessons learned are lost when the team pivots to production, leading to repeated mistakes.
  - **Correct Approach:** Conclude the POC with an ADR recording what worked, what failed, and what architectural limits were hit.""",

    "greenfield/reference-architecture": """## Anti-patterns
- **Designing massive "ivory tower" reference architectures with no implementation paths**
  - **Consequence:** Developers ignore the architecture entirely because it is too abstract to map to their daily code.
  - **Correct Approach:** Tie reference architectures to concrete patterns, code boilerplates, and deployable Terraform modules.
- **Failing to include operational concerns like logging, tracing, and metrics**
  - **Consequence:** Teams build functional components but operations teams cannot support or monitor them in production.
  - **Correct Approach:** Bake observability tools and incident diagnostic endpoints directly into the core reference layers.
- **Mandating a "one size fits all" technology stack without context options**
  - **Consequence:** Teams use heavyweight frameworks for simple microservices, increasing compute costs and maintenance.
  - **Correct Approach:** Provide distinct architectural profiles (e.g., small function vs. large monolith) targeting different service scales.""",

    "greenfield/roadmap": """## Anti-patterns
- **Plotting long-term roadmaps packed with rigid, unmovable delivery dates**
  - **Consequence:** Failure to adapt to shifting business priorities, leading to missed deadlines and rushed, buggy code.
  - **Correct Approach:** Use horizon planning (Now, Next, Later) with flexible outcomes based on continuous dependency discovery.
- **Sequencing infrastructure delivery after application development**
  - **Consequence:** Developers finish features but are blocked from testing or releasing because target environments do not exist.
  - **Correct Approach:** Prioritize Landing Zone, CI/CD, and core database provisioning as "Phase 0" before functional sprints begin.
- **Silencing risk and architectural debt remediation out of the roadmap**
  - **Consequence:** Slower velocity over time as accumulated technical debt collapses the system's ability to safely change.
  - **Correct Approach:** Dedicate 20% of every roadmap phase explicitly to refactoring, security patching, and technical debt reduction.""",

    "greenfield/technology-evaluation": """## Anti-patterns
- **Evaluating tools based completely on "Hello World" or optimal-path demos**
  - **Consequence:** The tool collapses under the weight of real-world complexities, legacy integrations, or complex security rules.
  - **Correct Approach:** Evaluate tools using your organization's specific complex scenarios, including failure recovery.
- **Ignoring the health, community size, and release cadence of open-source projects**
  - **Consequence:** Adopting an abandoned project, leaving the organization with unpatchable security flaws.
  - **Correct Approach:** Check GitHub stars, recent commit activity, issue resolution speed, and corporate backing before selection.
- **Underestimating the organizational learning curve and training costs**
  - **Consequence:** Tool is purchased but remains unused or misused because engineers do not know how to leverage it.
  - **Correct Approach:** Factor ramp-up time, paid training needs, and available hiring pool into the evaluation scorecard.""",
}
