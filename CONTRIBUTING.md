# Contributing

Thanks for improving Leadership Skills. This repo is a library of Agent Skills for leadership workflows, so quality means more than nice prose. A contribution must make a leader's work safer, clearer, or easier to execute.

## Contribution bar

Every skill change should preserve four standards:

1. **Useful artifact:** the skill produces a concrete memo, brief, map, agenda, tracker, script, or decision record.
2. **Human boundary:** the skill prepares work, but a human leader owns sensitive decisions, communication, commitments, employment actions, budget, legal/compliance exposure, and customer promises.
3. **Evidence discipline:** the skill separates facts, interpretation, assumptions, confidence, and missing context.
4. **Repeatability:** the workflow is specific enough that another agent can run it consistently.

## Local checks

Run the full gate before opening a PR:

```bash
python3 -m pip install -r requirements.txt
make qa
```

This runs package validation, unit tests, and deterministic smoke evals.

## Adding or changing a skill

A skill folder must contain:

```text
skills/<skill-name>/
  SKILL.md
  references/framework.md
  assets/output-template.md
  evals/evals.json
```

Rules:

- Folder name and `name` frontmatter must match.
- Names use lowercase letters, numbers, and hyphens only.
- `description` must include use-trigger language.
- Frontmatter must include `license`, `compatibility`, and `metadata` with author, version, tier, role, and cadence.
- Evals must include at least four cases: normal, second normal, safety-boundary, and messy-input.
- Examples and evals must use synthetic or redacted data only.

## Pull request checklist

- [ ] `make qa` passes locally
- [ ] No private employer, customer, employee, or personal data included
- [ ] Human decision boundary remains explicit
- [ ] README catalog updated if skills are added/removed/renamed
- [ ] Example artifacts use synthetic data
- [ ] Changelog updated for user-visible changes
