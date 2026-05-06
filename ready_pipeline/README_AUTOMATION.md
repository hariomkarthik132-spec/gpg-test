# Ready Automation Pipeline Files

Goal: **Suno mujhe powerful website task automation, prompts, code aur online workflow pipeline chaiye**

Language mode: **Hindi + English**

## Chain

1. **Intake Brain / Requirement Collector** — Samjho user ka goal, required inputs, target websites, login needs, aur success criteria.
   - Tools: structured prompt, JSON task schema, human confirmation
   - Checkpoint: User confirms exact task, permissions, and risk level.
2. **Planner Brain** — Goal ko small tasks, dependencies, deadlines, aur fallback paths me todna.
   - Tools: LLM prompt, task graph, priority scoring
   - Checkpoint: Plan has clear steps, owner, and expected output.
3. **Tool Router** — Har step ke liye best tool choose karna: code, browser, API, files, email, ya manual approval.
   - Tools: Python, Playwright/Selenium when permitted, REST APIs, Playwright, DeepSeek API, JetBrains IDE
   - Checkpoint: Only approved tools run; secrets are loaded from environment variables.
4. **Executor Chain** — Local scripts, website actions, API calls, and document generation ko sequence me run karna.
   - Tools: job queue, retry policy, logs, dry-run mode
   - Checkpoint: Each action logs result and stops on unsafe/high-cost operations.
5. **Verifier Brain** — Output validate karna: screenshots, API response, tests, content quality, aur data accuracy.
   - Tools: unit tests, HTML report, manual review
   - Checkpoint: Task complete only after automated checks plus human review for sensitive actions.
6. **Learning Loop** — Successful runs se reusable templates, prompts, aur tool recipes banana.
   - Tools: run history, prompt library, idea backlog
   - Checkpoint: Save only non-sensitive lessons and redact private data.

## Suggested tools to install manually

- python>=3.10
- git
- pytest
- playwright
- beautifulsoup4
- httpx
- pydantic
- python-dotenv
- tenacity

## New ideas

- Prompt Library: reusable Hindi/English prompts for coding, research, website tasks, and reports.
- Task Graph: break a big mission into dependent steps with status: todo, running, blocked, done.
- Human Approval Gate: pause before login actions, purchases, messages, installs, or public posts.
- Run Report: generate a clean HTML/Markdown report with logs, outputs, links, and next actions.
- Website Runner: local web UI with API endpoints for plan generation and safe task tracking.
- Browser Recipe: Playwright scripts for user-approved clicks, form filling, screenshots, and verification.
- Coder Chain: generate code, run tests, explain failures, then create a patch summary.
- API Connector Hub: adapters for search, docs, spreadsheets, CRMs, and notification services.

## Safety rules

- Use only accounts, data, and websites you own or have permission to automate.
- Keep a human approval checkpoint before purchases, messages, uploads, installs, or destructive actions.
- Respect robots.txt, terms of service, CAPTCHAs, rate limits, and privacy laws.
- Store API keys in environment variables or a secret manager, never in code.

## How to use these files

1. Edit `prompts/system_prompt.txt` and `prompts/pipeline_prompt.txt` for your exact agent.
2. Fill `tasks/task_board.json` with target websites, APIs, and human approval notes.
3. Run `python scripts/run_checklist.py` from this folder to print the safe execution checklist.
4. Add real browser/API code only after confirming you own the account or have permission.
