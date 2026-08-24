import os
import json
import pathlib

root = pathlib.Path(".")
skills = list(root.rglob("SKILL.md"))

categories = {}
for s in skills:
    rel = s.relative_to(root)
    cat = rel.parts[0]
    if cat not in categories:
        categories[cat] = []
    categories[cat].append(s)

print(f"Total categories: {len(categories)}")
for cat, sk_list in sorted(categories.items()):
    print(f" - {cat}: {len(sk_list)} skills")
