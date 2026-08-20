---
name: owasp-review
owner: Security Architecture
version: 0.1.0
last-reviewed: 2026-08-09
description: "Use when auditing a banking API or AI-native surface against known vulnerability categories â€” produces an OWASP findings report (API Top 10 + LLM Top 10 for AI surfaces) with remediation owners and severity."
required-inputs:
  - The surface in scope (API endpoints, an LLM app, an agent)
  - API contract / agent tool surface (what calls exist, what data flows)
  - Authn/authz posture (FAPI2, scopes, mTLS)
  - Known PII / payment / biometric flows through the surface
expected-deliverables:
  - OWASP findings report (API Top 10 + LLM Top 10 where AI)
  - Per-finding severity, evidence, remediation owner
  - Cross-reference to /threat-model for structural issues found here
togaf-phases: [Phase D]
togaf-artifacts: [Security Baseline]
bian-service-domains: [Security.Auth]
---

# /owasp-review

## When to apply
Use for the *vulnerability-list* review of an existing API or AI-native surface â€” distinct from the structural `/threat-model` (which designs the trust surface). Pairs with `/threat-model` (review the v-model) and feeds `/security-architecture-review`. Especially load-bearing for the bank's **AI-native mobile** surface, where the LLM Top 10 joins the API Top 10.

## Inputs
- **The surface** â€” API endpoints (REST/Async) or an LLM app/agent (its prompts, tools, retrievers, the model gateway).
- **API contract / agent tool surface** â€” what operations exist, what data each carries, what outbound tool-calls an agent can make.
- **Authn/authz posture** â€” OAuth2/FAPI2 for open-banking, mTLS for internal, scopes per operation.
- **PII / payment / biometric flows** â€” which categories the surface handles, so the disclosure/leakage findings land on the right risks.

## Process

1. **Pick the relevant OWASP sets by surface.**
   - **API Top 10** (Broken Object-Level Authorization, Broken Auth, Broken Function-Level Auth, Unrestricted Resource Consumption, Broken Function-Level Authâ€¦) for any API surface.
   - **LLM Top 10** (Prompt Injection, Insecure Output Handling, Training Data Poisoning, Excessive Agencyâ€¦) for any agent/LLM surface â€” the bank's AI-native mobile on existing REST APIs sits squarely here.
   - Apply **both** if the surface is an LLM-driven API (which most bank AI-mobile surfaces are).

2. **Run each Top-10 item as a finding question against the surface.** Per item: is the surface vulnerable? evidence? severity? remediation owner? Don't handwave a category as N/A without evidence.

3. **Anchor authorization findings in the data model.** Broken Object-Level Authorization (BOPLA / IDOR-equivalent for APIs) is the canonical critical because an authenticated user accesses another's resources; trace it by resource-ownership â€” every endpoint exposing an account/payment/customer-id must verify the caller owns that object.

4. **For LLM surfaces, weight prompt-injection + excessive-agency.** The bank's AI-native journey has **deterministic anchors** (BPM owns KYC/issuance); an agent with tool-calls to those deterministic steps is the LLM-Top-10 surface. Find the **prompt-injection paths**, the **insecure-output-handling** (LLM output driving a downstream action unvalidated), and the **excessive-agency** (an agent with more decision-power than the regulated spine permits).

5. **Add the bank-specific disclose/leakage lens.** PII/payment/biometric disclosure through the surface, error-message leakage (stack traces, account-existence enumeration), and **observability-path leakage** (PII riding telemetry/logs across a residency boundary â€” the silent exfiltration path).

6. **Score severity consequence-weighted, not size-weighted.** A small IDOR on a payment status is Critical; a verbose error message on a back-office endpoint is Minor. Reserve Critical for payment/PII/biometric/regulated paths.

7. **Cross-reference structural findings to `/threat-model`.** When an OWASP finding reveals a trust-boundary or data-flow gap, escalate it into the structural threat model rather than treating it as a vuln-list line â€” the model owns the design fix.

8. **Capture remediation owners + a re-test path.** Each finding needs an owner and a verification path (re-test by OWASP, gate via `/security-architecture-review`). Findings without re-test ownership rot.

## Banking pitfalls
- **API Top-10 run on AI surfaces without the LLM Top-10** â€” the bank's AI-native mobile sits squarely in prompt-injection + excessive-agency territory; an API-only review misses them entirely. Run both.
- **BOPLA/IDOR scored Minor** â€” broken object-level auth on an account/payment endpoint is Critical by consequence; score consequence-weighted.
- **Prompt-injection treated as "it'll refuse"** â€” the regulated spine is the mitigation, not LLM refusals; model how injected/external text could drive the agent's tool-calls, and where the deterministic anchors stop it.
- **Excessive-agency uncaught** â€” agents granted more decision-power than the BPM-owned KYC/issuance spine permits; review the agent's tool-call authority separately from the LLM's wording.
- **Observability-path leakage missed** â€” PII riding traces/logs across a residency boundary; the OWASP review that ignores the telemetry path misses a disclosure surface.
- **Open-banking authz scored loosely** â€” FAPI2 + sender-constraining + per-TPP scopes are the posture for partner/open-banking; a review that accepts uniform scopes or no sender-constraint on regulated surfaces is weak.
- **OWASP without authn/authz posture evidence** â€” scoring authn findings without the actual OAuth2/FAPI2/mTLS config in hand is guessing; require the posture.
- **Findings without re-test path** â€” an OWASP report with owners but no verification gate rots; gate via `/security-architecture-review`.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of owasp-review meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the owasp-review process.**

## Outputs
- **OWASP findings report** â€” API Top 10 + LLM Top 10 (where AI); per-finding evidence, severity, owner.
- **Bank-specific disclosure/leakage findings** â€” PII/payment/biometric, error-enumeration, telemetry-path leakage.
- **Structural escalations** â€” findings handed to `/threat-model` (boundary/flow gaps).
- **Re-test path** â€” verification gating via `/security-architecture-review`.

## Related skills
- [threat-model](../threat-model/SKILL.md) â€” the structural review this pairs with and escalates into.
- [security-architecture-review](../security-architecture-review/SKILL.md) â€” the broader review that gates these findings.
- [api-design](../../integration/api-design/SKILL.md) â€” the contract whose authn/authz this reviews.
- [zero-trust](../zero-trust/SKILL.md) â€” the posture that prevents BOPLA / lateral movement.
- [compliance](../compliance/SKILL.md) â€” the obligations these findings may breach.
- [observability](../../devops/observability/SKILL.md) â€” the telemetry-path leakage pitfall, owned here.
- [production-readiness](../../governance/production-readiness/SKILL.md) â€” the gate that verifies findings closed before go-live.


### Banking Context & Examples

#### (1) Credit Card Onboarding Example
**Scenario:** OWASP API review for a third-party credit card origination endpoint.
- **Architecture Lens Check:** Focused evaluation on `BOPLA` (Broken Object-Level Authorization) allowing one user to query another user's credit application status and ensuring `AECB` data snippets are not leaked in error messages.
- **Sample Outcome:** "Findings: IDOR vulnerability detected on `/applications/{id}` endpoint; remediate by enforcing per-request owner-check against the authenticated `UAE Pass` session."
- **Common Pitfall:** Assuming that because an endpoint is `OAuth2` protected, per-object authorization check is redundant; this leads to broken object-level authorization (BOPLA) gaps.

#### (2) Customer Profile Management Example
**Scenario:** Security review for an AI-native profile management bot.
- **Architecture Lens Check:** Stress-testing against `Prompt Injection` trying to exfiltrate customer bank account details via PII leakage and checks for `Insecure Output Handling` when displaying data fetched from legacy core.
- **Sample Outcome:** "LLM Findings: Critical - injection path detected allowing bot to reveal account masking patterns. Remediation: Implement strict response-validation regex for customer account displays."
- **Common Pitfall:** Trusting raw AI responses from legacy data-fetching tools without sanitizing the output, which allows LLM hallucination-led data disclosure.

#### (3) Lending/Loans Onboarding Example
**Scenario:** Security review for Sharia-compliant loan origination API.
- **Architecture Lens Check:** Validating `FAPI2` compliance for Open Banking API access and ensuring business logic (i.e., loan modification) checks comply with `Sharia Board` rules via transactional signature enforcement.
- **Sample Outcome:** "API Security: Verified FAPI2 compliance. Finding: Missing per-operation sender-constraint on `/loan/modify` endpoint."
- **Common Pitfall:** Applying generic API security templates that lack sender-constraint, thus failing open-banking API standards (FAPI2) required for regulated financial integrations.
## Bulletproofing
- **Governance Policy:** Enforce [CBUAE Rulebook](governance/policy/regulations.yaml#CBUAE), [PDPL](governance/policy/regulations.yaml#PDPL), and [PCI-DSS](governance/policy/regulations.yaml#PCI-DSS) where applicable.

## Anti-patterns
- **Relying entirely on perimeter firewalls (WAF) instead of fixing underlying code vulnerabilities**
  - **Consequence:** Sophisticated attackers bypass the WAF (e.g., via specialized SQL injection strings) and gain full control of the application backend.
  - **Correct Approach:** Implement defense-in-depth by fixing code vulnerabilities directly using parameterized queries and input sanitization libraries.
- **Using outdated, manual penetration testing as the primary method to find OWASP Top 10 vulnerabilities**
  - **Consequence:** Security feedback is too slow, and critical vulnerabilities are released to production between annual penetration tests.
  - **Correct Approach:** Integrate automated Static (SAST), Dynamic (DAST), and Software Composition Analysis (SCA) directly into the CI/CD pipeline.
- **Implementing "roll-your-own" cryptography, hashing, or session management logic**
  - **Consequence:** Introduction of subtle cryptographic flaws (e.g., weak salts, timing attacks) that attackers readily exploit.
  - **Correct Approach:** Mandate the use of well-vetted, standard industry libraries (e.g., Argon2 for hashing, robust JWT libraries) and never author custom crypto.
