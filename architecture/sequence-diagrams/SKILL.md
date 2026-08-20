---
name: sequence-diagrams
owner: Solution Architecture
version: 0.1.0
last-reviewed: 2026-08-08
description: "Use when you need to show how a banking flow behaves end-to-end â€” produces sequence diagrams (via /archify) covering happy path + exception/escalation/retake paths, with regulated gates and legacy-core seams marked."
required-inputs:
  - The flow(s) to model (the journey or operation)
  - Actors & systems involved (incl. legacy core, channels, partners)
  - The regulated gates in the flow (KYC, risk, AML, issuance)
  - Known exception / fallback / escalation paths
expected-deliverables:
  - Sequence diagram(s) for the flow(s) â€” happy path
  - Exception-path sequence fragments (escalate, retake, timeout, abort)
  - Bank-convention markers: regulated gates, provenance points, legacy-core seams
togaf-phases: [Phase C]
togaf-artifacts: [HLD]
bian-service-domains: [Integration.API]
---

# /sequence-diagrams

## When to apply
Use whenever a flow's behavior has to be made precise â€” the LLD detail step, a design review where "and then what happens if X fails" is the question, a compliance walkthrough. Rendering delegates to `/archify`. Pairs with `/c4-model` (the static structure) â€” sequence is the dynamic complement.

## Inputs
- **The flow(s)** â€” the journey or operation (onboarding happy path, payment, account opening, KYC verification, etc.).
- **Actors & systems** â€” incl. the legacy core modules, channels, the UAE identity fabric (UAE Pass/EFR/UAEKYC), payment rails, partners.
- **Regulated gates** â€” the deterministic KYC/risk/AML/issuance steps that must sit on the flow (from `/hld-generator` or the compliance work).
- **Known exception / fallback / escalation paths** â€” the retake, escalate-to-human, timeout, abandon-resume stories.

## Process
1. **Name the flow and its entry & exit points.** Start state, end state, who initiates. A sequence diagram for a flow you can't state the endpoints of is unfocused.

2. **Fix the actors (left-to-right) by zone, not by alphabet.** Group the participating systems by zone â€” customer channel / AI tier / deterministic backbone / legacy core / external (UAE identity, rails). Lifelines in a zone grid make the cross-zone crossings â€” the interesting bits â€” jump out.

3. **Draw the happy path first, simply.** Just the calls that make the flow succeed. Keep messages concise (verb + object); detail goes into the next step, not the happy path's prose.

4. **Layer regulated gates onto the happy path.** Mark the deterministic KYC verdict, risk/AML screening, issuance ceremony as gate blocks. This is where the flow's *control* lives, and a sequence without the gates is the dynamic equivalent of a context diagram with 40 boxes.
   > Banking convention: gate blocks marked; a provenance point noted where a value becomes "authoritative" (e.g., post-IDV EID).

5. **Draw the exception paths as separate fragments.** Each exception â€” provider-SDK retake (AI never re-OCRs), Tier-3 escalate-to-human, timeout/abort, abandon-resume, duplicate-idempotency-rejection â€” is its own fragment or its own diagram. Don't try to cram all of the exception surface into the happy path with `alt` boxes that nobody will trace.
   > In a bank, the exception paths are the *most likely* paths; the happy path is the rarest one in the wild.

6. **Capture retry, idempotency, and reconcile strokes.** Where a flow retries (with an idempotency key), where it reconciles (a camt-style statement vs ledger), where it escalates â€” these are the strokes that make a sequence reviewable by Compliance.

7. **Delegate rendering to `/archify`.** Hand it the structured sequence input (plain-language or pasted Mermaid sequenceDiagram); it returns polished explorable diagrams (light/dark, PNG/JPEG/SVG/WebM). This skill owns the *content* â€” actors-by-zone, gates, fragments â€” not the rendering.

8. **Annotate provenance and audit points.** Where a value becomes authoritative, where an audit log is written, where a dual-signature ceremony happens â€” mark them. These are the points Compliance and the `/threat-model` review zero in on.

## Bulletproofing against Rationalization
- **Happy-path-only sequences** â€” the rarest path alone; the exception / escalation / retake / reconcile stories are where the design earns its keep and where Compliance reads.
- **No regulated gates on the flow** â€” a sequence that glides through KYC/risk/AML/issuance as ordinary calls misrepresents who controls the journey; mark the gates.
- **Actors not grouped by zone** â€” alphabetical lifelines hide the cross-zone crossings (the design center); zone-grouping surfaces them at a glance.
- **Idempotency & reconciliation invisible** â€” retry without an idempotency key, payment without reconcile â€” these are the defects Compliance finds in review; show the strokes.
- **Crammed exception alt-boxes** â€” every exception folded into one diagram via `alt`/`loop` makes it untraceable; split into fragments.
- **AI-as-decider on regulated steps** â€” sequences that show an AI bot making the KYC/AML/issuance verdict instead of a deterministic BPM actor have broken the compliance boundary; the AI orchestrates, BPM decides.
- **Rendering over content** â€” the elegant sequence diagram that misrepresents an exception path is worse than a rough honest one; own the content, delegate the rendering.

## Bulletproofing against Rationalization
To prevent Sequence Diagrams from being happy-path fantasies, you MUST:

1. **Mandatory Failure Path Inclusion:** Every single synchronous integration call (API, Database, Event Publish) MUST explicitly model its Timeout/Failure/Fallback response route.
2. **Mandatory Gateway Validation:** Sequence flows MUST explicitly document Auth/Token validation paths at the boundary. "Magic auth" is forbidden.
3. **Idempotency Tracing:** State-mutating steps (e.g. POST, PUT, transactions) MUST document the idempotency key flow visually.
4. **Real-world Latency Notation:** You MUST NOT model multi-region or cross-zone data interactions as instantaneous; boundary jumps must be acknowledged.

**Violating these rules invalidates the Sequence Diagram.**

## Outputs
- **Sequence diagram(s)** â€” happy path, rendered by `/archify`.
- **Exception-path fragments** â€” escalate / retake / timeout / abort / resume.
- **Bank-convention markers** â€” regulated gates, provenance/authoritative-value points, audit-write points, legacy-core seams.

## Related skills
- [/archify](../../../../) â€” rendering engine for the diagrams.
- [c4-model](../c4-model/SKILL.md) â€” the static complement to these dynamic views.
- [deployment-diagrams](../deployment-diagrams/SKILL.md) â€” the topology view this pairs with.
- [lld-generator](../lld-generator/SKILL.md) â€” the doc these sequences embed in.
- [threat-model](../../security/threat-model/SKILL.md) â€” reads these sequences to find the threat surface at each crossing.
- [event-driven](../../integration/event-driven/SKILL.md) â€” where async events replace/extend the sync sequence.

### Banking Context & Examples

#### (1) Retail Banking Scenario
**Scenario:** Applying this skill in a retail bank core-modernization effort.
- **Architecture Lens Check:** Verification of compliance with CBUAE data-residency rules (e.g. [[compliance]]).
- **Sample Outcome:** "Design: Automated workflow integration; [[observability]] logs scrubbed of PII."
- **Common Pitfall:** Ignoring the Sharia-governance impact on the product-schema.

#### (2) Corporate Banking Scenario
**Scenario:** Using this skill for a corporate digital-onboarding integration.
- **Architecture Lens Check:** Alignment with AECB credit-reporting integration for legal-entity applicants.
- **Sample Outcome:** "Design: Integration-seam validated for high-assurance KYC; [[api-design]] handles large payload-signatures."
- **Common Pitfall:** Bypassing the mandatory legal-entity KYC check due to tight project timelines.

#### (3) Islamic Banking Scenario
**Scenario:** Utilizing this skill for Sharia-compliant loan product rollouts.
- **Architecture Lens Check:** Sharia-Board approval workflow documented within the [[architecture-decision-records]].
- **Sample Outcome:** "Design: Profit-distribution calculation encapsulated; [[api-design]] schema includes mandatory Sharia-compliance flag."
- **Common Pitfall:** Applying standard interest-based loan models to Islamic products, violating compliance.

## Bulletproofing
- **Governance Policy:** Enforce [CBUAE Rulebook](governance/policy/regulations.yaml#CBUAE), [PDPL](governance/policy/regulations.yaml#PDPL), and [PCI-DSS](governance/policy/regulations.yaml#PCI-DSS) where applicable.

## Anti-patterns
- **Neglecting to map retry logic and timeout scenarios on external steps**
  - **Consequence:** Cascading timeouts and thread pool exhaustion when an upstream dependency experiences latency.
  - **Correct Approach:** Model circuit breakers, retry counts, fallback APIs, and timeout limits on all external network call arrows.
- **Overloading a single diagram with detailed branch logic and loops**
  - **Consequence:** Visual clutter that makes the sequence flow illegible to business stakeholders and developers.
  - **Correct Approach:** Keep diagrams focused on primary architectural pathways and split complex scenarios into separate documents.
- **Assuming instantaneous message delivery across distributed systems**
  - **Consequence:** Design gaps that lead to inconsistencies, out-of-order execution, or message drops.
  - **Correct Approach:** Model asynchronous queues, ACK/NACK behaviors, and out-of-order handling explicitly.
