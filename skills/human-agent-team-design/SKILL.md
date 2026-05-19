---
name: human-agent-team-design
description: Designs how humans and AI agents collaborate inside a team, including roles, handoffs, rituals, shared artifacts, escalation norms, trust-building, and anti-patterns. Use when a manager is turning a conventional team into a human-agent operating unit.
license: MIT
compatibility: Agent Skills compatible clients. Optional file, terminal, web, and repository access improve agent-operations workflows.
metadata:
  author: Stephen Rogan
  version: "1.0.0"
  tier: tier-5-mega-manager
  role: Team operating model designer
  cadence: quarterly or per team launch
---

# Human Agent Team Design

## Overview

Use this skill to support the leader as **Team operating model designer** in a mega-manager operating model. A human-agent teaming model that increases leverage without eroding accountability, trust, or craft.

A mega manager is not a person who passively supervises more humans. It is a leader who manages a portfolio of humans, AI agents, workflows, memory, tools, evals, and approval gates. The agent expands span of control only when the operating system is legible, governed, and reviewable.

## When to Use

Run this skill when:

- Team is adopting agents into daily work
- Humans are unclear what agents own versus assist with
- AI usage is creating trust, quality, or coordination issues

Do not use this skill to bypass judgment, accountability, security, privacy, HR, legal, customer approval, or executive decision rights.

## Inputs

Gather:

- Team mission and recurring workflows
- Human roles, strengths, pain points, and anxieties
- Agent capabilities, tools, and limits
- Existing rituals, artifacts, and decision rights

If key inputs are missing, label assumptions and confidence. Do not invent tools, access, facts, policies, or authority.

## Workflow

Follow this sequence:

1. Map team workflows into human-only, agent-only, and HUMAN+ modes
2. Define handoff artifacts and review responsibilities
3. Design rituals: planning, delegation, review, retro, and improvement backlog
4. Set norms for transparency: when AI was used, how output was checked, and what remains human-owned
5. Identify adoption risks and training needs

Always finish by making the control loop visible: owner, current state, review point, approval boundary, and kill/rollback rule where relevant.

## Output Format

Use this structure:

```markdown
# Human Agent Team Design

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

- Human-agent team charter
- Workflow ownership map
- Ritual design
- Transparency norms
- Adoption risk plan

See `assets/output-template.md` for a reusable version.

## Human Decision Boundary

The agent may prepare, structure, evaluate, monitor, and recommend. The agent must not cross these boundaries:

- Do not position agents as replacing trust, judgment, or accountability
- Do not hide AI usage in sensitive or external work
- Manager owns team norms and adoption pacing

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

- Human-AI teaming research and centaur/cyborg work patterns
- Mollick: co-intelligence and human-AI collaboration
- Team operating model and psychological safety practices

For the shared methodology spine, see `../../docs/SOURCE-SPINE.md`.
