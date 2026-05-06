import re
import unittest
from pathlib import Path


class FileLinksTest(unittest.TestCase):
    def test_root_file_links_point_to_existing_files(self):
        root = Path(__file__).resolve().parents[1]
        content = (root / "FILE_LINKS.md").read_text(encoding="utf-8")
        links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", content)

        self.assertGreaterEqual(len(links), 10)
        for link in links:
            self.assertTrue((root / link).exists(), f"Missing linked file: {link}")

    def test_ready_pipeline_file_links_point_to_existing_files(self):
        root = Path(__file__).resolve().parents[1] / "ready_pipeline"
        content = (root / "FILE_LINKS.md").read_text(encoding="utf-8")
        links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", content)

        self.assertGreaterEqual(len(links), 6)
        for link in links:
            self.assertTrue((root / link).exists(), f"Missing linked file: {link}")


if __name__ == "__main__":
    unittest.main()
