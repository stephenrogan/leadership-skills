---
name: agent-performance-management
description: "Evaluates AI agent performance over time using task outcomes, acceptance rate, revision causes, error patterns, latency, cost, risk incidents, and user trust. Use when managing AI workers, agent workflows, or automated loops as part of a leadership operating system."
license: MIT
compatibility: "Agent Skills compatible clients. Optional file, terminal, web, and repository access improve agent-operations workflows."
metadata:
  author: Stephen Rogan
  version: "1.0.0"
  tier: tier-5-mega-manager
  role: AI worker performance manager
  cadence: weekly or monthly
---

# Agent Performance Management

## Overview

Use this skill to support the leader as **AI worker performance manager** in a mega-manager operating model. A performance management loop for agents that improves reliability instead of anthropomorphizing them.

A mega manager is not a person who passively supervises more humans. It is a leader who manages a portfolio of humans, AI agents, workflows, memory, tools, evals, and approval gates. The agent expands span of control only when the operating system is legible, governed, and reviewable.

## When to Use

Run this skill when:

- An agent is used repeatedly for important work
- Outputs require frequent correction or review time is high
- Leader needs to decide whether to improve, constrain, replace, or retire an agent

Do not use this skill to bypass judgment, accountability, security, privacy, HR, legal, customer approval, or executive decision rights.

## Inputs

Gather:

- Task history and output samples
- Acceptance/revision/rejection decisions
- Error categories, incidents, latency, and cost
- User feedback and downstream outcomes

If key inputs are missing, label assumptions and confidence. Do not invent tools, access, facts, policies, or authority.

## Workflow

Follow this sequence:

1. Define the agent job scorecard: outcomes, quality, safety, speed, and cost
2. Measure accepted, revised, rejected, and escalated outputs
3. Cluster failure causes: prompt, context, tool, model, data, scope, or governance
4. Recommend intervention: better brief, skill update, tool change, eval, narrower scope, or retirement
5. Set next review date and expected improvement signal

Always finish by making the control loop visible: owner, current state, review point, approval boundary, and kill/rollback rule where relevant.

## Output Format

Use this structure:

```markdown
# Agent Performance Management

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

- Agent performance scorecard
- Failure-mode analysis
- Improvement plan
- Retire/constrain/scale recommendation
- Eval update backlog

See `assets/output-template.md` for a reusable version.

## Human Decision Boundary

The agent may prepare, structure, evaluate, monitor, and recommend. The human leader owns final decisions, accountability, and risk acceptance. The agent must not cross these boundaries:

- Do not personify agent performance as intent or attitude
- Do not scale an agent with unresolved high-risk failures
- Human owner accepts or rejects operational changes

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

- MLOps monitoring concepts applied to agents
- Eval-driven iteration from Agent Skills docs
- Quality management: acceptance criteria and defect taxonomy

For the shared methodology spine, see `../../docs/SOURCE-SPINE.md`.
