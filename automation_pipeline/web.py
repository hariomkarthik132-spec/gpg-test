"""Small dependency-free web app for the automation planner."""

from __future__ import annotations

import json
from dataclasses import asdict
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

from .engine import AutomationEngine

HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Advantage Automation Pipeline</title>
  <style>
    body { font-family: system-ui, sans-serif; margin: 0; background: #0f172a; color: #e2e8f0; }
    main { max-width: 980px; margin: auto; padding: 32px; }
    textarea, input, button { width: 100%; box-sizing: border-box; border-radius: 12px; border: 1px solid #334155; padding: 12px; }
    textarea, input { background: #020617; color: #e2e8f0; margin: 8px 0 16px; }
    button { background: #38bdf8; color: #082f49; font-weight: 800; cursor: pointer; }
    section { background: #111827; border: 1px solid #334155; border-radius: 18px; padding: 20px; margin-top: 18px; }
    .step { border-left: 4px solid #38bdf8; padding-left: 14px; margin: 14px 0; }
    code { color: #7dd3fc; }
  </style>
</head>
<body>
<main>
  <h1>Advantage Automation Pipeline Chain System</h1>
  <p>Hindi + English planner for safe task automation, website workflows, code prompts, tool routing, and approval gates.</p>
  <label for="goal">Goal / Task</label>
  <textarea id="goal" rows="5">Mujhe website task automation, code generation, prompts, aur online task tracking pipeline chahiye.</textarea>
  <label for="tools">Extra tools (comma separated)</label>
  <input id="tools" value="Playwright, DeepSeek API, JetBrains IDE">
  <button onclick="buildPlan()">Build Pipeline</button>
  <section id="result"><p>Enter a goal and click Build Pipeline.</p></section>
</main>
<script>
async function buildPlan() {
  const goal = document.getElementById('goal').value;
  const tools = document.getElementById('tools').value;
  const response = await fetch('/api/plan', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({goal, tools: tools.split(',').map(t => t.trim()).filter(Boolean)})
  });
  const plan = await response.json();
  document.getElementById('result').innerHTML = `
    <h2>${plan.goal}</h2>
    <p><strong>Language:</strong> ${plan.language}</p>
    <h3>System Prompt</h3><pre>${plan.system_prompt}</pre>
    <h3>Chain</h3>${plan.steps.map((s, i) => `<div class="step"><h4>${i + 1}. ${s.name}</h4><p>${s.purpose}</p><p><strong>Tools:</strong> ${s.tools.join(', ')}</p><p><strong>Checkpoint:</strong> ${s.checkpoint}</p></div>`).join('')}
    <h3>Ideas</h3><ul>${plan.ideas.map(i => `<li>${i}</li>`).join('')}</ul>
    <h3>Suggested installs</h3><p><code>${plan.install_suggestions.join(' ')}</code></p>
    <h3>Safety</h3><ul>${plan.safety_rules.map(r => `<li>${r}</li>`).join('')}</ul>`;
}
</script>
</body>
</html>
"""


class PlannerHandler(BaseHTTPRequestHandler):
    """HTTP handler for the planner UI and JSON API."""

    engine = AutomationEngine()

    def _send_json(self, payload: dict, status: int = 200) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:  # noqa: N802 - required by BaseHTTPRequestHandler
        parsed = urlparse(self.path)
        if parsed.path == "/api/plan":
            query = parse_qs(parsed.query)
            goal = query.get("goal", ["Build a safe automation pipeline"])[0]
            plan = self.engine.build_plan(goal)
            self._send_json(asdict(plan))
            return
        body = HTML.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self) -> None:  # noqa: N802 - required by BaseHTTPRequestHandler
        if urlparse(self.path).path != "/api/plan":
            self._send_json({"error": "not found"}, status=404)
            return
        length = int(self.headers.get("Content-Length", "0"))
        raw_body = self.rfile.read(length).decode("utf-8") if length else "{}"
        try:
            payload = json.loads(raw_body)
        except json.JSONDecodeError:
            self._send_json({"error": "invalid JSON"}, status=400)
            return
        plan = self.engine.build_plan(str(payload.get("goal", "")), extra_tools=payload.get("tools", []))
        self._send_json(asdict(plan))


def run(host: str = "127.0.0.1", port: int = 8000) -> None:
    """Run the local web application."""
    server = ThreadingHTTPServer((host, port), PlannerHandler)
    print(f"Advantage Automation Pipeline running at http://{host}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    run()
