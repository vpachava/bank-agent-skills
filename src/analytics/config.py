import os

LOG_PATH = os.getenv("ANALYTICS_LOG_PATH", "/var/log/bank-agent/analytics.json")
SAMPLING_RATE = float(os.getenv("ANALYTICS_SAMPLING_RATE", "1.0"))
