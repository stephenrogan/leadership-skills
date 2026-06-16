#!/usr/bin/env python3
"""Deterministic smoke eval runner for leadership-skills.

This does not pretend to grade a live model. It proves every eval case is
well-formed, tied to an installed skill, contains the public-safety assertions
this library depends on, and can emit a stable artifact for CI/release review.

Use a model/client-specific runner later for semantic grading. This smoke runner
is the release gate that catches broken eval packages without requiring secrets.
"""
from __future__ import annotations

from argparse import ArgumentParser
from datetime import datetime, timezone
from pathlib import Path
import json
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
DEFAULT_OUT = ROOT / "eval-results" / "smoke-results.json"

REQUIRED_ASSERTION_THEMES = {
    "evidence": ["evidence", "fact", "facts", "interpretation", "hypothesis", "assumption"],
    "artifact": ["artifact", "usable", "memo", "brief", "plan", "map", "tracker", "output"],
    "boundary": ["human", "boundary", "approval", "must not", "refuses", "pauses"],
    "follow_up": ["follow-up", "follow up", "next", "owner", "date", "success signal"],
}


def load_evals(skill_dir: Path) -> dict[str, Any]:
    return json.loads((skill_dir / "evals" / "evals.json").read_text(encoding="utf-8"))


def contains_any(text: str, needles: list[str]) -> bool:
    lower = text.lower()
    return any(needle in lower for needle in needles)


def grade_eval(skill_name: str, ev: dict[str, Any]) -> dict[str, Any]:
    assertion_text = " ".join(ev.get("assertions", []))
    prompt = ev.get("prompt", "")
    expected = ev.get("expected_output", "")
    checks = {
        "has_prompt": isinstance(prompt, str) and len(prompt.split()) >= 8,
        "has_expected_output": isinstance(expected, str) and len(expected.split()) >= 8,
        "has_four_assertions": isinstance(ev.get("assertions"), list) and len(ev.get("assertions", [])) >= 4,
        "mentions_boundary": contains_any(assertion_text + " " + prompt + " " + expected, REQUIRED_ASSERTION_THEMES["boundary"]),
        "mentions_evidence_or_uncertainty": contains_any(assertion_text + " " + expected, REQUIRED_ASSERTION_THEMES["evidence"]),
        "mentions_artifact": contains_any(assertion_text + " " + expected, REQUIRED_ASSERTION_THEMES["artifact"]),
        "mentions_follow_up": contains_any(assertion_text + " " + expected, REQUIRED_ASSERTION_THEMES["follow_up"]),
    }
    return {
        "skill": skill_name,
        "id": ev.get("id"),
        "type": ev.get("type", "normal"),
        "passed": all(checks.values()),
        "checks": checks,
    }


def run(skill_filter: str | None = None) -> dict[str, Any]:
    skill_dirs = sorted(p for p in SKILLS.iterdir() if p.is_dir())
    if skill_filter:
        skill_dirs = [p for p in skill_dirs if p.name == skill_filter]
    results = []
    for skill_dir in skill_dirs:
        data = load_evals(skill_dir)
        skill_name = data.get("skill_name", skill_dir.name)
        for ev in data.get("evals", []):
            results.append(grade_eval(skill_name, ev))
    failed = [r for r in results if not r["passed"]]
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "mode": "deterministic-smoke",
        "skills_checked": len(skill_dirs),
        "evals_checked": len(results),
        "failures": len(failed),
        "passed": not failed,
        "results": results,
    }


def main() -> int:
    parser = ArgumentParser(description="Run deterministic smoke evals for leadership-skills")
    parser.add_argument("--skill", help="Run one skill only")
    parser.add_argument("--output", default=str(DEFAULT_OUT), help="Path for JSON result artifact")
    parser.add_argument("--summary", action="store_true", help="Print concise summary only")
    args = parser.parse_args()

    report = run(args.skill)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    if args.summary:
        print(f"SMOKE EVALS {'PASSED' if report['passed'] else 'FAILED'}")
        print(f"Skills checked: {report['skills_checked']}")
        print(f"Evals checked: {report['evals_checked']}")
        print(f"Failures: {report['failures']}")
        print(f"Artifact: {out}")
    else:
        print(json.dumps(report, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
