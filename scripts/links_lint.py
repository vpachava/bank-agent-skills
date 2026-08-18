
import re
import os
import sys

def check_links(directory):
    errors = []
    # Regex for [text](path)
    std_link_re = re.compile(r'\[.*?\]\((?!http)(.*?)\)')

    for root, _, files in os.walk(directory):
        for file in files:
            if not file.endswith('.md'):
                continue

            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            for match in std_link_re.finditer(content):
                link = match.group(1).split('#')[0] # ignore anchor
                if not link: continue

                # Resolve relative to current file
                target = os.path.normpath(os.path.join(root, link))
                if not os.path.exists(target):
                    errors.append(f"{file_path}: Broken link to {link}")

    return errors

if __name__ == "__main__":
    results = check_links('.')
    if results:
        for err in results: print(err)
        sys.exit(1)
    else:
        print("All internal links valid.")
        sys.exit(0)
