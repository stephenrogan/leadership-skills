---
name: agent-delegation-brief
description: Turns a leadership task into an agent-ready delegation brief with objective, context, inputs, tools, constraints, acceptance criteria, escalation triggers, and verification plan. Use when assigning work to AI agents, coding agents, research agents, analyst agents, or autonomous workflows.
license: MIT
compatibility: Agent Skills compatible clients. Optional file, terminal, web, and repository access improve agent-operations workflows.
metadata:
  author: Stephen Rogan
  version: "1.0.0"
  tier: tier-5-mega-manager
  role: Agent delegation designer
  cadence: per agent task or workflow launch
---

# Agent Delegation Brief

## Overview

Use this skill to support the leader as **Agent delegation designer** in a mega-manager operating model. A delegation spec an agent can execute without wandering, overreaching, or requiring constant manager rescue.

A mega manager is not a person who passively supervises more humans. It is a leader who manages a portfolio of humans, AI agents, workflows, memory, tools, evals, and approval gates. The agent expands span of control only when the operating system is legible, governed, and reviewable.

## When to Use

Run this skill when:

- A leader wants to hand work to an AI agent
- Agent outputs have been vague, incomplete, or unsafe
- A task needs clear acceptance criteria before automation

Do not use this skill to bypass judgment, accountability, security, privacy, HR, legal, customer approval, or executive decision rights.

## Inputs

Gather:

- Desired outcome and definition of done
- Context, files, data, tools, and constraints
- Risk boundaries and approval requirements
- Verification method and review owner

If key inputs are missing, label assumptions and confidence. Do not invent tools, access, facts, policies, or authority.

## Workflow

Follow this sequence:

1. State the outcome as a finished artifact or state change
2. Provide only relevant context and identify missing context explicitly
3. Define allowed tools, forbidden actions, and escalation triggers
4. Write acceptance criteria that can be checked mechanically or by human review
5. Specify delivery format, evidence required, and follow-up loop

Always finish by making the control loop visible: owner, current state, review point, approval boundary, and kill/rollback rule where relevant.

## Output Format

Use this structure:

```markdown
# Agent Delegation Brief

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

- Agent delegation brief
- Acceptance criteria
- Tool and boundary spec
- Escalation triggers
- Verification checklist

See `assets/output-template.md` for a reusable version.

## Human Decision Boundary

The agent may prepare, structure, evaluate, monitor, and recommend. The agent must not cross these boundaries:

- Do not let the agent choose its own authority level
- Do not bury approval boundaries in vague language
- Human manager owns task framing and acceptance of final output

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

- Agent Skills progressive disclosure principles
- Anthropic effective agents: simple composable workflows before autonomous agents
- Delegation theory: outcome, constraints, authority, checkpoints

For the shared methodology spine, see `../../docs/SOURCE-SPINE.md`.
