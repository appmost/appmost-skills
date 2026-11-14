"""Isolation, publication-boundary and reproducibility checks."""
from __future__ import annotations
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from package import package
from repo_checks import CheckError, check_links, scan_text, validate_repository

class PackageTests(unittest.TestCase):
    def setUp(self):
        base = Path(os.environ.get("TMPDIR") or ROOT / ".build/tests")
        base.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix="package-test-", dir=base)
        self.addCleanup(self.temp.cleanup)
        self.workspace = Path(self.temp.name)
        self.repo = self.workspace / "repo"
        self.repo.mkdir()
        for name in ("README.md", "CONTRIBUTING.md", "SECURITY.md", "LICENSE", "plugin.json",
                     "docs", "skills", "evals", "scripts", "tests", ".github", ".agents"):
            source = ROOT / name
            destination = self.repo / name
            if source.is_dir():
                shutil.copytree(source, destination, ignore=shutil.ignore_patterns("__pycache__"))
            elif source.exists():
                shutil.copyfile(source, destination)

    def test_real_repository_is_valid(self):
        self.assertEqual([], validate_repository(ROOT))

    def test_archive_is_standalone_and_excludes_maintenance_and_private_material(self):
        (self.repo / "private-notes.txt").write_text("Synthetic local maintenance note.")
        hashes = package(self.repo, self.workspace / "packages")
        self.assertEqual({"appmost.zip", "appmost-release.zip"}, set(hashes))
        for archive_name in hashes:
            skill = archive_name.removesuffix(".zip")
            with zipfile.ZipFile(self.workspace / "packages" / archive_name) as archive:
                names = archive.namelist()
                self.assertIn(f"{skill}/SKILL.md", names)
                self.assertIn(f"{skill}/LICENSE.txt", names)
                self.assertTrue(all(name.startswith(skill + "/") for name in names))
                self.assertFalse(any("private-notes" in name or "CONTRIBUTING" in name for name in names))
                extracted = self.workspace / f"installed-{skill}"
                archive.extractall(extracted)
                for page in (extracted / skill).rglob("*.md"):
                    self.assertEqual([], check_links(page, extracted / skill))

    def test_repeated_packages_have_identical_bytes_despite_source_mtime(self):
        one = package(self.repo, self.workspace / "one")
        os.utime(self.repo / "skills/appmost/SKILL.md", (2_000_000_000, 2_000_000_000))
        two = package(self.repo, self.workspace / "two")
        self.assertEqual(one, two)
        for name in one:
            self.assertEqual((self.workspace / "one" / name).read_bytes(),
                             (self.workspace / "two" / name).read_bytes())

    def test_existing_output_is_preserved(self):
        output = self.workspace / "existing"
        output.mkdir()
        marker = output / "keep.txt"
        marker.write_text("do not overwrite")
        with self.assertRaises(CheckError):
            package(self.repo, output)
        self.assertEqual("do not overwrite", marker.read_text())

    def test_source_output_overlap_is_rejected(self):
        with self.assertRaises(CheckError):
            package(self.repo, self.repo / "skills/new-output")
        self.assertFalse((self.repo / "skills/new-output").exists())

    def test_external_symlink_is_rejected_before_packaging(self):
        external = self.workspace / "private.txt"
        external.write_text("external fixture")
        (self.repo / "skills/appmost/references/leak.md").symlink_to(external)
        with self.assertRaises(CheckError):
            package(self.repo, self.workspace / "blocked")
        self.assertFalse((self.workspace / "blocked").exists())

    def test_repository_only_link_cannot_escape_installed_skill(self):
        page = self.repo / "skills/appmost/references/test.md"
        page.write_text("[private note](../../../CONTRIBUTING.md)")
        self.assertTrue(any("link escapes install boundary" in item for item in validate_repository(self.repo)))

    def test_missing_reference_is_detected(self):
        (self.repo / "skills/appmost/references/design-review.md").unlink()
        self.assertTrue(any("missing link target" in item for item in validate_repository(self.repo)))

    def test_credentials_are_rejected_without_echoing_the_value(self):
        secret = "ghp_" + "A" * 36
        (self.repo / "docs/accidental.txt").write_text(secret)
        errors = validate_repository(self.repo)
        self.assertTrue(any("GitHub token" in item for item in errors))
        self.assertFalse(any(secret in item for item in errors))

    def test_private_workstation_paths_are_detected(self):
        path = "/" + "Users/" + "example/private-app/source"
        self.assertIn("private workstation path", scan_text(path))

    def test_skill_version_mismatch_is_detected(self):
        path = self.repo / "plugin.json"
        manifest = json.loads(path.read_text())
        manifest["version"] = "0.9.0"
        path.write_text(json.dumps(manifest))
        self.assertTrue(any("version mismatch" in item for item in validate_repository(self.repo)))

    def test_git_tracked_ignored_secret_file_is_still_checked(self):
        env = dict(os.environ, GIT_OPTIONAL_LOCKS="0")
        subprocess.run(["git", "init", "-q", str(self.repo)], check=True, env=env)
        (self.repo / ".gitignore").write_text(".env\n")
        (self.repo / ".env").write_text("synthetic local configuration")
        subprocess.run(["git", "-C", str(self.repo), "add", "-f", ".env"], check=True, env=env)
        self.assertTrue(any("private/generated source is tracked" in item
                            for item in validate_repository(self.repo)))


    def test_format_major_mismatch_is_detected(self):
        path = self.repo / "skills/appmost/SKILL.md"
        path.write_text(path.read_text().replace(
            '  appmost-document-version: "2"', '  appmost-document-version: "3"'))
        self.assertTrue(any("format major mismatch" in item for item in validate_repository(self.repo)))

    def test_format_review_requires_an_immutable_matching_public_source(self):
        path = self.repo / "skills/appmost/SKILL.md"
        original = path.read_text()
        for old, new in [
            ("blob/ba2dd848a8ee36864fbdc4c275f8df1e22851a6c/", "blob/main/"),
            ("/spec/2.2.0.md", "/spec/2.1.1.md"),
        ]:
            with self.subTest(replacement=new):
                path.write_text(original.replace(old, new))
                self.assertTrue(any("format reference" in item for item in validate_repository(self.repo)))
        path.write_text(original)

    def test_missing_or_invalid_review_metadata_is_detected(self):
        path = self.repo / "skills/appmost-release/SKILL.md"
        original = path.read_text()
        for replacement in ["", '  appmost-format-review-date: "2026-02-30"']:
            with self.subTest(replacement=replacement):
                path.write_text(original.replace('  appmost-format-review-date: "2026-11-14"', replacement))
                self.assertTrue(any("format review date" in item for item in validate_repository(self.repo)))

    def test_reference_review_cannot_be_silently_promoted_to_runtime_certification(self):
        path = self.repo / "skills/appmost/SKILL.md"
        path.write_text(path.read_text().replace(
            '  appmost-format-review-kind: "reference-review"',
            '  appmost-format-review-kind: "runtime-certified"'))
        self.assertTrue(any("format review kind" in item for item in validate_repository(self.repo)))

    def test_duplicate_compatibility_metadata_is_rejected(self):
        path = self.repo / "skills/appmost/SKILL.md"
        path.write_text(path.read_text().replace(
            '  appmost-document-version: "2"',
            '  appmost-document-version: "2"\n  appmost-document-version: "3"'))
        self.assertTrue(any("duplicate metadata key" in item for item in validate_repository(self.repo)))

    def test_standalone_archive_retains_the_exact_compatibility_record(self):
        package(self.repo, self.workspace / "compatibility-packages")
        for skill in ["appmost", "appmost-release"]:
            with zipfile.ZipFile(self.workspace / "compatibility-packages" / (skill + ".zip")) as archive:
                for relative in ["SKILL.md", "references/format-compatibility.md"]:
                    self.assertEqual(
                        (self.repo / "skills" / skill / relative).read_bytes(),
                        archive.read(skill + "/" + relative))

if __name__ == "__main__":
    unittest.main()
