import yaml
import sys
from pathlib import Path

def validate_workflow(workflow_file):
    with open(workflow_file, 'r') as f:
        workflow = yaml.safe_load(f)
    
    available_artifacts = set()
    # Assuming initial project state has these base inputs
    available_artifacts.add('Requirements_Baseline')
    
    for step in workflow['sequence']:
        # Check if inputs are available
        for inp in step.get('inputs', []):
            if inp not in available_artifacts:
                print(f"Error: Missing artifact input '{inp}' for skill '{step['skill_id']}' in {workflow['name']}")
                return False
        
        # Add outputs to available
        for outp in step.get('outputs', []):
            available_artifacts.add(outp)
            
    print(f"Workflow '{workflow['name']}' is valid.")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_workflow.py <workflow.yaml>")
        sys.exit(1)
    
    if not validate_workflow(sys.argv[1]):
        sys.exit(1)
