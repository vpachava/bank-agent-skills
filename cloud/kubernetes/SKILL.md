---
name: kubernetes
owner: Architectural Governance
version: 0.1.0
last-reviewed: 2026-08-15
description: "Use when reviewing or planning banking Kubernetes clusters (AKS/EKS/GKE) — produces a K8s-review (pod-security, networking, ingress, residency)."
required-inputs:
  - Banking workload/app-design
  - Infrastructure/VPC/Region network configuration
  - Cluster security posture (RBAC, PodSecurity)
  - Data-residency/Transfer requirements
expected-deliverables:
  - K8s readiness assessment report
  - Pod/Namespace security-profile
  - Network/Ingress/Egress risk-profile
---

# /kubernetes

## When to apply
Use to validate that a Kubernetes environment (AKS/EKS/GKE) is hardened for high-stakes banking workloads, not just developer convenience. Focuses on cluster-hardening, tenancy, and regulatory data-isolation.

## Inputs
- **Cluster Design** — IaC, Network policies, cluster-scope.
- **Security Posture** — Pod-security-standards, RBAC setup.
- **Residency Target** — UAE regions.

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
5. **Operational Audit.** Ensure Prometheus/Grafana or cloud-native logs flow securely to the bank’s SOC.

## Banking pitfalls
- **Permissive pod-security** — Running privileged containers or containers with hostPath access.
- **"Flat" Networking/Flat-cluster** — Allowing unrestricted pod-to-pod communication across different banking-domains; must segmented by namespace+NetworkPolicy.
- **Stale secrets-management** — Kubernetes Secrets-in-etcd-plain-text (must use CSI-driver with Azure/AWS/GCP Secrets Manager).
- **Public-API-server** — The K8s API server being reachable from the public internet (must have authorized-IPs or be private-link).

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of kubernetes meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the kubernetes process.**

## Outputs
- **K8s readiness assessment** — Hardening gaps, config findings.
- **Security-profile** — Documentation of tenant/namespace isolation.
- **Risk-profile** — Network/Ingress/Egress risks.

## Related skills
- [aws-review](../aws-review/SKILL.md)
- [azure-review](../azure-review/SKILL.md)
- [gcp-review](../gcp-review/SKILL.md)
