import json
import os
import sys
from datetime import datetime

def is_stale(handoff_path, days=30):
    with open(handoff_path, 'r') as f:
        data = json.load(f)

    last_updated = datetime.fromisoformat(data['timestamp'])
    delta = datetime.now() - last_updated
    return delta.days > days, delta.days

def run_crawler(root_dir):
    files = []
    for root, dirs, files_in_dir in os.walk(root_dir):
        for file in files_in_dir:
            if file == "handoff.json":
                path = os.path.join(root, file)
                stale, age = is_stale(path)
                files.append({"path": path, "stale": stale, "age": age})
    print(json.dumps(files))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    run_crawler(sys.argv[1])
