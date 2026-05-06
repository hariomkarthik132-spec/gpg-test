"""Command-line interface for the automation planner."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict

from .engine import AutomationEngine
from .file_builder import StarterFileBuilder


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a safe Hindi/English automation pipeline plan.")
    parser.add_argument("goal", nargs="*", help="Automation goal, e.g. 'website task automation with approval gates'.")
    parser.add_argument("--tool", action="append", default=[], help="Extra tool you want to include in the plan.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    parser.add_argument("--write-files", metavar="DIR", help="Write ready-to-edit automation files into DIR.")
    args = parser.parse_args()

    engine = AutomationEngine()
    plan = engine.build_plan(" ".join(args.goal), extra_tools=args.tool)

    if args.write_files:
        written = StarterFileBuilder(engine).write_files(args.write_files, plan.goal, extra_tools=args.tool)
        print("Wrote automation starter files:")
        for path in written:
            print(f"- {path}")
        return

    if args.json:
        print(json.dumps(asdict(plan), indent=2, ensure_ascii=False))
        return

    print(f"Goal: {plan.goal}")
    print(f"Language: {plan.language}")
    print("\nSystem Prompt:\n" + plan.system_prompt)
    print("\nAutomation Chain:")
    for index, step in enumerate(plan.steps, start=1):
        print(f"{index}. {step.name}: {step.purpose}")
        print(f"   Tools: {', '.join(step.tools)}")
        print(f"   Checkpoint: {step.checkpoint}")
    print("\nNew Ideas:")
    for idea in plan.ideas:
        print(f"- {idea}")
    print("\nSuggested Tools:")
    for tool in plan.install_suggestions:
        print(f"- {tool}")
    print("\nSafety Rules:")
    for rule in plan.safety_rules:
        print(f"- {rule}")


if __name__ == "__main__":
    main()
