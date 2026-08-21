import json
from governance.scripts.archify import generate_mermaid

def test_mermaid_generation():
    design = {
        "containers": [
            {"name": "Payment Hub", "bian_domain": "Integration.API"},
            {"name": "Ledger DB", "bian_domain": "Security.Auth"}
        ],
        "key_flows": [
            {"source": "Payment Hub", "target": "Ledger DB", "description": "WriteTx"}
        ]
    }
    
    code = generate_mermaid(design)
    assert "graph TD" in code
    assert "Payment_Hub" in code
    assert "Ledger_DB" in code
    assert "WriteTx" in code
