# 🎬 5-Minute Video Tutorial: Getting Started with bank-agent-skills

## Video Metadata
- **Title:** Master Solution Architecture in 5 Minutes with bank-agent-skills
- **Target Audience:** Solution Architects, Enterprise Architects, Principal Engineers, CISOs
- **Target Duration:** 05:00
- **Resolution:** 1080p60 / 4K30 (Clean Terminal Font: JetBrains Mono / Fira Code @ 18pt)

---

## 📜 Full Timestamped Script & Screen Action Plan

### [00:00 - 00:30] Intro: What is bank-agent-skills?
* **Visual:** Speaker on camera or dynamic title slide overlaying a clean terminal showing `vpachava/bank-agent-skills`.
* **Audio (Narrator):**
  > "Welcome! If you're a Solution Architect in enterprise banking or regulated tech, you know the pain: endless HLD documents, manual threat modeling, compliance friction, and architectural drift.
  > Meet `bank-agent-skills`: an open-source, AI-native Governance Engine packed with 100 executable skills, 16 domains, and multi-jurisdictional compliance across UAE, KSA, EU, US, UK, and beyond.
  > In just 5 minutes, let me show you how to turn architecture from static text into executable code."

---

### [00:30 - 01:30] Step 1: Installation Wizard (1 Minute)
* **Visual:** Screen recording of terminal. User clones repo and runs `python scripts/install-wizard.py`.
* **Terminal Actions:**
  ```bash
  git clone https://github.com/vpachava/bank-agent-skills.git
  cd bank-agent-skills
  python scripts/install-wizard.py
  ```
* **Audio (Narrator):**
  > "Getting started takes less than 60 seconds. Clone the repo and fire up `install-wizard.py`.
  > The wizard automatically detects your OS and AI CLI environment—whether you're using Claude Code, Hermes Agent, Codex, or OpenCode.
  > Choose Global, Hermes, or Project-Local mode, select your primary jurisdiction—we'll pick UAE CBUAE and PDPL—and the wizard sets up your profile, downloads the registry, and configures pre-commit quality hooks automatically."

---

### [01:30 - 02:30] Step 2: Running Your First Skill (`/requirements-analysis`)
* **Visual:** Terminal running Claude Code or Hermes Agent CLI. User invokes `/requirements-analysis`.
* **Terminal Actions:**
  ```text
  /requirements-analysis
  > Requirement: Build a real-time card payment gateway supporting mTLS and ISO 20022 messaging.
  ```
* **Audio (Narrator):**
  > "Now let's launch our first skill: `/requirements-analysis`.
  > Notice how the agent doesn't just ask generic questions—it immediately extracts functional scope, non-functional requirements, data residency constraints, and ISO 20022 message envelopes.
  > It formats the output into a clean, structured JSON handoff artifact containing a unique `artifact_id` and baseline NFR metrics."

---

### [02:30 - 04:00] Step 3: Executing a Skill Chain (`gap-analysis` ➔ `hld-generator` ────────► `evidence-gate`)
* **Visual:** Terminal showing a chained execution flow. Output displays generated Mermaid diagrams via `/archify` and the validation pass from `/evidence-gate`.
* **Terminal Actions:**
  ```text
  /hld-generator
  /archify
  python governance/scripts/evidence-gate.py handoff.json
  ```
* **Audio (Narrator):**
  > "Here's where the magic happens: Skill Chaining.
  > We feed our requirements into `/hld-generator` to create our High-Level Design. Next, `/archify` automatically compiles our JSON design payload into a version-controlled Mermaid.js architecture diagram.
  > Finally, we run `evidence-gate`. Instead of taking the AI's word for it, `evidence-gate` inspects our actual Terraform and Kubernetes code in the repository. If the code matches our security claims, the gate passes. If not, it blocks the build."

---

### [04:00 - 04:30] Step 4: Exporting to OpenAPI & Issue Trackers (Jira / Linear)
* **Visual:** Terminal running `export_to_spec.py` and `export_to_tracker.py`. Split screen showing generated `openapi.yaml` and formatted Jira markdown ticket.
* **Terminal Actions:**
  ```bash
  python scripts/export_to_spec.py handoff.json
  python scripts/export_to_tracker.py handoff.json --format jira
  ```
* **Audio (Narrator):**
  > "When design is complete, handing off to engineering is 1-click.
  > `export_to_spec.py` generates valid OpenAPI 3.1 and AsyncAPI 3.0 specs with FAPI 2.0 security headers injected.
  > `export_to_tracker.py` formats the architecture directly into a Jira or Linear ticket complete with BIAN service domain mappings and acceptance criteria."

---

### [04:30 - 05:00] Outro: Where to Learn More
* **Visual:** Closing slide with GitHub link, documentation QR code, and star callout.
* **Audio (Narrator):**
  > "And that's it! In 5 minutes, we went from raw requirements to a verified, compliant, diagrammed architecture ready for production.
  > Check out the repo at `github.com/vpachava/bank-agent-skills`. Star the project, try out the 100+ skills, and join the community. Happy architecting!"

---

## 📹 Screen Recording & Production Checklist

### Pre-Recording Setup:
- [ ] **Terminal Setup:** Set terminal size to 1920x1080, font to JetBrains Mono / Fira Code 18pt.
- [ ] **Theme:** Use a dark high-contrast theme (e.g., One Dark, Dracula, GitHub Dark).
- [ ] **OBS Studio Settings:** 1080p 60fps, Bitrate: 12,000 Kbps, Audio: 320 Kbps AAC.
- [ ] **Audio Hardware:** Dedicated XLR/USB Condenser Mic with noise gate/compressor filter enabled.

### Recording Steps:
1. **Scene 1:** Clean Terminal - Run `install-wizard.py` (00:30 - 01:30)
2. **Scene 2:** Agent CLI - Invoke `/requirements-analysis` (01:30 - 02:30)
3. **Scene 3:** Agent CLI + Editor - Run `/hld-generator`, `/archify`, and `evidence-gate.py` (02:30 - 04:00)
4. **Scene 4:** Terminal + Spec Output - Run `export_to_spec.py` & `export_to_tracker.py` (04:00 - 04:30)

---

## 🚀 Publish-to-Social-Media & Distribution Plan

| Platform | Format | Specific Actions & Call to Action |
| :--- | :--- | :--- |
| **YouTube** | Public Video | Title: *"5-Minute Masterclass: AI-Native Solution Architecture with bank-agent-skills"*. Include timestamped chapters, CC transcript, and link to GitHub. |
| **LinkedIn** | Native Video Upload | Post short teaser (60 sec) + full video attachment. Tag #SolutionArchitecture #Fintech #EnterpriseArchitecture #AIEngineering. |
| **GitHub README.md** | Embedded Badge/Video | Embed YouTube thumbnail / preview link directly under the Bird's-Eye View section in `README.md`. |
| **Reddit** | Text Post + Link | Post step-by-step guide to r/CloudArchitect, r/devops, and r/programming titled *"How we automated CBUAE/DORA compliance checks and HLD generation using AI agents"*. |
