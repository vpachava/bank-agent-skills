# State-Awareness & Stale-Design Detection Plan

Goal: Implement a mechanism to track design artifacts and flag staleness when foundational dependencies or regulatory policies change.

## Architecture
- Develop `governance/scripts/staleness-detector.py` that scans for aging metadata/artifact links.
- Integrity: Utilize artifact_id and last-updated metadata.
- Compliance: Flag designs that rely on pre-centralized regulatory references.

## Tech Stack
- Python (CLI)
- Git (commit history for staleness)
- JSON/YAML parsing

## Tasks

- [ ] Task 1: Initialize metadata crawler for artifact tracking.
- [ ] Task 2: Implement timestamp decay calculation logic.
- [ ] Task 3: Flag assets using legacy regulatory references.
- [ ] Task 4: Integrate with CI release-gate.

---

## Global Constraints

- Consistency: Matches handoff metadata from existing artifacts.
- Automation: Skips manual review where auto-detect is possible.
- Scope: Only architectural artifacts (C4, HLDs, etc).

---

### Task 1: Initialize metadata crawler

**Files:**
- Create: `governance/scripts/staleness-detector.py`

**Interfaces:**
- Input: Repo root path
- Produces: Hash of all metadata artifacts.

- [ ] Step 1: Write crawler that identifies all files matching handoff.schema.json.
- [ ] Step 2: Commit.

### Task 2: Implement timestamp decay logic

**Files:**
- Modify: `governance/scripts/staleness-detector.py`

**Interfaces:**
- Produces: Delta between current date and handoff timestamp.

- [ ] Step 1: Write decay function (threshold = 30 days).
- [ ] Step 2: Commit.

### Task 3: Legacy Policy Check

**Files:**
- Modify: `governance/scripts/staleness-detector.py`

**Interfaces:**
- Consumes: `governance/policy/regulations.yaml`

- [ ] Step 1: Add check for legacy CBUAE/PDPL/PCI-DSS string occurrences in detected files.
- [ ] Step 2: Commit.

### Task 4: CI Integration

**Files:**
- Modify: `.github/workflows/governance.yaml` (assuming existence)

**Interfaces:**
- Consumes: `governance/scripts/staleness-detector.py`

- [ ] Step 1: Add check stage.
- [ ] Step 2: Commit.
