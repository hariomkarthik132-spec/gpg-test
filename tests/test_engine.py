import json
import subprocess
import sys
import unittest

from automation_pipeline import AutomationEngine


class AutomationEngineTest(unittest.TestCase):
    def test_build_plan_is_bilingual_and_safe(self):
        plan = AutomationEngine().build_plan("Suno mujhe website automation pipeline chaiye", extra_tools=["DeepSeek API"])

        self.assertEqual(plan.language, "Hindi + English")
        self.assertGreaterEqual(len(plan.steps), 5)
        self.assertIn("DeepSeek API", plan.steps[2].tools)
        self.assertTrue(any("CAPTCHAs" in rule for rule in plan.safety_rules))
        self.assertTrue(any("Website Runner" in idea for idea in plan.ideas))

    def test_cli_json_output(self):
        result = subprocess.run(
            [sys.executable, "-m", "automation_pipeline.cli", "code automation website", "--json"],
            check=True,
            text=True,
            capture_output=True,
        )
        payload = json.loads(result.stdout)
        self.assertEqual(payload["goal"], "code automation website")
        self.assertTrue(payload["steps"])


if __name__ == "__main__":
    unittest.main()
