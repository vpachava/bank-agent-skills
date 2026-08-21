import os
import json
from src.analytics.monitor import dummy_skill, LOG_PATH

def test_monitor_skill_logs_success():
    if LOG_PATH.exists():
        LOG_PATH.unlink()

    dummy_skill()

    assert LOG_PATH.exists()
    with open(LOG_PATH, "r") as f:
        line = f.readline()
        event = json.loads(line)
        assert event["skill_name"] == "dummy_skill"
        assert event["status"] == "success"
