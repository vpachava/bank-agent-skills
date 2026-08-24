import json
import pytest
from pathlib import Path

def test_sample_skill_execution(tmp_path):
    input_file = Path(__file__).parent / "example-input.json"
    assert input_file.exists()
    
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    assert "requirement" in data
    assert data["jurisdiction"] == "UAE"
