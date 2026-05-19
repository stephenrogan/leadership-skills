---
name: context-memory-ops
description: Designs context, memory, and knowledge flows for agent-managed work: what agents should know, retrieve, remember, forget, cite, and never store. Use when agent quality depends on durable context, sensitive information boundaries, or cross-session continuity.
license: MIT
compatibility: Agent Skills compatible clients. Optional file, terminal, web, and repository access improve agent-operations workflows.
metadata:
  author: Stephen Rogan
  version: "1.0.0"
  tier: tier-5-mega-manager
  role: Context and memory steward
  cadence: weekly or per workflow design
---

# Context Memory Ops

## Overview

Use this skill to support the leader as **Context and memory steward** in a mega-manager operating model. A memory architecture that gives agents useful continuity without privacy leaks or stale-context drift.

A mega manager is not a person who passively supervises more humans. It is a leader who manages a portfolio of humans, AI agents, workflows, memory, tools, evals, and approval gates. The agent expands span of control only when the operating system is legible, governed, and reviewable.

## When to Use

Run this skill when:

- Agents keep losing context or repeating old mistakes
- Sensitive context may be leaking into outputs or memory
- Knowledge sources are fragmented, stale, or overloaded

Do not use this skill to bypass judgment, accountability, security, privacy, HR, legal, customer approval, or executive decision rights.

## Inputs

Gather:

- Knowledge sources and data sensitivity levels
- Recurring workflows and context requirements
- Memory policies, retention rules, and deletion needs
- Known stale docs, contradictions, and source-of-truth systems

If key inputs are missing, label assumptions and confidence. Do not invent tools, access, facts, policies, or authority.

## Workflow

Follow this sequence:

1. Classify context into task input, durable memory, reference knowledge, and forbidden memory
2. Define source of truth and retrieval order for each workflow
3. Create rules for what to remember, cite, update, and forget
4. Add staleness checks and conflict resolution paths
5. Document privacy, retention, and audit requirements

Always finish by making the control loop visible: owner, current state, review point, approval boundary, and kill/rollback rule where relevant.

## Output Format

Use this structure:

```markdown
# Context Memory Ops

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

- Context architecture
- Memory policy
- Source-of-truth map
- Staleness and conflict rules
- Sensitive-data guardrails

See `assets/output-template.md` for a reusable version.

## Human Decision Boundary

The agent may prepare, structure, evaluate, monitor, and recommend. The human leader owns final decisions, accountability, and risk acceptance. The agent must not cross these boundaries:

- Do not store secrets, temporary task state, or sensitive personal details without policy
- Do not let stale memory override live evidence
- Human/system owner approves memory and retention rules

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

- Retrieval-augmented generation and source-of-truth patterns
- Agent Skills progressive disclosure
- Privacy-by-design and data minimization principles

For the shared methodology spine, see `../../docs/SOURCE-SPINE.md`.
