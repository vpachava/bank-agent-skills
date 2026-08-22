import json
import jsonschema
from jsonschema import validate
import sys

def run_tests():
    with open('./solution-arch-orchestrator/handoff.schema.json', 'r') as f:
        schema = json.load(f)

    # GREEN SCENARIO
    valid_data = {
        "version": "1.0.0",
        "initiative_id": "MOD-8821",
        "current_phase": "discovery",
        "metadata": {
            "generated_by": "gap-analysis-skill",
            "timestamp": "2026-08-18T10:00:00Z"
        },
        "findings": [
            {
                "id": "F-01",
                "domain": "security",
                "description": "Legacy authentication lacks MFA",
                "verifiable_evidence_paths": ["/src/legacy/auth.ts"]
            }
        ],
        "constraints": [
            {
                "type": "regulatory",
                "description": "Must comply with CBUAE data residency",
                "reference": "CBUAE-DR-01"
            }
        ]
    }

    # RED SCENARIO
    invalid_data = {
        "version": "1.0.0",
        "initiative_id": "MOD-8821",
        "current_phase": "unknown-phase", # Should fail enum
        "metadata": {
            "generated_by": "gap-analysis-skill"
        },
        "findings": [],
        "constraints": []
    }

    try:
        validate(instance=valid_data, schema=schema)
        print("GREEN: Valid data passed schema validation.")
    except jsonschema.exceptions.ValidationError as err:
        print(f"Error: GREEN test failed! {err}")
        sys.exit(1)

    try:
        validate(instance=invalid_data, schema=schema)
        print("Error: RED test passed when it should have failed!")
        sys.exit(1)
    except jsonschema.exceptions.ValidationError as err:
        print(f"RED: Invalid data correctly blocked by schema: {err.message}")

    print("All tests passed.")

if __name__ == "__main__":
    run_tests()
