# Evidence Gate Logic Implementation Plan

Goal: Implement programmatically verifiable evidence gating for architectural artifacts.

## Architecture
- Develop `governance/scripts/evidence-gate.py` that ingests JSON handoff artifacts and validates linked assets against repo filesystem.
- Integrity: Verify artifact_id matches the generated manifest.
- Compliance: Fail on missing or inaccessible evidence links.

## Tech Stack
- Python (CLI tool)
- JSON Schema validation
- Path/IO checks

## Tasks

- [ ] Task 1: Create verification script shell
- [ ] Task 2: Implement evidence path validation
- [ ] Task 3: Implement resource pattern grep
- [ ] Task 4: Integrate with handoff schema validation

---

## Global Constraints

- Fail fast: Any missing file or empty evidence array auto-fails.
- Tool-First: Use existing repo tools (`Read`, `Bash`) where possible instead of custom logic.
- Schema: All inputs must conform to `schemas/handoff.schema.json`.
- Consistency: Audit all links in `artifact_id` manifest.

---

### Task 1: Create verification script shell

**Files:**
- Create: `governance/scripts/evidence-gate.py`

**Interfaces:**
- Input: path/to/handoff.json
- Output: Exit code 0 (Pass), 1 (Fail) + STDERR error

- [ ] Step 1: Write boiler-plate script for parsing JSON handoff.
- [ ] Step 2: Validate existance of evidence_links array.
- [ ] Step 3: Implement basic exit codes.
- [ ] Step 4: Commit.

### Task 2: Implement evidence path validation

**Files:**
- Modify: `governance/scripts/evidence-gate.py`

**Interfaces:**
- Produces: Boolean path accessibility checks.

- [ ] Step 1: Add path existence checking loop.
- [ ] Step 2: Implement logging for check results.
- [ ] Step 3: Commit.

### Task 3: Implement resource pattern grep

**Files:**
- Modify: `governance/scripts/evidence-gate.py`

**Interfaces:**
- Produces: Content validation for security/infra files.

- [ ] Step 1: Add grep logic for IaC files.
- [ ] Step 2: Integrate with check loop.
- [ ] Step 3: Commit.

### Task 4: Integrate with handoff schema validation

**Files:**
- Modify: `governance/scripts/evidence-gate.py`

**Interfaces:**
- Consumes: `schemas/handoff.schema.json`

- [ ] Step 1: Add JSON schema validation step.
- [ ] Step 2: Commit.
