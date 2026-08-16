---
name: owasp-review
owner: Security Architecture
version: 0.1.0
last-reviewed: 2026-08-09
description: "Use when auditing a banking API or AI-native surface against known vulnerability categories — produces an OWASP findings report (API Top 10 + LLM Top 10 for AI surfaces) with remediation owners and severity."
required-inputs:
  - The surface in scope (API endpoints, an LLM app, an agent)
  - API contract / agent tool surface (what calls exist, what data flows)
  - Authn/authz posture (FAPI2, scopes, mTLS)
  - Known PII / payment / biometric flows through the surface
expected-deliverables:
  - OWASP findings report (API Top 10 + LLM Top 10 where AI)
  - Per-finding severity, evidence, remediation owner
  - Cross-reference to /threat-model for structural issues found here
---

# /owasp-review

## When to apply
Use for the *vulnerability-list* review of an existing API or AI-native surface — distinct from the structural `/threat-model` (which designs the trust surface). Pairs with `/threat-model` (review the v-model) and feeds `/security-architecture-review`. Especially load-bearing for the bank's **AI-native mobile** surface, where the LLM Top 10 joins the API Top 10.

## Inputs
- **The surface** — API endpoints (REST/Async) or an LLM app/agent (its prompts, tools, retrievers, the model gateway).
- **API contract / agent tool surface** — what operations exist, what data each carries, what outbound tool-calls an agent can make.
- **Authn/authz posture** — OAuth2/FAPI2 for open-banking, mTLS for internal, scopes per operation.
- **PII / payment / biometric flows** — which categories the surface handles, so the disclosure/leakage findings land on the right risks.

## Process

1. **Pick the relevant OWASP sets by surface.**
   - **API Top 10** (Broken Object-Level Authorization, Broken Auth, Broken Function-Level Auth, Unrestricted Resource Consumption, Broken Function-Level Auth…) for any API surface.
   - **LLM Top 10** (Prompt Injection, Insecure Output Handling, Training Data Poisoning, Excessive Agency…) for any agent/LLM surface — the bank's AI-native mobile on existing REST APIs sits squarely here.
   - Apply **both** if the surface is an LLM-driven API (which most bank AI-mobile surfaces are).

2. **Run each Top-10 item as a finding question against the surface.** Per item: is the surface vulnerable? evidence? severity? remediation owner? Don't handwave a category as N/A without evidence.

3. **Anchor authorization findings in the data model.** Broken Object-Level Authorization (BOPLA / IDOR-equivalent for APIs) is the canonical critical because an authenticated user accesses another's resources; trace it by resource-ownership — every endpoint exposing an account/payment/customer-id must verify the caller owns that object.

4. **For LLM surfaces, weight prompt-injection + excessive-agency.** The bank's AI-native journey has **deterministic anchors** (BPM owns KYC/issuance); an agent with tool-calls to those deterministic steps is the LLM-Top-10 surface. Find the **prompt-injection paths**, the **insecure-output-handling** (LLM output driving a downstream action unvalidated), and the **excessive-agency** (an agent with more decision-power than the regulated spine permits).

5. **Add the bank-specific disclose/leakage lens.** PII/payment/biometric disclosure through the surface, error-message leakage (stack traces, account-existence enumeration), and **observability-path leakage** (PII riding telemetry/logs across a residency boundary — the silent exfiltration path).

6. **Score severity consequence-weighted, not size-weighted.** A small IDOR on a payment status is Critical; a verbose error message on a back-office endpoint is Minor. Reserve Critical for payment/PII/biometric/regulated paths.

7. **Cross-reference structural findings to `/threat-model`.** When an OWASP finding reveals a trust-boundary or data-flow gap, escalate it into the structural threat model rather than treating it as a vuln-list line — the model owns the design fix.

8. **Capture remediation owners + a re-test path.** Each finding needs an owner and a verification path (re-test by OWASP, gate via `/security-architecture-review`). Findings without re-test ownership rot.

## Banking pitfalls
- **API Top-10 run on AI surfaces without the LLM Top-10** — the bank's AI-native mobile sits squarely in prompt-injection + excessive-agency territory; an API-only review misses them entirely. Run both.
- **BOPLA/IDOR scored Minor** — broken object-level auth on an account/payment endpoint is Critical by consequence; score consequence-weighted.
- **Prompt-injection treated as "it'll refuse"** — the regulated spine is the mitigation, not LLM refusals; model how injected/external text could drive the agent's tool-calls, and where the deterministic anchors stop it.
- **Excessive-agency uncaught** — agents granted more decision-power than the BPM-owned KYC/issuance spine permits; review the agent's tool-call authority separately from the LLM's wording.
- **Observability-path leakage missed** — PII riding traces/logs across a residency boundary; the OWASP review that ignores the telemetry path misses a disclosure surface.
- **Open-banking authz scored loosely** — FAPI2 + sender-constraining + per-TPP scopes are the posture for partner/open-banking; a review that accepts uniform scopes or no sender-constraint on regulated surfaces is weak.
- **OWASP without authn/authz posture evidence** — scoring authn findings without the actual OAuth2/FAPI2/mTLS config in hand is guessing; require the posture.
- **Findings without re-test path** — an OWASP report with owners but no verification gate rots; gate via `/security-architecture-review`.

## Bulletproofing against Rationalization
To prevent this skill from being applied as superficial box-ticking, you MUST:

1. **Mandatory Explicit Verification:** You CANNOT assume compliance. You MUST explicitly verify that the output of owasp-review meets all regulatory, security, and enterprise standards.
2. **Mandatory Accountability:** Every output artifact MUST clearly trace back to an identified business requirement, NFR, or technical constraint without ambiguity.
3. **No Unjustified Exemptions:** Any deviation from the standard architecture patterns MUST be explicitly documented as a critical risk and formally accepted.

**Violating these rules invalidates the owasp-review process.**

## Outputs
- **OWASP findings report** — API Top 10 + LLM Top 10 (where AI); per-finding evidence, severity, owner.
- **Bank-specific disclosure/leakage findings** — PII/payment/biometric, error-enumeration, telemetry-path leakage.
- **Structural escalations** — findings handed to `/threat-model` (boundary/flow gaps).
- **Re-test path** — verification gating via `/security-architecture-review`.

## Related skills
- [threat-model](../threat-model/SKILL.md) — the structural review this pairs with and escalates into.
- [security-architecture-review](../security-architecture-review/SKILL.md) — the broader review that gates these findings.
- [api-design](../../integration/api-design/SKILL.md) — the contract whose authn/authz this reviews.
- [zero-trust](../zero-trust/SKILL.md) — the posture that prevents BOPLA / lateral movement.
- [compliance](../compliance/SKILL.md) — the obligations these findings may breach.
- [observability](../../devops/observability/SKILL.md) — the telemetry-path leakage pitfall, owned here.
- [production-readiness](../../governance/production-readiness/SKILL.md) — the gate that verifies findings closed before go-live.
