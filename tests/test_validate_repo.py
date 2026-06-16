import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def _load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None
    assert spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


validate_mod = _load_module('validate_repo', ROOT / 'scripts' / 'validate_repo.py')
run_evals_mod = _load_module('run_evals', ROOT / 'scripts' / 'run_evals.py')


class RepositoryValidationTests(unittest.TestCase):
    def test_repo_validation_passes(self):
        self.assertEqual(validate_mod.validate(), [])

    def test_skill_count_and_eval_count(self):
        skill_dirs = [p for p in (ROOT / 'skills').iterdir() if p.is_dir()]
        self.assertGreaterEqual(len(skill_dirs), 20)
        total_evals = 0
        for d in skill_dirs:
            eval_path = d / 'evals' / 'evals.json'
            self.assertTrue(eval_path.exists())
            total_evals += len(json.loads(eval_path.read_text())['evals'])
        self.assertGreaterEqual(total_evals, 80)

    def test_smoke_evals_pass(self):
        report = run_evals_mod.run()
        self.assertTrue(report['passed'])
        self.assertEqual(report['failures'], 0)
        self.assertGreaterEqual(report['evals_checked'], 80)


if __name__ == '__main__':
    unittest.main()
