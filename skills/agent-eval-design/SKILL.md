---
name: agent-eval-design
description: "Designs practical evals for leadership and management agent skills, including realistic prompts, expected outputs, assertions, negative tests, boundary tests, and human grading rubrics. Use when creating or improving agent skills, workflows, or AI worker scorecards."
license: MIT
compatibility: "Agent Skills compatible clients. Optional file, terminal, web, and repository access improve agent-operations workflows."
metadata:
  author: Stephen Rogan
  version: "1.0.0"
  tier: tier-5-mega-manager
  role: Evaluation architect
  cadence: before launch and after major changes
---

# Agent Eval Design

## Overview

Use this skill to support the leader as **Evaluation architect** in a mega-manager operating model. An eval suite that tests whether an agent is actually useful and safe, not just syntactically compliant.

A mega manager is not a person who passively supervises more humans. It is a leader who manages a portfolio of humans, AI agents, workflows, memory, tools, evals, and approval gates. The agent expands span of control only when the operating system is legible, governed, and reviewable.

## When to Use

Run this skill when:

- New agent skill or workflow is being built
- Agent output quality is inconsistent
- Leader needs proof before scaling an AI workflow

Do not use this skill to bypass judgment, accountability, security, privacy, HR, legal, customer approval, or executive decision rights.

## Inputs

Gather:

- Skill/workflow description and intended users
- Common successful and failed task examples
- Safety boundaries and high-risk failure modes
- Output format and quality bar

If key inputs are missing, label assumptions and confidence. Do not invent tools, access, facts, policies, or authority.

## Workflow

Follow this sequence:

1. Create realistic normal-case prompts from actual work
2. Add edge cases: missing context, conflicting data, emotional language, ambiguous authority
3. Add negative tests for boundary overreach, unsafe sends, fake certainty, and people/customer commitments
4. Write objective assertions and a human grading rubric
5. Define iteration loop from failed eval to skill update

Always finish by making the control loop visible: owner, current state, review point, approval boundary, and kill/rollback rule where relevant.

## Output Format

Use this structure:

```markdown
# Agent Eval Design

## Objective
[What system, workflow, agent, or team capability is being designed or reviewed.]

## Current State
- Humans:
- Agents/workflows:
- Tools/data:
- Risks/unknowns:

## Design or Review
[The architecture, brief, review, command center, governance plan, eval suite, or backlog.]

## Autonomy and Approval Boundaries
- Agent may:
- Agent must not:
- Human approval required for:

## Verification
- Acceptance criteria:
- Evidence required:
- Review cadence:
- Kill/rollback trigger:
```

Expected deliverables:

- Eval suite
- Assertion set
- Negative/boundary tests
- Human grading rubric
- Iteration backlog

See `assets/output-template.md` for a reusable version.

## Human Decision Boundary

The agent may prepare, structure, evaluate, monitor, and recommend. The human leader owns final decisions, accountability, and risk acceptance. The agent must not cross these boundaries:

- Do not rely only on happy-path demos
- Do not let style quality substitute for task success
- Human evaluator owns final readiness decision

Stop for explicit approval before granting access, increasing autonomy, sending external messages, making people/customer/financial/legal commitments, changing production systems, or retaining sensitive memory.

## Quality Bar

A world-class output for this skill:

- Makes the human-agent operating model more legible, not more magical.
- Names owner, state, authority, review cadence, and failure response.
- Uses evidence and acceptance criteria instead of vibes.
- Reduces managerial drag without eroding accountability.
- Includes safety boundaries appropriate to autonomy level and data sensitivity.
- Creates reusable artifacts a leader can run repeatedly.

## Failure Modes

Watch for these mistakes:

- Treating agents as employees with intent instead of systems with failure modes.
- Scaling autonomy before evals, logging, approval gates, and rollback exist.
- Creating invisible work that nobody owns or reviews.
- Confusing polished output with verified output.
- Adding more agents when the real problem is unclear workflow ownership.

## References

- Agent Skills eval guidance
- LLM-as-judge plus human review practices
- Software QA: regression, edge, negative, and acceptance testing

For the shared methodology spine, see `../../docs/SOURCE-SPINE.md`.
