import json
import tempfile
import unittest
from pathlib import Path

from automation_pipeline.file_builder import StarterFileBuilder


class StarterFileBuilderTest(unittest.TestCase):
    def test_write_files_creates_ready_pipeline_folder(self):
        with tempfile.TemporaryDirectory() as directory:
            written = StarterFileBuilder().write_files(directory, "website code automation", extra_tools=["Playwright"])
            paths = {path.relative_to(directory).as_posix() for path in written}

            self.assertIn("README_AUTOMATION.md", paths)
            self.assertIn("prompts/system_prompt.txt", paths)
            self.assertIn("tasks/task_board.json", paths)
            self.assertIn("scripts/run_checklist.py", paths)

            board = json.loads((Path(directory) / "tasks" / "task_board.json").read_text(encoding="utf-8"))
            self.assertEqual(board["goal"], "website code automation")
            self.assertTrue(any(task["human_approval_required"] for task in board["tasks"]))
            self.assertIn("Playwright", board["tasks"][2]["tools"])


if __name__ == "__main__":
    unittest.main()
