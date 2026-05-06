# gpg-test

Termux based toolkit with GPG, encryption, and security features.

## Advantage Automation Pipeline Chain System

This repository now includes a dependency-free Python starter system for a powerful but safe automation workflow. It understands Hindi + English goals, writes reusable prompts, suggests tools, creates new workflow ideas, and can run as a local website.

### What it does

- Builds a step-by-step automation chain from a natural-language goal.
- Produces a system prompt and builder prompt for AI coding/task agents.
- Suggests tools such as Playwright, API clients, FastAPI, and test utilities without installing anything silently.
- Adds safety gates before sensitive actions such as purchases, messages, installs, uploads, destructive actions, or third-party website account activity.
- Runs a local web UI for planning website tasks and online workflows.

### Quick start

Generate a plan in the terminal:

```bash
python -m automation_pipeline.cli "Suno mujhe website task automation, code prompts, aur online workflow pipeline chaiye"
```

Generate JSON for another tool:

```bash
python -m automation_pipeline.cli "code automation website" --tool "DeepSeek API" --tool "JetBrains IDE" --json
```


Create editable starter files in any folder:

```bash
python -m automation_pipeline.cli "website task automation" --tool "Playwright" --write-files my_pipeline
```

A ready-made example is already committed in `ready_pipeline/` with prompts, a JSON task board, and a checklist script. Open [File links](FILE_LINKS.md) for direct links to every important file.

Run the local website:

```bash
python -m automation_pipeline.web
```

Then open <http://127.0.0.1:8000> and enter your automation goal.

### Safe automation policy

The planner is designed for user-owned or permission-based automation. It will not help bypass logins, CAPTCHAs, paywalls, rate limits, website security controls, or terms of service. Keep API keys in environment variables or a secret manager, and use a human approval checkpoint before any high-impact action.

### Suggested next upgrades

1. Add Playwright scripts for approved browser actions and screenshots.
2. Add `.env` loading for API keys.
3. Add a job queue for long-running tasks.
4. Add connectors for search, spreadsheets, email drafts, and project trackers.
5. Add encrypted storage for run logs and secrets using the existing security-toolkit direction.
