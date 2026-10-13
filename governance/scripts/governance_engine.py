#!/usr/bin/env python3
"""
Governance Engine Adapter — Unified Compliance & Audit Verification Module.
Provides a deep module interface combining Evidence Gate validation, Staleness detection, 
and Dashboard generation into a single callable API and CLI command.
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime

class GovernanceEngine:
    def __init__(self, repo_root: str = None):
        self.repo_root = Path(repo_root).resolve() if repo_root else Path(__file__).parents[2]
        self.governance_dir = self.repo_root / "governance"

    def run_evidence_gate(self, handoff_path: str = None) -> dict:
        """Runs evidence verification checks against handoff JSON schemas and evidence paths."""
        results = {"status": "success", "errors": [], "checked_artifacts": 0}
        
        # Scan for handoff files if none specified
        handoffs = [Path(handoff_path)] if handoff_path else list(self.repo_root.rglob("handoff.json"))
        
        for h_path in handoffs:
            results["checked_artifacts"] += 1
            if not h_path.exists():
                results["errors"].append(f"Handoff not found: {h_path}")
                continue
            try:
                with open(h_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                # Check evidence links
                for link in data.get("evidence_links", []):
                    link_path = self.repo_root / link.get("path", "")
                    if not link_path.exists():
                        results["errors"].append(f"Evidence path inaccessible: {link_path}")
            except Exception as e:
                results["errors"].append(f"Failed to parse {h_path}: {e}")

        if results["errors"]:
            results["status"] = "failed"
        return results

    def run_staleness_check(self, days: int = 30) -> dict:
        """Scans for stale artifacts exceeding the threshold."""
        stale_items = []
        total_checked = 0
        
        for path in self.repo_root.rglob("handoff.json"):
            total_checked += 1
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                ts_str = data.get('timestamp', '').replace('Z', '')
                if ts_str:
                    ts = datetime.fromisoformat(ts_str)
                    delta = (datetime.now() - ts).days
                    if delta > days:
                        stale_items.append({"path": str(path), "age_days": delta})
            except Exception:
                pass
                
        return {
            "total_checked": total_checked,
            "stale_count": len(stale_items),
            "stale_items": stale_items
        }

    def execute_unified_audit(self) -> dict:
        """Deep module entry point executing all governance checks and returning a compliance vector."""
        evidence_res = self.run_evidence_gate()
        staleness_res = self.run_staleness_check()
        
        unified_report = {
            "timestamp": datetime.now().isoformat(),
            "repository": str(self.repo_root),
            "evidence_gate": evidence_res,
            "staleness_audit": staleness_res,
            "overall_status": "PASS" if evidence_res["status"] == "success" else "FAIL"
        }
        
        return unified_report

if __name__ == "__main__":
    engine = GovernanceEngine()
    report = engine.execute_unified_audit()
    print(json.dumps(report, indent=2))
    sys.exit(0 if report["overall_status"] == "PASS" else 1)
