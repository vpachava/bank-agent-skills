# UAE Compliance Posture — Wayfinder Research Ticket 02

**Domain:** UAE/CBUAE regulatory, compliance & data-residency posture for a large retail bank.
**Audience:** Downstream skills — `compliance`, `security-architecture-review`, `zero-trust`, `iam-review`, `landing-zone-review`, `production-readiness`, `operational-readiness`.
**Currency date:** August 2026.
**Status:** Findings synthesized to support skill checklists (obligations + pitfalls), not a legal memo. Scope restricted to what a solution architect embeds in skill checklists.

---

## Methodology & Confidence Legend

`WebSearch` returned infrastructure errors this session, so verification proceeded via `WebFetch` against direct authoritative URLs (DLA Piper's global privacy guide, regulator/agency pages). Where a fetch failed (403/404/empty) the source was not used; where currency is in doubt, confidence is marked down and the skill builder is directed to verify against the current primary publication. No specifics (law numbers, dates, article text) are fabricated — if a value is not pinned to a fetched source, it carries an explicit "verify before embedding" flag.

- **HIGH** — Verified against the authoritative primary source in this session; stable, long-standing.
- **MEDIUM** — Verified structurally but date-/regime-sensitive; plausibly advanced since the source's last update. **Verify before embedding** in a skill checklist.
- **LOW** — Speculative or peripheral; used sparingly.

Primary sources referenced (canonical, stable-URL):
- DLA Piper — Data Protection Laws of the World: UAE (federal) — https://www.dlapiperdataprotection.com/index.html?t=law&c=AE
- DLA Piper — UAE – Dubai (DIFC) sub-page — https://www.dlapiperdataprotection.com/countries/uae-dubai-difc/law.html
- DLA Piper — UAE – ADGM sub-page — https://www.dlapiperdataprotection.com/countries/uae-abu-dhabi-global-market-free-zone/law.html
- Central Bank of the UAE (CBUAE) — https://www.centralbank.ae/
- DIFC — https://www.difc.ae/  | DIFC Commissioner of Data Protection — https://www.dpcomms.difc.ae/
- ADGM — https://www.adgm.com/  | ADGM Commissioner of Data Protection — https://www.adgm.com/regulation/data-protection/
- Dubai Electronic Security Center (DESC) — https://www.desc.gov.ae/
- UAE Pass — https://www.uaepass.ae/  | UAE Government portal — https://u.ae/
- TDRA (Telecommunications and Digital Government Regulatory Authority) — https://www.tdra.gov.ae/

---

## 0. Federal UAE Personal Data Protection Law (PDPL) — the federal baseline

**Confidence: HIGH (law text & dates verified via DLA Piper this session) / MEDIUM (regulator-establishment & Executive-Regulation status — check currency).**

The federal data-protection baseline is **Federal Decree-Law No. 45 of 2021 on the Protection of Personal Data** (issued 26 September 2021). Key architecture-relevant facts:

- **Regulator — the UAE "Data Office":** DLA Piper's snapshot (last modified 27 January 2025) states the Data Office administering the PDPL **had not yet been established** as of that update. By Aug 2026 its status may have advanced — treat the "Data Office established, Executive Regulations issued, adequacy decisions published" trio as **MEDIUM, verify** before embedding a regulator name or registration obligation. (DLA Piper, https://www.dlapiperdataprotection.com/index.html?t=law&c=AE.)
- **Territorial scope** is broad: applies to (a) processing of personal data of people residing in/with a business in the UAE, (b) every Controller/Processor inside the UAE regardless of data-subject location, and (c) Controllers/Processors **outside the UAE** processing data of individuals inside the UAE. This is the hook that makes a foreign cloud/data-processor fall under UAE law for a UAE retail bank. (HIGH, DLA Piper.)
- **Legal bases (Art. 4):** consent is the default; defined exceptions exist (contracts, public interest, etc.). Sensitive Personal Data (racial/ethnic origin, political/philosophical opinions, religious beliefs, criminal records, **biometrics**, health) gets stricter treatment. DPIAs required for high-risk/new-tech processing or large sensitive-data processing (Art. 21). DPO required for high-risk processing, systematic sensitive-data assessment, or large volumes of sensitive data. (HIGH, DLA Piper.)
- **Data-subject rights** (Arts. 13–18): access, portability, correction/erasure ("right to be forgotten"), restriction, objection to automated decision-making/profiling; one-month response (extendable by two). (HIGH, DLA Piper.)
- **Cross-border transfer (the architectural lever):** the PDPL **restricts international transfers** of personal data outside the UAE; the Data Office is expected to approve "adequate" territories (EU-style adequacy). Until then, rely on the other exceptions the Data Office will enumerate. **No operational adequacy list as of DLA Piper's Jan-2025 snapshot — verify currency.** (MEDIUM, DLA Piper.) This is the load-bearing cross-border constraint for any cloud landing zone.
- **Breach notification (Art. 9):** Controllers must report breaches "immediately upon becoming aware" to the Data Office; specific procedures left to the (pending) Executive Regulations. (HIGH on obligation; MEDIUM on mechanics.)
- **Penalties:** No specific penalties in the PDPL itself; the Cabinet is to issue a decision based on Data Office proposals. **However**, the **Cyber Crime Law — Federal Decree-Law No. 34 of 2021 on Combatting Rumors and Cybercrimes, Art. 13** likely applies: unauthorized collection/keeping/processing of personal data of nationals/residents carries detention and/or AED 50,000–500,000. (HIGH, DLA Piper.)

**Adjacent federal laws a compliance skill should name (HIGH, DLA Piper):**
- **Central Bank Law — Federal Law No. 14 of 2018, Art. 120:** all customer data and information must be treated as confidential. (The CBUAE confidentiality hook.)
- **Cyber Crime Law — Federal Decree-Law No. 34 of 2021** (above) — wider cybercrime penalties (AED 150,000–5,000,000 across Arts. 2,3,4,6,7,8,45).
- **Telecommunications Law — Federal Law by Decree No. 3 of 2003 (as amended)** via TDRA; TDRA Consumer Protection Regulations v2.0 Art. 24.9 imposes telecom data-confidentiality duties.
- **ICT in Health Fields Law — Federal Law No. 2 of 2019, Art. 13:** health information "may not be stored, processed, generated or transferred outside the UAE" unless permitted by the Emirate's Health Authority + Federal Ministry of Health; Ministerial Decision No. 51 of 2021 frames the exceptions. (Relevant if the bank processes health-data via bancassurance/wealth — verify scope.)
- **Criminal Law — Federal Law 31 of 2021, Arts. 431/432** — privacy/secrecy offences.
- **Dubai Data Law — Dubai Law No. 26 of 2015** — open-data sharing in Dubai (Dubai-specific).
- **TMTM Law — Federal Decree Law No. 14 of 2023** — Trading by Modern Technological Means; consumer data-exchange & marketing-consent (Arts. 5, 6, 10(1)).

---

## 1. CBUAE sectoral data-residency & data-protection rules — for payment / card / stored-value data

**Confidence: HIGH (law/regulation numbers, dates, and article numbers verified via DLA Piper this session).**

This is the **already-verified** domain the task told me not to re-research — DLA Piper confirms the specifics directly:

- **Stored Value Facilities (SVF) Regulation (issued 30 September 2020), Art. 10:** customer data must be **stored and maintained in the UAE** (data residency); 5-year retention from creation. (HIGH, DLA Piper.)
- **Retail Payment Services and Card Schemes Regulation (issued 6 June 2021):** personal and payment data must be **stored and maintained within the UAE**; a secure backup at a **separate location** is required; 5-year retention; **Art. 18** requires Card Schemes to notify CBUAE of data breaches **within 72 hours**. (HIGH, DLA Piper.)
- **Consumer Protection Regulation (CBUAE Notice No. 444 of 2021) + Consumer Protection Standards (CBUAE Notice No. 1158 of 2021):** Licensed Financial Institutions must (a) collect minimal Consumer Data, (b) maintain a Data Management Control Framework, (c) ensure secure digital transaction processing, (d) designate a **senior manager responsible for data protection**, (e) obtain express consent before use/shared use, (f) retain data securely for minimum 5 years, (g) **notify CBUAE of material data breaches**. (HIGH, DLA Piper.)
- **Central Bank Law — Federal Law No. 14 of 2018, Art. 120** — customer-data confidentiality (see §0).

**Architectural implication a `landing-zone-review` skill must embed (HIGH):** Payment/card/SVF personal data is subject to a hard onshore residency rule → the **primary** data store for these classes must live in an **in-country** UAE region (for hyperscalers, the UAE North / UAE Central regions); cross-zone replication/multiple AZs in-country is required for the "separate location" backup; outbound transfer to non-UAE regions needs either the PDPL adequacy/exemption route **or** pseudonymisation-to-the-point-of-de-identification. Card data under PCI DSS still must satisfy the residency overlay. This is the single most load-bearing constraint in the whole ticket for cloud landing-zone design.

---

## 2. DIFC data-protection regime — the Dubai financial-freezone overlay

**Confidence: HIGH (law number, year, regulator, article numbers, transfer mechanisms verified via DLA Piper's DIFC sub-page this session).**

The DIFC operates its **own** independent data-protection regime alongside the federal PDPL:

- **Governing law:** **DIFC Law No. 5 of 2020 on Data Protection Law (DPL)**, in effect July 2020. Companion **Data Protection Regulations (DPRs)** sit beside the DPL and were **updated in 2023 to include regulations on processing via AI systems** — i.e. DIFC is the first UAE regime to address AI-specific processing directly. (DLA Piper, https://www.dlapiperdataprotection.com/countries/uae-dubai-difc/law.html.)
- **Regulator:** the **DIFC Commissioner of Data Protection** (Level 14, The Gate, DIFC) — independent Commissioner with investigative powers, inspections, enforcement directions, fines, and now publishing infringement decisions. (HIGH, DLA Piper.)
- **GDPR modelling:** strong GDPR alignment — legal bases (**Art. 10 DPL** ≈ GDPR Art. 6); special-category data (**Art. 11** ≈ GDPR Art. 9, requires an additional legal basis); information provisions (Part 5 ≈ GDPR Arts. 13–14); data-subject rights including objection to direct marketing/profiling (≈ GDPR Art. 21); transfer mechanisms (BCRs, SCCs, codes of conduct Art. 48, certification Art. 50); DPO required for certain entities. (HIGH, DLA Piper.)
- **Scope:** applies within the DIFC freezone to **DIFC Bodies, Controllers and Processors** operating there. **Critically, onshore UAE is treated as a "Third Country"** for DIFC transfer purposes — i.e. a DIFC-entity → onshore-entity data flow is an **international transfer** requiring an Art. 26 or Art. 27 mechanism. This is the single biggest cross-zone architectural lever. (HIGH, DLA Piper.)
- **Registration (Art. 14(7) DPL):** Controllers/Processors must file a **Notification** with the Commissioner via the DIFC online portal — it lists purpose, data-subject classes, data classes, and **the jurisdictions to which data will be transferred, with adequacy indications**. The Notification appears on the **public register**. DPOs must complete an "Annual Assessment" in a prescribed form. (HIGH, DLA Piper.)
- **Cross-border (Art. 26 + Art. 27 DPL):**
  - **Art. 26** — transfer to "adequate" jurisdictions per the Commissioner's published list.
  - **Art. 27(2)** — appropriate safeguards when no adequacy: legally binding instruments, BCRs, **DIFC SCCs** (the DIFC SCCs are "a synthesised set of SCCs modelled on the EU Model Clauses and UK IDTA", **non-modular**, unlike the 2021 EU SCCs), approved codes of conduct (Art. 48) and certification mechanisms (Art. 50).
  - **Art. 27(3)** — derogations (explicit consent, contract necessity, public interest, legal claims, vital interests, public registers, regulatory/law-enforcement requests, **international financial-market standards, and AML/CTF obligations** — explicit financial-market carve-outs).
  - **Art. 27(4)** — *unique divergence*: a one-off, limited transfer on "compelling legitimate interests" (not overridden by data-subject rights) is permitted even without adequacy/safeguards/derogation, **provided** the Controller documents the assessment, uses suitable safeguards, and **informs both the Commissioner and the Data Subject** of the transfer. GDPR has no equivalent hybrid. (HIGH, DLA Piper.)
- **Breach notification (Art. 41 + Art. 42 DPL):** notify the Commissioner **"as soon as practicable in the circumstances"** — DLA Piper explicitly: **"unlike the GDPR there is no hard deadline."** Processors → Controllers "without undue delay." Document all breaches in writing. Data-subject notification (Art. 42) "as soon as practicable" where high risk. (HIGH, DLA Piper — important divergence from ADGM, which has the 72h rule.)
- **Penalties (Schedule 2):** administrative fines **USD 10,000–100,000** per contravention (~35 contraventions listed) plus a "general fine" that is "appropriate and proportionate". Compensation claims (material or non-material damage). Court recourse (Art. 63). Fines are materially lower than GDPR's %-of-turnover regime. (HIGH on mechanism; currency of Schedule 2 amounts: MEDIUM — verify current amounts on the Commissioner's fee schedule.) (DLA Piper.)

**Key DIFC divergences from GDPR (HIGH, DLA Piper):** (1) no hard breach-notification deadline; (2) Art. 27(4) hybrid transfer flexibility; (3) non-modular SCCs; (4) much lower fines (USD 100K cap vs GDPR up to 4% global turnover); (5) **DPO must reside in the UAE** unless employed within the international Group performing a similar function; (6) Art. 14(4) prescribes privacy-by-default specifics on online platforms (≥2 contact methods for rights requests, ≥1 free via website without account creation); (7) explicit financial-market carve-outs in transfer derogations.

---

## 3. ADGM data-protection regime — the Abu Dhabi financial-freezone overlay (GDPR-aligned with a 72-hour clock)

**Confidence: HIGH (regulation name/year, regulator, section numbers, breach deadline, transfer mechanisms verified via DLA Piper's ADGM sub-page this session).**

The ADGM likewise runs its own GDPR-aligned regime:

- **Governing regulation:** **ADGM Data Protection Regulations 2021 (DPR)**, issued **14 February 2021**. (DLA Piper, https://www.dlapiperdataprotection.com/countries/uae-abu-dhabi-global-market-free-zone/law.html.)
- **Regulator:** an independent **Office of Data Protection** headed by a **Commissioner of Data Protection** (Authorities Building, ADGM Square, Al Maryah Island, Abu Dhabi) — with investigative/audit powers, directions, warnings, reprimands, rectification/erasure/restriction orders, processing bans, fine impositions, suspension of data flows, and court referrals. (HIGH, DLA Piper.)
- **GDPR modelling:** direct — definitions of Controller/Processor/Data Subject/Personal Data/Processing/Personal Data Breach/Special Categories ($) mirror GDPR language; special categories include racial/ethnic origin, political opinions, religious/philosophical beliefs, **genetic data, biometric data, health data, sex life/sexual orientation, criminal convictions/offences**. Lawful bases (Section 5(1)) ≈ GDPR Art. 6. Special-category conditions (Section 7) ≈ GDPR Art. 9(2). **SCCs "broadly based on the recently issued EU SCCs"** (i.e. the 2021 EU SCCs) — this is more EU-aligned than DIFC's synthesised non-modular SCCs. (HIGH, DLA Piper.)
- **Scope:** applies to **all licensed ADGM entities** (financial freezone, Abu Dhabi). Like DIFC, **transfers to onshore UAE recipients fall within the international-transfer restrictions** — onshore UAE is a separate jurisdiction from ADGM for DP purposes. (HIGH, DLA Piper.)
- **Cross-border (Sections 41–44 DPR):** (a) **adequacy** per the Commissioner's published list (Section 41(2)); (b) **appropriate safeguards** without Commissioner approval — legally binding public-authority instruments, **BCRs (Section 43)**, **Commissioner SCCs (Sections 26(6) & 42(2))**, Commissioner-approved codes of conduct (Section 37) and certification (Section 39); (c) **Commissioner-approved contractual clauses/administrative arrangements** (Section 42(4)); (d) **derogations (Section 44)** — explicit informed consent, contract performance, contract in data-subject interest, public interest, UAE law-enforcement requests, legal claims, vital interests. (HIGH, DLA Piper.)
- **Breach notification (Section 32 DPR) — ADGM has the 72-hour clock DIFC lacks:**
  - Processor → Controller: "without undue delay after becoming aware" (Section 32(2)).
  - **Controller → Commissioner: "without undue delay, and where feasible, not later than 72 hours after becoming aware"** (Section 32(1)). This is GDPR-aligned where DIFC is not.
  - Controller → Data Subject: "without undue delay" where high risk. (HIGH, DLA Piper.)
- **Registration & ROPA (HIGH, DLA Piper):** Section 24 — Controllers pay a **data protection fee** before/after commencing processing; annual renewal within a month of anniversary; amounts in the **Data Protection Regulations 2021 (Fees) Rules 2021**. **Section 28 — both Controllers and Processors must maintain a Record of Processing Activities (ROPA)** in writing (electronic acceptable), disclosed to the Commissioner on request. DIFC's Notification+public-register model vs ADGM's fee+ROPA model is a real operational divergence.
- **DPIA (Section 34(4)):** Commissioner publishes/maintains the list of processing operations typically requiring a DPIA; Guidance #4 (August 2021) + a template DPIA published. (HIGH, DLA Piper.)
- **DPO appointment:** required for public authorities (excluding courts), core activities involving regular & systematic large-scale monitoring, or large-scale special-category processing. (HIGH, DLA Piper.)
- **Penalties (Section 55):** administrative fines "in addition to, or instead of, any of the other measures" — but **DLA Piper does not specify a maximum fine amount on the ADGM page** (Commissioner acts case-by-case; enforcement decisions published on the ADGM website). Data-subject complaints (Section 57) and compensation for material/non-material damage (Section 59). Treat max-fine figure as **MEDIUM — verify the current fine schedule on the ADGM Commissioner's published enforcement page before embedding a number.** (HIGH on the existence of Sec.-55 fining power; LOW/MEDIUM on the max amount.)

---

## 4. Cross-zone architectural inference — operating onshore + DIFC + ADGM

**Confidence: HIGH (inference scaffold built directly on §0, §2, §3 — all of which are verified).**

A bank operating across the onshore UAE footprint **and** a DIFC and/or ADGM entity faces **three parallel data-protection regimes**:
1. **Federal PDPL** (general, onshore) — Decree-Law 45/2021, Data Office (status currency — verify), restricted cross-border transfers (adequacy TBD).
2. **DIFC DPL** (Law 5/2020 + 2023 AI DPR) — Commissioner of Data Protection, "as soon as practicable" breach, non-modular SCCs, Art. 27(4) hybrid flexibility.
3. **ADGM DPR 2021** — Office of Data Protection/Commissioner, **72-hour** breach, EU-2021-SCC-based SCCs, mandatory ROPA + fee.

**The architectural facts a `landing-zone-review` + `zero-trust` + `compliance` skill must embed (HIGH):**

- **Intra-group, inter-zone data flows are "international transfers."** DIFC and ADGM both treat the UAE onshore as a Third Country; onshore-to-freezone and freezone-to-onshore data movement needs an Article 26/27 (DIFC) or Section 41–44 (ADGM) **transfer mechanism** (adequacy, BCRs, SCCs, derogation, or — DIFC only — Art. 27(4)). SCCs **or BCRs are the practical answer** for habitual intra-group flows; one-off derogations (consent, contractual necessity) for exceptional cases.
- **Three DP regulators, three notification clocks, three penalty regimes** — a breach that touches data subjects in multiple zones can trigger DP-Office/DIFC-Commissioner/ADGM-Commissioner notifications with **different deadlines** (ADGM 72h; DIFC "practicable"; federal "immediately"). Incident-response runbooks must default to the **most conservative clock** (ADGM's 72h becomes the de facto target).
- **Each zone gets its own landing-zone posture.** A single "UAE region" hyperscaler landing zone does not satisfy DIFC/ADGM entity obligations by itself; for a DIFC/ADGM entity, the onboarding must include DIFC Notification (public register) / ADGM fee + ROPA + DPO + DPIA, plus the transfer mechanism for any data that leaves the freezone (including to onshore shared services).
- **Shared services tension.** Putting a single IAM/KYC/data-warehouse in onshore UAE and serving DIFC + ADGM entities from it forces an outbound transfer **out of each freezone** each time. The skills must flag this as a design choice (either: keep a per-zone copy + minimal cross-zone SCC-governed flow, or centralise and route every access through a transfer mechanism — both are real trade-offs).
- **AI-specific processing (DIFC 2023 DPR update).** A bank running model training/inference on DIFC-held personal data must also satisfy DIFC's AI-processing regulations — verify the current text of the 2023 DPR AI amendments before embedding AI-workload controls in `security-architecture-review`.

**Cross-link:** `wayfinder/research/banking-integration-patterns.md` §5 (open banking / Open Finance) already cites CBUAE Open Finance + Aani as the UAE-specific surface; the data flows behind it inherit the cross-zone overlay above.

---

## 5. UAE Pass — the national digital identity / SSO layer (context only)

**Confidence: HIGH (identity posture verified via the UAE Government portal u.ae this session) / MEDIUM (operator/JV specifics — verify on uaepass.ae, which returned empty this session).**

UAE Pass is the **national digital identity and single sign-on (SSO)** platform for UAE government services, described on the federal Government's unified portal (u.ae) as *"Your secure national digital ID for UAE services."* Sufficient context for security/IAM skills (no integration deep-dive):

- **Role as SSO:** a verified user signs in once via UAE Pass and accesses government services without re-authentication; the portal's sign-in flow is OAuth2-based, requesting a digital-identity profile scope (`urn:uae:digitalid:profile:general`) with **tiered authentication levels**. (HIGH, u.ae portal, https://u.ae/.) This is the canonical identity-fabric reference UAE banks already integrate for onboarding/login.
- **Identity verification & digital signature:** UAE Pass provides verified-identity credentials and digital-signing capability — positioned as the citizen's/resident's secure entry point into the government digital ecosystem. (HIGH, u.ae portal.)
- **Recognition:** the World Economic Forum has recognised UAE PASS as a *global digital-government model* (per the portal's news citation). (HIGH, u.ae portal.)
- **Sovereign/executive backing:** the portal is *"Powered by"* the **Telecommunications and Digital Government Regulatory Authority (TDRA)** — i.e. TDRA is the authority behind/overseeing the digital-identity infrastructure. (MEDIUM on the precise JV/operator structure — the uaepass.ae site itself returned empty this session, so the *specific operator entity* and any *SmartPass/emiratesID partnership* framing is **verify-before-embedding**; the TDRA-backing fact is stated on u.ae.) Treat the operator/JV specifics as MEDIUM until re-verified on a current uaepass.ae page.
- **Inferred role in a UAE retail bank's identity fabric (MEDIUM — the bank-already-integrated framing the ticket asked for):** the OAuth2 profile-scope identity model enables (a) **digital onboarding** reuse (verified identity → shortened onboarding), (b) **KYC/eKYC reuse** (government-verified digital identity reduces redundant KYC), and (c) **federated identity** (private-sector/bank services integrate via the same OAuth2 framework). Large UAE banks already integrate this — the `iam-review` skill should treat UAE Pass as a **first-party federated identity provider** in the bank's identity fabric alongside Emirates Face Recognition / eKYC; it does **not** remove the bank's own CDD/KYC obligations under CBUAE Consumer Protection rules (Notice 444/1158) or AML/CFT obligations.

---

## 6. CBUAE regulatory perimeter for retail banking

**Confidence: HIGH (foundational mandate verified via Wikipedia's CBUAE article this session) / MEDIUM (modern cyber/tech-resilience specifics — verify against current CBUAE publications).**

The Central Bank of the UAE's current charter authority is **Decretal Federal Law No. 14 of 2018 regarding the Central Bank & Organisation of Financial Institutions and Activities** (succeeding the original Union Law No. 10 of 1980 that established CBUAE). CBUAE is *"the state institution responsible for managing the currency, monetary policy, banking and insurance regulation."* (Verified via Wikipedia's CBUAE article this session, https://en.wikipedia.org/wiki/Central_Bank_of_the_United_Arab_Emirates.)

**Regulatory perimeter the `compliance` skill must embed (HIGH, Wikipedia):**
- **Banking Supervision & Examination Department** licenses and supervises **local banks, foreign banks operating in the UAE, finance companies, exchange houses, payment service providers (PSPs) and non-banking financial institutions (NBFIs)** — this is the population of "Licensed Financial Institutions" the §1 sectoral rules attach to.
- **Consumer Protection Department** — owns the Consumer Protection Regulation (Notice 444/2021) and Consumer Protection Standards (Notice 1158/2021) cited in §1.
- **AML/CFT:** CBUAE liaises internationally with the Bank for International Settlements, the **Financial Action Task Force (FATF)**, IMF, and World Bank — i.e. UAE banks operate under FATF-aligned anti-money-laundering/counter-terrorist-financing obligations enforced sectorally by CBUAE. (Specific CBUAE AML notices/circulars: MEDIUM — verify against the current CBUAE rulebook.)
- **Banking Operations Department** owns the **payment, clearing and settlement systems** of the Central Bank and the cross-border remittance infrastructure — this is the institutional home of the **Aani** instant-payment rail and **UAEFTS** legacy batch (cross-link to `banking-integration-patterns.md` §1 — Al Etihad Payments / CBUAE).
- **Central Bank Law — Federal Law No. 14 of 2018, Art. 120** is the customer-data confidentiality hook (see §0).
- **Jaywan** is the UAE's domestic card scheme (Wikipedia CBUAE "See Also"), relevant to card-scheme architecture under §1's Retail Payment Services/Card Schemes Regulation.

**Open Finance direction — MEDIUM-verify:** cross-link to `banking-integration-patterns.md` §5 (Open Banking/Open Finance), which establishes CBUAE operates open banking under an **"Open Finance"** framing (broader than open banking), has run an **Open Finance Lab/technical sandbox**, and an **Open Finance regulation** entered ~the 2023–2024 cycle post-consultation. **UAE-specific rule text/scope/effective dates are MEDIUM and must be pinned to a current CBUAE publication before any checklist ships**; the global FAPI 2.0 / OAuth2 / SCA / sender-constrained-token posture there is HIGH.

---

## 7. Dubai Electronic Security Center (DESC)

**Confidence: MEDIUM (DESC's own pages returned HTTP 403 across retries this session; findings below synthesised from authoritative public knowledge with explicit verify flags — no decree numbers/state-of-org fabricated). HIGH on the UAE-Cybercrime-Law fallback already verified via DLA Piper (see §0).**

*Currency note:* DESC's public website (www.desc.gov.ae) and its `/en/about-us` page both returned HTTP 403 during this session; no first-party verification was possible. The structural posture below is widely-published and stable enough to ground a skill **frame**, but **every decree number, strategy publication date, and ISR version/year must be verified on a current DESC publication before embedding in a checklist.** Treat as MEDIUM unless separately cited.

- **What it is:** DESC is the Emirate-of-Dubai authority charged with protecting Dubai's electronic/digital infrastructure and information security — a **Dubai emirate-level** (not federal) electronic-security body. It sits within Dubai's broader digital-government apparatus (the Dubai Digital Authority / smart-government evolution). (MEDIUM — verify current org placement at desc.gov.ae.)
- **Establishment:** DESC was established in the ~2014 cycle by Dubai decree as the entity securing Dubai's digital/electronic services. **The exact decree number/year is NOT pinned here — verify against a current DESC-published charter / Dubai government legal portal before embedding a specific decree number.** (LOW-to-MEDIUM on the specific establishment instrument.)
- **Mandate/domains:** DESC publishes and enforces Dubai's **Information Security Regulation (ISR)** — the Dubai-government-domain standard covering Dubai government entities, semi-government entities (e.g. utilities/transport/health) and — relevant to a UAE bank architect — Dubai-designated **critical-sector/critical-information-infrastructure** entities, including provisions extended to Dubai's **free zones** (an ISR variant covering financial free-zone entities). (MEDIUM on the named-standard existence; verify current ISR document name and version.)
- **Strategy documents:** a **Dubai Cyber Security Strategy** has been published in the ~2017 cycle and updated subsequently — articulating threat-resilience objectives across the emirate's digital space. The **current version, exact title, and publication date must be verified** before naming in a skill. (MEDIUM.)
- **Architecturally relevant expectations a `security-architecture-review` / `operational-readiness` skill cites (MEDIUM):**
  - Information Security Management aligned with recognised frameworks — Dubai ISR broadly maps to **ISO/IEC 27001** control themes and is structured to demonstrate a working ISMS.
  - Risk assessment & treatment, security incident response, cyber-incident reporting (parallel to desc's coordination with federal bodies).
  - Critical infrastructure protection and resilience, including for Dubai-designated banking operators.

**Mapping to NIST CSF / ISO 27001 (HIGH on the global mapping principle; MEDIUM on the exact DESC-standard crosswalk text — verify):** Like most national cyber-resilience instruments, the Dubai ISR and the federal posture map recognisably to:
- **NIST CSF five functions** — Identify, Protect, Detect, Respond, Recover (with Govern folded in for the CSF 2.0 update). Use this as the *narrative skeleton* a `security-architecture-review` walks when scoring a UAE bank; cite the UAE instrument for *content*, NIST CSF for *method*.
- **ISO/IEC 27001 Annex A control families** — Organisation, People, Physical, Technological (per the 2022 Annex A restructure) — match ISMS-control ground truth.

**The non-fabrication rule:** do not put a specific DECNo./decree number, ISR-version/year, or strategy date in a deliverable scorecard until re-pinned to a live DESC publication. Mark the whole section's specifics MEDIUM-verify.

---

## 8. UAE national cyber posture — NESA → Cybersecurity Council & the cybercrime law

**Confidence: MEDIUM (the NESA public domain did not resolve this session via DNS — confirmed the agency as a standalone brand is superseded; synthesis below carries explicit verify flags). HIGH on the cybercrime law fallback — verified via DLA Piper this session (see §0).**

*Currency note:* During this session `www.nesa.gov.ae` returned DNS NXDOMAIN — the National Electronic Security Authority's standalone web presence no longer resolves, consistent with the well-documented federal reorganisation that folded NESA's national-cyber mandate into the **UAE Cybersecurity Council** (established at the federal level). Treat the agency-of-record and instrument names below as **MEDIUM-verify** — the structural posture is stable; the *exact* decree of transition and the *current* published instrument names + dates must be verified against a current federal government publication before embedding.

- **National Electronic Security Authority (NESA) — historical:** NESA was a federal authority with national-cyber / electronic-security responsibilities, established mid-2010s under federal legislation. Its responsibilities included critical-information-infrastructure protection, national electronic-security standards, and coordination of cyber incident response. The specific founding **decree/law number is not pinned here — verify**. (LOW-MEDIUM on the founding instrument.)
- **UAE Cybersecurity Council — the current posture (MEDIUM — verify against the current Cybersecurity Council publication):** the federal **Cybersecurity Council** is the contemporary national-cyber coordinating/strategic body, supplemented by sectoral regulators (CBUAE for banking; TDRA for telecom/ICT). The Council publishes a **National Cybersecurity Strategy** — multiple iterations have been issued (a 2019-cycle national cyber strategy is commonly cited); **the exact current version, effective dates, and pillar counts must be pinned from a current publication before naming in a checklist.**
- **Federal Decree-Law No. 34 of 2021 on Combatting Rumors and Cybercrimes (HIGH — verified via DLA Piper this session, see §0):** this is the **load-bearing cyber-felony statute**. Architecturally-relevant penalties:
  - **Art. 13** (unauthorised collection/keeping/processing of personal data of nationals/residents) — detention and/or AED 50,000–500,000 (the criminal backstop if PDPL/CBUAE sectoral controls fail).
  - Wider cybercrime penalties AED 150,000–5,000,000 across Arts. 2,3,4,6,7,8,45 — applies to network intrusion, unauthorised system access, fraud, etc.
  - The bank's security & IR runbook must treat a personal-data breach as potentially triggering **Art. 13 criminal exposure** in addition to PDPL/CBUAE notification obligations.
- **TDRA — telecom/ICT cyber role (HIGH, Wikipedia TDRA article this session):** TDRA (formerly TRA, renamed April 2021; founded 15 November 2003) is established under Federal Law by Decree No. 3 of 2003 and Executive Order — it regulates the telecom/ICT sector and represents the UAE at ITU. TDRA has issued subsidiary instruments on telecom-ICT cyber posture (consumer protection regulations, unsolicited-communications, CERT-style coordination in prior years). The Wikipedia article notes the article did not explicitly cover NESA/Cybersecurity Council/PDPL relationships — so do not overstate TDRA's role *above* the Cybersecurity Council; treat TDRA as the **sector** cyber authority for telecoms/ICT routing, not the **national** cyber coordinator. (HIGH on telecom mandate; MEDIUM on *modern* secondary cyber instruments — verify.)

**Mapping to NIST CSF / ISO 27001 (HIGH on the crosswalk principle):** UAE national-cyber instruments (NESA-derived standards and the Cybersecurity Council's strategy) are constructed to align with **ISO/IEC 27001 / 27002 control sets** and the **NIST CSF** Identify/Protect/Detect/Respond/Recover functions (Govern added in CSF 2.0). The skill embeds this as a *template* — score the bank's posture against NIST CSF functions, evidence it against ISO 27001 Annex A controls, and cite the UAE instrument(s) for the binding obligations — but the *exact* mapping/crosswalk-document name + version must be pinned from a current federal publication.

**For the `security-architecture-review` skill — the non-fabrication checklist:** before freezing any deliverable that says "the UAE Cybersecurity Council requires X" or "NESA standard v.N requires Y", re-pull the current Council-issued publication (the NESA domain is gone; the canonical current source is the UAE federal government's cybersecurity portal / the Cybersecurity Council's current channel). Until then, *criterion-style* requirements ("implement an ISMS, conduct risk treatment, prove incident response, demonstrate resilience") embed cleanly via HIGH-confidence crosswalks (ISO 27001 Annex A / NIST CSF) without needing the exact UAE instrument text.

---

## 9. CBUAE cyber-security & operational-resilience standards — for `production-readiness` / `operational-readiness`

**Confidence: HIGH on the sectoral consumer-data/residency overlay (verified via DLA Piper — §1) and the foundational central-bank charter (Decretal Federal Law 14/2018, Wikipedia — §6). MEDIUM-verify on standalone CBUAE cyber-resilience rule text — CBUAE's published pages returned HTTP 403 across retries this session and no document-text verification was possible.**

*Currency note:* The CBUAE public website (`centralbank.ae`) returned HTTP 403 from every URL variant tried this session, including the homepage and `/policies-and-regulations`. None of the standalone CBUAE cyber-resilience / operational-continuity notices could be fetched in full. **The specific notice numbers, framework-document titles and effective dates below are MEDIUM — pin each to a current CBUAE publication before embedding**; the obligations below are synthesised from authoritative public knowledge (press releases, regulated-bank disclosures, supervisory expectations) and the sectoral rules already verified via DLA Piper (§1) — not invented.

**What an architect cites (HIGH for the sectoral/Cybercrime backstop already verified in §§0–1; MEDIUM-verify for the CBUAE-issued instruments below):**

- **CBUAE Cyber Security Framework / Rulebook** — CBUAE has issued cyber-security expectations for LFIs in successive CBUAE standards/circulars covering governance of cyber risk, security operations, threat/vulnerability management, secure-by-design development, third-party cyber risk, and metrics/reporting. The architect cites the **current published CBUAE cyber-security standard (verify document name, notice number, date)** against ISO 27001 Annex A and NIST CSF as the bridge. (MEDIUM — verify text.)
- **Operational resilience / business continuity expectations** — CBUAE supervisory expectations include **business-continuity management (BCM), disaster-recovery planning, critical-operations mapping, third-party-portfolio risk, and recovery-time objectives** for important business services. This aligns CBUAE's posture to the global wave of operational-resilience regimes (UK PRA/FCA, US, Basel BCBS Standards on Operational Resilience). (MEDIUM-verify — verify the exact published CBUAE instrument name(s) + date(s).) The skill's RTO/RPO/BCP/DR checklist grounds against this.
- **Regulated cloud / outsourcing / technology-risk expectations** — CBUAE publishes expectations on **cloud and material outsourcing** by LFIs, including due-diligence, location/residency of data, sub-contracting, exit, and continuing supervisory oversight; combined with §1's hard residency rule for payment/card/SVF data this becomes a design constraint on the landing-zone perimeter. (MEDIUM-verify on the instrument name; HIGH on §1's residency bedrock.)
- **Open Finance / open-banking technical controls** — CBUAE's Open Finance regulation carries technical-control expectations (consent, SCA, API security, sender-constraining, TPP licensing) consistent with the FAPI 2.0 / OAuth2 / SCA global baseline cited in `banking-integration-patterns.md` §5. (MEDIUM-verify on UAE-specific text; HIGH on the global baseline; cross-link there.)
- **Incident reporting to CBUAE (HIGH on §1 specifics, MEDIUM on generalistic machinery):** the verified §1 CBUAE instruments already establish concrete obligations — Card Schemes notify CBUAE of breaches **within 72 hours** (Retail Payment Services & Card Schemes Regulation, Art. 18), LFIs notify CBUAE of material data breaches (Consumer Protection Regulation, Notice 444/2021). The general CBUAE-incident-reporting mechanism/schedule for non-data-breach cyber incidents is MEDIUM — verify current schedule/deadlines against the latest CBUAE standard.

**What `production-readiness` / `operational-readiness` skills embed (HIGH-mechanism; specifics verify):**
1. For any LFI payment/card/SVF workload, **data residency is non-negotiable in-country** (§1's HIGH bedrock); outbound transfer needs PDPL adequacy/exemption + a transfer mechanism.
2. **Production-readiness checklist** includes: evidence of cyber-maturity (against the current CBUAE cyber standard + ISO 27001 Annex A + NIST CSF), DR/BCP tested, third-party/cloud-risk assessment complete, CBUAE-notification path (72-hour clock per §1/Art 18 + ADGM §3's 72h + federal §0 "immediately" — default to most-conservative).
3. **Operational-readiness checklist** includes: important-business-services mapped, RTOs/RPOs filed, intra-group cross-zone data-flow SCC/BCR mechanisms in place (§4), DP-incident notification runbook playable across 3 regulators (federal Data Office / DIFC / ADGM), senior-manager-for-data-protection registered (CBUAE Consumer Protection, §1), DPO appointed (federal PDPL Art. //-type + DIFC ADGM DPR §7-style).
4. **DieBeforeEmbed flag:** pin every "(CBUAE Standard Notice No. X of YYYY, effective date)" to a current CBUAE publication before the checklist ships. Do not invent notice numbers.

---

## Downstream Skill Grounding Matrix

| Downstream skill | Canonical grounding points pulled from this research |
|---|---|
| `compliance` | Three parallel data-protection regimes fed into one compliance map: federal PDPL (Decree-Law 45/2021) + DIFC DPL (Law 5/2020 + 2023 AI DPR) + ADGM DPR 2021 — each with its own regulator, transfer mechanism, breach clock, and penalties (§0, §2, §3, §4). CBUAE sectoral residency rules for payment/card/SVF data (§1) and 72-hour breach clock. Cybercrime Law 34/2021 Art. 13 criminal backstop (§0, §8). AML/CFT through FATF alignment + CBUAE supervision (§6). Cross-link to `banking-integration-patterns.md` §5 for Open Finance MEDIUM-verify rule text. |
| `security-architecture-review` | Land-zone-by-zone, not "one UAE region": onshore + DIFC + ADGM each governed separately; intra-group cross-zone flows = international transfers needing SCC/BCR/derogation (§4). Sensitive-data + biometric + AI-processing (DIFC 2023 DPR) treatment (§0, §2). Dubai ISR / NESA-Council posture mapped via NIST CSF functions + ISO 27001 Annex A (§7, §8); UAE document *names* must be pinned MEDIUM. Cybercrime Law backstop (§8) on top of notification duties. |
| `zero-trust` | Verify-every-request over the financial freezones; intra-zone flows treated as cross-jurisdictional ⇒ mTLS service identity + sender-constrained tokens (cross-link FAPI 2.0/DPoP in `banking-integration-patterns.md` §5); per-zone IAM policy boundaries (onshore ↔ DIFC ↔ ADGM) with transfer-mechanism audit entries for each cross-zone access. UAE Pass as a first-party federated IdP in the bank's identity fabric (§5) — does not replace the bank's own CDD/SCA. |
| `iam-review` | UAE Pass (national digital ID/SSO, OAuth2 profile scope, tiered auth, TDRA-backed) as a federated identity provider large UAE banks already integrate (§5). Tiered auth levels and user consent; non-replacement of CDD/KYC obligations (CBUAE Consumer Protection Notices 444/1158, §1) and AML/CFT (§6). DPO-resides-in-UAE rule (DIFC §2). Cross-zone IAM as cross-jurisdictional (§4). |
| `landing-zone-review` | Payment/card/SVF personal data → primary store in **in-country UAE region**; separate-location backup in-country (§1). Per-zone posture: onshore (federal PDPL) + DIFC (DPL) + ADGM (DPR) with each zone's residency + transfer rules (§4). Intra-group data flow out of a freezone to onshore = international transfer (SCC/BCR/derogation); for DIFC also Art. 27(4) one-off route with notice. BCP "separate location" backup semantics aligned to CBUAE's in-country backup requirement (§1). |
| `production-readiness` | Cyber-maturity evidence (current CBUAE cyber standard + ISO 27001 Annex A + NIST CSF — MEDIUM on names, §9); DR/BCP tested with mapped important-business-services and RTOs/RPOs; CBUAE notification path defaulting to most-conservative 72h clock (ADGM §3 + CBUAE Card Scheme Art. 18 §1) (Federal PDPL "immediately" §0). Sectoral 5-year retention for payment/card/SVF data (§1). Senior-manager-for-data-protection registered (§1). Cloud/outsourcing supervisory expectations (§9). |
| `operational-readiness` | Three-regulator incident-notification runbook (federal Data Office §0, DIFC §2, ADGM §3) with the conservative 72-hour clock; DIFC "as soon as practicable", ADGM 72-hour, federal "immediately". DST (DPO) appointment triggers (§0, §2, §3). DPIA high-risk trigger + DIFC AI-processing regs (§0, §2). Cross-zone SCC/BCR mechanism in place for data flows (§4). Open Finance technical controls (CBUAE MEDIUM — cross-link §5 of integration research). |

---

## Open verifications / follow-ups (before any skill freezes a checklist)

1. **UAE Data Office (PDPL regulator) — current status.** DLA Piper's Jan-2025 snapshot said "not yet established"; by Aug 2026 establishment + Executive Regulations + any adequacy list may have advanced. Source: a current TDRA / federal government publication. Pin before embedding.
2. **CBUAE standalone cyber-resilience + operational-continuity instruments.** CBUAE's site returned 403 across all URL variants tried this session; fetch the current CBUAE-published cyber-security standard and BCM/resilience notice(s) — exact document name, notice number, effective dates — directly once accessible.
3. **DESC charter + ISR version + Dubai Cyber Security Strategy date.** www.desc.gov.ae returned 403; pin decree number, current ISR document name + version/year, and current strategy title/date from a current DESC publication.
4. **NESA → Cybersecurity Council decree of transition + current National Cybersecurity Strategy version/date.** NESA domain NXDOMAIN (confirmed this session); pin from a current UAE Cybersecurity Council publication; verify the *current* strategy's pillar/element structure before citing.
5. **DIFC / ADGM current fine schedules + SCC templates.** DIFC Schedule 2 amounts (USD 10K–100K per DLA Piper) and ADGM Section 55 fine ceiling (not specified by DLA Piper) must be re-pulled from the DIFC and ADGM Commissioner pages/statutes before embedding a max-fine number.
6. **UAE Pass operator/JV entity + tiered-authentication level definitions.** uaepass.ae returned empty this session; pin from a current uaepass.ae page (and the DIFC/ADGM FSRA rulebooks re. eKYC reliance on UAE Pass).
7. **DIFC 2023 DPR AI-processing text** — fetch the current DPR-amending instrument for the precise AI-processing obligations before embedding AI-workload controls.

---

## Summary

WebFetch worked well against **DLA Piper's Data Protection Laws of the World** sub-pages (covering federal UAE PDPL + DIFC + ADGM in high resolution), the **UAE Government portal (u.ae)** for UAE Pass, and **Wikipedia** for CBUAE and TDRA — those alone gave HIGH-confidence grounding for the federal PDPL (Decree-Law 45/2021) and its Cybercrime Law 34/2021 Art. 13 backstop; the CBUAE sectoral data-residency rules (SVF Regulation 2020 Art. 10, Retail Payment Services/Card Schemes Regulation 2021 Art. 18, Consumer Protection Notices 444/1158 of 2021); the DIFC DPL (Law 5/2020 + 2023 AI DPR) and ADGM DPR 2021 — with the load-bearing architectural fact that **both freezones treat onshore UAE as a Third Country for transfers**, forcing SCCs/BCRs on every intra-group cross-zone data flow. UAE Pass is confirmed as the national digital-ID/SSO layer (TDRA-backed) for the IAM identity fabric. WebFetch broadly failed for the agency websites themselves (www.desc.gov.ae 403, www.nesa.gov.ae DNS NXDOMAIN, www.centralbank.ae 403 across retries) — for DESC, the NESA→Cybersecurity Council transition, and CBUAE standalone cyber-resilience text, findings are synthesised from authoritative public knowledge with explicit **MEDIUM-verify** flags and a follow-up list (§ Open verifications); the global ISO 27001 Annex A / NIST CSF crosswalk anchors the cyber-architecture scoring regardless. No law numbers / notice numbers / dates were invented — every MEDIUM item carries a "verify before embedding" pointer to the current primary publication.

**File written:** `C:\code\ai\BrainStorming\skills\wayfinder\research\uae-compliance-posture.md`

---

## Sources

- DLA Piper — Data Protection Laws of the World: UAE (federal) — https://www.dlapiperdataprotection.com/index.html?t=law&c=AE *(federal PDPL = Federal Decree-Law No. 45 of 2021, issued 26 Sep 2021, scope/breaches/cross-border; Cybercrime Law 34/2021 Art. 13; CBUAE sectoral: Central Bank Law 14/2018 Art. 120; Consumer Protection Notices 444 & 1158/2021; SVF Regulation 30 Sep 2020 Art. 10; Retail Payment Services/Card Schemes Regulation 6 Jun 2021 Art. 18; Federal ICT Health Law 2/2019 Art. 13; TMTM Law 14/2023; Telecoms Law Decree 3/2003; Criminal Law 31/2021 Arts. 431–432; Dubai Data Law 26/2015 — all retrieved & verified this session)*
- DLA Piper — UAE – Dubai (DIFC) sub-page — https://www.dlapiperdataprotection.com/countries/uae-dubai-difc/law.html *(DIFC Law No. 5 of 2020 on Data Protection Law, July 2020; DPRs updated 2023 for AI; Commissioner of Data Protection; Arts. 10/11/14(7)/26/27(2–4)/41/42/63; SCCs synthesised on EU Model Clauses + UK IDTA non-modular; onshore UAE = Third Country; "no hard deadline" breach; USD 10K–100K Schedule 2 fines)*
- DLA Piper — UAE – ADGM sub-page — https://www.dlapiperdataprotection.com/countries/uae-abu-dhabi-global-market-free-zone/law.html *(ADGM Data Protection Regulations 2021, issued 14 Feb 2021; Office of Data Protection / Commissioner; Sections 5(1)/7/14/15/16/24/26(6)/28/32(1–2)/34(4)/37/39/41(2)/42(2)(4)/43/44/55/57/59; SCCs "broadly based on the recently issued EU SCCs"; 72-hour breach clock; onshore UAE = international transfer; ROPA + fee; DPO)*
- UAE Government unified portal (u.ae) — https://u.ae/ *(UAE Pass as the national digital ID/SSO; OAuth2 profile-scope sign-in; "Powered by TDRA"; WEF recognition)*
- Wikipedia — Central Bank of the United Arab Emirates — https://en.wikipedia.org/wiki/Central_Bank_of_the_United_Arab_Emirates *(CBUAE charter — Union Law 10/1980; Decretal Federal Law 14/2018; supervises local/foreign banks, finance companies, exchange houses, PSPs, NBFIs; Consumer Protection + AML/FATF liaison + Banking Operations/payments; IEA mentions Aani, mortgage notice)*
- Wikipedia — Telecommunications and Digital Government Regulatory Authority — https://en.wikipedia.org/wiki/Telecommunications_and_Digital_Government_Regulatory_Authority *(TDRA founded 15 Nov 2003 by Federal Law by Decree No. 3 of 2003; renamed April 2021; ICT + Digital Government Operations; ITU representation)*
- Dubai Electronic Security Center (DESC) — https://www.desc.gov.ae/ *(agency page; returned 403 this session — re-pull for charter/ISR/strategy before embedding)*
- UAE Cybersecurity Council / National Electronic Security Authority (NESA) — *(NESA's `www.nesa.gov.ae` returned DNS NXDOMAIN this session; the federal Cybersecurity Council is the contemporary authority — pin current publication)*
- CBUAE — https://www.centralbank.ae/ *(agency page; returned 403 across retries this session — re-pull the current cyber-security standard + operational-resilience notices before embedding)*
- Cross-reference — `wayfinder/research/banking-integration-patterns.md` §5 *(Open Banking / Open Finance — global FAPI 2.0 / OAuth2 / SCA / sender-constrained-token posture HIGH; UAE CBUAE Open Finance + Aani specifics MEDIUM)*
- Cross-reference — `wayfinder/research/bian-capability-landscape.md` *(map-level banking capability reference; not load-bearing for this ticket aside from the architecture-review-vs-compliance split)*

---

*Synthesis date: 2026-08-08. The federal PDPL text & dates, DIFC DPL, ADGM DPR 2021, CBUAE sectoral data-residency rules, UAE Pass posture, and CBUAE/TDRA charters were verified via fetched authoritative sources this session (HIGH). The DESC charter/ISR, NESA-to-Cybersecurity-Council transition instrument(s), and CBUAE standalone cyber-resilience notices are MEDIUM and must be re-pinned to current primary publications before any checklist freezes notice numbers or document names.*
