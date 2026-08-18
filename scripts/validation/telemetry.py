import json
import datetime
import os

LOG_FILE = "validation-logs.json"

def log_skill_usage(skill_name, success, duration, feedback=None):
    entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "skill": skill_name,
        "success": success,
        "duration": duration,
        "feedback": feedback
    }

    data = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []

    data.append(entry)

    with open(LOG_FILE, 'w') as f:
        json.dump(data, f, indent=2)

print("Telemetry logger infrastructure ready.")
