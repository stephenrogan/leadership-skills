import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('validate_repo', ROOT / 'scripts' / 'validate_repo.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class RepositoryValidationTests(unittest.TestCase):
    def test_repo_validation_passes(self):
        self.assertEqual(mod.validate(), [])

    def test_skill_count_and_eval_count(self):
        skill_dirs = [p for p in (ROOT / 'skills').iterdir() if p.is_dir()]
        self.assertGreaterEqual(len(skill_dirs), 20)
        for d in skill_dirs:
            self.assertTrue((d / 'evals' / 'evals.json').exists())

if __name__ == '__main__':
    unittest.main()
