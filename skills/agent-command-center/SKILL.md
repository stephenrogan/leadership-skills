---
name: agent-command-center
description: "Creates a command-center view for managing multiple AI agents and human-agent workflows, including active work, owners, state, blockers, quality signals, risk level, approvals, and next decisions. Use when a leader needs visibility across an agent-powered operating system."
license: MIT
compatibility: "Agent Skills compatible clients. Optional file, terminal, web, and repository access improve agent-operations workflows."
metadata:
  author: Stephen Rogan
  version: "1.0.0"
  tier: tier-5-mega-manager
  role: Manager cockpit designer
  cadence: weekly or continuous operations
---

# Agent Command Center

## Overview

Use this skill to support the leader as **Manager cockpit designer** in a mega-manager operating model. A single control surface that stops agent work from becoming invisible, duplicated, or ungoverned.

A mega manager is not a person who passively supervises more humans. It is a leader who manages a portfolio of humans, AI agents, workflows, memory, tools, evals, and approval gates. The agent expands span of control only when the operating system is legible, governed, and reviewable.

## When to Use

Run this skill when:

- Leader has multiple agents/workflows running
- Agent work is hard to track or approve
- There are duplicate, stale, or risky automated loops

Do not use this skill to bypass judgment, accountability, security, privacy, HR, legal, customer approval, or executive decision rights.

## Inputs

Gather:

- Agent/workflow inventory
- Current tasks, outputs, schedules, and owners
- Approval queues, errors, and quality signals
- Business priorities and risk classes

If key inputs are missing, label assumptions and confidence. Do not invent tools, access, facts, policies, or authority.

## Workflow

Follow this sequence:

1. Inventory every active agent/workflow and its owner
2. Classify state: running, blocked, pending approval, stale, failed, or complete
3. Surface highest-risk and highest-leverage items first
4. Identify duplicates, orphaned work, and missing review loops
5. Produce a weekly command-center brief and decision queue

Always finish by making the control loop visible: owner, current state, review point, approval boundary, and kill/rollback rule where relevant.

## Output Format

Use this structure:

```markdown
# Agent Command Center

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

- Agent command center brief
- Workflow state table
- Risk and approval queue
- Duplicate/stale work list
- Next decision ladder

See `assets/output-template.md` for a reusable version.

## Human Decision Boundary

The agent may prepare, structure, evaluate, monitor, and recommend. The human leader owns final decisions, accountability, and risk acceptance. The agent must not cross these boundaries:

- Do not create more automation to solve illegibility before pruning current loops
- Do not approve agent actions automatically
- Leader owns prioritisation and kill/continue decisions

Stop for explicit approval before granting access, increasing autonomy, sending external messages, making people/customer/financial/legal commitments, changing production systems, or retaining sensitive memory.

## Quality Bar

A strong output for this skill:

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

- Operational control-plane patterns
- Closed-loop operator principles: visible state, owners, verification, kill rules
- Agent Skills progressive disclosure and eval loops

For the shared methodology spine, see `../../docs/SOURCE-SPINE.md`.
