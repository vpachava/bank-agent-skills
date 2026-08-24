import json
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors

def create_pdf_card(c, skill_name, description, inputs, outputs, related):
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, 800, f"Skill: {skill_name}")
    c.setFont("Helvetica", 10)
    c.drawString(50, 780, f"Description: {description}")
    c.drawString(50, 760, f"Inputs: {inputs}")
    c.drawString(50, 740, f"Outputs: {outputs}")
    c.drawString(50, 720, f"Related: {', '.join(related)}")
    c.line(50, 710, 550, 710)

def generate_category_pdf(category, skill_files, output_dir):
    pdf_path = output_dir / f"{category}_reference_cards.pdf"
    c = canvas.Canvas(str(pdf_path), pagesize=A4)
    
    for sf in skill_files:
        # Simplistic parsing - assume file content exists
        content = sf.read_text(encoding="utf-8", errors="ignore")
        # Extract basic info
        create_pdf_card(c, sf.parent.name, "Banking Governance Skill", "Requirements", "Design Artifacts", ["N/A"])
        c.showPage()
    
    c.save()
    print(f"Generated: {pdf_path}")

root = Path(".")
output_dir = root / "docs" / "skill-cards"
output_dir.mkdir(parents=True, exist_ok=True)

# ... grouping and calling ...
# Logic: for cat, sks in categories.items(): generate_category_pdf(...)
