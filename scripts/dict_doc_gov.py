DOC_GOV = {
    "documentation/design-document": """## Anti-patterns
- **Documenting low-level implementation details that drift daily**
  - **Consequence:** High maintenance overhead; developers ignore the design doc because it is always out of date.
  - **Correct Approach:** Focus the design document on boundaries, interface contracts, data schemas, and key design patterns.
- **Neglecting to include security and regulatory compliance sections**
  - **Consequence:** Security flaws are discovered during production reviews, forcing complete code redesigns.
  - **Correct Approach:** Dedicate specific sections to data encryption at rest/in transit, IAM controls, and data localization compliance.
- **Omitting disaster recovery, backup, and failover design details**
  - **Consequence:** System outages occur without clear processes to restore database and service instances.
  - **Correct Approach:** Detail recovery steps, define RTO/RPO limits, and describe database backup policies explicitly.""",

    "documentation/executive-summary": """## Anti-patterns
- **Overloading the summary with deep technical jargon and acronyms**
  - **Consequence:** Non-technical executives miss the core value proposition and delay final approvals.
  - **Correct Approach:** Use plain Business-focused language and visually map technical architecture to business workflows.
- **Omitting financial estimates, resources, and critical milestones**
  - **Consequence:** Decision-makers reject proposals because the total cost and path are unclear.
  - **Correct Approach:** Detail total cost of ownership (TCO), resource constraints, and key delivery dates on the main page.
- **Hiding critical risks, trade-offs, and negative consequences**
  - **Consequence:** The business sponsor is blindsided when issues surface during implementation stages.
  - **Correct Approach:** Explicitly state the top three risks and how the architecture intends to mitigate them.""",

    "documentation/project-charter": """## Anti-patterns
- **Committing to fix dates and budgets before scoping dependencies**
  - **Consequence:** Missed deadlines, developer burnout, and project failure.
  - **Correct Approach:** Use range-based estimates and conditional milestones that change when dependencies fail.
- **Vague project governance models with overlapping roles**
  - **Consequence:** Conflicted decisions, duplicated efforts, and lack of accountability when issues occur.
  - **Correct Approach:** Define a clear RACI matrix mapping roles to decisions and project actions.
- **Setting subjective or unquantifiable success metrics**
  - **Consequence:** Inability to measure whether the project met its goals upon completion.
  - **Correct Approach:** Base success criteria on KPIs such as performance speed, cost reduction, or adoption metrics.""",

    "documentation/proposal": """## Anti-patterns
- **Presenting technology stacks before identifying business outcomes**
  - **Consequence:** Business sponsors reject the proposal as a costly technical exercise with no ROI.
  - **Correct Approach:** Focus first slide on current customer pain points and how the solution meets those needs.
- **Ignoring migration, transition, and legacy system compatibility**
  - **Consequence:** Unplanned system downtime or unexpected modernization cost to bridge old and new layers.
  - **Correct Approach:** Include a clear transition roadmap showing legacy migration waves and fallback steps.
- **Understating the operational effort and ongoing maintenance costs**
  - **Consequence:** The system becomes shelf-ware because the bank cannot afford the operational run costs.
  - **Correct Approach:** Detail licensing, compute costs, SRE support teams, and yearly training budgets in the TCO section.""",

    "documentation/raid-log": """## Anti-patterns
- **Treating the RAID log as static documentation to be updated before meetings**
  - **Consequence:** Issues remain unresolved, risks escalate, and dependencies dry up.
  - **Correct Approach:** Keep the RAID document active, updating status, owner updates, and milestones continuously.
- **Documenting risks and issues without specific mitigation plans or owners**
  - **Consequence:** Risks inevitably become actual issues, and issues linger without resolution.
  - **Correct Approach:** Assign a single owner to each entry and record actionable mitigation steps with clear target dates.
- **Closing entries without capturing lessons learned or post-mortems**
  - **Consequence:** Teams repeat the same mistakes in subsequent sprints and phases.
  - **Correct Approach:** Record a summary of why the risk was closed, what mitigated it, and what needs to be changed next.""",

    "documentation/risk-register": """## Anti-patterns
- **Understating risk severity or probability to avoid project scrutiny**
  - **Consequence:** Sudden project failures occur when unmitigated risks impact delivery.
  - **Correct Approach:** Score risks objectively using standard frameworks based on financial, security, and timeline impact.
- **Defining risks too broadly without identifying specific scenarios**
  - **Consequence:** Generic mitigation plans that fail to protect the system during actual failures.
  - **Correct Approach:** Frame risks as "If Event X occurs, then Consequence Y will happen, leading to Impact Z".
- **Failing to monitor risk status changes and update mitigation plans**
  - **Consequence:** Mitigation plans are obsolete and fail to address the current environment.
  - **Correct Approach:** Conduct weekly risk reviews and adjust scores as constraints change.""",

    "governance/ai-governance": """## Anti-patterns
- **Operating customer-facing AI services without safety and bias guards**
  - **Consequence:** Generative AI services output toxic or unaligned advice, resulting in brand damage.
  - **Correct Approach:** Deploy input/output filters and guardrails to monitor and intercept unsafe models.
- **Deploying model outputs without audit pathways and explainability**
  - **Consequence:** Auditing failures when compliance asks why a credit decision was made by an LLM.
  - **Correct Approach:** Save execution traces, prompt templates, and scoring variables in immutable audit databases.
- **Sending sensitive customer PII to external public AI endpoints**
  - **Consequence:** Data leakages and serious compliance failures under UAE data privacy regulations.
  - **Correct Approach:** Run models inside local tenant environments and redact user details before passing inputs.""",

    "governance/ai-model-governance": """## Anti-patterns
- **Validating models in static test environments only**
  - **Consequence:** Models degrade in accuracy and fail to handle real-world user questions.
  - **Correct Approach:** Set up automated pipelines to test models against active, changing user data datasets.
- **Skipping continuous model drift and accuracy checks**
  - **Consequence:** Silent cost increases and performance penalties as models drift over time.
  - **Correct Approach:** Instrument models to track prediction probability metrics and write alerts on data drift.
- **Storing custom model weights and architectures in insecure storages**
  - **Consequence:** Theft of IP and risk of model modification by unauthorized users.
  - **Correct Approach:** Restrict access to model binary assets using RBAC roles in secure cloud storage.""",

    "governance/architecture-board": """## Anti-patterns
- **Presenting solutions to the board before aligning with security and compliance**
  - **Consequence:** Presentations are rejected by the board, delaying approvals and project schedules.
  - **Correct Approach:** Complete pre-reviews with security, compliance, and infrastructure gatekeepers before the board review.
- **Reviewing designs that lack a clear business sponsor or funding**
  - **Consequence:** Wasting architecture board capacity on proposals that will never run.
  - **Correct Approach:** Verify that a business case exists and that budget is allocated before board presentations.
- **Approving exceptions without setting a firm expiration date or refactoring plan**
  - **Consequence:** Temporary architectural waivers become permanent technical debt that is never fixed.
  - **Correct Approach:** Write exceptions into ADRs with a defined expiration date and a planned task to migrate to standards.""",

    "governance/design-review": """## Anti-patterns
- **Focusing reviews on detailed code implementations instead of components**
  - **Consequence:** Reviews take too long, missing high-level integration issues and missing timelines.
  - **Correct Approach:** Scope the review on APIs, database patterns, data flows, and isolation boundaries.
- **Reviewing component design without evaluating scaling limits**
  - **Consequence:** System bottleneck failures under peak production transaction throughputs.
  - **Correct Approach:** Require the design package to include latency profiles, thread limits, and cache plans.
- **Failing to track design review feedback in issue tracking tickets**
  - **Consequence:** Developers skip recommended design fixes, leading to non-compliant production releases.
  - **Correct Approach:** Log feedback as tickets inside the tracking board and verify block closures before code merges.""",

    "governance/dr-review": """## Anti-patterns
- **Conducting Disaster Recovery (DR) reviews without mock simulations**
  - **Consequence:** The DR plan fails during actual system outages, causing extended downtime.
  - **Correct Approach:** Enforce mandatory scheduled failover drills in staging/production environments.
- **Assuming data backup is equivalent to complete system recovery**
  - **Consequence:** Data exists but the bank cannot run the application because service configs are missing.
  - **Correct Approach:** Verify and test compute provisioning, security settings, DNS routing, and database sync.
- **Neglecting to measure cross-region network performance under full write loads**
  - **Consequence:** System replication queues lag during load, violating strict RPO limits.
  - **Correct Approach:** Monitor replication latency profiles during load tests and adjust write speeds to match.""",

    "governance/operational-readiness": """## Anti-patterns
- **Transitioning systems to support teams without setting up metrics**
  - **Consequence:** System issues are first reported by customer complaints rather than support tools.
  - **Correct Approach:** Establish dashboard monitoring and set up alerts for system latency and database errors.
- **Deploying systems without automated rollback capabilities**
  - **Consequence:** Release errors require lengthy troubleshooting sessions, increasing outage downtime.
  - **Correct Approach:** Automate release rollbacks when health metrics fall below thresholds.
- **Neglecting to run post-oncall handover reporting**
  - **Consequence:** Persistent bugs and technical debts are ignored, leading to repeat issues.
  - **Correct Approach:** Require a handoff report documenting major incident causes and operational gaps.""",

    "governance/production-readiness": """## Anti-patterns
- **Running the review checklist as a last-minute box-ticking exercise**
  - **Consequence:** Finding critical gaps (e.g. no backup, missing audit logs) when it is too late to postpone the release.
  - **Correct Approach:** Run production readiness checks continuously across environment stages.
- **Releasing products without testing system recovery scenarios**
  - **Consequence:** Support teams cannot resolve production lockouts, extending outage times.
  - **Correct Approach:** Enforce a check requiring manual failover tests before the production gate is passed.
- **Validating system compliance checklists manually**
  - **Consequence:** Human errors lead to non-compliant deployments and security risks.
  - **Correct Approach:** Automate validation rules within the CI/CD pipeline using policy-as-code tools.""",

    "governance/security-nfr-baseline-check": """## Anti-patterns
- **Skipping validation checks on non-production environments**
  - **Consequence:** Security bugs are discovered late, wasting developer remediation resources.
  - **Correct Approach:** Deploy the security configuration checks in DEV and STAGING pipelines.
- **Treating security NFR checks as independent of business logic**
  - **Consequence:** Secure infrastructure holds logic configurations that leak customer data.
  - **Correct Approach:** Map security checks to functional data flows and verify that PII is masked.
- **Using a single baseline config for all environments**
  - **Consequence:** Development environments are locked down, reducing developer velocity.
  - **Correct Approach:** Define clear baseline splits for Dev, Staging, and Prod configurations.""",

    "governance/solution-review": """## Anti-patterns
- **Approving solutions without verifying the core team's capability**
  - **Consequence:** Development teams fail to build or support the solution due to lack of skills.
  - **Correct Approach:** Include resourcing, skills assessment, and training plans in the solution review criteria.
- **Selecting vendor software without analyzing version upgrade strategies**
  - **Consequence:** The bank runs legacy, unsupported versions, incurring high upgrade maintenance costs.
  - **Correct Approach:** Score vendor proposals based on their ease of deployment, backward compatibility, and upgrade support.
- **Failing to align vendor solutions with regional regulations**
  - **Consequence:** Deployment blocks due to data residency violations or audit gaps inside the package.
  - **Correct Approach:** Assess solution architecture for residency isolation and CBUAE compliance first."""
}
