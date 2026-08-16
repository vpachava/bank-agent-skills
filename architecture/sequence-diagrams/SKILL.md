---
name: sequence-diagrams
owner: Solution Architecture
version: 0.1.0
last-reviewed: 2026-08-08
description: "Use when you need to show how a banking flow behaves end-to-end — produces sequence diagrams (via /archify) covering happy path + exception/escalation/retake paths, with regulated gates and legacy-core seams marked."
required-inputs:
  - The flow(s) to model (the journey or operation)
  - Actors & systems involved (incl. legacy core, channels, partners)
  - The regulated gates in the flow (KYC, risk, AML, issuance)
  - Known exception / fallback / escalation paths
expected-deliverables:
  - Sequence diagram(s) for the flow(s) — happy path
  - Exception-path sequence fragments (escalate, retake, timeout, abort)
  - Bank-convention markers: regulated gates, provenance points, legacy-core seams
---

# /sequence-diagrams

## When to apply
Use whenever a flow's behavior has to be made precise — the LLD detail step, a design review where "and then what happens if X fails" is the question, a compliance walkthrough. Rendering delegates to `/archify`. Pairs with `/c4-model` (the static structure) — sequence is the dynamic complement.

## Inputs
- **The flow(s)** — the journey or operation (onboarding happy path, payment, account opening, KYC verification, etc.).
- **Actors & systems** — incl. the legacy core modules, channels, the UAE identity fabric (UAE Pass/EFR/UAEKYC), payment rails, partners.
- **Regulated gates** — the deterministic KYC/risk/AML/issuance steps that must sit on the flow (from `/hld-generator` or the compliance work).
- **Known exception / fallback / escalation paths** — the retake, escalate-to-human, timeout, abandon-resume stories.

## Process
1. **Name the flow and its entry & exit points.** Start state, end state, who initiates. A sequence diagram for a flow you can't state the endpoints of is unfocused.

2. **Fix the actors (left-to-right) by zone, not by alphabet.** Group the participating systems by zone — customer channel / AI tier / deterministic backbone / legacy core / external (UAE identity, rails). Lifelines in a zone grid make the cross-zone crossings — the interesting bits — jump out.

3. **Draw the happy path first, simply.** Just the calls that make the flow succeed. Keep messages concise (verb + object); detail goes into the next step, not the happy path's prose.

4. **Layer regulated gates onto the happy path.** Mark the deterministic KYC verdict, risk/AML screening, issuance ceremony as gate blocks. This is where the flow's *control* lives, and a sequence without the gates is the dynamic equivalent of a context diagram with 40 boxes.
   > Banking convention: gate blocks marked; a provenance point noted where a value becomes "authoritative" (e.g., post-IDV EID).

5. **Draw the exception paths as separate fragments.** Each exception — provider-SDK retake (AI never re-OCRs), Tier-3 escalate-to-human, timeout/abort, abandon-resume, duplicate-idempotency-rejection — is its own fragment or its own diagram. Don't try to cram all of the exception surface into the happy path with `alt` boxes that nobody will trace.
   > In a bank, the exception paths are the *most likely* paths; the happy path is the rarest one in the wild.

6. **Capture retry, idempotency, and reconcile strokes.** Where a flow retries (with an idempotency key), where it reconciles (a camt-style statement vs ledger), where it escalates — these are the strokes that make a sequence reviewable by Compliance.

7. **Delegate rendering to `/archify`.** Hand it the structured sequence input (plain-language or pasted Mermaid sequenceDiagram); it returns polished explorable diagrams (light/dark, PNG/JPEG/SVG/WebM). This skill owns the *content* — actors-by-zone, gates, fragments — not the rendering.

8. **Annotate provenance and audit points.** Where a value becomes authoritative, where an audit log is written, where a dual-signature ceremony happens — mark them. These are the points Compliance and the `/threat-model` review zero in on.

## Bulletproofing against Rationalization
- **Happy-path-only sequences** — the rarest path alone; the exception / escalation / retake / reconcile stories are where the design earns its keep and where Compliance reads.
- **No regulated gates on the flow** — a sequence that glides through KYC/risk/AML/issuance as ordinary calls misrepresents who controls the journey; mark the gates.
- **Actors not grouped by zone** — alphabetical lifelines hide the cross-zone crossings (the design center); zone-grouping surfaces them at a glance.
- **Idempotency & reconciliation invisible** — retry without an idempotency key, payment without reconcile — these are the defects Compliance finds in review; show the strokes.
- **Crammed exception alt-boxes** — every exception folded into one diagram via `alt`/`loop` makes it untraceable; split into fragments.
- **AI-as-decider on regulated steps** — sequences that show an AI bot making the KYC/AML/issuance verdict instead of a deterministic BPM actor have broken the compliance boundary; the AI orchestrates, BPM decides.
- **Rendering over content** — the elegant sequence diagram that misrepresents an exception path is worse than a rough honest one; own the content, delegate the rendering.

## Bulletproofing against Rationalization
To prevent Sequence Diagrams from being happy-path fantasies, you MUST:

1. **Mandatory Failure Path Inclusion:** Every single synchronous integration call (API, Database, Event Publish) MUST explicitly model its Timeout/Failure/Fallback response route.
2. **Mandatory Gateway Validation:** Sequence flows MUST explicitly document Auth/Token validation paths at the boundary. "Magic auth" is forbidden.
3. **Idempotency Tracing:** State-mutating steps (e.g. POST, PUT, transactions) MUST document the idempotency key flow visually.
4. **Real-world Latency Notation:** You MUST NOT model multi-region or cross-zone data interactions as instantaneous; boundary jumps must be acknowledged.

**Violating these rules invalidates the Sequence Diagram.**

## Outputs
- **Sequence diagram(s)** — happy path, rendered by `/archify`.
- **Exception-path fragments** — escalate / retake / timeout / abort / resume.
- **Bank-convention markers** — regulated gates, provenance/authoritative-value points, audit-write points, legacy-core seams.

## Related skills
- [/archify](../../../../) — rendering engine for the diagrams.
- [c4-model](../c4-model/SKILL.md) — the static complement to these dynamic views.
- [deployment-diagrams](../deployment-diagrams/SKILL.md) — the topology view this pairs with.
- [lld-generator](../lld-generator/SKILL.md) — the doc these sequences embed in.
- [threat-model](../../security/threat-model/SKILL.md) — reads these sequences to find the threat surface at each crossing.
- [event-driven](../../integration/event-driven/SKILL.md) — where async events replace/extend the sync sequence.
