"""Core planning engine for a safe automation pipeline."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable

from .prompts import IDEA_PROMPT, PIPELINE_PROMPT, SYSTEM_PROMPT


@dataclass(frozen=True)
class PipelineStep:
    """One stage in the automation chain."""

    name: str
    purpose: str
    tools: tuple[str, ...]
    checkpoint: str


@dataclass(frozen=True)
class PipelinePlan:
    """Complete automation plan returned by the engine."""

    goal: str
    language: str
    system_prompt: str
    builder_prompt: str
    steps: tuple[PipelineStep, ...]
    ideas: tuple[str, ...]
    safety_rules: tuple[str, ...]
    install_suggestions: tuple[str, ...] = field(default_factory=tuple)


class AutomationEngine:
    """Generate bilingual automation chains, prompts, and tool suggestions.

    The engine intentionally plans tasks and produces safe execution checklists;
    it does not bypass third-party website protections or act inside accounts
    without a human-controlled browser/session.
    """

    DEFAULT_SAFETY_RULES = (
        "Use only accounts, data, and websites you own or have permission to automate.",
        "Keep a human approval checkpoint before purchases, messages, uploads, installs, or destructive actions.",
        "Respect robots.txt, terms of service, CAPTCHAs, rate limits, and privacy laws.",
        "Store API keys in environment variables or a secret manager, never in code.",
    )

    def detect_language(self, text: str) -> str:
        """Detect whether the user likely wants Hindi, English, or mixed output."""
        lowered = text.lower()
        hindi_markers = {"mujhe", "chaiye", "bana", "kare", "hindi", "samjhe", "suno", "bhe"}
        english_markers = {"automation", "pipeline", "code", "prompt", "website", "task", "tools"}
        has_hindi = any(marker in lowered for marker in hindi_markers) or any("\u0900" <= char <= "\u097f" for char in text)
        has_english = any(marker in lowered for marker in english_markers)
        if has_hindi and has_english:
            return "Hindi + English"
        if has_hindi:
            return "Hindi"
        return "English"

    def build_plan(self, goal: str, extra_tools: Iterable[str] | None = None) -> PipelinePlan:
        """Build a practical automation chain for the supplied goal."""
        clean_goal = " ".join(goal.split()) or "Build a safe automation assistant"
        language = self.detect_language(clean_goal)
        requested_tools = tuple(tool.strip() for tool in (extra_tools or ()) if tool.strip())
        steps = (
            PipelineStep(
                name="Intake Brain / Requirement Collector",
                purpose="Samjho user ka goal, required inputs, target websites, login needs, aur success criteria.",
                tools=("structured prompt", "JSON task schema", "human confirmation"),
                checkpoint="User confirms exact task, permissions, and risk level.",
            ),
            PipelineStep(
                name="Planner Brain",
                purpose="Goal ko small tasks, dependencies, deadlines, aur fallback paths me todna.",
                tools=("LLM prompt", "task graph", "priority scoring"),
                checkpoint="Plan has clear steps, owner, and expected output.",
            ),
            PipelineStep(
                name="Tool Router",
                purpose="Har step ke liye best tool choose karna: code, browser, API, files, email, ya manual approval.",
                tools=("Python", "Playwright/Selenium when permitted", "REST APIs", *requested_tools),
                checkpoint="Only approved tools run; secrets are loaded from environment variables.",
            ),
            PipelineStep(
                name="Executor Chain",
                purpose="Local scripts, website actions, API calls, and document generation ko sequence me run karna.",
                tools=("job queue", "retry policy", "logs", "dry-run mode"),
                checkpoint="Each action logs result and stops on unsafe/high-cost operations.",
            ),
            PipelineStep(
                name="Verifier Brain",
                purpose="Output validate karna: screenshots, API response, tests, content quality, aur data accuracy.",
                tools=("unit tests", "HTML report", "manual review"),
                checkpoint="Task complete only after automated checks plus human review for sensitive actions.",
            ),
            PipelineStep(
                name="Learning Loop",
                purpose="Successful runs se reusable templates, prompts, aur tool recipes banana.",
                tools=("run history", "prompt library", "idea backlog"),
                checkpoint="Save only non-sensitive lessons and redact private data.",
            ),
        )
        ideas = self.suggest_ideas(clean_goal)
        install_suggestions = self.suggest_tools(clean_goal)
        return PipelinePlan(
            goal=clean_goal,
            language=language,
            system_prompt=SYSTEM_PROMPT,
            builder_prompt=PIPELINE_PROMPT.format(goal=clean_goal, language=language),
            steps=steps,
            ideas=ideas,
            safety_rules=self.DEFAULT_SAFETY_RULES,
            install_suggestions=install_suggestions,
        )

    def suggest_ideas(self, domain: str) -> tuple[str, ...]:
        """Return implementation ideas tailored to the requested domain."""
        lowered = domain.lower()
        ideas = [
            "Prompt Library: reusable Hindi/English prompts for coding, research, website tasks, and reports.",
            "Task Graph: break a big mission into dependent steps with status: todo, running, blocked, done.",
            "Human Approval Gate: pause before login actions, purchases, messages, installs, or public posts.",
            "Run Report: generate a clean HTML/Markdown report with logs, outputs, links, and next actions.",
        ]
        if any(word in lowered for word in ("website", "site", "web")):
            ideas.append("Website Runner: local web UI with API endpoints for plan generation and safe task tracking.")
            ideas.append("Browser Recipe: Playwright scripts for user-approved clicks, form filling, screenshots, and verification.")
        if any(word in lowered for word in ("code", "developer", "jet", "brain")):
            ideas.append("Coder Chain: generate code, run tests, explain failures, then create a patch summary.")
        if any(word in lowered for word in ("online", "api", "tool")):
            ideas.append("API Connector Hub: adapters for search, docs, spreadsheets, CRMs, and notification services.")
        return tuple(ideas)

    def suggest_tools(self, goal: str) -> tuple[str, ...]:
        """Suggest installable tools without installing them automatically."""
        lowered = goal.lower()
        tools = ["python>=3.10", "git", "pytest"]
        if any(word in lowered for word in ("website", "web", "site", "browser")):
            tools.extend(["playwright", "beautifulsoup4", "httpx"])
        if any(word in lowered for word in ("api", "online", "task")):
            tools.extend(["pydantic", "python-dotenv", "tenacity"])
        if any(word in lowered for word in ("ui", "dashboard", "run")):
            tools.extend(["fastapi", "uvicorn"])
        return tuple(dict.fromkeys(tools))

    def idea_prompt(self, domain: str) -> str:
        """Build the standalone idea-generation prompt."""
        return IDEA_PROMPT.format(domain=" ".join(domain.split()) or "automation")
