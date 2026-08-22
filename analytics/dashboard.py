#!/usr/bin/env python3
"""
Local Web Dashboard for bank-agent-skills Analytics & Quality Scoring.
Runs via standard Python http.server or Flask if installed.
"""

import json
from pathlib import Path
from http.server import HTTPServer, BaseHTTPRequestHandler

ANALYTICS_DIR = Path.home() / ".bank-agent-skills" / "analytics"
TELEMETRY_FILE = ANALYTICS_DIR / "usage.json"

class DashboardHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/dashboard":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            
            data = {"total_invocations": 0, "success_rate": 100.0, "avg_duration_ms": 0.0}
            if TELEMETRY_FILE.exists():
                try:
                    with open(TELEMETRY_FILE, "r", encoding="utf-8") as f:
                        events = json.load(f)
                        if events:
                            successes = sum(1 for e in events if e.get("success", True))
                            data = {
                                "total_invocations": len(events),
                                "success_rate": round((successes / len(events)) * 100, 2),
                                "avg_duration_ms": round(sum(e.get("duration_ms", 0) for e in events) / len(events), 2)
                            }
                except Exception:
                    pass
                    
            html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>bank-agent-skills Analytics Dashboard</title>
                <style>
                    body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #0d1117; color: #c9d1d9; padding: 40px; }}
                    .card {{ background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 24px; margin-bottom: 20px; max-width: 600px; box-shadow: 0 4px 12px rgba(0,0,0,0.3); }}
                    h1 {{ color: #58a6ff; font-size: 24px; }}
                    .metric {{ font-size: 32px; font-weight: bold; color: #39d353; margin-top: 10px; }}
                </style>
            </head>
            <body>
                <h1>Global Banking Architecture Engine - Analytics Dashboard</h1>
                <div class="card">
                    <h3>Total Skill Invocations</h3>
                    <div class="metric">{data['total_invocations']}</div>
                </div>
                <div class="card">
                    <h3>Success Rate</h3>
                    <div class="metric">{data['success_rate']}%</div>
                </div>
                <div class="card">
                    <h3>Average Execution Duration</h3>
                    <div class="metric">{data['avg_duration_ms']} ms</div>
                </div>
            </body>
            </html>
            """
            self.wfile.write(html.encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

def run_server(port=8080):
    server_address = ('', port)
    httpd = HTTPServer(server_address, DashboardHandler)
    print(f"[+] Analytics Dashboard running at http://localhost:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
