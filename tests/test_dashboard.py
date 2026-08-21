import json
from pathlib import Path
from governance.scripts.generate_dashboard import generate_dashboard

def test_generate_dashboard():
    # Execute dashboard generation
    dashboard = generate_dashboard()
    
    assert "report_time" in dashboard
    assert "risk_summary" in dashboard
    assert "staleness" in dashboard
    assert isinstance(dashboard["risk_summary"]["total_risks"], int)
    assert isinstance(dashboard["staleness"]["total_artifacts"], int)
    
    script_path = Path(__file__).resolve()
    skills_root = script_path.parents[1]
    output_path = skills_root / "governance" / "dashboard.json"
    
    assert output_path.exists()
