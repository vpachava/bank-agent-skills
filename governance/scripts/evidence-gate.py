import json
import sys
import os
import subprocess
from jsonschema import validate, ValidationError

def validate_handoff(handoff_path):
    if not os.path.exists(handoff_path):
        print(f"Error: {handoff_path} not found.")
        sys.exit(1)

    with open('../schemas/handoff.schema.json', 'r') as f:
        schema = json.load(f)

    with open(handoff_path, 'r') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print(f"Error: {handoff_path} is not valid JSON.")
            sys.exit(1)

    # Schema validation
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        print(f"Schema Validation Error: {e.message}")
        sys.exit(1)

    # Path and Content validation
    for link in data["evidence_links"]:
        path = link.get("path")
        if not os.path.exists(path):
            print(f"Error: Evidence path inaccessible: {path}")
            sys.exit(1)

        # Resource Pattern Grep for IaC/Security files
        if link["type"] in ["iac", "config"]:
            result = subprocess.run(["grep", "-q", "resource", path], capture_output=True)
            if result.returncode != 0:
                print(f"Error: IaC resource definition not found in {path}")
                sys.exit(1)

    print("Evidence gate validation passed.")
    sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: evidence-gate.py <handoff.json>")
        sys.exit(1)
    validate_handoff(sys.argv[1])
