#!/usr/bin/env python3
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
