import json
import os
import sys
from pathlib import Path
import tempfile
from datetime import datetime
import functools
import time
import uuid

# Use platform-agnostic temp/log path or configurable env var
LOG_DIR = Path(os.getenv("BANK_AGENT_LOG_DIR", tempfile.gettempdir())) / "bank-agent"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_PATH = LOG_DIR / "analytics.json"

def monitor_skill(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        status = "success"
        try:
            result = func(*args, **kwargs)
            return result
        except Exception:
            status = "failure"
            raise
        finally:
            end_time = time.time()
            duration = (end_time - start_time) * 1000
            event = {
                "skill_name": func.__name__,
                "status": status,
                "duration_ms": duration,
                "correlation_id": str(uuid.uuid4()),
                "timestamp": datetime.now().isoformat()
            }
            with open(LOG_PATH, "a") as f:
                f.write(json.dumps(event) + "\n")
    return wrapper

@monitor_skill
def dummy_skill():
    return "ok"
