---
name: agent-improvement-backlog
description: Converts agent failures, user corrections, eval misses, review notes, and workflow friction into a prioritized improvement backlog. Use when improving agent skills, prompts, tools, memory, evals, or operating procedures over time.
license: MIT
compatibility: Agent Skills compatible clients. Optional file, terminal, web, and repository access improve agent-operations workflows.
metadata:
  author: Stephen Rogan
  version: "1.0.0"
  tier: tier-5-mega-manager
  role: Continuous improvement operator
  cadence: weekly or monthly
---

# Agent Improvement Backlog

## Overview

Use this skill to support the leader as **Continuous improvement operator** in a mega-manager operating model. A disciplined improvement loop that turns agent mistakes into durable system upgrades.

A mega manager is not a person who passively supervises more humans. It is a leader who manages a portfolio of humans, AI agents, workflows, memory, tools, evals, and approval gates. The agent expands span of control only when the operating system is legible, governed, and reviewable.

## When to Use

Run this skill when:

- Users keep correcting the same agent behaviour
- Evals fail or outputs require repeated revision
- Agent workflows need continuous improvement rather than ad hoc prompt tweaks

Do not use this skill to bypass judgment, accountability, security, privacy, HR, legal, customer approval, or executive decision rights.

## Inputs

Gather:

- Failed outputs and review comments
- User corrections and acceptance/rejection notes
- Eval results and incident logs
- Current skill, prompt, tool, and memory design

If key inputs are missing, label assumptions and confidence. Do not invent tools, access, facts, policies, or authority.

## Workflow

Follow this sequence:

1. Cluster issues by root cause: unclear brief, missing context, weak skill, bad tool, risky autonomy, model limit, or process gap
2. Rank by frequency, severity, and leverage
3. Decide fix type: skill patch, eval addition, tool change, memory update, governance rule, or retire workflow
4. Write backlog items with acceptance criteria and owner
5. Close the loop by rerunning evals and updating QA evidence

Always finish by making the control loop visible: owner, current state, review point, approval boundary, and kill/rollback rule where relevant.

## Output Format

Use this structure:

```markdown
# Agent Improvement Backlog

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

- Agent improvement backlog
- Root-cause clusters
- Prioritized fixes
- Acceptance criteria
- QA/eval rerun plan

See `assets/output-template.md` for a reusable version.

## Human Decision Boundary

The agent may prepare, structure, evaluate, monitor, and recommend. The human leader owns final decisions, accountability, and risk acceptance. The agent must not cross these boundaries:

- Do not keep patching prompts when the workflow is structurally wrong
- Do not store temporary task outcomes as durable memory
- Human owner chooses priorities and accepts fixes

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

- Agent Skills refine-with-real-execution practice
- Continuous improvement and defect taxonomy
- MLOps/model monitoring feedback loops

For the shared methodology spine, see `../../docs/SOURCE-SPINE.md`.
