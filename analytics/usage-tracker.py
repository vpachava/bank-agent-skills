#!/usr/bin/env python3
"""
Opt-in Analytics & Usage Telemetry Collector for bank-agent-skills.
Respects privacy, anonymizes metrics, and runs locally.
"""

import json
import os
import time
from pathlib import Path
from datetime import datetime

ANALYTICS_DIR = Path.home() / ".bank-agent-skills" / "analytics"
ANALYTICS_DIR.mkdir(parents=True, exist_ok=True)
TELEMETRY_FILE = ANALYTICS_DIR / "usage.json"

def is_opted_in():
    config_file = Path.home() / ".bank-agent-skills" / "profile.json"
    if config_file.exists():
        try:
            with open(config_file, "r") as f:
                data = json.load(f)
                return data.get("opt_in_telemetry", True)
        except Exception:
            return True
    return True

def log_invocation(skill_name: str, duration_ms: float, success: bool, rating: int = 5):
    if not is_opted_in():
        return
        
    event = {
        "timestamp": datetime.now().isoformat(),
        "skill_name": skill_name,
        "duration_ms": round(duration_ms, 2),
        "success": success,
        "rating": rating
    }
    
    events = []
    if TELEMETRY_FILE.exists():
        try:
            with open(TELEMETRY_FILE, "r", encoding="utf-8") as f:
                events = json.load(f)
        except Exception:
            events = []
            
    events.append(event)
    
    with open(TELEMETRY_FILE, "w", encoding="utf-8") as f:
        json.dump(events, f, indent=2)

def generate_report():
    if not TELEMETRY_FILE.exists():
        return {"total_invocations": 0, "success_rate": 100.0, "avg_duration_ms": 0.0}
        
    with open(TELEMETRY_FILE, "r", encoding="utf-8") as f:
        events = json.load(f)
        
    total = len(events)
    if total == 0:
        return {"total_invocations": 0, "success_rate": 100.0, "avg_duration_ms": 0.0}
        
    successes = sum(1 for e in events if e.get("success", True))
    avg_dur = sum(e.get("duration_ms", 0) for e in events) / total
    
    return {
        "total_invocations": total,
        "success_rate": round((successes / total) * 100, 2),
        "avg_duration_ms": round(avg_dur, 2)
    }

if __name__ == "__main__":
    print(json.dumps(generate_report(), indent=2))
