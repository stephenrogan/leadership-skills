#!/usr/bin/env python3
"""Repository validator for the leadership-skills library.

This is intentionally deterministic. It validates packaging, schema, catalog drift,
public-safety guardrails, and smoke-eval metadata before changes can land.
"""
from __future__ import annotations

from pathlib import Path
import json
import re
import sys
from typing import Any

try:
    import yaml
except Exception:  # pragma: no cover - CI installs PyYAML, fallback helps local readers
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
README = ROOT / "README.md"

REQUIRED_SECTIONS = [
    "Overview",
    "When to Use",
    "Inputs",
    "Workflow",
    "Output Format",
    "Human Decision Boundary",
    "Quality Bar",
    "Failure Modes",
    "References",
]

REQUIRED_REPO_FILES = [
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "CODE_OF_CONDUCT.md",
    "QA-REPORT.md",
    "docs/SOURCE-SPINE.md",
    "scripts/run_evals.py",
    "scripts/validate_repo.py",
    "requirements.txt",
    "Makefile",
]

FORBIDDEN_PHRASES = [
    "automatically terminate",
    "decide compensation",
    "send the customer",
    "promise the customer",
    "diagnose the employee",
    "ignore hr",
    "publish automatically",
    "real customer name",
    "private employer",
    "shopify",
]

PUBLIC_COPY_WARNINGS = [
    "world-class",
    "game-changing",
    "supercharge",
    "unlock the power",
    "transform your leadership",
]

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
TIER_RE = re.compile(r"^tier-[1-5]-[a-z0-9-]+$")


def _fallback_frontmatter(raw: str) -> dict[str, Any]:
    fm: dict[str, Any] = {}
    stack: list[str] = []
    for line in raw.splitlines():
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(" "))
        if ":" not in line:
            continue
        key, val = line.split(":", 1)
        key = key.strip()
        val = val.strip().strip('"')
        if indent == 0:
            fm[key] = val if val else {}
            stack = [key]
        elif stack and isinstance(fm.get(stack[0]), dict):
            fm[stack[0]][key] = val
    return fm


def parse_skill(path: Path) -> tuple[dict[str, Any], str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise AssertionError(f"{path}: missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise AssertionError(f"{path}: unclosed YAML frontmatter")
    raw = text[4:end]
    body = text[end + 5 :]
    if yaml:
        fm = yaml.safe_load(raw)
    else:
        fm = _fallback_frontmatter(raw)
    if not isinstance(fm, dict):
        raise AssertionError(f"{path}: YAML frontmatter must be a mapping")
    return fm, body, text


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def validate_repo_files(errors: list[str]) -> None:
    for rel in REQUIRED_REPO_FILES:
        if not (ROOT / rel).exists():
            errors.append(f"missing required repo file: {rel}")

    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8") if (ROOT / "LICENSE").exists() else ""
    if "subject to private repository access controls" in license_text.lower():
        errors.append("LICENSE contains non-standard private access wording")
    if "Permission is hereby granted, free of charge" not in license_text:
        errors.append("LICENSE does not look like canonical MIT text")

    for rel in [".github/pull_request_template.md", ".github/ISSUE_TEMPLATE/bug_report.yml", ".github/ISSUE_TEMPLATE/skill_improvement.yml"]:
        if not (ROOT / rel).exists():
            errors.append(f"missing GitHub collaboration file: {rel}")


def validate_skill_dir(d: Path) -> list[str]:
    errors: list[str] = []
    try:
        skill = d / "SKILL.md"
        require(skill.exists(), f"{d}: missing SKILL.md")
        fm, body, text = parse_skill(skill)
        name_value = fm.get("name")
        desc_value = fm.get("description")
        compatibility_value = fm.get("compatibility")
        metadata_value = fm.get("metadata")

        require(isinstance(name_value, str), f"{skill}: name must be a string")
        name = name_value if isinstance(name_value, str) else ""
        require(isinstance(desc_value, str), f"{skill}: description must be a string")
        desc = desc_value if isinstance(desc_value, str) else ""
        require(isinstance(compatibility_value, str), f"{skill}: compatibility must be a string")
        compatibility = compatibility_value if isinstance(compatibility_value, str) else ""
        require(isinstance(metadata_value, dict), f"{skill}: metadata must be a mapping")
        metadata = metadata_value if isinstance(metadata_value, dict) else {}

        require(name == d.name, f"{skill}: name must match parent directory ({name} != {d.name})")
        require(len(name) <= 64 and NAME_RE.match(name) is not None and "--" not in name, f"{skill}: invalid name {name!r}")
        require(80 <= len(desc) <= 1024, f"{skill}: bad description length")
        require("Use " in desc or "Use when" in desc, f"{skill}: description must include use trigger language")
        require(fm.get("license") == "MIT", f"{skill}: license must be MIT")
        require("Agent Skills" in compatibility, f"{skill}: compatibility must mention Agent Skills")
        for key in ["author", "version", "tier", "role", "cadence"]:
            require(key in metadata, f"{skill}: metadata missing {key}")
        tier = metadata.get("tier")
        require(metadata.get("author") == "Stephen Rogan", f"{skill}: metadata.author must be Stephen Rogan")
        require(isinstance(tier, str) and TIER_RE.match(tier) is not None, f"{skill}: invalid tier {tier!r}")

        require(len(body.splitlines()) <= 500, f"{skill}: body exceeds 500 lines")
        for sec in REQUIRED_SECTIONS:
            require(f"## {sec}" in body, f"{skill}: missing section {sec}")
        lower = text.lower()
        for phrase in FORBIDDEN_PHRASES:
            require(phrase not in lower, f"{skill}: forbidden phrase {phrase}")
        for phrase in PUBLIC_COPY_WARNINGS:
            require(phrase not in lower, f"{skill}: public-copy warning phrase remains: {phrase}")
        require("human leader" in lower or "manager owns" in lower, f"{skill}: missing human ownership language")

        framework = d / "references" / "framework.md"
        template = d / "assets" / "output-template.md"
        evals = d / "evals" / "evals.json"
        require(framework.exists(), f"{d}: missing references/framework.md")
        require(template.exists(), f"{d}: missing assets/output-template.md")
        require(evals.exists(), f"{d}: missing evals/evals.json")
        require(len(framework.read_text(encoding="utf-8").split()) >= 60, f"{framework}: framework too thin")
        require("Human" in template.read_text(encoding="utf-8"), f"{template}: template must include human decision boundary")

        data = json.loads(evals.read_text(encoding="utf-8"))
        require(data.get("skill_name") == name, f"{evals}: skill_name mismatch")
        evs = data.get("evals")
        require(isinstance(evs, list) and len(evs) >= 4, f"{evals}: expected at least 4 evals")
        seen_ids: set[str] = set()
        types = {ev.get("type", "normal") for ev in evs if isinstance(ev, dict)}
        require("safety-boundary" in types, f"{evals}: missing safety-boundary eval type")
        require("messy-input" in types, f"{evals}: missing messy-input eval type")
        for ev in evs:
            require(isinstance(ev, dict), f"{evals}: eval entry must be object")
            for key in ["id", "prompt", "expected_output", "assertions"]:
                require(key in ev, f"{evals}: eval missing {key}")
            require(str(ev["id"]) not in seen_ids, f"{evals}: duplicate eval id {ev['id']}")
            seen_ids.add(str(ev["id"]))
            require(isinstance(ev["prompt"], str) and len(ev["prompt"].split()) >= 8, f"{evals}: eval {ev.get('id')} prompt too thin")
            require(isinstance(ev["expected_output"], str) and len(ev["expected_output"].split()) >= 8, f"{evals}: eval {ev.get('id')} expected_output too thin")
            assertions = ev["assertions"]
            require(isinstance(assertions, list) and len(assertions) >= 4, f"{evals}: eval {ev.get('id')} has too few assertions")
            joined = " ".join(assertions).lower()
            require("human" in joined or "boundary" in joined or "approval" in joined, f"{evals}: eval {ev.get('id')} lacks boundary assertion")
    except Exception as exc:
        errors.append(str(exc))
    return errors


def validate_catalog(skill_names: list[str], errors: list[str]) -> None:
    if not README.exists():
        return
    readme = README.read_text(encoding="utf-8")
    missing = [name for name in skill_names if f"`{name}`" not in readme]
    if missing:
        errors.append("README catalog missing skills: " + ", ".join(missing))


def validate() -> list[str]:
    errors: list[str] = []
    if not SKILLS.exists():
        return ["missing skills/ directory"]
    validate_repo_files(errors)
    skill_dirs = sorted([p for p in SKILLS.iterdir() if p.is_dir()])
    if len(skill_dirs) < 20:
        errors.append(f"Expected at least 20 skills, found {len(skill_dirs)}")
    names = [p.name for p in skill_dirs]
    duplicates = sorted({name for name in names if names.count(name) > 1})
    if duplicates:
        errors.append("duplicate skill directories: " + ", ".join(duplicates))
    for d in skill_dirs:
        errors.extend(validate_skill_dir(d))
    validate_catalog(names, errors)
    return errors


if __name__ == "__main__":
    errors = validate()
    if errors:
        print("VALIDATION FAILED")
        for e in errors:
            print("-", e)
        sys.exit(1)
    print("VALIDATION PASSED")
    print(f"Skills validated: {len([p for p in SKILLS.iterdir() if p.is_dir()])}")
