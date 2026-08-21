import json
from pathlib import Path
from datetime import datetime

def generate_dashboard():
    # Detect the skills root dynamically based on the location of this script
    script_path = Path(__file__).resolve()
    skills_root = script_path.parents[2] # Go up from governance/scripts/generate_dashboard.py to skills/
    
    raid_log = skills_root / "governance" / "raid-log.json"
    
    # 1. RAID Analysis
    risks = []
    if raid_log.exists():
        try:
            with open(raid_log, 'r', encoding='utf-8') as f:
                raid_data = json.load(f)
                risks = raid_data.get("raid_items", [])
        except Exception as e:
            print(f"Warning: Failed to load raid-log.json: {e}")
            
    # 2. Staleness Tracking (Scan for handoff.json files)
    stale_count = 0
    total_artifacts = 0
    for path in skills_root.rglob("handoff.json"):
        total_artifacts += 1
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # Simple 30-day stale check
                ts_str = data.get('timestamp', '').replace('Z', '')
                if ts_str:
                    ts = datetime.fromisoformat(ts_str)
                    if (datetime.now() - ts).days > 30:
                        stale_count += 1
        except Exception as e:
            print(f"Warning: Failed to parse handoff.json at {path}: {e}")
                
    dashboard = {
        "report_time": datetime.now().isoformat(),
        "risk_summary": {
            "total_risks": len(risks),
            "high_severity": len([r for r in risks if r.get('severity', 0) > 7])
        },
        "staleness": {
            "total_artifacts": total_artifacts,
            "stale_artifacts": stale_count,
            "health_score": round(((total_artifacts - stale_count) / total_artifacts * 100) if total_artifacts > 0 else 100, 2)
        }
    }
    
    output_path = skills_root / "governance" / "dashboard.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(dashboard, f, indent=4)
        
    return dashboard

if __name__ == "__main__":
    print(json.dumps(generate_dashboard(), indent=2))
