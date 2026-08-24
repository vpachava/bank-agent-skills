# Contributing to bank-agent-skills

Welcome! We are thrilled that you want to contribute to the **Global Banking Solution-Architect Skills Library**. Whether you are fixing a bug, adding a regional compliance overlay, or contributing a brand-new skill, your help makes this engine better for enterprise architects worldwide.

---

## 📜 Code of Conduct
- Be respectful, welcoming, and inclusive.
- Constructive feedback is encouraged; ad-hominem attacks will not be tolerated.
- Uphold high engineering standards and robust security practices.

---

## 🛠️ How to Contribute a Skill

1. **Fork the Repository:** Fork `vpachava/bank-agent-skills` to your personal GitHub account.
2. **Create a Feature Branch:** `git checkout -b feature/my-new-skill`
3. **Choose the Right Category:** Place your skill inside the appropriate domain directory under root (e.g., `security/`, `integration/`, `architecture/`).
4. **Use the Skill Template:** Follow the `SKILL.md` archetype provided in `skill-template/`.
5. **Write Unit Tests:** Every skill or feature must include a corresponding pytest test under `tests/`.
6. **Submit a Pull Request (PR):** Open a PR against `main`. Our automated CI/CD pipeline will validate your syntax, schema, and test suite.

---

## 📋 Skill Template Structure
Every skill requires a valid YAML frontmatter and standard markdown sections. See `skill-template/SKILL.md` for the exact reference.

---

## 🧪 Testing Requirements
- All contributions must pass the test suite:
  ```bash
  PYTHONPATH=. pytest tests/ -v
  ```
- 100% test pass rate is mandatory for merge approval.

---

## 🚀 Release Cycle
- **Patch Releases:** Weekly (bug fixes and small compliance updates).
- **Minor Releases:** Monthly (new skills, regional overlays, and features).
- **Major Releases:** Quarterly (breaking schema updates, core orchestration refactors).
