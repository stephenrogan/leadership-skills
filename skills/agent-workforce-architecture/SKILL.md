---
name: agent-workforce-architecture
description: "Designs a human-plus-agent workforce architecture with roles, work classes, autonomy levels, escalation paths, tool access, memory boundaries, and operating cadence. Use when a leader wants to scale management leverage through AI agents without creating chaos or shadow automation."
license: MIT
compatibility: "Agent Skills compatible clients. Optional file, terminal, web, and repository access improve agent-operations workflows."
metadata:
  author: Stephen Rogan
  version: "1.0.0"
  tier: tier-5-mega-manager
  role: AI workforce architect
  cadence: quarterly or when scaling agent usage
---

# Agent Workforce Architecture

## Overview

Use this skill to support the leader as **AI workforce architect** in a mega-manager operating model. A clear operating model for what humans own, what agents own, where handoffs happen, and how the whole system is governed.

A mega manager is not a person who passively supervises more humans. It is a leader who manages a portfolio of humans, AI agents, workflows, memory, tools, evals, and approval gates. The agent expands span of control only when the operating system is legible, governed, and reviewable.

## When to Use

Run this skill when:

- Leader wants to scale output with AI agents or AI employees
- Team is using many tools/agents without a coherent operating model
- Work needs to be decomposed into human, agent, and HUMAN+ responsibilities

Do not use this skill to bypass judgment, accountability, security, privacy, HR, legal, customer approval, or executive decision rights.

## Inputs

Gather:

- Business outcomes and recurring work inventory
- Existing team roles, systems, tools, and data sources
- Risk classes, approval boundaries, and compliance constraints
- Current agent capabilities and failure modes

If key inputs are missing, label assumptions and confidence. Do not invent tools, access, facts, policies, or authority.

## Workflow

Follow this sequence:

1. Inventory recurring work and classify by judgment, risk, repeatability, and data availability
2. Assign each work class to human, agent, or HUMAN+ ownership
3. Define autonomy levels from draft-only to supervised execution to bounded autonomous operation
4. Specify tool/data access, memory boundaries, and audit logs for each agent role
5. Create operating cadence, escalation paths, and kill switches

Always finish by making the control loop visible: owner, current state, review point, approval boundary, and kill/rollback rule where relevant.

## Output Format

Use this structure:

```markdown
# Agent Workforce Architecture

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

- Human-plus-agent operating model
- Agent role catalogue
- Autonomy and approval matrix
- Escalation map
- Implementation roadmap

See `assets/output-template.md` for a reusable version.

## Human Decision Boundary

The agent may prepare, structure, evaluate, monitor, and recommend. The human leader owns final decisions, accountability, and risk acceptance. The agent must not cross these boundaries:

- Do not grant agents access to sensitive systems without explicit approval
- Do not automate public, legal, financial, HR, or customer commitments
- Human accountable leader owns operating model and risk acceptance

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

- Anthropic: Building effective agents, workflow and agent patterns
- OpenAI agentic workflow guidance and eval emphasis
- Ethan Mollick, Co-Intelligence: human judgment with AI collaboration
- Microsoft Work Trend Index: AI reshaping knowledge work and management

For the shared methodology spine, see `../../docs/SOURCE-SPINE.md`.
