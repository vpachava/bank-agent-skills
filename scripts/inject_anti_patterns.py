import os
import re
from pathlib import Path

# Mapping of relative skill path/ID to its markdown Anti-patterns section
ANTI_PATTERNS = {
    ".claude/tdd-documentation": """## Anti-patterns
- **Skipping test failures to write more code**
  - **Consequence:** Accumulated bugs, regression loops, and unreliable codebases.
  - **Correct Approach:** Treat any test failure as a blocking event; stop and fix it before implementing new features.
- **Writing tests post-hoc to match existing implementation**
  - **Consequence:** Confirmatory bias, poor design modularity, and missing edge cases.
  - **Correct Approach:** Practice strict red-green-refactor by writing the test assertion first, watching it fail, and then implementing the minimal code to pass.
- **Isolating tests from business functional logic**
  - **Consequence:** Green tests that pass technical constraints but fail actual user stories.
  - **Correct Approach:** Align test cases directly with business acceptance criteria and functional specifications.""",

    "architecture/architecture-decision-records": """## Anti-patterns
- **Treating ADRs as post-facto documentation rather than decision-making tools**
  - **Consequence:** Lack of real options analysis, architectural drift, and inability to justify choices to regulators or audit teams.
  - **Correct Approach:** Author ADRs during the design phase to align stakeholders before writing any production code.
- **Failing to record "Do Nothing" or alternative options considered**
  - **Consequence:** Future team members re-evaluate the same options or do not understand why the obvious alternative lost.
  - **Correct Approach:** Always document at least two active alternatives plus the 'Do Nothing' option with clear technical and financial costs.
- **Omitting negative consequences or reversibility costs**
  - **Consequence:** Unanticipated lock-in, resource debt, and system failure when reversing are required.
  - **Correct Approach:** Explicitly state negative consequences, run-cost implications, skill-set debt, and the steps/costs to reverse the decision.""",

    "architecture/architecture-review": """## Anti-patterns
- **Conducting the review as an end-of-project gate**
  - **Consequence:** Discovered architectural flaws are too costly to fix, leading to exceptions, compromises, and launch delays.
  - **Correct Approach:** Schedule lightweight checkpoint reviews at major design and implementation milestones throughout the lifecycle.
- **Focusing on technical purity over business value and constraints**
  - **Consequence:** High cost, complex designs that fail to deliver the core business capability on time.
  - **Correct Approach:** Evaluate designs against business requirements, NFR metrics, and compliance limits rather than theoretical ideals.
- **Reviewing systems without simulating peak production-like throughputs**
  - **Consequence:** Performance degradation and sudden system failure under live consumer load.
  - **Correct Approach:** Require load-test results and stress-simulation reports as part of the architecture review materials.""",

    "architecture/c4-model": """## Anti-patterns
- **Mixing abstractions across different C4 levels**
  - **Consequence:** Confusing diagrams that show specific class implementations next to high-level context blocks, reducing readability.
  - **Correct Approach:** Keep visual boundaries separated into distinct Context (L1), Container (L2), Component (L3), and Code (L4) diagrams.
- **Omitting communication protocols and technologies on links**
  - **Consequence:** Ambiguous diagrams where the implementation details of integration paths are completely hidden.
  - **Correct Approach:** Annotate every connection line with the technology (e.g., HTTPS, gRPC, AMQP) and interaction style (e.g., Sync, Async).
- **Letting diagrams drift from codebase reality**
  - **Consequence:** Outdated diagrams mislead architects during incident resolution or design iterations.
  - **Correct Approach:** Embed diagram generation in documentation repositories and update them alongside any code changes.""",

    "architecture/database-design": """## Anti-patterns
- **Hardcoding schemas without AI or vector indexing paths where RAG is expected**
  - **Consequence:** Inability to scale semantic search or contextual integration for banking AI bots, creating a modernization bottleneck.
  - **Correct Approach:** Design databases with modular vector extensions or hybrid search schemas from the start.
- **Relying entirely on application/client-side logic for data integrity**
  - **Consequence:** Corrupt or inconsistent data in database tables due to bypass scripts, multiple clients, or concurrent writes.
  - **Correct Approach:** Enforce foreign keys, unique constraints, and check constraints directly at the database engine schema layer.
- **Failing to plan database schema migrations under active live write-load**
  - **Consequence:** Severe database locking, timeouts, and transaction failures during application updates.
  - **Correct Approach:** Adopt online, zero-downtime migration patterns like Expanding and Contracting (Blue-Green database schema changes).""",

    "architecture/deployment-diagrams": """## Anti-patterns
- **Conflating logical container interfaces with physical network paths**
  - **Consequence:** Vulnerabilities from exposing backend APIs to insecure network segments without perimeter firewalls or API gateways.
  - **Correct Approach:** Explicitly map physical networks, subnet boundaries, firewall rules, and API gateway routing.
- **Failing to show regional and availability zone boundaries**
  - **Consequence:** Single-point-of-failure architectures that cannot meet resilience or data residency constraints (e.g. UAE data laws).
  - **Correct Approach:** Structure diagrams to show replication, failover, and active-active setups across distinct zones/regions.
- **Omitting deployment/management components like CI/CD runners or jump boxes**
  - **Consequence:** Hidden attack vectors and unmonitored access points to production database/compute nodes.
  - **Correct Approach:** Document the management and control plane boundary alongside the runtime application architecture.""",

    "architecture/hld-generator": """## Anti-patterns
- **Including low-level implementation details and specific code snippets**
  - **Consequence:** Fast obsolescence of the High-Level Design (HLD) document and developer micro-management.
  - **Correct Approach:** Focus on container boundaries, integration patterns, data schemas, and non-functional requirements.
- **Designing the system without linking to specific NFRs (RTO/RPO)**
  - **Consequence:** Failure to achieve business SLA metrics when disaster recovery is executed in production.
  - **Correct Approach:** Include dedicated sections mapping structural design choices directly to RTO, RPO, and security metrics.
- **Oversimplifying the integration boundary between legacy systems and new cloud systems**
  - **Consequence:** Underestimating sync requirements, resulting in data inconsistency, lag, or API exhaustion.
  - **Correct Approach:** Detail data format mappings, sync/async styles, latency boundaries, and failover pathways for all legacy links.""",

    "architecture/lld-generator": """## Anti-patterns
- **Failing to specify precise data models and parameter types**
  - **Consequence:** Miscommunication between contract designers and developers, leading to coding bugs and integration mismatches.
  - **Correct Approach:** Define interfaces, parameters, and return types using schema standards (OpenAPI, JSON Schema, Protobuf).
- **Ignoring exception and boundary state handling in sequence and component flows**
  - **Consequence:** Cascading failures and incomplete logging during edge-case errors in live setups.
  - **Correct Approach:** Model alternate, exception, and rollback paths for all primary workflow paths.
- **Designing specifications that ignore concurrency, locking, and race conditions**
  - **Consequence:** Intermittent database deadlock errors or race conditions when scaling beyond a single thread.
  - **Correct Approach:** Explicitly document synchronization locks, transactional boundaries, and thread safety mechanisms.""",

    "architecture/nfr-checklist": """## Anti-patterns
- **Targeting NFR metrics without identifying corresponding measurement tools**
  - **Consequence:** Unverifiable performance claims that lead to conflicts during deployment and operational validation.
  - **Correct Approach:** Define each NFR with a measurable metric, target threshold, and the tool/script used to monitor it.
- **Setting excessive/unnecessary NFR targets (e.g., 99.999% uptime) without budget alignment**
  - **Consequence:** Disproportionately high infrastructure architecture costs and extended delivery timelines.
  - **Correct Approach:** Balance engineering uptime targets against the financial impact of downtime and actual business budget.
- **Treating NFR checklist validation as a post-implementation compliance phase**
  - **Consequence:** Discovery of structural failures (e.g., bad RTO replication) late, requiring costly retrofitting work.
  - **Correct Approach:** Evaluate and mock-test NFR achievements continuously during design spikes and integration sprints.""",

    "architecture/sequence-diagrams": """## Anti-patterns
- **Neglecting to map retry logic and timeout scenarios on external steps**
  - **Consequence:** Cascading timeouts and thread pool exhaustion when an upstream dependency experiences latency.
  - **Correct Approach:** Model circuit breakers, retry counts, fallback APIs, and timeout limits on all external network call arrows.
- **Overloading a single diagram with detailed branch logic and loops**
  - **Consequence:** Visual clutter that makes the sequence flow illegible to business stakeholders and developers.
  - **Correct Approach:** Keep diagrams focused on primary architectural pathways and split complex scenarios into separate documents.
- **Assuming instantaneous message delivery across distributed systems**
  - **Consequence:** Design gaps that lead to inconsistencies, out-of-order execution, or message drops.
  - **Correct Approach:** Model asynchronous queues, ACK/NACK behaviors, and out-of-order handling explicitly.""",

    "cloud/aws-review": """## Anti-patterns
- **Deploying a flat cloud VPC without clear subnet boundary isolations**
  - **Consequence:** Compromised application instances expose secure database instances directly to public network traffic.
  - **Correct Approach:** Segment infrastructure into public, private, and isolated data subnets with strict security groups.
- **Using IAM users with long-lived access keys instead of IAM Roles/STS**
  - **Consequence:** Hardcoded keys in source control, credential leakage, and high risk of unauthorized cloud manipulation.
  - **Correct Approach:** Authenticate services using AWS IAM Roles for Service Accounts (IRSA) or instance profiles.
- **Ignoring UAE-specific AWS data residency boundaries**
  - **Consequence:** Violation of CBUAE or PDPL data hosting regulations by routing PII out of country.
  - **Correct Approach:** Pin deployment resources to the UAE region and run local audits to block any cross-region data transit.""",

    "cloud/azure-review": """## Anti-patterns
- **Exposing Azure SQL database or Storage services directly using public endpoints**
  - **Consequence:** Security vulnerabilities and exposure to brute force attacks on database credentials.
  - **Correct Approach:** Enforce Azure Private Endpoints (Private Link) to route data traffic strictly over internal VNets.
- **Granting broad Owner/Contributor permissions at subscription level instead of custom RBAC**
  - **Consequence:** Operational mistakes, accidental deletion of resource groups, and security compromise.
  - **Correct Approach:** Implement the principle of least privilege using Azure Active Directory (Entra ID) and custom RBAC scopes.
- **Ignoring Azure cross-region PII data movement boundaries**
  - **Consequence:** Unintentional storage of customer records in European/American datacenters, violating UAE data privacy laws.
  - **Correct Approach:** Restrict Azure Policy to enforce resources and geo-redundancies to reside exclusively within UAE North.""",

    "cloud/gcp-review": """## Anti-patterns
- **Using the default VPC network and its automatic subnet IP allocations**
  - **Consequence:** Overlapping IP ranges with corporate networks block on-prem VPN access, and public IP footprints are larger than needed.
  - **Correct Approach:** Create custom VPCs and define explicit subnet IP allocations with private Google Access enabled.
- **Saving GCP Service Account keys in local JSON files or repository code**
  - **Consequence:** Security leakage risks, lack of key rotation, and potential privilege escalation.
  - **Correct Approach:** Leverage Workload Identity Federation to authenticate workloads without requiring long-lived key files.
- **Running Google Cloud storage buckets without configuring uniform bucket-level access**
  - **Consequence:** Public exposure of critical banking objects due to granular ACL misconfigurations.
  - **Correct Approach:** Enforce Uniform Bucket-Level Access and run regular IAM reviews in GCP Security Command Center.""",

    "cloud/kubernetes": """## Anti-patterns
- **Running containers with privileged flags or hostPath directory access**
  - **Consequence:** Host node compromises, privilege escalation vulnerabilities, and compliance gate failures.
  - **Correct Approach:** Apply Pod Security Standards (restricted) and run containers strictly as non-root users.
- **Deploying a flat namespace cluster without network interface policies**
  - **Consequence:** Undetected pod-to-pod communication across different namespaces/security zones, violating isolation rules.
  - **Correct Approach:** Implement deny-all network policies by default and explicitly white-list required ports and targets.
- **Storing API keys and database credentials in standard base64 Kubernetes Secrets**
  - **Consequence:** Secrets are saved in plain text in etcd, allowing host-level users or backups to compromise them.
  - **Correct Approach:** Use external Secrets Store CSI Driver integration (e.g. AWS Secrets Manager/Azure Key Vault) to inject secrets dynamically.
- **Exposing the Kubernetes API server directly to the public internet**
  - **Consequence:** High exposure to zero-day K8s API exploits and brute force access attempts.
  - **Correct Approach:** Bind the API server to private endpoints, load balancers, or enforce strict authorized IP listings.""",

    "cloud/landing-zone-review": """## Anti-patterns
- **Setting up isolated subscriptions/projects without central network hub routing**
  - **Consequence:** High cost, complex point-to-point network tunnels, and lack of firewall visibility across zones.
  - **Correct Approach:** Deploy a Hub-and-Spoke topology with centralized Azure Firewall or AWS Network Firewall.
- **Relying on manual provisioning of environments inside landing zone folders**
  - **Consequence:** Configuration drift, auditing failures, and inconsistent security practices across tenants.
  - **Correct Approach:** Enforce Landing Zone deployment via IaC and orchestrate subscriptions using GitOps.
- **Missing centralized syslog and activity log forwarding**
  - **Consequence:** Inability to perform compliance forensically or trace user actions during a security incident.
  - **Correct Approach:** Auto-integrate Centralized Logging (SIEM/SOC integration) for all landing zone accounts from day one.""",

    "cloud/terraform": """## Anti-patterns
- **Committing local terraform.tfstate files or sensitive secrets to git**
  - **Consequence:** Credentials exposure, state locking issues, and resource overwrites during parallel executions.
  - **Correct Approach:** Store terraform state in a secure remote backend (e.g., S3/GCS) with DynamoDB/Firestore locking.
- **Hardcoding cloud resource variables inside Terraform modules**
  - **Consequence:** Code repetition, lack of reusability, and deployment errors across environments (dev/prod).
  - **Correct Approach:** Use tfvars files and modularize code to accept input parameters dynamically.
- **Skipping strict static analysis or validation tools (tflint, tfsec, checkov) in pipeline**
  - **Consequence:** Deployment of insecure infrastructure (e.g., open security groups, unencrypted databases).
  - **Correct Approach:** Integrate automated compliance check gates inside CI/CD linting phases before applying Terraform plans."""
}
