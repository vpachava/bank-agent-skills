import time
import uuid
import json
import functools
from src.analytics.config import LOG_PATH

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
                "correlation_id": str(uuid.uuid4())
            }
            with open(LOG_PATH, "a") as f:
                f.write(json.dumps(event) + "\n")
    return wrapper
