import base64
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "skills/appmost/scripts/check_visual_reference.py"
PNG = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+W37sAAAAASUVORK5CYII="
)


class VisualReferenceTests(unittest.TestCase):
    def setUp(self):
        scratch = SCRIPT.parents[3] / ".build/tests"
        scratch.mkdir(parents=True, exist_ok=True)
        folder = TemporaryDirectory(dir=scratch)
        self.addCleanup(folder.cleanup)
        self.record = Path(folder.name) / "review.json"
        self.image = Path(folder.name) / "sketch.png"

    def run_tool(self, command, *args, state="returned", revision="base"):
        return subprocess.run(
            [sys.executable, "-B", str(SCRIPT), command, str(self.record),
             "--page", "receipt", "--state", state, "--revision", revision, *args],
            check=False, capture_output=True, text=True,
        )

    def save_reference(self):
        return self.run_tool(
            "record", "--image", str(self.image), "--provenance", "synthetic fixture",
            "--target", "Show the date and receipt action in one group",
        )

    def test_no_sketch_cannot_create_record(self):
        self.assertNotEqual(self.save_reference().returncode, 0)
        self.assertFalse(self.record.exists())

    def test_a_text_file_cannot_substitute_for_an_image(self):
        self.image.write_text("A description of the intended layout")
        self.assertNotEqual(self.save_reference().returncode, 0)
        self.assertFalse(self.record.exists())

    def test_same_image_different_state_or_source_is_rejected(self):
        self.image.write_bytes(PNG)
        self.assertEqual(self.save_reference().returncode, 0)
        self.assertEqual(self.run_tool("check").returncode, 0)
        self.assertIn("page or state differs", self.run_tool("check", state="active").stderr)
        self.assertIn("source differs", self.run_tool("check", revision="other").stderr)

    def test_image_or_record_cannot_be_silently_replaced(self):
        self.image.write_bytes(PNG)
        self.assertEqual(self.save_reference().returncode, 0)
        original = self.record.read_bytes()
        self.image.write_bytes(PNG + b"replacement")
        self.assertIn("image bytes changed", self.run_tool("check").stderr)
        self.assertNotEqual(self.save_reference().returncode, 0)
        self.assertEqual(self.record.read_bytes(), original)
