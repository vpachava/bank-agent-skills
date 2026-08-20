import json
import os
import sys

def get_handoff_files(root_dir):
    handoffs = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file == "handoff.json":
                handoffs.append(os.path.join(root, file))
    return handoffs

def run_crawler(root_dir):
    files = get_handoff_files(root_dir)
    print(json.dumps(files))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    run_crawler(sys.argv[1])
