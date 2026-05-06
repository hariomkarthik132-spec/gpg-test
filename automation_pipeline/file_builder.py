"""Write ready-to-edit automation starter files to disk."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

from .engine import AutomationEngine, PipelinePlan


class StarterFileBuilder:
    """Create concrete files from a generated automation pipeline plan."""

    def __init__(self, engine: AutomationEngine | None = None) -> None:
        self.engine = engine or AutomationEngine()

    def write_files(self, output_dir: str | Path, goal: str, extra_tools: Iterable[str] | None = None) -> tuple[Path, ...]:
        """Write prompts, task board, checklist script, and README files.

        Existing files are overwritten so the command can be re-run after changing
        the goal. The generated files contain placeholders for secrets and manual
        approvals instead of executing online actions automatically.
        """
        plan = self.engine.build_plan(goal, extra_tools=extra_tools)
        root = Path(output_dir)
        files = {
            root / "README_AUTOMATION.md": self._readme(plan),
            root / "prompts" / "system_prompt.txt": plan.system_prompt + "\n",
            root / "prompts" / "pipeline_prompt.txt": plan.builder_prompt + "\n",
            root / "prompts" / "idea_prompt.txt": self.engine.idea_prompt(plan.goal) + "\n",
            root / "tasks" / "task_board.json": self._task_board(plan),
            root / "scripts" / "run_checklist.py": self._checklist_script(),
        }
        written: list[Path] = []
        for path, content in files.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
            written.append(path)
        return tuple(written)

    def _readme(self, plan: PipelinePlan) -> str:
        steps = "\n".join(
            f"{index}. **{step.name}** — {step.purpose}\n"
            f"   - Tools: {', '.join(step.tools)}\n"
            f"   - Checkpoint: {step.checkpoint}"
            for index, step in enumerate(plan.steps, start=1)
        )
        tools = "\n".join(f"- {tool}" for tool in plan.install_suggestions)
        safety = "\n".join(f"- {rule}" for rule in plan.safety_rules)
        ideas = "\n".join(f"- {idea}" for idea in plan.ideas)
        return f"""# Ready Automation Pipeline Files

Goal: **{plan.goal}**

Language mode: **{plan.language}**

## Chain

{steps}

## Suggested tools to install manually

{tools}

## New ideas

{ideas}

## Safety rules

{safety}

## How to use these files

1. Edit `prompts/system_prompt.txt` and `prompts/pipeline_prompt.txt` for your exact agent.
2. Fill `tasks/task_board.json` with target websites, APIs, and human approval notes.
3. Run `python scripts/run_checklist.py` from this folder to print the safe execution checklist.
4. Add real browser/API code only after confirming you own the account or have permission.
"""

    def _task_board(self, plan: PipelinePlan) -> str:
        payload = {
            "goal": plan.goal,
            "language": plan.language,
            "status_values": ["todo", "running", "blocked", "needs_human_approval", "done"],
            "tasks": [
                {
                    "id": f"step-{index}",
                    "title": step.name,
                    "purpose": step.purpose,
                    "tools": list(step.tools),
                    "checkpoint": step.checkpoint,
                    "status": "todo",
                    "human_approval_required": index in {1, 3, 4, 5},
                }
                for index, step in enumerate(plan.steps, start=1)
            ],
            "secrets": {
                "storage": "Use environment variables or a secret manager only.",
                "example_env_names": ["OPENAI_API_KEY", "DEEPSEEK_API_KEY", "BROWSER_PROFILE_PATH"],
            },
            "blocked_actions": [
                "bypass CAPTCHA/login/paywall/security controls",
                "spam or mass-message people without consent",
                "purchase/publish/delete/install without human confirmation",
            ],
        }
        return json.dumps(payload, indent=2, ensure_ascii=False) + "\n"

    def _checklist_script(self) -> str:
        return r'''#!/usr/bin/env python3
"""Print a safe execution checklist for this generated automation folder."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TASK_BOARD = ROOT / "tasks" / "task_board.json"


def main() -> None:
    board = json.loads(TASK_BOARD.read_text(encoding="utf-8"))
    print(f"Goal: {board['goal']}")
    print("\nSafe execution checklist:")
    for task in board["tasks"]:
        approval = "YES" if task["human_approval_required"] else "NO"
        print(f"- [{task['status']}] {task['id']}: {task['title']} | approval: {approval}")
        print(f"  checkpoint: {task['checkpoint']}")
    print("\nBlocked actions:")
    for action in board["blocked_actions"]:
        print(f"- {action}")


if __name__ == "__main__":
    main()
'''
