---
name: agent-risk-governance
description: "Creates governance for AI agents with risk classes, approval gates, audit logs, access controls, red lines, incident response, and rollback rules. Use before deploying agents into leadership, customer, people, financial, or external-facing workflows."
license: MIT
compatibility: "Agent Skills compatible clients. Optional file, terminal, web, and repository access improve agent-operations workflows."
metadata:
  author: Stephen Rogan
  version: "1.0.0"
  tier: tier-5-mega-manager
  role: AI governance operator
  cadence: monthly and before deployment
---

# Agent Risk Governance

## Overview

Use this skill to support the leader as **AI governance operator** in a mega-manager operating model. A practical governance layer that enables agent leverage without pretending risk disappears.

A mega manager is not a person who passively supervises more humans. It is a leader who manages a portfolio of humans, AI agents, workflows, memory, tools, evals, and approval gates. The agent expands span of control only when the operating system is legible, governed, and reviewable.

## When to Use

Run this skill when:

- Agent will touch sensitive data or decisions
- Workflow has customer, HR, legal, finance, security, or reputation risk
- Autonomy level is increasing

Do not use this skill to bypass judgment, accountability, security, privacy, HR, legal, customer approval, or executive decision rights.

## Inputs

Gather:

- Agent/workflow description and autonomy level
- Data/tool access and external surfaces
- Risk class, business impact, and failure modes
- Existing policies and approval owners

If key inputs are missing, label assumptions and confidence. Do not invent tools, access, facts, policies, or authority.

## Workflow

Follow this sequence:

1. Classify workflow risk by data sensitivity, action reversibility, external impact, and decision authority
2. Define allowed actions, approval gates, and prohibited actions
3. Specify logging, review cadence, and incident response
4. Create rollback/kill switch and owner map
5. Write launch checklist and residual risk statement

Always finish by making the control loop visible: owner, current state, review point, approval boundary, and kill/rollback rule where relevant.

## Output Format

Use this structure:

```markdown
# Agent Risk Governance

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

- Agent governance brief
- Risk classification
- Approval and access matrix
- Incident/rollback plan
- Launch checklist

See `assets/output-template.md` for a reusable version.

## Human Decision Boundary

The agent may prepare, structure, evaluate, monitor, and recommend. The human leader owns final decisions, accountability, and risk acceptance. The agent must not cross these boundaries:

- Do not launch high-risk autonomy without explicit approval
- Do not treat audit logs as optional
- Accountable human owns residual risk

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

- NIST AI Risk Management Framework concepts
- Human-in-the-loop governance patterns
- Security least privilege and auditability principles

For the shared methodology spine, see `../../docs/SOURCE-SPINE.md`.
