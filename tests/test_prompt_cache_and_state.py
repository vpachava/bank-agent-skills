import json
import pytest
from pathlib import Path
from scripts.context_compactor import compact_context
from scripts.prompt_cache import get_cached_response, set_cached_response

def test_prompt_cache(tmp_path):
    skill_name = "/architecture/hld-generator"
    payload = {"project": "payment-gateway", "jurisdiction": "UAE"}
    response = {"status": "SUCCESS", "hld_id": "HLD-101"}

    # Set cache
    set_cached_response(skill_name, payload, response, ttl=3600)

    # Get cache
    cached = get_cached_response(skill_name, payload)
    assert cached is not None
    assert cached["hld_id"] == "HLD-101"

def test_context_compactor():
    transcript = [{"turn": i, "content": f"Message {i}"} for i in range(15)]
    summary = compact_context(transcript)
    assert summary["original_turn_count"] == 15
    assert len(summary["active_turns"]) == 4
