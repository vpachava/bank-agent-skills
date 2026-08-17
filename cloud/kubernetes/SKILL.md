---
name: kubernetes
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when reviewing or planning banking Kubernetes clusters (AKS/EKS/GKE) â€” produces a K8s-review (pod-security, networking, ingress, residency)."
required-inputs:
  - Banking workload/app-design
  - Infrastructure/VPC/Region network configuration
  - Cluster security posture (RBAC, PodSecurity)
  - Data-residency/Transfer requirements
expected-deliverables:
  - K8s readiness assessment report
  - Pod/Namespace security-profile
  - Network/Ingress/Egress risk-profile
togaf-phases: [Phase D]
togaf-artifacts: [Deployment Diagram]
bian-service-domains: [Integration.API]
---

# /kubernetes

## When to apply
Use to validate that a Kubernetes environment (AKS/EKS/GKE) is hardened for high-stakes banking workloads, not just developer convenience. Focuses on cluster-hardening, tenancy, and regulatory data-isolation.

## Inputs
- **Cluster Design** â€” IaC, Network policies, cluster-scope.
- **Security Posture** â€” Pod-security-standards, RBAC setup.
- **Residency Target** â€” UAE regions.

## Process
1. **Verify UAE-Region/Zone.** Ensure nodes occupy compliant zones.
2. **Cluster Security Hardening.**
   - Pod Security Admissions (formerly PSPs).
   - RBAC strictly tied to EntraID/IAM roles.
   - Network Policies (deny-all-by-default).
3. **Ingress/Egress Governance.**
   - Ingress controller hardening.
   - Egress-gateway for filtering bank-to-external-API traffic (critical for security).
4. **Data-Residency/Encryption.** Ensure persistent-volumes (PVs) are encrypted at rest (CMK).
5. **Operational Audit.** Ensure Prometheus/Grafana or cloud-native logs flow securely to the bankâ€™s SOC.

## Banking pitfalls
- **Permissive pod-security** â€” Running privileged containers or containers with hostPath access.
- **"Flat" Networking/Flat-cluster** â€” Allowing unrestricted pod-to-pod communication across different banking-domains; must segmented by namespace+NetworkPolicy.
- **Stale secrets-management** â€” Kubernetes Secrets-in-etcd-plain-text (must use CSI-driver with Azure/AWS/GCP Secrets Manager).
- **Public-API-server** â€” The K8s API server being reachable from the public internet (must have authorized-IPs or be private-link).

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of kubernetes meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the kubernetes process.**

## Outputs
- **K8s readiness assessment** â€” Hardening gaps, config findings.
- **Security-profile** â€” Documentation of tenant/namespace isolation.
- **Risk-profile** â€” Network/Ingress/Egress risks.

## Related skills
- [aws-review](../aws-review/SKILL.md)
- [azure-review](../azure-review/SKILL.md)
- [gcp-review](../gcp-review/SKILL.md)

### Banking Context & Examples

#### (1) Pod Security Standards (PSS) Example
**Scenario:** Deploying a service processing sensitive payment messages.
- **Architecture Lens Check:** Verification that the Pod Security Admission (PSA) enforces the "restricted" profile, forbidding privileged mode and high-risk hostPath volumes.
- **Sample Outcome:** "Namespace `payments` verified for Restricted PSS; pods are prevented from escalating privileges, mitigating container breakout risks."
- **Common Pitfall:** Using "privileged" containers just to easily install debugging tools in staging; itâ€™s too easy to accidentally carry this configuration over to production, creating a massive security vulnerability.

#### (2) Flat Networking Segregation Example
**Scenario:** Running high-risk `KYC-Management` and low-risk `Marketing-Content` microservices on the same cluster.
- **Architecture Lens Check:** Enforcing `NetworkPolicies` to deny pod-to-pod traffic between `KYC` and `Marketing` namespaces by default.
- **Common Pitfall:** Assuming internal cluster traffic is inherently "trusted"; if the marketing service is compromised, a lack of `NetworkPolicies` allows the attacker to move laterally and scrape KYC customer data.

#### (3) Sharia Product Aggregator Egress Example
**Scenario:** Limiting egress from an aggregator pod to specifically approved third-party rate-providers.
- **Architecture Lens Check:** Using an `Egress-Gateway` to whitelist only authorized APIs, preventing data-exfiltration.
- **Sample Outcome:** "Egress Compliance: Pod traffic limited via Egress-Gateway to API-whitelisted domains only."
- **Common Pitfall:** Allowing `0.0.0.0/0` egress to the public internet. A compromised container can then exfiltrate sensitive data or reach a command-and-control server without being blocked by the clusterâ€™s network configuration.

### Regulatory References
1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/
2. **PDPL:** Personal Data Protection Law (Federal Decree-Law No. 45 of 2021)
3. **CBUAE Cybersecurity Framework:** Domain 1: Governance & Risk Management

## Anti-patterns
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
  - **Correct Approach:** Bind the API server to private endpoints, load balancers, or enforce strict authorized IP listings.
