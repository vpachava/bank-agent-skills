# Security Audit Report

Generated: 2026-08-31T23:53:27.390297

Total Files Scanned: Checked across root directories.
Total Findings: 233

### File: `mkdocs.yml`
- **[MEDIUM]** Category: `Network Call` (Line 4)
  - `Match: site_url: https://vpachava.github.io/bank-agent-skills/`

### File: `README.md`
- **[MEDIUM]** Category: `Network Call` (Line 59)
  - `Match: git clone https://github.com/vpachava/bank-agent-skills.git`

### File: `security-audit-report.md`
- **[MEDIUM]** Category: `Network Call` (Line 10)
  - `Match: - `Match: site_url: https://vpachava.github.io/bank-agent-skills/``
- **[MEDIUM]** Category: `Network Call` (Line 14)
  - `Match: - `Match: git clone https://github.com/vpachava/bank-agent-skills.git``
- **[MEDIUM]** Category: `Network Call` (Line 18)
  - `Match: - `Match: print(f"[+] Analytics Dashboard running at http://localhost:{port}")``
- **[MEDIUM]** Category: `Network Call` (Line 22)
  - `Match: - `Match: 1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/``
- **[CRITICAL]** Category: `Adversarial Instruction` (Line 26)
  - `Match: - `Match: - **Common Pitfall:** Allowing `0.0.0.0/0` egress to the public internet. A compromised container can then exfiltrate sensitive data or reach a command-and-control server without being blocked by the clusterâ€™s network configuration.``
- **[MEDIUM]** Category: `Network Call` (Line 30)
  - `Match: - `Match: 1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/``
- **[MEDIUM]** Category: `Network Call` (Line 34)
  - `Match: - `Match: 1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/``
- **[MEDIUM]** Category: `Network Call` (Line 38)
  - `Match: - `Match: Check it out on GitHub: [vpachava/bank-agent-skills](https://github.com/vpachava/bank-agent-skills) ⭐️``
- **[MEDIUM]** Category: `Network Call` (Line 40)
  - `Match: - `Match: 10/10 Star and clone the repo here: 🌟 👉 [https://github.com/vpachava/bank-agent-skills](https://github.com/vpachava/bank-agent-skills). Contributions, issues, and PRs are extremely welcome! Let's build better systems together. 🚀``
- **[CRITICAL]** Category: `Adversarial Instruction` (Line 44)
  - `Match: - `Match: - **Never instruct agents to bypass guardrails:** Avoid any prompt instructions that state *"ignore previous instructions"* or *"disable safety rules"*.``
- **[MEDIUM]** Category: `Network Call` (Line 48)
  - `Match: - `Match: git clone https://github.com/vpachava/bank-agent-skills.git``
- **[MEDIUM]** Category: `Network Call` (Line 52)
  - `Match: - `Match: 1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/``
- **[MEDIUM]** Category: `Network Call` (Line 56)
  - `Match: - `Match: 1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/``
- **[MEDIUM]** Category: `Network Call` (Line 60)
  - `Match: - `Match: 1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/``
- **[MEDIUM]** Category: `Network Call` (Line 64)
  - `Match: - `Match: 1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/``
- **[MEDIUM]** Category: `Network Call` (Line 68)
  - `Match: - `Match: "$schema": "http://json-schema.org/draft-07/schema#",``
- **[MEDIUM]** Category: `Network Call` (Line 72)
  - `Match: - `Match: 1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/``
- **[MEDIUM]** Category: `Network Call` (Line 76)
  - `Match: - `Match: 1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/``
- **[MEDIUM]** Category: `Network Call` (Line 80)
  - `Match: - `Match: link: https://rulebook.centralbank.ae/``
- **[MEDIUM]** Category: `Network Call` (Line 84)
  - `Match: - `Match: 1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/``
- **[MEDIUM]** Category: `Network Call` (Line 88)
  - `Match: - `Match: 1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/``
- **[MEDIUM]** Category: `Network Call` (Line 92)
  - `Match: - `Match: 1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/``
- **[MEDIUM]** Category: `Network Call` (Line 96)
  - `Match: - `Match: 1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/``
- **[MEDIUM]** Category: `Network Call` (Line 100)
  - `Match: - `Match: 1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/``
- **[MEDIUM]** Category: `Network Call` (Line 104)
  - `Match: - `Match: "$schema": "http://json-schema.org/draft-07/schema#",``
- **[MEDIUM]** Category: `Network Call` (Line 108)
  - `Match: - `Match: "$schema": "http://json-schema.org/draft-07/schema#",``
- **[MEDIUM]** Category: `Network Call` (Line 112)
  - `Match: - `Match: "$schema": "http://json-schema.org/draft-07/schema#",``
- **[MEDIUM]** Category: `Network Call` (Line 116)
  - `Match: - `Match: {"url": "https://api.bank.ae/v1", "description": "Production Regulated Gateway"}``
- **[MEDIUM]** Category: `Network Call` (Line 118)
  - `Match: - `Match: "authorizationUrl": "https://auth.bank.ae/oauth2/authorize",``
- **[MEDIUM]** Category: `Network Call` (Line 120)
  - `Match: - `Match: "tokenUrl": "https://auth.bank.ae/oauth2/token",``
- **[MEDIUM]** Category: `Network Call` (Line 124)
  - `Match: - `Match: Global Banking Solution-Architect Skills Library | https://github.com/vpachava/bank-agent-skills``
- **[MEDIUM]** Category: `Network Call` (Line 128)
  - `Match: - `Match: - Network calls (http, requests, curl, fetch, urllib, socket)``
- **[CRITICAL]** Category: `Adversarial Instruction` (Line 130)
  - `Match: - `Match: r"ignore previous instructions",``
- **[CRITICAL]** Category: `Adversarial Instruction` (Line 132)
  - `Match: - `Match: r"bypass safety",``
- **[CRITICAL]** Category: `Adversarial Instruction` (Line 134)
  - `Match: - `Match: r"hide actions",``
- **[CRITICAL]** Category: `Adversarial Instruction` (Line 136)
  - `Match: - `Match: r"exfiltrate",``
- **[CRITICAL]** Category: `Adversarial Instruction` (Line 138)
  - `Match: - `Match: r"disable guardrails"``
- **[MEDIUM]** Category: `Network Call` (Line 140)
  - `Match: - `Match: r"urllib",``
- **[CRITICAL]** Category: `Adversarial Instruction` (Line 144)
  - `Match: - `Match: - **Architecture Lens Check:** Stress-testing against `Prompt Injection` trying to exfiltrate customer bank account details via PII leakage and checks for `Insecure Output Handling` when displaying data fetched from legacy core.``
- **[CRITICAL]** Category: `Adversarial Instruction` (Line 148)
  - `Match: - `Match: - **Residency leakage via logs/traces** â€” observability pipelines can exfiltrate PII across regions faster than the data store; model the telemetry path as a flow.``
- **[MEDIUM]** Category: `Network Call` (Line 152)
  - `Match: - `Match: "$schema": "http://json-schema.org/draft-07/schema#",``
- **[CRITICAL]** Category: `Adversarial Instruction` (Line 156)
  - `Match: - `Match: - **Residency leakage via logs/traces** — observability pipelines can exfiltrate PII across regions faster than the data store; model the telemetry path as a flow.``
- **[MEDIUM]** Category: `Network Call` (Line 160)
  - `Match: - `Match: - ISO 20022 standard portal — https://www.iso20022.org/``
- **[MEDIUM]** Category: `Network Call` (Line 162)
  - `Match: - `Match: - SWIFT CBPR+ programme — https://www.swift.com/our-solutions/global-financial-messaging/cross-border-payments/cbpr``
- **[MEDIUM]** Category: `Network Call` (Line 164)
  - `Match: - `Match: - Apache Kafka docs — https://kafka.apache.org/documentation/``
- **[MEDIUM]** Category: `Network Call` (Line 166)
  - `Match: - `Match: - Confluent docs / blog (event sourcing, CDC, EOS) — https://docs.confluent.io/ , https://www.confluent.io/blog``
- **[MEDIUM]** Category: `Network Call` (Line 168)
  - `Match: - `Match: - Debezium (CDC) — https://debezium.io/documentation/``
- **[MEDIUM]** Category: `Network Call` (Line 170)
  - `Match: - `Match: - Martin Fowler bliki: StranglerFig, EventSourcing — https://martinfowler.com/bliki/``
- **[MEDIUM]** Category: `Network Call` (Line 172)
  - `Match: - `Match: - microservices.io (core patterns: ACL, API gateway, Saga, Outbox) — https://microservices.io/patterns/``
- **[MEDIUM]** Category: `Network Call` (Line 174)
  - `Match: - `Match: - OpenID Foundation FAPI profiles — https://openid.net/wg/fapi/``
- **[MEDIUM]** Category: `Network Call` (Line 176)
  - `Match: - `Match: - Central Bank of the UAE (CBUAE) — https://www.centralbank.ae/``
- **[MEDIUM]** Category: `Network Call` (Line 178)
  - `Match: - `Match: - Al Etihad Payments (Aani) — https://aletihadpayments.ae/``
- **[HIGH]** Category: `Hardcoded Credential` (Line 180)
  - `Match: - `Match: 2. Tokens are sender-constrained (mTLS-bound or DPoP); pure bearer is non-compliant.``
- **[MEDIUM]** Category: `Network Call` (Line 184)
  - `Match: - `Match: - BIAN home / deliverables — https://www.bian.org/ , https://www.bian.org/deliverables/service-landscape/``
- **[MEDIUM]** Category: `Network Call` (Line 186)
  - `Match: - `Match: - BIAN News Room (v14.0 announcement) — https://www.bian.org/news/``
- **[MEDIUM]** Category: `Network Call` (Line 188)
  - `Match: - `Match: - BIAN Coreless Banking deliverable — https://www.bian.org/deliverables/coreless-banking/``
- **[MEDIUM]** Category: `Network Call` (Line 190)
  - `Match: - `Match: - BIAN Portal (catalog, behind access form) — https://portal.bian.org/``
- **[MEDIUM]** Category: `Network Call` (Line 192)
  - `Match: - `Match: - Wikipedia: Banking Industry Architecture Network (reproduces BIAN's published metamodel description) — https://en.wikipedia.org/wiki/Banking_Industry_Architecture_Network``
- **[MEDIUM]** Category: `Network Call` (Line 194)
  - `Match: - `Match: - The Open Group (TOGAF) — https://www.opengroup.org/forum/togaf , https://www.opengroup.org/togaf``
- **[MEDIUM]** Category: `Network Call` (Line 196)
  - `Match: - `Match: - IFX Forum (BIAN's implementation-message partner) — https://www.ifxforum.org/ (referenced via Wikipedia's BIAN article)``
- **[MEDIUM]** Category: `Network Call` (Line 198)
  - `Match: - `Match: - ISO 20022 (BIAN metamodel alignment) — https://www.iso20022.org/``
- **[MEDIUM]** Category: `Network Call` (Line 200)
  - `Match: - `Match: 1. **Exact v14.0 Service Domain count & re-list** — confirm 322 still holds or is updated; confirm the **Insurance** area's three new Service Domains by name; confirm the **Payment Area** reorganization detail. Source: BIAN Portal (login-gated) — https://portal.bian.org/.``
- **[MEDIUM]** Category: `Network Call` (Line 202)
  - `Match: - `Match: - BIAN home — https://www.bian.org/ *(v14.0 announcement; "250 APIs and more than 5,000 service domains"; partner listing)*``
- **[MEDIUM]** Category: `Network Call` (Line 204)
  - `Match: - `Match: - BIAN Service Landscape deliverable — https://www.bian.org/deliverables/service-landscape/ *"All 322 service domains completed" (v11.0); "+ 5000 Service definitions"; "+ 250 Semantic APIs"; v14.0 release notes — Insurance added, Payment Area reorganized, "Unnecessary Service Operations are eliminated")*``
- **[MEDIUM]** Category: `Network Call` (Line 206)
  - `Match: - `Match: - BIAN News Room — https://www.bian.org/news/ *("BIAN Unveils New Service Landscape 14.0 to Accelerate AI‑Ready Banking Architecture")*``
- **[MEDIUM]** Category: `Network Call` (Line 208)
  - `Match: - `Match: - BIAN Coreless Banking — https://www.bian.org/deliverables/coreless-banking/ *(definition; the 1.0/2.0/3.0/4.0 selective-adoption arc)*``
- **[MEDIUM]** Category: `Network Call` (Line 210)
  - `Match: - `Match: - BIAN Portal (catalog, login-gated) — https://portal.bian.org/``
- **[MEDIUM]** Category: `Network Call` (Line 212)
  - `Match: - `Match: - Wikipedia — Banking Industry Architecture Network — https://en.wikipedia.org/wiki/Banking_Industry_Architecture_Network *(reproduces BIAN's published metamodel description: Business Area → Business Domain → Service Domain; Service Domain as "elemental building blocks"; "layout can be varied depending on use"; ISO 20022 metamodel alignment; IFX Forum implementation partnership; retail/private/corporate scope; standards partners: OMG, The Open Group, IFX Forum, ISO 20022)*``
- **[MEDIUM]** Category: `Network Call` (Line 214)
  - `Match: - `Match: - The Open Group TOGAF — https://www.opengroup.org/forum/togaf , https://www.opengroup.org/togaf *(TOGAF 10th Ed.: Fundamental Content + Series Guides; general-purpose EA methodology; no banking capability content)*``
- **[MEDIUM]** Category: `Network Call` (Line 218)
  - `Match: - `Match: - Microsoft Learn — Azure Well-Archited Framework: `what-is-well-architected-framework` — https://learn.microsoft.com/en-us/azure/well-architected/what-is-well-architected-framework *(ms.date 2026-03-31, page fetched 2026-08-09)*``
- **[MEDIUM]** Category: `Network Call` (Line 220)
  - `Match: - `Match: - AWS Docs — AWS Well-Architected Framework (publication date Nov 6, 2024) — https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html , https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html *(pages fetched 2026-08-09)*``
- **[MEDIUM]** Category: `Network Call` (Line 222)
  - `Match: - `Match: - Microsoft Learn — Cloud Adoption Framework: "What is an Azure landing zone?" — https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/ *(ms.date 2025-07-24, page fetched 2026-08-09)*``
- **[MEDIUM]** Category: `Network Call` (Line 224)
  - `Match: - `Match: - Google Cloud — Cloud Architecture Framework — https://cloud.google.com/architecture/framework *(redirects to `docs.cloud.google.com/architecture/framework`; redirect target returned 404 + network-verification failure this session — re-verify the current page before embedding pillar names)*``
- **[MEDIUM]** Category: `Network Call` (Line 226)
  - `Match: - `Match: The authoritative Azure Well-Architected Framework page (Microsoft Learn, `what-is-well-architected-framework`) states verbatim that the framework "is founded on the five pillars of architectural excellence, which are mapped to those goals. They are: **Reliability**, **Security**, **Cost Optimization**, **Operational Excellence**, and **Performance Efficiency**." (WebFetch, https://learn.microsoft.com/en-us/azure/well-architected/what-is-well-architected-framework.)``
- **[MEDIUM]** Category: `Network Call` (Line 228)
  - `Match: - `Match: The authoritative AWS Well-Architected page (the pillars-of-the-framework) states verbatim: "When architecting technology solutions, if you neglect the **six pillars** of operational excellence, security, reliability, performance efficiency, cost optimization, and **sustainability**, it can become challenging to build a system that delivers on your expectations and requirements." (WebFetch, https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html.) The page lists these six peer pillars:``
- **[MEDIUM]** Category: `Network Call` (Line 230)
  - `Match: - `Match: **Banking/regulated-workload lenses (MEDIUM — specific lens availability must be confirmed in this doc):** the page this session listed six peer pillar topics and did not display a Financial Services Lens headline on the pillars page itself. AWS publishes **Well-Architected Framework lenses** (the canonical mechanism for industry/regional overlays — e.g., a Financial Services lens, a Data Analytics lens, etc.), and lenses are consumed via the AWS Well-Architected Tool or as standalone downloads. The precise current lens catalog as of Aug 2026 (whether a "Financial Services Industry" lens, a "Sustainability" lens, or a sovereign/region lens applies to this bank) must be pinned from the current AWS Well-Architected Lens list before an aws-review skill cites a lens document name. (MEDIUM — verify lens catalog at https://aws.amazon.com/architecture/well-architected/ before embedding lens names.)``
- **[MEDIUM]** Category: `Network Call` (Line 232)
  - `Match: - `Match: Google Cloud publishes the **Cloud Architecture Framework** as its Well-Architected equivalent. Its canonical URL is `https://cloud.google.com/architecture/framework` (which in 2026 redirected to a `docs.cloud.google.com/architecture/framework` host that this session returned 404 / network-verification failure). The structural posture widely published through 2024–2025 organises recommendations into **top-level categories** (commonly rendered as pillars/groups) including:``
- **[MEDIUM]** Category: `Network Call` (Line 234)
  - `Match: - `Match: 1. **Re-verify the current pillar/topic list order/count** at `https://cloud.google.com/architecture/framework` (and the `docs.cloud.google.com/architecture/framework` redirect target) before naming the categories in a checklist — the framework layout has been reorganised more than once and the doc failed to fetch this session.``
- **[MEDIUM]** Category: `Network Call` (Line 236)
  - `Match: - `Match: *Currency note:* The canonical AWS Landing Zone Accelerator (LZA) solution page (`https://aws.amazon.com/solutions/landing-zone-accelerator/`) and the prescriptive-guidance landing-zone doc returned errors this session and could not be first-party verified. The structural posture below is widely published and ground-truth for AWS multi-account design — but every claim that names a specific **product/SAM acceleration module**, its **scope**, and whether it's now **marketed under AWS Control Tower_bundling** is **MEDIUM — verify against the current AWS Solutions landing-zone page**.``
- **[MEDIUM]** Category: `Network Call` (Line 238)
  - `Match: - `Match: (HIGH — page fetched at https://docs.aws.amazon.com/general/latest/gr/rande.html.) The widely-published launch year for `me-central-1` is 2022 (MEDIUM — verify the exact launch announcement from AWS's newsroom before citing a date).``
- **[MEDIUM]** Category: `Network Call` (Line 240)
  - `Match: - `Match: **Oracle — MEDIUM (couldn't fetch the Oracle Cloud regions page this session — returned 403; widely published structural facts only, with verify flags):** Oracle Cloud Infrastructure (OCI) operates UAE-region cloud capacity — commonly published as **OCI region `me-abudhabi-1` (Abu Dhabi)** and **`me-dubai-1` (Dubai)** — i.e. the Oracle Cloud equivalent of in-country multi-region capacity. Oracle additionally has a **Government Cloud** / US/Israel/UK Sovereign Cloud flavour (Sovereign Cloud for EU and Oracle EU Sovereign Cloud) — but a UAE-sovereign flavour's availability dating must be verified against `https://www.oracle.com/cloud/regions/` and Oracle's printed cloud-compliance offerings before embedding a UAE-sovereign-OCI claim in a checklist. (MEDIUM — verify Oracle region codes + sovereignty-flavour availability directly from Oracle's cloud page, which 403'd this session.)``
- **[MEDIUM]** Category: `Network Call` (Line 242)
  - `Match: - `Match: **Confidence: HIGH (fetched the authoritative AWS EKS Best Practices Guide this session at `https://aws.github.io/aws-eks-best-practices/`).**``
- **[MEDIUM]** Category: `Network Call` (Line 244)
  - `Match: - `Match: 1. **GCP Cloud Architecture Framework — current pillar/topic list + names.** The canonical page redirected and the redirect target returned 404/network-verification-failure this session. Re-fetch `https://cloud.google.com/architecture/framework` (and the `docs.cloud.google.com/architecture/framework` redirect target) and pin the current top-level category names + count before `gcp-review` ships.``
- **[MEDIUM]** Category: `Network Call` (Line 246)
  - `Match: - `Match: 3. **AWS Well-Architected Lenses catalog — current list, and the Financial-Services-industry lens title.** The pillars page did not display the lens catalog. Verify at `https://aws.amazon.com/architecture/well-architected/` (Well-Architected homepage) before an `aws-review` skill cites a lens document name.``
- **[MEDIUM]** Category: `Network Call` (Line 248)
  - `Match: - `Match: - Microsoft Learn — Azure Well-Architected Framework: How to use — https://learn.microsoft.com/en-us/azure/well-architected/what-is-well-architected-framework *(ms.date 2026-03-31, fetched 2026-08-09)* — **verbatim five pillars: Reliability, Security, Cost Optimization, Operational Excellence, Performance Efficiency** (no Sustainability pillar); layered pillars→workloads→service-guides→design-guides; per-pillar design principles + checklists + tradeoffs + maturity model; Azure Well-Architected Review instrument.``
- **[MEDIUM]** Category: `Network Call` (Line 250)
  - `Match: - `Match: - AWS Docs — AWS Well-Architected Framework (publication date Nov 6, 2024) — https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html , https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html *(fetched 2026-08-09)* — **verbatim "six pillars of operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability"**; AWS Well-Architected Tool, Labs, APN Partner program.``
- **[MEDIUM]** Category: `Network Call` (Line 252)
  - `Match: - `Match: - Microsoft Learn — Cloud Adoption Framework: "What is an Azure landing zone?" — https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/ *(ms.date 2025-07-24, fetched 2026-08-09)* — platform landing zone (one per Entra tenant) + application landing zones; management-group hierarchy; Centralized resources (Connectivity, Identity, Management, Security subscriptions); Online/Corp/Local/Sandbox/Decommissioned management groups; Hub&Spoke or Virtual WAN topology; Azure Policy inheritance; subscription vending.``
- **[MEDIUM]** Category: `Network Call` (Line 254)
  - `Match: - `Match: - Microsoft Learn — Azure reliability: "List of Azure regions" — https://learn.microsoft.com/en-us/azure/reliability/regions-list *(ms.date 2025-09-23, last updated 2026-07-28, fetched 2026-08-09)* — **`uaenorth` (Dubai, AZ-supported, paired with `uaecentral`) ↔ `uaecentral` (Abu Dhabi, restricted access, paired with `uaenorth`)** — both in the UAE geography.``
- **[MEDIUM]** Category: `Network Call` (Line 256)
  - `Match: - `Match: - AWS Docs — AWS service endpoints — https://docs.aws.amazon.com/general/latest/gr/rande.html *(fetched 2026-08-09)* — region endpoints table verbatim: **`me-central-1` = Middle East (UAE)**, **`me-south-1` = Middle East (Bahrain)**.``
- **[MEDIUM]** Category: `Network Call` (Line 258)
  - `Match: - `Match: - AWS-eks-best-practices (AWS GitHub) — https://aws.github.io/aws-eks-best-practices/ *(fetched 2026-08-09)* — day-2 best-practices Guide categories: Security (incl. Multi-tenancy, Detective Controls, Multi-Account Strategy, Regulatory Compliance, Data Encryption/Secrets, Image Security) + Cluster Autoscaling + Reliability + Networking + Scalability + Cluster Upgrades + Cost Optimization + Windows Containers; `hardeneks` CLI validator.``
- **[MEDIUM]** Category: `Network Call` (Line 260)
  - `Match: - `Match: - HashiCorp Terraform — "State" — https://developer.hashicorp.com/terraform/language/state *(fetched 2026-08-09)* — state stores bindings between remote systems and config; remote/HCP Terraform backend strongly recommended (never commit `.tfstate` to VCS); pre-operation `refresh` reconciles drift; never edit `.tfstate` directly.``
- **[MEDIUM]** Category: `Network Call` (Line 262)
  - `Match: - `Match: - Google Cloud — Cloud Architecture Framework — https://cloud.google.com/architecture/framework *(redirected to `docs.cloud.google.com/architecture/framework`; redirect target returned 404 + network-verification failure this session — re-verify the current pillar/topic list before embedding)*``
- **[MEDIUM]** Category: `Network Call` (Line 264)
  - `Match: - `Match: - Oracle Cloud — Oracle Cloud Regions page — https://www.oracle.com/cloud/regions/ *(returned 403 this session — re-pin `me-abudhabi-1` / `me-dubai-1` codes + sovereignty flavour availability)*``
- **[MEDIUM]** Category: `Network Call` (Line 268)
  - `Match: - `Match: - DLA Piper — Data Protection Laws of the World: UAE (federal) — https://www.dlapiperdataprotection.com/index.html?t=law&c=AE``
- **[MEDIUM]** Category: `Network Call` (Line 270)
  - `Match: - `Match: - DLA Piper — UAE – Dubai (DIFC) sub-page — https://www.dlapiperdataprotection.com/countries/uae-dubai-difc/law.html``
- **[MEDIUM]** Category: `Network Call` (Line 272)
  - `Match: - `Match: - DLA Piper — UAE – ADGM sub-page — https://www.dlapiperdataprotection.com/countries/uae-abu-dhabi-global-market-free-zone/law.html``
- **[MEDIUM]** Category: `Network Call` (Line 274)
  - `Match: - `Match: - Central Bank of the UAE (CBUAE) — https://www.centralbank.ae/``
- **[MEDIUM]** Category: `Network Call` (Line 276)
  - `Match: - `Match: - DIFC — https://www.difc.ae/  | DIFC Commissioner of Data Protection — https://www.dpcomms.difc.ae/``
- **[MEDIUM]** Category: `Network Call` (Line 278)
  - `Match: - `Match: - ADGM — https://www.adgm.com/  | ADGM Commissioner of Data Protection — https://www.adgm.com/regulation/data-protection/``
- **[MEDIUM]** Category: `Network Call` (Line 280)
  - `Match: - `Match: - Dubai Electronic Security Center (DESC) — https://www.desc.gov.ae/``
- **[MEDIUM]** Category: `Network Call` (Line 282)
  - `Match: - `Match: - UAE Pass — https://www.uaepass.ae/  | UAE Government portal — https://u.ae/``
- **[MEDIUM]** Category: `Network Call` (Line 284)
  - `Match: - `Match: - TDRA (Telecommunications and Digital Government Regulatory Authority) — https://www.tdra.gov.ae/``
- **[MEDIUM]** Category: `Network Call` (Line 286)
  - `Match: - `Match: - **Regulator — the UAE "Data Office":** DLA Piper's snapshot (last modified 27 January 2025) states the Data Office administering the PDPL **had not yet been established** as of that update. By Aug 2026 its status may have advanced — treat the "Data Office established, Executive Regulations issued, adequacy decisions published" trio as **MEDIUM, verify** before embedding a regulator name or registration obligation. (DLA Piper, https://www.dlapiperdataprotection.com/index.html?t=law&c=AE.)``
- **[MEDIUM]** Category: `Network Call` (Line 288)
  - `Match: - `Match: - **Governing law:** **DIFC Law No. 5 of 2020 on Data Protection Law (DPL)**, in effect July 2020. Companion **Data Protection Regulations (DPRs)** sit beside the DPL and were **updated in 2023 to include regulations on processing via AI systems** — i.e. DIFC is the first UAE regime to address AI-specific processing directly. (DLA Piper, https://www.dlapiperdataprotection.com/countries/uae-dubai-difc/law.html.)``
- **[MEDIUM]** Category: `Network Call` (Line 290)
  - `Match: - `Match: - **Governing regulation:** **ADGM Data Protection Regulations 2021 (DPR)**, issued **14 February 2021**. (DLA Piper, https://www.dlapiperdataprotection.com/countries/uae-abu-dhabi-global-market-free-zone/law.html.)``
- **[MEDIUM]** Category: `Network Call` (Line 292)
  - `Match: - `Match: - **Role as SSO:** a verified user signs in once via UAE Pass and accesses government services without re-authentication; the portal's sign-in flow is OAuth2-based, requesting a digital-identity profile scope (`urn:uae:digitalid:profile:general`) with **tiered authentication levels**. (HIGH, u.ae portal, https://u.ae/.) This is the canonical identity-fabric reference UAE banks already integrate for onboarding/login.``
- **[MEDIUM]** Category: `Network Call` (Line 294)
  - `Match: - `Match: The Central Bank of the UAE's current charter authority is **Decretal Federal Law No. 14 of 2018 regarding the Central Bank & Organisation of Financial Institutions and Activities** (succeeding the original Union Law No. 10 of 1980 that established CBUAE). CBUAE is *"the state institution responsible for managing the currency, monetary policy, banking and insurance regulation."* (Verified via Wikipedia's CBUAE article this session, https://en.wikipedia.org/wiki/Central_Bank_of_the_United_Arab_Emirates.)``
- **[MEDIUM]** Category: `Network Call` (Line 296)
  - `Match: - `Match: - DLA Piper — Data Protection Laws of the World: UAE (federal) — https://www.dlapiperdataprotection.com/index.html?t=law&c=AE *(federal PDPL = Federal Decree-Law No. 45 of 2021, issued 26 Sep 2021, scope/breaches/cross-border; Cybercrime Law 34/2021 Art. 13; CBUAE sectoral: Central Bank Law 14/2018 Art. 120; Consumer Protection Notices 444 & 1158/2021; SVF Regulation 30 Sep 2020 Art. 10; Retail Payment Services/Card Schemes Regulation 6 Jun 2021 Art. 18; Federal ICT Health Law 2/2019 Art. 13; TMTM Law 14/2023; Telecoms Law Decree 3/2003; Criminal Law 31/2021 Arts. 431–432; Dubai Data Law 26/2015 — all retrieved & verified this session)*``
- **[MEDIUM]** Category: `Network Call` (Line 298)
  - `Match: - `Match: - DLA Piper — UAE – Dubai (DIFC) sub-page — https://www.dlapiperdataprotection.com/countries/uae-dubai-difc/law.html *(DIFC Law No. 5 of 2020 on Data Protection Law, July 2020; DPRs updated 2023 for AI; Commissioner of Data Protection; Arts. 10/11/14(7)/26/27(2–4)/41/42/63; SCCs synthesised on EU Model Clauses + UK IDTA non-modular; onshore UAE = Third Country; "no hard deadline" breach; USD 10K–100K Schedule 2 fines)*``
- **[MEDIUM]** Category: `Network Call` (Line 300)
  - `Match: - `Match: - DLA Piper — UAE – ADGM sub-page — https://www.dlapiperdataprotection.com/countries/uae-abu-dhabi-global-market-free-zone/law.html *(ADGM Data Protection Regulations 2021, issued 14 Feb 2021; Office of Data Protection / Commissioner; Sections 5(1)/7/14/15/16/24/26(6)/28/32(1–2)/34(4)/37/39/41(2)/42(2)(4)/43/44/55/57/59; SCCs "broadly based on the recently issued EU SCCs"; 72-hour breach clock; onshore UAE = international transfer; ROPA + fee; DPO)*``
- **[MEDIUM]** Category: `Network Call` (Line 302)
  - `Match: - `Match: - UAE Government unified portal (u.ae) — https://u.ae/ *(UAE Pass as the national digital ID/SSO; OAuth2 profile-scope sign-in; "Powered by TDRA"; WEF recognition)*``
- **[MEDIUM]** Category: `Network Call` (Line 304)
  - `Match: - `Match: - Wikipedia — Central Bank of the United Arab Emirates — https://en.wikipedia.org/wiki/Central_Bank_of_the_United_Arab_Emirates *(CBUAE charter — Union Law 10/1980; Decretal Federal Law 14/2018; supervises local/foreign banks, finance companies, exchange houses, PSPs, NBFIs; Consumer Protection + AML/FATF liaison + Banking Operations/payments; IEA mentions Aani, mortgage notice)*``
- **[MEDIUM]** Category: `Network Call` (Line 306)
  - `Match: - `Match: - Wikipedia — Telecommunications and Digital Government Regulatory Authority — https://en.wikipedia.org/wiki/Telecommunications_and_Digital_Government_Regulatory_Authority *(TDRA founded 15 Nov 2003 by Federal Law by Decree No. 3 of 2003; renamed April 2021; ICT + Digital Government Operations; ITU representation)*``
- **[MEDIUM]** Category: `Network Call` (Line 308)
  - `Match: - `Match: - Dubai Electronic Security Center (DESC) — https://www.desc.gov.ae/ *(agency page; returned 403 this session — re-pull for charter/ISR/strategy before embedding)*``
- **[MEDIUM]** Category: `Network Call` (Line 310)
  - `Match: - `Match: - CBUAE — https://www.centralbank.ae/ *(agency page; returned 403 across retries this session — re-pull the current cyber-security standard + operational-resilience notices before embedding)*``

### File: `analytics\dashboard.py`
- **[MEDIUM]** Category: `Network Call` (Line 73)
  - `Match: print(f"[+] Analytics Dashboard running at http://localhost:{port}")`

### File: `architecture\architecture-review\SKILL.md`
- **[MEDIUM]** Category: `Network Call` (Line 113)
  - `Match: 1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/`

### File: `cloud\kubernetes\SKILL.md`
- **[CRITICAL]** Category: `Adversarial Instruction` (Line 85)
  - `Match: - **Common Pitfall:** Allowing `0.0.0.0/0` egress to the public internet. A compromised container can then exfiltrate sensitive data or reach a command-and-control server without being blocked by the clusterâ€™s network configuration.`

### File: `devops\cicd-review\SKILL.md`
- **[MEDIUM]** Category: `Network Call` (Line 76)
  - `Match: 1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/`

### File: `devops\performance-review\SKILL.md`
- **[MEDIUM]** Category: `Network Call` (Line 97)
  - `Match: 1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/`

### File: `docs\release-announcement.md`
- **[MEDIUM]** Category: `Network Call` (Line 17)
  - `Match: Check it out on GitHub: [vpachava/bank-agent-skills](https://github.com/vpachava/bank-agent-skills) ⭐️`
- **[MEDIUM]** Category: `Network Call` (Line 40)
  - `Match: 10/10 Star and clone the repo here: 🌟 👉 [https://github.com/vpachava/bank-agent-skills](https://github.com/vpachava/bank-agent-skills). Contributions, issues, and PRs are extremely welcome! Let's build better systems together. 🚀`

### File: `docs\security-best-practices.md`
- **[CRITICAL]** Category: `Adversarial Instruction` (Line 8)
  - `Match: - **Never instruct agents to bypass guardrails:** Avoid any prompt instructions that state *"ignore previous instructions"* or *"disable safety rules"*.`

### File: `docs\video-tutorial-script.md`
- **[MEDIUM]** Category: `Network Call` (Line 26)
  - `Match: git clone https://github.com/vpachava/bank-agent-skills.git`

### File: `documentation\project-charter\SKILL.md`
- **[MEDIUM]** Category: `Network Call` (Line 78)
  - `Match: 1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/`

### File: `documentation\proposal\SKILL.md`
- **[MEDIUM]** Category: `Network Call` (Line 104)
  - `Match: 1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/`

### File: `documentation\raid-log\SKILL.md`
- **[MEDIUM]** Category: `Network Call` (Line 78)
  - `Match: 1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/`

### File: `documentation\risk-register\SKILL.md`
- **[MEDIUM]** Category: `Network Call` (Line 78)
  - `Match: 1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/`

### File: `governance\raid-log-schema.json`
- **[MEDIUM]** Category: `Network Call` (Line 2)
  - `Match: "$schema": "http://json-schema.org/draft-07/schema#",`

### File: `governance\design-review\SKILL.md`
- **[MEDIUM]** Category: `Network Call` (Line 71)
  - `Match: 1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/`

### File: `governance\dr-review\SKILL.md`
- **[MEDIUM]** Category: `Network Call` (Line 81)
  - `Match: 1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/`

### File: `governance\policy\regulations.yaml`
- **[MEDIUM]** Category: `Network Call` (Line 10)
  - `Match: link: https://rulebook.centralbank.ae/`

### File: `greenfield\reference-architecture\SKILL.md`
- **[MEDIUM]** Category: `Network Call` (Line 71)
  - `Match: 1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/`

### File: `integration\messaging\SKILL.md`
- **[MEDIUM]** Category: `Network Call` (Line 96)
  - `Match: 1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/`

### File: `mcp-servers\azure-devops-mcp.json`
- **[MEDIUM]** Category: `Network Call` (Line 7)
  - `Match: "AZDO_ORG_URL": "https://dev.azure.com/your-org",`

### File: `mcp-servers\confluence-mcp.json`
- **[MEDIUM]** Category: `Network Call` (Line 7)
  - `Match: "CONFLUENCE_URL": "https://your-domain.atlassian.net/wiki",`

### File: `mcp-servers\jira-mcp.json`
- **[MEDIUM]** Category: `Network Call` (Line 7)
  - `Match: "JIRA_URL": "https://your-domain.atlassian.net",`

### File: `migration\application-migration\SKILL.md`
- **[MEDIUM]** Category: `Network Call` (Line 78)
  - `Match: 1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/`

### File: `migration\cloud-migration\SKILL.md`
- **[MEDIUM]** Category: `Network Call` (Line 79)
  - `Match: 1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/`

### File: `modernization\legacy-assessment\SKILL.md`
- **[MEDIUM]** Category: `Network Call` (Line 94)
  - `Match: 1. **CBUAE Rulebook:** https://rulebook.centralbank.ae/`

### File: `multi_agent\handoff-protocol.json`
- **[MEDIUM]** Category: `Network Call` (Line 2)
  - `Match: "$schema": "http://json-schema.org/draft-07/schema#",`

### File: `schemas\handoff.schema.json`
- **[MEDIUM]** Category: `Network Call` (Line 2)
  - `Match: "$schema": "http://json-schema.org/draft-07/schema#",`

### File: `schemas\raid-log.schema.json`
- **[MEDIUM]** Category: `Network Call` (Line 2)
  - `Match: "$schema": "http://json-schema.org/draft-07/schema#",`

### File: `scripts\export_to_spec.py`
- **[MEDIUM]** Category: `Network Call` (Line 27)
  - `Match: {"url": "https://api.bank.ae/v1", "description": "Production Regulated Gateway"}`
- **[MEDIUM]** Category: `Network Call` (Line 37)
  - `Match: "authorizationUrl": "https://auth.bank.ae/oauth2/authorize",`
- **[MEDIUM]** Category: `Network Call` (Line 38)
  - `Match: "tokenUrl": "https://auth.bank.ae/oauth2/token",`

### File: `scripts\generate_skill_cards.py`
- **[MEDIUM]** Category: `Network Call` (Line 127)
  - `Match: Global Banking Solution-Architect Skills Library | https://github.com/vpachava/bank-agent-skills`

### File: `scripts\security-audit.py`
- **[MEDIUM]** Category: `Network Call` (Line 6)
  - `Match: - Network calls (http, requests, curl, fetch, urllib, socket)`
- **[CRITICAL]** Category: `Adversarial Instruction` (Line 21)
  - `Match: r"ignore previous instructions",`
- **[CRITICAL]** Category: `Adversarial Instruction` (Line 22)
  - `Match: r"bypass safety",`
- **[CRITICAL]** Category: `Adversarial Instruction` (Line 23)
  - `Match: r"hide actions",`
- **[CRITICAL]** Category: `Adversarial Instruction` (Line 24)
  - `Match: r"exfiltrate",`
- **[CRITICAL]** Category: `Adversarial Instruction` (Line 25)
  - `Match: r"disable guardrails"`
- **[MEDIUM]** Category: `Network Call` (Line 33)
  - `Match: r"urllib",`

### File: `security\owasp-review\SKILL.md`
- **[CRITICAL]** Category: `Adversarial Instruction` (Line 98)
  - `Match: - **Architecture Lens Check:** Stress-testing against `Prompt Injection` trying to exfiltrate customer bank account details via PII leakage and checks for `Insecure Output Handling` when displaying data fetched from legacy core.`

### File: `security\threat-model\SKILL.md`
- **[CRITICAL]** Category: `Adversarial Instruction` (Line 61)
  - `Match: - **Residency leakage via logs/traces** â€” observability pipelines can exfiltrate PII across regions faster than the data store; model the telemetry path as a flow.`

### File: `solution-arch-orchestrator\handoff.schema.json`
- **[MEDIUM]** Category: `Network Call` (Line 2)
  - `Match: "$schema": "http://json-schema.org/draft-07/schema#",`

### File: `solution-arch-orchestrator\skill-archetype.md`
- **[CRITICAL]** Category: `Adversarial Instruction` (Line 134)
  - `Match: - **Residency leakage via logs/traces** — observability pipelines can exfiltrate PII across regions faster than the data store; model the telemetry path as a flow.`

### File: `solution-arch-orchestrator\research\banking-integration-patterns.md`
- **[MEDIUM]** Category: `Network Call` (Line 19)
  - `Match: - ISO 20022 standard portal — https://www.iso20022.org/`
- **[MEDIUM]** Category: `Network Call` (Line 20)
  - `Match: - SWIFT CBPR+ programme — https://www.swift.com/our-solutions/global-financial-messaging/cross-border-payments/cbpr`
- **[MEDIUM]** Category: `Network Call` (Line 21)
  - `Match: - Apache Kafka docs — https://kafka.apache.org/documentation/`
- **[MEDIUM]** Category: `Network Call` (Line 22)
  - `Match: - Confluent docs / blog (event sourcing, CDC, EOS) — https://docs.confluent.io/ , https://www.confluent.io/blog`
- **[MEDIUM]** Category: `Network Call` (Line 23)
  - `Match: - Debezium (CDC) — https://debezium.io/documentation/`
- **[MEDIUM]** Category: `Network Call` (Line 24)
  - `Match: - Martin Fowler bliki: StranglerFig, EventSourcing — https://martinfowler.com/bliki/`
- **[MEDIUM]** Category: `Network Call` (Line 25)
  - `Match: - microservices.io (core patterns: ACL, API gateway, Saga, Outbox) — https://microservices.io/patterns/`
- **[MEDIUM]** Category: `Network Call` (Line 26)
  - `Match: - OpenID Foundation FAPI profiles — https://openid.net/wg/fapi/`
- **[MEDIUM]** Category: `Network Call` (Line 27)
  - `Match: - Central Bank of the UAE (CBUAE) — https://www.centralbank.ae/`
- **[MEDIUM]** Category: `Network Call` (Line 28)
  - `Match: - Al Etihad Payments (Aani) — https://aletihadpayments.ae/`
- **[HIGH]** Category: `Hardcoded Credential` (Line 174)
  - `Match: 2. Tokens are sender-constrained (mTLS-bound or DPoP); pure bearer is non-compliant.`

### File: `solution-arch-orchestrator\research\bian-capability-landscape.md`
- **[MEDIUM]** Category: `Network Call` (Line 19)
  - `Match: - BIAN home / deliverables — https://www.bian.org/ , https://www.bian.org/deliverables/service-landscape/`
- **[MEDIUM]** Category: `Network Call` (Line 20)
  - `Match: - BIAN News Room (v14.0 announcement) — https://www.bian.org/news/`
- **[MEDIUM]** Category: `Network Call` (Line 21)
  - `Match: - BIAN Coreless Banking deliverable — https://www.bian.org/deliverables/coreless-banking/`
- **[MEDIUM]** Category: `Network Call` (Line 22)
  - `Match: - BIAN Portal (catalog, behind access form) — https://portal.bian.org/`
- **[MEDIUM]** Category: `Network Call` (Line 23)
  - `Match: - Wikipedia: Banking Industry Architecture Network (reproduces BIAN's published metamodel description) — https://en.wikipedia.org/wiki/Banking_Industry_Architecture_Network`
- **[MEDIUM]** Category: `Network Call` (Line 24)
  - `Match: - The Open Group (TOGAF) — https://www.opengroup.org/forum/togaf , https://www.opengroup.org/togaf`
- **[MEDIUM]** Category: `Network Call` (Line 25)
  - `Match: - IFX Forum (BIAN's implementation-message partner) — https://www.ifxforum.org/ (referenced via Wikipedia's BIAN article)`
- **[MEDIUM]** Category: `Network Call` (Line 26)
  - `Match: - ISO 20022 (BIAN metamodel alignment) — https://www.iso20022.org/`
- **[MEDIUM]** Category: `Network Call` (Line 222)
  - `Match: 1. **Exact v14.0 Service Domain count & re-list** — confirm 322 still holds or is updated; confirm the **Insurance** area's three new Service Domains by name; confirm the **Payment Area** reorganization detail. Source: BIAN Portal (login-gated) — https://portal.bian.org/.`
- **[MEDIUM]** Category: `Network Call` (Line 231)
  - `Match: - BIAN home — https://www.bian.org/ *(v14.0 announcement; "250 APIs and more than 5,000 service domains"; partner listing)*`
- **[MEDIUM]** Category: `Network Call` (Line 232)
  - `Match: - BIAN Service Landscape deliverable — https://www.bian.org/deliverables/service-landscape/ *"All 322 service domains completed" (v11.0); "+ 5000 Service definitions"; "+ 250 Semantic APIs"; v14.0 release notes — Insurance added, Payment Area reorganized, "Unnecessary Service Operations are eliminated")*`
- **[MEDIUM]** Category: `Network Call` (Line 233)
  - `Match: - BIAN News Room — https://www.bian.org/news/ *("BIAN Unveils New Service Landscape 14.0 to Accelerate AI‑Ready Banking Architecture")*`
- **[MEDIUM]** Category: `Network Call` (Line 234)
  - `Match: - BIAN Coreless Banking — https://www.bian.org/deliverables/coreless-banking/ *(definition; the 1.0/2.0/3.0/4.0 selective-adoption arc)*`
- **[MEDIUM]** Category: `Network Call` (Line 235)
  - `Match: - BIAN Portal (catalog, login-gated) — https://portal.bian.org/`
- **[MEDIUM]** Category: `Network Call` (Line 236)
  - `Match: - Wikipedia — Banking Industry Architecture Network — https://en.wikipedia.org/wiki/Banking_Industry_Architecture_Network *(reproduces BIAN's published metamodel description: Business Area → Business Domain → Service Domain; Service Domain as "elemental building blocks"; "layout can be varied depending on use"; ISO 20022 metamodel alignment; IFX Forum implementation partnership; retail/private/corporate scope; standards partners: OMG, The Open Group, IFX Forum, ISO 20022)*`
- **[MEDIUM]** Category: `Network Call` (Line 237)
  - `Match: - The Open Group TOGAF — https://www.opengroup.org/forum/togaf , https://www.opengroup.org/togaf *(TOGAF 10th Ed.: Fundamental Content + Series Guides; general-purpose EA methodology; no banking capability content)*`

### File: `solution-arch-orchestrator\research\cloud-well-architected-banking.md`
- **[MEDIUM]** Category: `Network Call` (Line 19)
  - `Match: - Microsoft Learn — Azure Well-Archited Framework: `what-is-well-architected-framework` — https://learn.microsoft.com/en-us/azure/well-architected/what-is-well-architected-framework *(ms.date 2026-03-31, page fetched 2026-08-09)*`
- **[MEDIUM]** Category: `Network Call` (Line 20)
  - `Match: - AWS Docs — AWS Well-Architected Framework (publication date Nov 6, 2024) — https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html , https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html *(pages fetched 2026-08-09)*`
- **[MEDIUM]** Category: `Network Call` (Line 21)
  - `Match: - Microsoft Learn — Cloud Adoption Framework: "What is an Azure landing zone?" — https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/ *(ms.date 2025-07-24, page fetched 2026-08-09)*`
- **[MEDIUM]** Category: `Network Call` (Line 22)
  - `Match: - Google Cloud — Cloud Architecture Framework — https://cloud.google.com/architecture/framework *(redirects to `docs.cloud.google.com/architecture/framework`; redirect target returned 404 + network-verification failure this session — re-verify the current page before embedding pillar names)*`
- **[MEDIUM]** Category: `Network Call` (Line 34)
  - `Match: The authoritative Azure Well-Architected Framework page (Microsoft Learn, `what-is-well-architected-framework`) states verbatim that the framework "is founded on the five pillars of architectural excellence, which are mapped to those goals. They are: **Reliability**, **Security**, **Cost Optimization**, **Operational Excellence**, and **Performance Efficiency**." (WebFetch, https://learn.microsoft.com/en-us/azure/well-architected/what-is-well-architected-framework.)`
- **[MEDIUM]** Category: `Network Call` (Line 50)
  - `Match: The authoritative AWS Well-Architected page (the pillars-of-the-framework) states verbatim: "When architecting technology solutions, if you neglect the **six pillars** of operational excellence, security, reliability, performance efficiency, cost optimization, and **sustainability**, it can become challenging to build a system that delivers on your expectations and requirements." (WebFetch, https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html.) The page lists these six peer pillars:`
- **[MEDIUM]** Category: `Network Call` (Line 65)
  - `Match: **Banking/regulated-workload lenses (MEDIUM — specific lens availability must be confirmed in this doc):** the page this session listed six peer pillar topics and did not display a Financial Services Lens headline on the pillars page itself. AWS publishes **Well-Architected Framework lenses** (the canonical mechanism for industry/regional overlays — e.g., a Financial Services lens, a Data Analytics lens, etc.), and lenses are consumed via the AWS Well-Architected Tool or as standalone downloads. The precise current lens catalog as of Aug 2026 (whether a "Financial Services Industry" lens, a "Sustainability" lens, or a sovereign/region lens applies to this bank) must be pinned from the current AWS Well-Architected Lens list before an aws-review skill cites a lens document name. (MEDIUM — verify lens catalog at https://aws.amazon.com/architecture/well-architected/ before embedding lens names.)`
- **[MEDIUM]** Category: `Network Call` (Line 71)
  - `Match: Google Cloud publishes the **Cloud Architecture Framework** as its Well-Architected equivalent. Its canonical URL is `https://cloud.google.com/architecture/framework` (which in 2026 redirected to a `docs.cloud.google.com/architecture/framework` host that this session returned 404 / network-verification failure). The structural posture widely published through 2024–2025 organises recommendations into **top-level categories** (commonly rendered as pillars/groups) including:`
- **[MEDIUM]** Category: `Network Call` (Line 82)
  - `Match: 1. **Re-verify the current pillar/topic list order/count** at `https://cloud.google.com/architecture/framework` (and the `docs.cloud.google.com/architecture/framework` redirect target) before naming the categories in a checklist — the framework layout has been reorganised more than once and the doc failed to fetch this session.`
- **[MEDIUM]** Category: `Network Call` (Line 122)
  - `Match: *Currency note:* The canonical AWS Landing Zone Accelerator (LZA) solution page (`https://aws.amazon.com/solutions/landing-zone-accelerator/`) and the prescriptive-guidance landing-zone doc returned errors this session and could not be first-party verified. The structural posture below is widely published and ground-truth for AWS multi-account design — but every claim that names a specific **product/SAM acceleration module**, its **scope**, and whether it's now **marketed under AWS Control Tower_bundling** is **MEDIUM — verify against the current AWS Solutions landing-zone page**.`
- **[MEDIUM]** Category: `Network Call` (Line 151)
  - `Match: (HIGH — page fetched at https://docs.aws.amazon.com/general/latest/gr/rande.html.) The widely-published launch year for `me-central-1` is 2022 (MEDIUM — verify the exact launch announcement from AWS's newsroom before citing a date).`
- **[MEDIUM]** Category: `Network Call` (Line 155)
  - `Match: **Oracle — MEDIUM (couldn't fetch the Oracle Cloud regions page this session — returned 403; widely published structural facts only, with verify flags):** Oracle Cloud Infrastructure (OCI) operates UAE-region cloud capacity — commonly published as **OCI region `me-abudhabi-1` (Abu Dhabi)** and **`me-dubai-1` (Dubai)** — i.e. the Oracle Cloud equivalent of in-country multi-region capacity. Oracle additionally has a **Government Cloud** / US/Israel/UK Sovereign Cloud flavour (Sovereign Cloud for EU and Oracle EU Sovereign Cloud) — but a UAE-sovereign flavour's availability dating must be verified against `https://www.oracle.com/cloud/regions/` and Oracle's printed cloud-compliance offerings before embedding a UAE-sovereign-OCI claim in a checklist. (MEDIUM — verify Oracle region codes + sovereignty-flavour availability directly from Oracle's cloud page, which 403'd this session.)`
- **[MEDIUM]** Category: `Network Call` (Line 196)
  - `Match: **Confidence: HIGH (fetched the authoritative AWS EKS Best Practices Guide this session at `https://aws.github.io/aws-eks-best-practices/`).**`
- **[MEDIUM]** Category: `Network Call` (Line 298)
  - `Match: 1. **GCP Cloud Architecture Framework — current pillar/topic list + names.** The canonical page redirected and the redirect target returned 404/network-verification-failure this session. Re-fetch `https://cloud.google.com/architecture/framework` (and the `docs.cloud.google.com/architecture/framework` redirect target) and pin the current top-level category names + count before `gcp-review` ships.`
- **[MEDIUM]** Category: `Network Call` (Line 300)
  - `Match: 3. **AWS Well-Architected Lenses catalog — current list, and the Financial-Services-industry lens title.** The pillars page did not display the lens catalog. Verify at `https://aws.amazon.com/architecture/well-architected/` (Well-Architected homepage) before an `aws-review` skill cites a lens document name.`
- **[MEDIUM]** Category: `Network Call` (Line 321)
  - `Match: - Microsoft Learn — Azure Well-Architected Framework: How to use — https://learn.microsoft.com/en-us/azure/well-architected/what-is-well-architected-framework *(ms.date 2026-03-31, fetched 2026-08-09)* — **verbatim five pillars: Reliability, Security, Cost Optimization, Operational Excellence, Performance Efficiency** (no Sustainability pillar); layered pillars→workloads→service-guides→design-guides; per-pillar design principles + checklists + tradeoffs + maturity model; Azure Well-Architected Review instrument.`
- **[MEDIUM]** Category: `Network Call` (Line 322)
  - `Match: - AWS Docs — AWS Well-Architected Framework (publication date Nov 6, 2024) — https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html , https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html *(fetched 2026-08-09)* — **verbatim "six pillars of operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability"**; AWS Well-Architected Tool, Labs, APN Partner program.`
- **[MEDIUM]** Category: `Network Call` (Line 323)
  - `Match: - Microsoft Learn — Cloud Adoption Framework: "What is an Azure landing zone?" — https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/ *(ms.date 2025-07-24, fetched 2026-08-09)* — platform landing zone (one per Entra tenant) + application landing zones; management-group hierarchy; Centralized resources (Connectivity, Identity, Management, Security subscriptions); Online/Corp/Local/Sandbox/Decommissioned management groups; Hub&Spoke or Virtual WAN topology; Azure Policy inheritance; subscription vending.`
- **[MEDIUM]** Category: `Network Call` (Line 324)
  - `Match: - Microsoft Learn — Azure reliability: "List of Azure regions" — https://learn.microsoft.com/en-us/azure/reliability/regions-list *(ms.date 2025-09-23, last updated 2026-07-28, fetched 2026-08-09)* — **`uaenorth` (Dubai, AZ-supported, paired with `uaecentral`) ↔ `uaecentral` (Abu Dhabi, restricted access, paired with `uaenorth`)** — both in the UAE geography.`
- **[MEDIUM]** Category: `Network Call` (Line 325)
  - `Match: - AWS Docs — AWS service endpoints — https://docs.aws.amazon.com/general/latest/gr/rande.html *(fetched 2026-08-09)* — region endpoints table verbatim: **`me-central-1` = Middle East (UAE)**, **`me-south-1` = Middle East (Bahrain)**.`
- **[MEDIUM]** Category: `Network Call` (Line 326)
  - `Match: - AWS-eks-best-practices (AWS GitHub) — https://aws.github.io/aws-eks-best-practices/ *(fetched 2026-08-09)* — day-2 best-practices Guide categories: Security (incl. Multi-tenancy, Detective Controls, Multi-Account Strategy, Regulatory Compliance, Data Encryption/Secrets, Image Security) + Cluster Autoscaling + Reliability + Networking + Scalability + Cluster Upgrades + Cost Optimization + Windows Containers; `hardeneks` CLI validator.`
- **[MEDIUM]** Category: `Network Call` (Line 327)
  - `Match: - HashiCorp Terraform — "State" — https://developer.hashicorp.com/terraform/language/state *(fetched 2026-08-09)* — state stores bindings between remote systems and config; remote/HCP Terraform backend strongly recommended (never commit `.tfstate` to VCS); pre-operation `refresh` reconciles drift; never edit `.tfstate` directly.`
- **[MEDIUM]** Category: `Network Call` (Line 328)
  - `Match: - Google Cloud — Cloud Architecture Framework — https://cloud.google.com/architecture/framework *(redirected to `docs.cloud.google.com/architecture/framework`; redirect target returned 404 + network-verification failure this session — re-verify the current pillar/topic list before embedding)*`
- **[MEDIUM]** Category: `Network Call` (Line 329)
  - `Match: - Oracle Cloud — Oracle Cloud Regions page — https://www.oracle.com/cloud/regions/ *(returned 403 this session — re-pin `me-abudhabi-1` / `me-dubai-1` codes + sovereignty flavour availability)*`

### File: `solution-arch-orchestrator\research\uae-compliance-posture.md`
- **[MEDIUM]** Category: `Network Call` (Line 19)
  - `Match: - DLA Piper — Data Protection Laws of the World: UAE (federal) — https://www.dlapiperdataprotection.com/index.html?t=law&c=AE`
- **[MEDIUM]** Category: `Network Call` (Line 20)
  - `Match: - DLA Piper — UAE – Dubai (DIFC) sub-page — https://www.dlapiperdataprotection.com/countries/uae-dubai-difc/law.html`
- **[MEDIUM]** Category: `Network Call` (Line 21)
  - `Match: - DLA Piper — UAE – ADGM sub-page — https://www.dlapiperdataprotection.com/countries/uae-abu-dhabi-global-market-free-zone/law.html`
- **[MEDIUM]** Category: `Network Call` (Line 22)
  - `Match: - Central Bank of the UAE (CBUAE) — https://www.centralbank.ae/`
- **[MEDIUM]** Category: `Network Call` (Line 23)
  - `Match: - DIFC — https://www.difc.ae/  | DIFC Commissioner of Data Protection — https://www.dpcomms.difc.ae/`
- **[MEDIUM]** Category: `Network Call` (Line 24)
  - `Match: - ADGM — https://www.adgm.com/  | ADGM Commissioner of Data Protection — https://www.adgm.com/regulation/data-protection/`
- **[MEDIUM]** Category: `Network Call` (Line 25)
  - `Match: - Dubai Electronic Security Center (DESC) — https://www.desc.gov.ae/`
- **[MEDIUM]** Category: `Network Call` (Line 26)
  - `Match: - UAE Pass — https://www.uaepass.ae/  | UAE Government portal — https://u.ae/`
- **[MEDIUM]** Category: `Network Call` (Line 27)
  - `Match: - TDRA (Telecommunications and Digital Government Regulatory Authority) — https://www.tdra.gov.ae/`
- **[MEDIUM]** Category: `Network Call` (Line 37)
  - `Match: - **Regulator — the UAE "Data Office":** DLA Piper's snapshot (last modified 27 January 2025) states the Data Office administering the PDPL **had not yet been established** as of that update. By Aug 2026 its status may have advanced — treat the "Data Office established, Executive Regulations issued, adequacy decisions published" trio as **MEDIUM, verify** before embedding a regulator name or registration obligation. (DLA Piper, https://www.dlapiperdataprotection.com/index.html?t=law&c=AE.)`
- **[MEDIUM]** Category: `Network Call` (Line 77)
  - `Match: - **Governing law:** **DIFC Law No. 5 of 2020 on Data Protection Law (DPL)**, in effect July 2020. Companion **Data Protection Regulations (DPRs)** sit beside the DPL and were **updated in 2023 to include regulations on processing via AI systems** — i.e. DIFC is the first UAE regime to address AI-specific processing directly. (DLA Piper, https://www.dlapiperdataprotection.com/countries/uae-dubai-difc/law.html.)`
- **[MEDIUM]** Category: `Network Call` (Line 100)
  - `Match: - **Governing regulation:** **ADGM Data Protection Regulations 2021 (DPR)**, issued **14 February 2021**. (DLA Piper, https://www.dlapiperdataprotection.com/countries/uae-abu-dhabi-global-market-free-zone/law.html.)`
- **[MEDIUM]** Category: `Network Call` (Line 143)
  - `Match: - **Role as SSO:** a verified user signs in once via UAE Pass and accesses government services without re-authentication; the portal's sign-in flow is OAuth2-based, requesting a digital-identity profile scope (`urn:uae:digitalid:profile:general`) with **tiered authentication levels**. (HIGH, u.ae portal, https://u.ae/.) This is the canonical identity-fabric reference UAE banks already integrate for onboarding/login.`
- **[MEDIUM]** Category: `Network Call` (Line 155)
  - `Match: The Central Bank of the UAE's current charter authority is **Decretal Federal Law No. 14 of 2018 regarding the Central Bank & Organisation of Financial Institutions and Activities** (succeeding the original Union Law No. 10 of 1980 that established CBUAE). CBUAE is *"the state institution responsible for managing the currency, monetary policy, banking and insurance regulation."* (Verified via Wikipedia's CBUAE article this session, https://en.wikipedia.org/wiki/Central_Bank_of_the_United_Arab_Emirates.)`
- **[MEDIUM]** Category: `Network Call` (Line 270)
  - `Match: - DLA Piper — Data Protection Laws of the World: UAE (federal) — https://www.dlapiperdataprotection.com/index.html?t=law&c=AE *(federal PDPL = Federal Decree-Law No. 45 of 2021, issued 26 Sep 2021, scope/breaches/cross-border; Cybercrime Law 34/2021 Art. 13; CBUAE sectoral: Central Bank Law 14/2018 Art. 120; Consumer Protection Notices 444 & 1158/2021; SVF Regulation 30 Sep 2020 Art. 10; Retail Payment Services/Card Schemes Regulation 6 Jun 2021 Art. 18; Federal ICT Health Law 2/2019 Art. 13; TMTM Law 14/2023; Telecoms Law Decree 3/2003; Criminal Law 31/2021 Arts. 431–432; Dubai Data Law 26/2015 — all retrieved & verified this session)*`
- **[MEDIUM]** Category: `Network Call` (Line 271)
  - `Match: - DLA Piper — UAE – Dubai (DIFC) sub-page — https://www.dlapiperdataprotection.com/countries/uae-dubai-difc/law.html *(DIFC Law No. 5 of 2020 on Data Protection Law, July 2020; DPRs updated 2023 for AI; Commissioner of Data Protection; Arts. 10/11/14(7)/26/27(2–4)/41/42/63; SCCs synthesised on EU Model Clauses + UK IDTA non-modular; onshore UAE = Third Country; "no hard deadline" breach; USD 10K–100K Schedule 2 fines)*`
- **[MEDIUM]** Category: `Network Call` (Line 272)
  - `Match: - DLA Piper — UAE – ADGM sub-page — https://www.dlapiperdataprotection.com/countries/uae-abu-dhabi-global-market-free-zone/law.html *(ADGM Data Protection Regulations 2021, issued 14 Feb 2021; Office of Data Protection / Commissioner; Sections 5(1)/7/14/15/16/24/26(6)/28/32(1–2)/34(4)/37/39/41(2)/42(2)(4)/43/44/55/57/59; SCCs "broadly based on the recently issued EU SCCs"; 72-hour breach clock; onshore UAE = international transfer; ROPA + fee; DPO)*`
- **[MEDIUM]** Category: `Network Call` (Line 273)
  - `Match: - UAE Government unified portal (u.ae) — https://u.ae/ *(UAE Pass as the national digital ID/SSO; OAuth2 profile-scope sign-in; "Powered by TDRA"; WEF recognition)*`
- **[MEDIUM]** Category: `Network Call` (Line 274)
  - `Match: - Wikipedia — Central Bank of the United Arab Emirates — https://en.wikipedia.org/wiki/Central_Bank_of_the_United_Arab_Emirates *(CBUAE charter — Union Law 10/1980; Decretal Federal Law 14/2018; supervises local/foreign banks, finance companies, exchange houses, PSPs, NBFIs; Consumer Protection + AML/FATF liaison + Banking Operations/payments; IEA mentions Aani, mortgage notice)*`
- **[MEDIUM]** Category: `Network Call` (Line 275)
  - `Match: - Wikipedia — Telecommunications and Digital Government Regulatory Authority — https://en.wikipedia.org/wiki/Telecommunications_and_Digital_Government_Regulatory_Authority *(TDRA founded 15 Nov 2003 by Federal Law by Decree No. 3 of 2003; renamed April 2021; ICT + Digital Government Operations; ITU representation)*`
- **[MEDIUM]** Category: `Network Call` (Line 276)
  - `Match: - Dubai Electronic Security Center (DESC) — https://www.desc.gov.ae/ *(agency page; returned 403 this session — re-pull for charter/ISR/strategy before embedding)*`
- **[MEDIUM]** Category: `Network Call` (Line 278)
  - `Match: - CBUAE — https://www.centralbank.ae/ *(agency page; returned 403 across retries this session — re-pull the current cyber-security standard + operational-resilience notices before embedding)*`

