from __future__ import annotations
import importlib.util, shutil, tempfile, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('validator', ROOT/'tools/validate_repo.py')
validator = importlib.util.module_from_spec(spec); spec.loader.exec_module(validator)

class RepositoryTests(unittest.TestCase):
    def test_current_repository(self):
        self.assertEqual([], validator.validate(ROOT))

    def mutate(self, fn):
        with tempfile.TemporaryDirectory() as td:
            copy=Path(td)/'repo'; shutil.copytree(ROOT,copy)
            fn(copy)
            self.assertTrue(validator.validate(copy))

    def test_missing_skill_fails(self):
        self.mutate(lambda r: shutil.rmtree(r/'skills/advertising-evaluate'))

    def test_missing_command_fails(self):
        self.mutate(lambda r: (r/'skills/advertising-build/commands/design-test.md').unlink())

    def test_broken_skill_link_fails(self):
        def change(r):
            p=r/'skills/advertising-build/SKILL.md'; p.write_text(p.read_text()+'\n[missing](missing.md)\n')
        self.mutate(change)

    def test_false_benchmark_execution_fails(self):
        def change(r):
            p=r/'benchmarks/suites.json'; p.write_text(p.read_text().replace('"not-run"','"passed"'))
        self.mutate(change)

if __name__ == '__main__': unittest.main()
