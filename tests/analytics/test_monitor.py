import pytest
import os
import json
from src.analytics.monitor import monitor_skill
from src.analytics.config import LOG_PATH

# Mock log path for testing
os.environ["ANALYTICS_LOG_PATH"] = "test_analytics.json"

@monitor_skill
def dummy_skill():
    return "ok"

def test_monitor_skill_logs_success():
    if os.path.exists("test_analytics.json"):
        os.remove("test_analytics.json")

    dummy_skill()

    assert os.path.exists("test_analytics.json")
    with open("test_analytics.json", "r") as f:
        log = json.loads(f.readline())
        assert log["skill_name"] == "dummy_skill"
        assert log["status"] == "success"

    os.remove("test_analytics.json")
