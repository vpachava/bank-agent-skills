import json
import yaml
from pathlib import Path
from scripts.export_to_spec import export_specs, generate_openapi_spec, generate_asyncapi_spec

def test_openapi_and_asyncapi_generation(tmp_path):
    design_data = {
        "artifact_id": "HLD-PAYMENTS-001",
        "title": "Payment Core Gateway",
        "version": "1.2.0",
        "region": "UAE",
        "endpoints": [
            {"path": "/v1/transfers", "method": "post", "summary": "Instant transfer", "bian_domain": "PaymentExecution"}
        ]
    }
    
    input_file = tmp_path / "design.json"
    with open(input_file, "w") as f:
        json.dump(design_data, f)
        
    openapi_file, asyncapi_file = export_specs(str(input_file), str(tmp_path))
    
    assert Path(openapi_file).exists()
    assert Path(asyncapi_file).exists()
    
    with open(openapi_file, "r") as f:
        o_data = yaml.safe_load(f)
        assert o_data["openapi"] == "3.1.0"
        assert "OAuth2_FAPI2" in o_data["components"]["securitySchemes"]
        assert "/v1/transfers" in o_data["paths"]
        
    with open(asyncapi_file, "r") as f:
        a_data = yaml.safe_load(f)
        assert a_data["asyncapi"] == "3.0.0"
        assert "paymentEvents" in a_data["channels"]
