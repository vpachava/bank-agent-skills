#!/usr/bin/env python3
"""
Generates HTML printable reference card sheets for each of the 16 skill categories.
These HTML files are clean, color-coded, black-and-white friendly, printable (A4/Letter),
and easily convertible to PDF using standard browser print or tools like WeasyPrint/Puppeteer.
"""

import pathlib
import json
import re

CATEGORY_COLORS = {
    "solution-arch-orchestrator": "#1f6beb",
    "discovery": "#238636",
    "architecture": "#8957e5",
    "business-architecture": "#d29922",
    "data-architecture": "#3fb950",
    "ai-ml-architecture": "#a371f7",
    "modernization": "#da3633",
    "migration": "#f0883e",
    "integration": "#58a6ff",
    "security": "#f85149",
    "cloud": "#388bfd",
    "devops": "#238636",
    "governance": "#f0883e",
    "documentation": "#8b949e",
    "greenfield": "#3fb950",
    "industries": "#a371f7"
}

def parse_skill(skill_file: pathlib.Path) -> dict:
    content = skill_file.read_text(encoding="utf-8", errors="ignore")
    lines = content.splitlines()
    
    name = skill_file.parent.name
    if name == ".":
        name = skill_file.parts[0]
        
    description = ""
    inputs = "User prompt / Context files / Requirements"
    outputs = "Architectural deliverable / Handoff payload / Diagram"
    
    # Parse YAML frontmatter if available
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            fm = parts[1]
            for line in fm.splitlines():
                if line.startswith("description:"):
                    description = line.replace("description:", "").strip().strip('"').strip("'")
                elif line.startswith("expected-deliverables:"):
                    outputs = line.replace("expected-deliverables:", "").strip()

    if not description:
        for line in lines:
            if line.strip() and not line.startswith("#") and not line.startswith("---"):
                description = line.strip()
                break
                
    if not description:
        description = f"Provides automated architecture capabilities for {name}."
        
    return {
        "name": f"/{skill_file.relative_to(pathlib.Path('.')).parent.as_posix()}",
        "short_name": name,
        "description": description[:150] + ("..." if len(description) > 150 else ""),
        "inputs": inputs,
        "outputs": outputs,
        "usage": f"/{name}",
        "category": skill_file.parts[0]
    }

def generate_category_html(category: str, skills: list, output_dir: pathlib.Path):
    color = CATEGORY_COLORS.get(category, "#58a6ff")
    cards_html = ""
    
    for sk in skills:
        cards_html += f"""
        <div class="card">
            <div class="card-header" style="border-left: 5px solid {color};">
                <span class="skill-name">{sk['usage']}</span>
                <span class="category-badge" style="background-color: {color}22; color: {color}; border: 1px solid {color}44;">{category}</span>
            </div>
            <div class="card-body">
                <p class="description"><strong>Description:</strong> {sk['description']}</p>
                <div class="io-grid">
                    <div><strong>Inputs:</strong> {sk['inputs']}</div>
                    <div><strong>Outputs:</strong> {sk['outputs']}</div>
                </div>
                <div class="usage-box">
                    <code>{sk['usage']}</code>
                </div>
            </div>
        </div>
        """
        
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{category.title()} Skill Reference Cards - bank-agent-skills</title>
    <style>
        @page {{ size: A4; margin: 15mm; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background: #fff; color: #1f2328; margin: 0; padding: 20px; }}
        h1 {{ font-size: 20pt; border-bottom: 2px solid {color}; padding-bottom: 5px; color: #0d1117; margin-top: 0; }}
        .header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }}
        .cards-container {{ display: grid; grid-template-columns: 1fr 1fr; gap: 15px; page-break-inside: avoid; }}
        .card {{ border: 1px solid #d0d7de; border-radius: 6px; padding: 12px; background: #f6f8fa; page-break-inside: avoid; }}
        .card-header {{ display: flex; justify-content: space-between; align-items: center; padding-left: 8px; margin-bottom: 8px; }}
        .skill-name {{ font-weight: bold; font-size: 11pt; font-family: monospace; color: #0969da; }}
        .category-badge {{ font-size: 8pt; padding: 2px 6px; border-radius: 12px; text-transform: uppercase; font-weight: bold; }}
        .description {{ font-size: 9pt; color: #57606a; margin: 4px 0 8px 0; }}
        .io-grid {{ font-size: 8pt; color: #24292f; margin-bottom: 8px; background: #fff; padding: 6px; border-radius: 4px; border: 1px solid #e1e4e8; }}
        .usage-box {{ background: #24292f; color: #f6f8fa; padding: 4px 8px; border-radius: 4px; font-size: 9pt; font-family: monospace; display: inline-block; }}
        .footer {{ margin-top: 30px; font-size: 8pt; color: #8c959f; text-align: center; border-top: 1px solid #d0d7de; padding-top: 10px; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>bank-agent-skills: {category.title()}</h1>
        <div>Category Reference Cards (v1.0.1)</div>
    </div>
    <div class="cards-container">
        {cards_html}
    </div>
    <div class="footer">
        Global Banking Solution-Architect Skills Library | https://github.com/vpachava/bank-agent-skills
    </div>
</body>
</html>
"""
    out_file = output_dir / f"{category}-reference-cards.html"
    out_file.write_text(html, encoding="utf-8")
    print(f"Generated card sheet: {out_file}")

def generate_explorer_html(all_skills: list, output_dir: pathlib.Path):
    skills_json = json.dumps(all_skills)
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Interactive Skill Explorer - bank-agent-skills</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #0d1117; color: #c9d1d9; margin: 0; padding: 30px; }}
        h1 {{ color: #58a6ff; font-size: 24px; margin-bottom: 5px; }}
        p {{ color: #8b949e; margin-bottom: 25px; }}
        .controls {{ display: flex; gap: 15px; margin-bottom: 25px; flex-wrap: wrap; }}
        input, select {{ background: #161b22; border: 1px solid #30363d; color: #c9d1d9; padding: 10px 14px; border-radius: 6px; font-size: 14px; outline: none; }}
        input {{ flex: 1; min-width: 250px; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 20px; }}
        .card {{ background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 18px; display: flex; flex-direction: column; justify-content: space-between; transition: transform 0.2s; }}
        .card:hover {{ border-color: #58a6ff; transform: translateY(-2px); }}
        .badge {{ background: #1f6beb22; color: #58a6ff; border: 1px solid #1f6beb44; font-size: 11px; padding: 3px 8px; border-radius: 12px; font-weight: bold; width: fit-content; text-transform: uppercase; margin-bottom: 10px; }}
        .title {{ font-size: 16px; font-weight: bold; color: #f0f6fc; font-family: monospace; margin-bottom: 8px; }}
        .desc {{ font-size: 13px; color: #8b949e; line-height: 1.4; margin-bottom: 15px; flex: 1; }}
        .copy-btn {{ background: #238636; color: #fff; border: none; padding: 8px 12px; border-radius: 6px; cursor: pointer; font-size: 12px; font-weight: bold; transition: background 0.2s; }}
        .copy-btn:hover {{ background: #2ea043; }}
    </style>
</head>
<body>
    <h1>Global Banking Solution-Architect Skill Explorer</h1>
    <p>Search and explore 100+ executable AI-native architecture skills across 16 categories.</p>
    
    <div class="controls">
        <input type="text" id="searchInput" placeholder="Search skills by name, description, keyword..." oninput="filterSkills()">
        <select id="categoryFilter" onchange="filterSkills()">
            <option value="all">All Categories (16)</option>
        </select>
    </div>
    
    <div class="grid" id="skillsGrid"></div>

    <script>
        const skills = {skills_json};
        
        // Populate category dropdown
        const categories = [...new Set(skills.map(s => s.category))].sort();
        const catSelect = document.getElementById("categoryFilter");
        categories.forEach(c => {{
            const opt = document.createElement("option");
            opt.value = c;
            opt.textContent = c;
            catSelect.appendChild(opt);
        }});
        
        function renderSkills(items) {{
            const grid = document.getElementById("skillsGrid");
            grid.innerHTML = "";
            items.forEach(s => {{
                const card = document.createElement("div");
                card.className = "card";
                card.innerHTML = `
                    <div>
                        <div class="badge">${{s.category}}</div>
                        <div class="title">${{s.usage}}</div>
                        <div class="desc">${{s.description}}</div>
                    </div>
                    <button class="copy-btn" onclick="copyCommand('${{s.usage}}')">Copy Skill Command</button>
                `;
                grid.appendChild(card);
            }});
        }}
        
        function filterSkills() {{
            const q = document.getElementById("searchInput").value.toLowerCase();
            const cat = document.getElementById("categoryFilter").value;
            
            const filtered = skills.filter(s => {{
                const matchesQ = s.name.toLowerCase().includes(q) || s.description.toLowerCase().includes(q) || s.category.toLowerCase().includes(q);
                const matchesCat = cat === "all" || s.category === cat;
                return matchesQ && matchesCat;
            }});
            
            renderSkills(filtered);
        }}
        
        function copyCommand(cmd) {{
            navigator.clipboard.writeText(cmd);
            alert("Copied command: " + cmd);
        }}
        
        renderSkills(skills);
    </script>
</body>
</html>
"""
    out_file = output_dir / "skill-explorer.html"
    out_file.write_text(html, encoding="utf-8")
    print(f"Generated interactive skill explorer: {out_file}")

def main():
    root = pathlib.Path(".")
    out_dir = root / "docs" / "skill-cards"
    out_dir.mkdir(parents=True, exist_ok=True)
    
    skill_files = list(root.rglob("SKILL.md"))
    categories = {}
    all_parsed_skills = []
    
    for sf in skill_files:
        rel = sf.relative_to(root)
        cat = rel.parts[0]
        parsed = parse_skill(sf)
        all_parsed_skills.append(parsed)
        
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(parsed)
        
    print(f"Generating printable reference card sheets for {len(categories)} categories...")
    for cat, sk_list in categories.items():
        generate_category_html(cat, sk_list, out_dir)
        
    generate_explorer_html(all_parsed_skills, out_dir)
    print("✓ All card sheets and interactive explorer successfully created!")

if __name__ == "__main__":
    main()
