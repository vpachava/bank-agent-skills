import json
import pytest

def test_sample_skill():
    sample_input = {
        "project_name": "Test-Project",
        "requirement": "Test requirement"
    }
    assert sample_input["project_name"] == "Test-Project"
    assert "requirement" in sample_input
