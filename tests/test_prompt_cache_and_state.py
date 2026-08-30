import sys
from pathlib import Path

scripts_dir = Path(__file__).resolve().parent.parent / "scripts"
if str(scripts_dir) not in sys.path:
    sys.path.insert(0, str(scripts_dir))

import json
import pytest
import importlib.util

# Load modules with hyphens in filenames
def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod

pc_mod = load_module("prompt_cache", scripts_dir / "prompt-cache.py")
cc_mod = load_module("context_compactor", scripts_dir / "context-compactor.py")

def test_prompt_cache(tmp_path):
    skill_name = "/architecture/hld-generator"
    payload = {"project": "payment-gateway", "jurisdiction": "UAE"}
    response = {"status": "SUCCESS", "hld_id": "HLD-101"}

    pc_mod.set_cached_response(skill_name, payload, response, ttl=3600)
    cached = pc_mod.get_cached_response(skill_name, payload)
    assert cached is not None
    assert cached["hld_id"] == "HLD-101"

def test_context_compactor():
    transcript = [{"turn": i, "content": f"Message {i}"} for i in range(15)]
    summary = cc_mod.compact_context(transcript)
    assert summary["original_turn_count"] == 15
    assert len(summary["active_turns"]) == 4
