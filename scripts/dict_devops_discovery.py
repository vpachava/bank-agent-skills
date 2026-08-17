DEVOPS_DISCOVERY = {
    "devops/cicd-review": """## Anti-patterns
- **Hardcoding secrets and environment configurations in build scripts**
  - **Consequence:** Leakage of production keys in repository history, compromising security.
  - **Correct Approach:** Store configurations and credentials in secure vault systems and inject them dynamically via environment variables during runners runtime.
- **Lacking automated compliance and vulnerability scanning in the pipeline**
  - **Consequence:** Insecure packages, critical vulnerabilities, and audit compliance gate failures in production.
  - **Correct Approach:** Integrate SAST, DAST, and dependency scanning checkpoints as mandatory steps before code merges.
- **Running pipeline executors with root or unrestricted system privileges**
  - **Consequence:** Escalated control plane risks where a compromised dependency allows full runner host access.
  - **Correct Approach:** Run executors on isolated virtual environments with min privileges needed for execution.""",

    "devops/finops-strategy": """## Anti-patterns
- **Provisioning resources without strict owner tagging or environmental labels**
  - **Consequence:** Untraceable cloud spend, making it impossible to identify which department or product is driving costs.
  - **Correct Approach:** Use global policy restrictions to block deployment of any resource missing mandatory environment, owner, and cost-center tags.
- **Leaving staging and development resources running 24/7 without usage checks**
  - **Consequence:** Significant resource waste and massive cloud bills for non-production environments.
  - **Correct Approach:** Implement automated shutdown scripts for idle DEV/TEST servers outside of banking working hours.
- **Budgeting without configuring real-time anomaly alerts and cost ceilings**
  - **Consequence:** Cost spikes go unnoticed until the end-of-month invoice, exceeding budgets.
  - **Correct Approach:** Configure real-time budget threshold alerts and automatic notification integrations with operations channels.""",

    "devops/observability": """## Anti-patterns
- **Logging raw or unmasked customer PII data in trace files**
  - **Consequence:** Violation of PDPL regulations and CBUAE compliance rules concerning data protection.
  - **Correct Approach:** Enforce a strict log-cleansing framework at the application layer to automatically redact credit card numbers, passwords, and IDs.
- **Setting up redundant or generic alerts, causing critical alerts to be missed**
  - **Consequence:** operational alert fatigue causing real incidents to be ignored.
  - **Correct Approach:** Define alert triggers based on customer impact metrics (SLOs) rather than generic CPU/Memory limits.
- **Lacking distributed trace identifiers across microservice boundaries**
  - **Consequence:** Extremely slow incident troubleshooting because requests cannot be traced across system boundaries.
  - **Correct Approach:** Implement trace headers correlation IDs (e.g. W3C Trace Context) in all API calls.""",

    "devops/performance-review": """## Anti-patterns
- **Running performance tests using simple, hot mock databases**
  - **Consequence:** Under-predicting latency by ignoring database locks and disk IO barriers.
  - **Correct Approach:** Test using realistic data distributions, mock latency on dependencies, and actual production scale databases.
- **Testing transaction performance purely at 100% capacity without spike simulation**
  - **Consequence:** Server crashes during unpredictable traffic spikes.
  - **Correct Approach:** Run stress tests, endurance runs, and sudden step-up spike workloads to identify bottleneck points.
- **Ignoring performance metrics and thread locks on legacy integration points**
  - **Consequence:** System failure because legacy systems freeze under load.
  - **Correct Approach:** Put down strict thread limits, queues, and connection timeouts on legacy system integrations.""",

    "devops/release-readiness": """## Anti-patterns
- **Releasing updates without automated canary or rollback procedures**
  - **Consequence:** Defective deployments immediately affect 100% of users, leading to service disruption and brand damage.
  - **Correct Approach:** Route traffic gradually via canary releases and configure auto-rollback triggers on error-rate spikes.
- **Proceeding with code deployments without formal QA and Security approvals**
  - **Consequence:** Introduction of regression bugs and serious security loopholes into production.
  - **Correct Approach:** Integrate electronic signature checks or automated pipeline gates checking for signed security/QA test passes.
- **Deploying application changes without updating internal runbooks**
  - **Consequence:** Operations teams struggle to triage incidents, increasing mean time to resolution (MTTR).
  - **Correct Approach:** Require audit check logs confirming documentation (runbook, configuration changes) is updated with each release.""",

    "devops/sre-review": """## Anti-patterns
- **Defining service level agreements (SLAs) without real SLI metrics**
  - **Consequence:** Outage events happen but dashboards continue to report green (false compliance).
  - **Correct Approach:** Link target SLOs to reliable, quantifiable metrics (e.g., successful request rates) at the entry gateway.
- **Treating post-incident reviews as a process of finding someone to blame**
  - **Consequence:** Teams hide mistakes, leading to repeated incidents and lack of learning.
  - **Correct Approach:** Conduct blameless post-mortem reviews focused on system improvements and process failures.
- **Running manual operational tasks repeatedly without work automation plans**
  - **Consequence:** High engineering overhead, burnout, and frequent human-error incidents.
  - **Correct Approach:** Track toil hours and dedicate engineering cycles to automate repeated tasks.""",

    "discovery/business-capability-map": """## Anti-patterns
- **Conflating technical components or systems with business capabilities**
  - **Consequence:** Inability to align IT investments with business outcomes, leading to system redundancy.
  - **Correct Approach:** Define capabilities as "what" the business does (e.g., Deposit Taking) rather than "how" it does it.
- **Developing the capability map inside a silo without business stake validation**
  - **Consequence:** Low adoption rate of the map, and inaccurate representing of real processes.
  - **Correct Approach:** Design the map in collaborative workshops with business unit leaders and analysts.
- **Failing to link capability definitions with regulatory controls**
  - **Consequence:** System gaps that violate compliance rules.
  - **Correct Approach:** Map regulatory requirements (CBUAE, PDPL) directly to affected capabilities in the taxonomy.""",

    "discovery/gap-analysis": """## Anti-patterns
- **Recommending solutions without clarifying the current state baseline**
  - **Consequence:** Inaccurate migration estimates, underestimating complexity, and project failure.
  - **Correct Approach:** Document the current architectural state, including active constraints and legacy tech debt.
- **Failing to prioritize identified capability gaps based on business impact**
  - **Consequence:** Wasted efforts on low-value gaps while critical business gaps remain unresolved.
  - **Correct Approach:** Score gaps by regulatory risk, business value, and implementation complexity.
- **Proposing architectural solutions that ignore organizational skill sets**
  - **Consequence:** Deploying technology that target teams cannot support or maintain.
  - **Correct Approach:** Identify training gaps as part of the analysis and plan resource training.""",

    "discovery/requirements-analysis": """## Anti-patterns
- **Eliciting functional features while neglecting non-functional requirements**
  - **Consequence:** Systems that meet functionality specs but fail under volume or scale.
  - **Correct Approach:** Require the specification of NFR limits (throughput, latency, RTO/RPO) for every requirement.
- **Accepting requirement changes without formal impact analysis**
  - **Consequence:** Scope creep, missed deadlines, and budget overruns.
  - **Correct Approach:** Put changes through an architectural gate to evaluate their impact on integration, security, and timeline.
- **Failing to trace requirements back to business case justifications**
  - **Consequence:** Implementation of custom features that add zero value to product success.
  - **Correct Approach:** Trace every technical requirement to business cases and compliance outcomes.""",

    "discovery/solution-options": """## Anti-patterns
- **Recommending a single solution without presenting alternative options**
  - **Consequence:** Confirmatory bias, lack of objective evaluation, and poor engineering decisions.
  - **Correct Approach:** Present at least 2 distinct alternative options alongside the "Do Nothing" baseline.
- **Structuring evaluation criteria around vendor biases rather than requirements**
  - **Consequence:** Vendor lock-in and high platform cost for features that are never used.
  - **Correct Approach:** Base criteria scoring on objective NFRs, business goals, and cost metrics.
- **Underestimating overall cost of ownership (TCO) and skill requirements**
  - **Consequence:** Projects run out of budget midway or rely on costly external consulting resource indefinitely.
  - **Correct Approach:** Include licensing, compute, operations, training, and maintenance costs in the TCO evaluation.""",

    "discovery/stakeholder-workshop": """## Anti-patterns
- **Running workshops without a designated and empowered decision owner**
  - **Consequence:** Endless debates that finish without consensus, delaying project progress.
  - **Correct Approach:** Identify the final decision maker before the workshop, and design exercises to align choices.
- **Proceeding with solutions before aligning on underlying problems**
  - **Consequence:** Building elegant solutions to the wrong problems, wasting time and resources.
  - **Correct Approach:** Dedicate the first half of the workshop to mapping pain points and journey constraints.
- **Excluding critical Risk, Compliance, and Security roles from initial workshops**
  - **Consequence:** Designed solutions are rejected at the board gate, requiring complete rework.
  - **Correct Approach:** Ensure representation from Risk, Compliance, and Security as key contributors in design sessions."""
}
