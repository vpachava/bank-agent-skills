import json
import argparse
from pathlib import Path

# Mapping BIAN domains to Mermaid shapes
BIAN_SHAPE_MAP = {
    "Integration.API": "rectangle",
    "Security.Auth": "database",
    "Customer Account.Origination": "stadium",
    "Integration.Migration": "parallelogram"
}

def generate_mermaid(design_data):
    """Generates a Mermaid C4-style diagram from design.json."""
    lines = ["graph TD"]
    
    # Process Containers
    containers = design_data.get("containers", [])
    for c in containers:
        name = c.get("name", "Unknown").replace(" ", "_")
        domain = c.get("bian_domain", "CoreBanking.Generic")
        shape = BIAN_SHAPE_MAP.get(domain, "rectangle")
        
        # Mermaid shape syntax (e.g., id[label])
        if shape == "database":
            lines.append(f"    {name}[(database: {c.get('name')})]")
        elif shape == "stadium":
            lines.append(f"    {name}({c.get('name')})")
        else:
            lines.append(f"    {name}[{c.get('name')}]")

    # Process Relationships
    flows = design_data.get("key_flows", [])
    for f in flows:
        source = f.get("source", "").replace(" ", "_")
        target = f.get("target", "").replace(" ", "_")
        desc = f.get("description", "")
        lines.append(f"    {source} -->|{desc}| {target}")
        
    return "\n".join(lines)

def archify(input_path, output_path):
    path = Path(input_path)
    with open(path, 'r') as f:
        design = json.load(f)
    
    mermaid_code = generate_mermaid(design)
    
    if output_path:
        with open(output_path, 'w') as f:
            f.write(mermaid_code)
    return mermaid_code

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Path to design.json")
    parser.add_argument("-o", "--output", help="Path to output .mmd file")
    args = parser.parse_args()
    
    print(archify(args.input, args.output))
