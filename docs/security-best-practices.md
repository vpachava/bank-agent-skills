# Security Best Practices for Skill Authors

To maintain enterprise-grade reliability and security across the **Global Banking Solution-Architect Skills Library**, all skill authors must adhere to the following security guidelines.

---

## 1. Zero Trust for AI Prompts (Adversarial Defense)
- **Never instruct agents to bypass guardrails:** Avoid any prompt instructions that state *"ignore previous instructions"* or *"disable safety rules"*.
- **Explicit Constraints:** Always constrain skill behavior within strict regulatory and business boundaries (e.g., CBUAE, GDPR, HIPAA).

## 2. Network & File System Auditing
- **No Unsanitized Network Calls:** Skills must not invoke raw curl, unauthenticated HTTP requests, or raw sockets without explicit user consent and mTLS/OAuth2 security envelopes.
- **Evidence-Gating:** All claims regarding infrastructure state must be verified locally using read-only filesystem inspection (`grep`, `ls`, `cat`) rather than trusted memory assertions.

## 3. Credential Protection
- **Never Hardcode Secrets:** API keys, tokens, passwords, and private certificates must never be hardcoded into `SKILL.md` or python helper scripts. Use environment variables (e.g., `os.getenv("API_KEY")`).

## 4. Review Lifecycle
Before any skill is merged into `main`, it must pass:
1. `scripts/security-audit.py` (Automated security scan)
2. `scripts/skills_lint/` (Structure and frontmatter validation)
3. `pytest tests/` (100% passing test suite)
