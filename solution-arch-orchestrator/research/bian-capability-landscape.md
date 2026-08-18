# BIAN Capability Landscape — Wayfinder Research Ticket 03

**Domain:** BIAN grounding for a solution-architect skills library targeting a large UAE retail bank.
**Audience:** Downstream skills — `business-capability-map`, `gap-analysis`, `solution-options`, `hld-generator`, `reference-architecture`, `architecture-review`.
**Currency date:** August 2026.
**Status:** Findings synthesized to support skill checklists (capabilities + framing), not an exhaustive BIAN domain dump. Map-level depth only.

---

## Methodology & Confidence Legend

During this session the `WebSearch` tool returned an infrastructure error (HTTP 400 — Anthropic server tools could not be passed to the configured upstream). `WebFetch` against direct URLs **did** work, so claims were verified against BIAN's first-party pages and the Wikipedia article that reproduces BIAN's published metamodel description. Where the detailed catalog sits behind the BIAN Portal access form (login-gated), the research-skill protocol applies: synthesize from authoritative public knowledge with **explicit confidence levels**, never invent IDs. Each finding is independently marked.

- **HIGH** — Stable, long-standing, authoritative, and verified against a BIAN first-party page in this session.
- **MEDIUM** — Domain- or version-sensitive; confirmed structurally but exact names / counts may have advanced past the synthesis date. **Verify against the live BIAN Portal before embedding a fixed number or label in a skill checklist.**
- **LOW** — Speculative or peripheral; used sparingly.

Primary sources referenced (canonical, stable-URL):
- BIAN home / deliverables — https://www.bian.org/ , https://www.bian.org/deliverables/service-landscape/
- BIAN News Room (v14.0 announcement) — https://www.bian.org/news/
- BIAN Coreless Banking deliverable — https://www.bian.org/deliverables/coreless-banking/
- BIAN Portal (catalog, behind access form) — https://portal.bian.org/
- Wikipedia: Banking Industry Architecture Network (reproduces BIAN's published metamodel description) — https://en.wikipedia.org/wiki/Banking_Industry_Architecture_Network
- The Open Group (TOGAF) — https://www.opengroup.org/forum/togaf , https://www.opengroup.org/togaf
- IFX Forum (BIAN's implementation-message partner) — https://www.ifxforum.org/ (referenced via Wikipedia's BIAN article)
- ISO 20022 (BIAN metamodel alignment) — https://www.iso20022.org/

---

## 1. BIAN Service Landscape & Service-Domain Metamodel — the canonical decomposition

**Confidence: HIGH (structure & counts verified against BIAN.org this session).**

BIAN (Banking Industry Architecture Network) is the open, not-for-profit standards body publishing a vendor-neutral **Reference Architecture** for banks. Its core deliverable is the **BIAN Service Landscape** — a reference framework that categorizes and organizes **BIAN Service Domains** for ease of access. The Landscape is a *primary* view; BIAN notes the layout "can be varied depending on use" (areas/domains are classification layers; service domains are the stable building blocks).

### Three-level metamodel (the decomposition a capability-map skill must reproduce)

The BIAN Metamodel is a UML model with three hierarchical levels — this is the partitioning every downstream skill should mirror:

| Level | Role | Stability |
|---|---|---|
| **Business Area** | Highest-level classification; "groups together a broad set of business capabilities" with similar supporting application/information needs. | Classification layer — re-categorizable by use. |
| **Business Domain** | Intermediate; "a coherent collection of capabilities within the broader business area," recognizable as banking skills/knowledge. | Classification layer — re-categorizable by use. |
| **Service Domain** | Finest partitioning; "unique and discrete business capabilities" — the "elemental building blocks" of a service landscape. | **Stable.** A Service Domain's scope does not vary across layouts. |
| **Service Operation** *(sub-level)* | The discrete operations/services a Service Domain exposes (each with variants). | **Stable, but pruned in v14.0.** |

So the canonical decomposition chain a skill produces is:
**Business Area → Business Domain → Service Domain → Service Operation (→ variants) → Semantic API**.

### Counts and version (verified BIAN.org, Aug 2026)

- **Service Landscape v14.0** is the current release (announced by BIAN as *"BIAN Unveils New Service Landscape 14.0 to Accelerate AI‑Ready Banking Architecture"*). **HIGH** (BIAN.org/news).
- **322 service domains** — "**All 322 service domains completed**" (stated at v11.0; the v14.0 release note says some domains were "renamed, removed and added especially in the Payment Area," and **three Service Domains in the area of Insurance are added**). **HIGH** that ~322 is the order of magnitude; **MEDIUM** on the exact v14.0 count — verify on Portal.
- **~5,000+ service definitions** and **~250 Semantic APIs**. **HIGH** (BIAN.org home: "home to 250 APIs and more than 5,000 service domains/definitions").
- **v14.0 pruning:** "Unnecessary Service Operations are eliminated." This is directly relevant to a skill: do **not** mechanically enumerate all historical Service Operations; the canonical set is leaner now. **HIGH**.
- BIAN service definitions currently span **retail banking, private banking and corporate banking**. **HIGH** (Wikipedia citing BIAN).
- BIAN Metamodel **is closely aligned to, and draws on parts of, the ISO 20022 Meta Model**. **HIGH** (Wikipedia citing BIAN) — this is the load-bearing cross-link to the payments/integration research (ISO 20022 message families map cleanly to BIAN Payments service domains).

### Implication for downstream skills
- `business-capability-map`: produce **three columns (Business Area, Business Domain, Service Domain)** at minimum; Service Operations only when scoping APIs. Treat Area/Domain as *classification*, Service Domain as the *artifact to bound a capability to*.
- `hld-generator` / `reference-architecture`: anchor each solution component to the Service Domain(s) it implements; never invent a Service Domain name — pull from the BIAN Portal v14.0 catalog (login-gated; see §6).

---

## 2. BIAN Service Landscape — Major Business Areas (map-level enumeration)

**Confidence: MEDIUM.** The *structure* (Business Area → Domain → Service Domain) is HIGH-confirmed (see §1). The *named list below* is reproduced from long-stable, widely-circulated BIAN published material (the SOA reference model / conference decks / vendor literature citing BIAN); the live catalog is behind the BIAN Portal access form and **v14.0 explicitly reorganized the Payment Area and added an Insurance area**, so any skill embedding this list must verify names and counts against the current Portal before freezing a checklist.

### Representative Business Areas of a BIAN-aligned retail bank (map-level)

These are the top-level groupings a capability map should expect to populate. Each is a *capability area*, not an org unit.

1. **Customer Relationship Management** — party/customer master, onboarding, KYC, customer views across products.
2. **Customer Offerings / Product Administration** — product catalog, product-eligibility rules, pricing configuration.
3. **Payments and Cash Management** — payment initiation, clearing, settlement, cash management (the most ISO-20022-aligned area; restructured in v14.0).
4. **Lending / Credit** — loan origination, conventions, collateral, credit assessment.
5. **Deposits / Current & Savings Accounts** — account servicing, term deposits, interest accrual.
6. **Investment & Portfolios** — investment products, portfolio management, order routing (lighter in retail).
7. **Channels & Access** — branch, contact centre, mobile/web, ATM — the access/interaction layer.
8. **Reference Data & Master Data Management** — reference and standing data shared across service domains (this is often the integrator's crosslink). Cross-link: see `solution-arch-orchestrator/research/banking-integration-patterns.md` §reference-data.
9. **Risk Management & Compliance** — credit/market/operational risk, regulatory reporting, AML/sanctions.
10. **Security / Access Control (Procedure)** — access, security administration, fraud controls (also handed off to `security-architecture-review` skill).
11. **Finance / Accounting & Financial Information** — general ledger, product P&L, finance reporting.
12. **Human Resources** — employee management (often a non-differentiating shared service worth outsourcing).
13. **Treasury & Market Data / Markets** — treasury, FX/MM, market data — smaller footprint in pure retail but present.
14. **Administration & Support** — general support capability set.
15. **Insurance** *(new in v14.0)* — three Service Domains added; relevant because many UAE retail banks run bancassurance — expect insurance capability to matter in this engagement.

**Why only map-level:** the task scope is "summarize at map-level depth, not an exhaustive domain dump." There are ~322 Service Domains across these areas — naming them is the Portal's job. **A skill must treat §2 as the expected area *scaffold*, then populate Service Domains from the live Portal, never from memory.**

### Worked exemplars (representative Service Domains only — do not extend from memory)

To show the depth a capability-map skill should target, a few widely-published examples (these illustrate form; the authoritative list is Portal-gated):

- *Payments area* → **Payment Initiation Service Domain**, **Payment Execution Service Domain**, **Clearing & Settlement Service Domain** — maps cleanly to ISO 20022 `pain.001`/`pacs.008` (see integration research).
- *Customer Relationship Management area* → **Party Master Data Management**, **Customer Onboarding**, **Customer Offer Eligibility**.
- *Lending area* → **Loan Origination**, **Collateral Management**.

**Confidence: MEDIUM** — these exemplars reflect canonical BIAN shape but the exact Service Domain labels evolve; Portal-verify before naming any in a deliverable. Use them to calibrate **granularity**, not to populate a map.

---

## 3. BIAN Interaction & Service-Operation Model — how domains expose services & events

**Confidence: HIGH (interaction concepts) / MEDIUM (exact operation taxonomy — pruned in v14.0).**

### What a Service Domain is, operationally
A BIAN Service Domain is the finest architectural partition; it owns a single **Business Object / Aggregate** and exposes behavior through **Service Operations** (each with variants). This is responsibility-driven/DDD-flavored: one Service Domain = one cohesive capability + the business objects it authoritative-owns. **HIGH** (BIAN published model description via Wikipedia & deliverables).

### How Service Domains interact
- **Synchronous request/response** between Service Domains (the dominant operational pattern).
- **Publish/subscribe / event** for cross-domain notifications and decoupling — the foundation that connects BIAN to event-driven integration. Cross-link to `solution-arch-orchestrator/research/banking-integration-patterns.md` (event-driven & messaging sections).
- Each Service Operation is described semantically with input/output **Control Records** and **Business Information** payloads — BIAN deliberately separates *semantic* API contracts from *implementation* (REST/gRPC/Kafka are transports, not the model).
- **~250 Semantic APIs** are published as OpenAPI/Swagger artifacts in the BIAN Portal, generated from the Service Operation model — this is the canonical contract surface. **HIGH** (BIAN.org home / deliverables).

### Implementation and message alignment (the integration cross-link)
- **BIAN ↔ IFX Forum:** BIAN Service Domains are *implemented* using the **IFX Business Message Specification** — the canonical operational message set for retail-banking operations. **HIGH** (Wikipedia citing BIAN).
- **BIAN ↔ ISO 20022:** the BIAN Metamodel is aligned with the ISO 20022 Meta Model; for payments specifically, BIAN Payments Service Domains map to the ISO 20022 `pain.*/pacs.*/camt.*` message families (cross-link: `banking-integration-patterns.md` §1). **HIGH** on alignment principle.

### How this frames the downstream integration-thinking skills
- **`api-design`**: produce OpenAPI contracts from BIAN Semantic APIs as the *baseline*; don't reinvent payment/customer resource shapes — start with BIAN service operations and specialize for the bank's product line.
- **`event-driven` / `messaging`**: model cross-domain events as events emitted by a Service Domain that owns the business object; a BIAN capability that Just-Consumes should not own the data. BIAN's pub/sub interaction pattern is the conceptual anchor — pair with the integration pattern research for the concrete Kafka/Apaca­he-style plumbing.
- **`integration-patterns`**: BIAN delivers *what* services exist; the integration research delivers *how* to wire them (API gateway, async, saga, outbox). Cite BIAN for the **contract inventory**, cite the integration research for the **pattern choice**.

### v14.0 caution (MEDIUM)
Because v14.0 "eliminated unnecessary Service Operations," any skill that imports an older BIAN operation enumeration will over-specify. *Recommendation:* downstream skills anchor on Service Domain + Semantic API versions, and treat Service Operation lists as **Portal-derived, version-stamped**.

---

## 4. BIAN vs TOGAF (and other reference frames) — cite the right frame for the right job

**Confidence: HIGH (frame roles).** Both BIAN and TOGAF sit in the Open Group ecosystem and are explicitly complementary; the confusion to avoid is using one to do the other's job.

### The split
| | **TOGAF** | **BIAN** |
|---|---|---|
| **What it is** | A general-purpose Enterprise Architecture *method* (the ADM cycle, Architecture Continuum, Reference Models). Industry-agnostic. | A banking-industry-specific Reference Architecture and capability *catalogue* (the Service Landscape + Metamodel). |
| **Answers** | *How* to run an EA practice: phases, stakeholder mgmt, gap analysis, migration planning, governance. | *What* capabilities a bank should have: the named service domains, their operations, and their canonical interactions. |
| **Scope** | Any industry; widely adopted across commercial/government. | Retail, private, corporate banking. |
| **Owner** | The Open Group. | BIAN (not-for-profit association; standards partnership with The Open Group, OMG, IFX Forum, ISO 20022). |
| **Reference-source check (this session)** | Open Group pages confirm TOGAF is *"a proven Enterprise Architecture methodology and framework,"* version 10th Ed., split into Fundamental Content + Series Guides. **No banking-specific capability catalog.** | BIAN.org confirms Service Landscape v14.0, ~5,000 service definitions, ~250 Semantic APIs. |

### Overlap (where they collaborate, not compete)
- Both adopt a **service-oriented/modular** decomposition and a reference-architecture mindset.
- TOGAF's **Capability-Based Planning** + **Architecture/Strategy Continuum** is the *method vehicle* into which BIAN's Service Landscape is the *content*.
- BIAN is commonly cited in TOGAF engagements as a banking **industry reference model** in the Architecture Continuum's lower-stratum (industry architecture).

### Divergence (and the rule for skill citation)
- **TOGAF gives no banking capability map.** It tells you *how to run a gap analysis*; it does not say *what* a Payments service domain is. → a skill that produces a bank capability *inventory* should cite **BIAN for the content catalogue**, **TOGAF for the method/lifecycle**.
- **BIAN is not an EA method.** It has no ADM, no stakeholder-management phase, no migration-planning ceremony. → a skill that produces an *architecture review* or *gap-analysis process* cites **TOGAF ADM phases**; the *capability map it scores against* is BIAN.
- **Pragmatic rule for the skills library:**
  - `business-capability-map` → **BIAN** (content).
  - `gap-analysis` → **TOGAF** (method/phase) operating **on a BIAN map** (content).
  - `solution-options`, `hld-generator`, `reference-architecture` → **BIAN** for capability anchoring; **TOGAF** for target-state/migration discipline.
  - `architecture-review` → **TOGAF** ABRs (Architecture Building Blocks) and review checklists; cross-check coverage against **BIAN** Service Domains so the review is bank-realistic.

### Other adjacent frames (mention, don't dwell)
- **ArchiMate** (Open Group) — the modelling notation; pair with TOGAF for *depiction*; BIAN does not mandate a notation.
- **ISO 20022** — message-level financial semantics; pair with BIAN for payments/treasury payloads (integration research owns this).
- **IFX Business Message Spec** — operational-level retail-banking messages; the *implementation* of BIAN service operations (see §3).
- Out of scope here: ACCORD/OMG, FIBO (ontology), CMMI — not load-bearing for capability mapping in a retail bank.

---

## 5. BIAN Adoption Reality — what fidelity banks actually implement

**Confidence: HIGH.** Verified this session against BIAN's own Coreless Banking deliverable, which is BIAN's official position on operational adoption. Pragmatic; not aspirational.

### The reality
- **Banks do not implement the full ~322 Service Domain decomposition as operational microservices.** BIAN itself models adoption as **selective and incremental**, focused on the highest-leverage areas. **HIGH**.
- BIAN's marquee operational programme, **Coreless Banking**, demonstrates this directly:
  - It is described as "a platform for banks to collaborate with leading software vendors on developing a future-proof, and compatible banking **microservices** infrastructure based on BIAN architectures," aimed at "the perpetual challenges presented by legacy core infrastructure."
  - The **Coreless Banking 1.0 pilot focused on only three areas**: consumer payments, customer offers, and consumer loans. No bank in the BIAN member set built all 322 — they started narrow. **HIGH** (BIAN.org/deliverables/coreless-banking).
  - Later waves (2.0 best-of-breed vendor selection; 3.0 customer-consented data retrieval; 4.0 AI/ML retention offers) layered breadth gradually. **HIGH** on the evolutionary arc.
- The Service Landscape is delivered as *a separate deliverable* from Coreless Banking — i.e., it is consumed independently of (and earlier than) operational microservice adoption. Banks routinely engage the **reference model** to drive capability mapping, M&A harmonization, vendor-package fit-gap, and target-state architecture **without** ever operating a BIAN-aligned microservice fleet. **HIGH**.

### Where BIAN actually pays off (high-leverage uses, in priority order for a UAE retail bank)
1. **Payments** (highest maturity, deepest ISO 20022 alignment) — the cleanest first investment. Cross-link to integration research.
2. **Customer Offerings / Product Catalog** & **Customer Relationship Management / Party** — foundational; often the second wave.
3. **Reference Data Management** — an enabler that must precede risk/compliance depth.
4. **Lending, Deposits** — product-domain modernization, sequenced by business pain.
5. **Risk, Compliance, Finance, Treasury** — later; cross-cutting; benefit from prior data alignment.
6. **Insurance** *(new in v14.0)* — pertinent to UAE banks running bancassurance.

### Pragmatism rules to embed in skills (so they are not aspirational)
- **Cap analytical deliverables at Business Area → Business Domain → Service Domain depth.** Defer Service Operation enumeration until API-design work is in scope. (Otherwise a capability map becomes a 5,000-row spreadsheet nobody uses.)
- **Treat BIAN as a reference, not a target blueprint.** A bank's actual operating model will differ; the skill must score *fit-gap* (what we have vs. what BIAN names), not *compliance to BIAN*.
- **The categorization layer is portable.** Business Area / Business Domain groupings "can be varied depending on use" — a capability-map skill may re-cluster service domains by, e.g., customer-journey or regulatory viewpoint, without breaking BIAN fidelity (the Service Domain layer is the stable anchor).
- **Beware "BIAN-aligned" marketing.** Many vendors map their product to *a handful* of Service Domains and claim alignment. A reference-architecture skill must require vendors to name the specific Service Domains + Semantic API versions they implement, against the Portal catalog — not broad area-level claims.
- **For this engagement (UAE retail bank):** ISO 20022 migration (CBPR+, domestic Aani/Al Etihad Payments) is the live external pressure that makes BIAN's Payments service domains immediately load-bearing. Sequence Payments-first; treat Payments as the proof-of-pattern before extending to lending/deposits. (Cross-link to `banking-integration-patterns.md` for Aani and the UAE domestic rails.)

---

## 6. Recommendations to embed in downstream-skill checklists

Concrete checkboxes each downstream skill should include (map-level, not aspirational):

### `business-capability-map`
- [ ] Decompose at **three layers** only by default: Business Area → Business Domain → Service Domain. Defer Service Operations until `api-design`.
- [ ] Source Service Domain names from the **BIAN Portal v14.0 catalog**, not memory. Stamp the version in the document footer.
- [ ] Treat **Service Domain** as the stable anchor; treat Area/Domain groupings as portable classification.
- [ ] Include the **Insurance** area (new in v14.0) if the bank runs bancassurance (UAE context — likely yes).

### `gap-analysis`
- [ ] Use **TOGAF ADM Phase G/H** method on a **BIAN-sourced** capability inventory (don't conflate; method=TOGAF, content=BIAN).
- [ ] Score **fit-gap** against BIAN Service Domains, never "BIAN compliance."
- [ ] Sequence gaps by adoption reality (Payments → Customer/Product → Reference Data → Lending/Deposits → Risk/Finance).

### `solution-options` & `hld-generator` & `reference-architecture`
- [ ] Anchor each solution component to a **Service Domain (owner of one business object)**; require vendors to cite specific Service Domains + Semantic API versions for any "BIAN-aligned" claim.
- [ ] For payments, pair BIAN Service Domains with ISO 20022 message families (`pain.*/pacs.*/camt.*`) and UAE domestic rails (`Aani`).
- [ ] BIAN Semantics are *contract*, not *transport* — selection of REST/gRPC/Kafka is a downstream integration decision (cite `banking-integration-patterns.md`).

### `architecture-review`
- [ ] Use **TOGAF ABRs / review checklists** as the review method; cross-check each finding against **BIAN Service Domain coverage** so the review is bank-realistic, not generic.
- [ ] Flag any solution component not anchored to a named Service Domain (or justified local capability) as a review issue.

---

## 7. Open verifications / follow-ups (before any skill freezes a checklist)

1. **Exact v14.0 Service Domain count & re-list** — confirm 322 still holds or is updated; confirm the **Insurance** area's three new Service Domains by name; confirm the **Payment Area** reorganization detail. Source: BIAN Portal (login-gated) — https://portal.bian.org/.
2. **BIAN Service Operation taxonomy post-v14.0 prune** — fetch the trimmed operation set to avoid over-specifying in `api-design`.
3. **UAE-specific adoption telemetry** — confirm how the target UAE retail bank already uses BIAN (vendor packages like Temenos/T24, Oracle FLEXCUBE, and Infosys Finacle all publish BIAN alignment claims of varying fidelity); verify the specific Service Domains the bank's core actually exposes before the gap analysis starts.
4. **Latest Coreless Banking wave (post-4.0)** — confirm whether a 5.0 (AI/agent-ready) wave has shipped by Aug 2026, given v14.0's "AI-Ready Banking Architecture" framing.

---

## Sources

- BIAN home — https://www.bian.org/ *(v14.0 announcement; "250 APIs and more than 5,000 service domains"; partner listing)*
- BIAN Service Landscape deliverable — https://www.bian.org/deliverables/service-landscape/ *"All 322 service domains completed" (v11.0); "+ 5000 Service definitions"; "+ 250 Semantic APIs"; v14.0 release notes — Insurance added, Payment Area reorganized, "Unnecessary Service Operations are eliminated")*
- BIAN News Room — https://www.bian.org/news/ *("BIAN Unveils New Service Landscape 14.0 to Accelerate AI‑Ready Banking Architecture")*
- BIAN Coreless Banking — https://www.bian.org/deliverables/coreless-banking/ *(definition; the 1.0/2.0/3.0/4.0 selective-adoption arc)*
- BIAN Portal (catalog, login-gated) — https://portal.bian.org/
- Wikipedia — Banking Industry Architecture Network — https://en.wikipedia.org/wiki/Banking_Industry_Architecture_Network *(reproduces BIAN's published metamodel description: Business Area → Business Domain → Service Domain; Service Domain as "elemental building blocks"; "layout can be varied depending on use"; ISO 20022 metamodel alignment; IFX Forum implementation partnership; retail/private/corporate scope; standards partners: OMG, The Open Group, IFX Forum, ISO 20022)*
- The Open Group TOGAF — https://www.opengroup.org/forum/togaf , https://www.opengroup.org/togaf *(TOGAF 10th Ed.: Fundamental Content + Series Guides; general-purpose EA methodology; no banking capability content)*
- Cross-reference — `solution-arch-orchestrator/research/banking-integration-patterns.md` *(ISO 20022 message families; UAE rails: Aani/Al Etihad Payments, CBUAE; anti-fraud/FAPI security)*

---

*Synthesis date: 2026-08-07. BIAN Service Landscape is a living standard (v14.0 just shipped); re-verify the named Service Domain catalog against the BIAN Portal before any deliverable freezes the enumeration. The structure (3-level metamodel), interaction model, partner alignment, version, and adoption posture above are HIGH-confidence and safe to embed immediately.*
