---
name: iam-review
owner: Security Architecture
version: 0.1.0
last-reviewed: 2026-08-09
description: "Use when reviewing a banking solution's identity, roles, least-privilege, and federation posture â€” produces an IAM review with findings, the UAE identity fabric (UAE Pass/EFR/UAEKYC) treatment, and remediation owners."
required-inputs:
  - IAM inventory (identity providers, role definitions, service accounts)
  - Federation & SSO configuration (incl. UAE Pass integration where present)
  - Cloud IAM policies (AWS IAM / Azure Entra ID / GCP IAM)
  - Application-level RBAC/ABAC definitions
expected-deliverables:
  - IAM review report with findings & severity
  - Least-privilege gap register
  - UAE identity fabric treatment (UAE Pass / EFR / UAEKYC assessment)
  - Remediation owners & timeline
togaf-phases: [Phase D]
togaf-artifacts: [Security Baseline]
bian-service-domains: [Security.Auth]
---

# /iam-review

## When to apply
Use when reviewing or designing a banking solution's identity and access posture â€” especially before go-live, after a material change to roles/federation, or when integrating the UAE identity fabric (UAE Pass, EFR, UAEKYC). Feeds `/zero-trust` (identity is its anchor) and `/security-architecture-review`.

## Inputs
- **IAM inventory** â€” identity providers (corporate AD/Entra ID, customer IdP), role definitions, service accounts, API keys; what identities exist and where they're managed.
- **Federation & SSO configuration** â€” how identity flows across boundaries; SAML/OIDC federation; UAE Pass integration (national ID/SSO via TDRA) where the solution touches citizen/resident identity.
- **Cloud IAM policies** â€” AWS IAM policies, Azure role assignments, GCP IAM bindings; the cloud-layer posture.
- **Application-level RBAC/ABAC** â€” the business-logic authorization layer; who can approve a payment, view a balance, trigger a KYC check.

## Process

1. **Inventory all identity sources and their trust anchors.** Map every identity provider â€” corporate, customer, partner/fintech, service-account, machine-identity (SPIFFE/mTLS). Each source needs a trust anchor: where is the assertion validated, what's the revocation path, what happens if the source is compromised?
   > NIST SP 800-63 (Digital Identity Guidelines) frames the assurance levels; map each identity source to an AAL/IAL.

2. **Review least-privilege across every layer.** For each role/policy/service-account: what can it access? Is the grant the minimum needed? Check cloud IAM (AWS policies, Azure roles, GCP bindings) and application RBAC/ABAC separately â€” cloud-layer and app-layer privileges drift independently.
   > The canonical banking failure: a service account granted admin at provisioning time, never scoped down, still admin two years later. Review *current* grants, not *intended* grants.

3. **Audit service accounts and machine identities.** Service accounts are the silent privilege-creep vector â€” they don't log in interactively, so over-privilege goes unnoticed. Enumerate every service account; verify each has a named owner, a rotation policy, and scoped-down permissions.

4. **Review federation and SSO trust boundaries.** Each federation link (SAML/OIDC) is a trust boundary. Verify: assertion validation (signature, audience, expiry), scope-down on the receiving side (don't inherit full rights from the assertion), and revocation propagation (if the source revokes, how fast does the relying party see it?).

5. **Assess the UAE identity fabric integration.**
   - **UAE Pass** â€” TDRA-backed national ID/SSO; it provides an identity *assertion*, not authorization. Verify: the bank consumes the assertion per-use, validates it (signature, freshness, audience), and never grants downstream rights solely on "UAE Pass authenticated." Treat UAE Pass as an identity source with its own trust boundary â€” the SDK is inside your scope.
   - **EFR / UAEKYC** â€” IDV/KYC SDKs (face-match, liveness, capture); they produce *verdicts* the regulated process depends on. Verify: the SDKâ†’your-app boundary is modelled as a trust boundary; verdicts are validated, not blindly trusted; biometric data handling respects PDPL residency.
   > UAE Pass/EFR/UAEKYC SDKs are trust boundaries *inside* your scope, not external-safe â€” they handle biometrics and identity assertions that downstream regulated decisions depend on.

6. **Check cross-zone identity propagation.** Where the bank straddles onshore + DIFC/ADGM, identity assertions crossing zones carry the SCC/BCR obligation. Verify: identity data (names, Emirates IDs, biometrics) crossing the boundary has a transfer basis logged; the free zone is treated as a separate trust domain, not "internal."

7. **Review break-glass and emergency access.** Emergency/break-glass accounts exist in every bank â€” verify they're inventoried, audited per-use (not just per-grant), time-limited, and that their use triggers an alert + a post-incident review.

8. **Check IAM observability.** Every authn/authz decision should be logged (who, what, when, decision, context). Verify: logs exist, are tamper-evident, feed the SIEM, and don't leak PII across a residency boundary via the logging pipeline.

## Banking pitfalls
- **Service-account privilege creep** â€” provisioned with admin, never scoped down, still admin years later; the silent IAM rot. Enumerate and scope every service account.
- **UAE Pass as trust transfer** â€” "UAE Pass logged them in, so they're authorized for everything"; consume the assertion per-use, scope-down, never inherit full rights.
- **EFR/UAEKYC verdict blindly trusted** â€” the SDK says "face matched," so the regulated decision proceeds without validating the verdict's integrity or freshness; model the SDK as a trust boundary.
- **Cloud IAM and app RBAC reviewed separately but never together** â€” a user with scoped app-RBAC but admin cloud-IAM can bypass the app layer entirely; review both layers in conjunction.
- **Break-glass accounts unaudited** â€” emergency access exists but its use isn't alerted or post-reviewed; break-glass must trigger an alert and a review.
- **Federation revocation lag** â€” identity revoked at the source but the relying party caches the assertion for hours; verify revocation propagation speed.
- **Cross-zone identity data unlogged** â€” Emirates IDs/biometrics crossing onshoreâ†”DIFC/ADGM without a transfer-basis log; the SCC/BCR obligation applies to identity data too.
- **Observability pipeline leaking PII** â€” IAM logs carrying identity data across a residency boundary; the logging path is a data flow subject to residency rules.

## Bulletproofing against Rationalization
To prevent systemic privilege escalation vectors, you MUST:

1. **Mandatory Least Privilege Enforcement:** Broad wildcards (e.g., `s3:*` or `AdministratorAccess`) are strictly prohibited in the final deployment posture.
2. **Mandatory Separation of Duties:** IAM checks MUST confirm that the entity deploying code is separate from the entity approving permissions.
3. **Mandatory Lifecycle Policy:** You MUST explicitly define how stale tokens, rotated keys, and departed users are pruned from the system automatically.

**Violating these rules invalidates the IAM Review.**

## Outputs
- **IAM review report** â€” per-layer findings (cloud IAM, app RBAC/ABAC, federation, service accounts) with severity.
- **Least-privilege gap register** â€” over-privileged grants, owners, remediation timeline.
- **UAE identity fabric assessment** â€” UAE Pass/EFR/UAEKYC trust-boundary treatment, integration posture.
- **Remediation owners & timeline** â€” per-finding handoff.

## Related skills
- [zero-trust](../zero-trust/SKILL.md) â€” identity is the anchor of zero-trust; this review feeds it.
- [threat-model](../threat-model/SKILL.md) â€” the privilege-creep and spoofing findings feed the threat model.
- [compliance](../compliance/SKILL.md) â€” UAE Pass/EFR/PDPL residency obligations bound the IAM posture.
- [security-architecture-review](../security-architecture-review/SKILL.md) â€” the broader review that gates IAM findings.
- [landing-zone-review](../../cloud/landing-zone-review/SKILL.md) â€” where cloud IAM policies physically live.
- [owasp-review](../owasp-review/SKILL.md) â€” BOPLA/broken-auth findings pair with IAM review.


### Banking Context & Examples

#### (1) Credit Card Onboarding Example
**Scenario:** IAM review for a new digital-only credit card issuance service integration.
- **Architecture Lens Check:** Verification of identity token scope-down when accessing `AECB` data services and ensuring service-account-to-service-account authentication uses mutual-TLS, not just static API keys.
- **Sample Outcome:** "IAM Gap: High-severity finding - service-account used to call AECB has broad-read access; remediation must scope to read-only for specific endpoint."
- **Common Pitfall:** Using a cross-application 'Super-API' identity for every onboarding subprocess instead of issuing granular, time-bound service-identities per transaction type.

#### (2) Customer Profile Management Example
**Scenario:** Integration review for UAE Pass authentication in a customer profile dashboard.
- **Architecture Lens Check:** Ensuring the `UAE Pass` assertion is consumed as a per-transaction identity proof and not used to generate a long-lived, over-permissive session token.
- **Sample Outcome:** "Identity Fabric: Verified UAE Pass integration boundary handles assertion validation and triggers session regeneration per profile change event."
- **Common Pitfall:** Relying solely on the presence of a `UAE Pass` session cookie for authorization, failing to cross-check authorization rights at each sensitive data-access step.

#### (3) Lending/Loans Onboarding Example
**Scenario:** Access controls review for Sharia-compliant product workflow management.
- **Architecture Lens Check:** Validating separation of duties for `Internal Sharia Governance Board` members and operational staff within the loan origination system.
- **Sample Outcome:** "RBAC Audit: Validated least-privilege enforcement - only certified Sharia board members have ability to approve loan structure changes."
- **Common Pitfall:** Granting broad `Loan Origination Admin` roles to all staff, which allows non-Sharia-certified staff to modify loan structures and triggers compliance violations.
### Regulatory References
1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/
2. **PDPL:** Personal Data Protection Law (Federal Decree-Law No. 45 of 2021)
3. **CBUAE Cybersecurity Framework:** Domain 1: Governance & Risk Management


