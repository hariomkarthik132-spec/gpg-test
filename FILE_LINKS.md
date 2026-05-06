# File Links

Boss, main files yahan se open karo:

## Ready-made automation files

- [Ready pipeline README](ready_pipeline/README_AUTOMATION.md)
- [System prompt](ready_pipeline/prompts/system_prompt.txt)
- [Pipeline prompt](ready_pipeline/prompts/pipeline_prompt.txt)
- [Idea prompt](ready_pipeline/prompts/idea_prompt.txt)
- [Task board JSON](ready_pipeline/tasks/task_board.json)
- [Checklist script](ready_pipeline/scripts/run_checklist.py)

## Generator source files

- [Automation engine](automation_pipeline/engine.py)
- [CLI runner](automation_pipeline/cli.py)
- [File builder](automation_pipeline/file_builder.py)
- [Local web UI/API](automation_pipeline/web.py)
- [Prompt templates](automation_pipeline/prompts.py)

## Tests

- [Engine tests](tests/test_engine.py)
- [File builder tests](tests/test_file_builder.py)

## Quick commands

```bash
python -m automation_pipeline.cli "website task automation" --tool "Playwright" --write-files my_pipeline
python ready_pipeline/scripts/run_checklist.py
python -m automation_pipeline.web
```
