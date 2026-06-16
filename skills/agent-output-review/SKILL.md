---
name: agent-output-review
description: "Reviews AI agent outputs for correctness, evidence, completeness, safety, decision boundaries, and usability before a leader relies on them. Use when evaluating reports, drafts, code, research, strategy memos, customer responses, or autonomous agent deliverables."
license: MIT
compatibility: "Agent Skills compatible clients. Optional file, terminal, web, and repository access improve agent-operations workflows."
metadata:
  author: Stephen Rogan
  version: "1.0.0"
  tier: tier-5-mega-manager
  role: Quality gatekeeper
  cadence: per agent output
---

# Agent Output Review

## Overview

Use this skill to support the leader as **Quality gatekeeper** in a mega-manager operating model. A disciplined review that treats agent output as work product requiring verification, not truth.

A mega manager is not a person who passively supervises more humans. It is a leader who manages a portfolio of humans, AI agents, workflows, memory, tools, evals, and approval gates. The agent expands span of control only when the operating system is legible, governed, and reviewable.

## When to Use

Run this skill when:

- Agent produced a deliverable that may influence a decision
- Output will be shared, acted on, or used for sensitive work
- Leader needs to decide whether to accept, revise, or reject agent work

Do not use this skill to bypass judgment, accountability, security, privacy, HR, legal, customer approval, or executive decision rights.

## Inputs

Gather:

- Agent output and original task brief
- Source material, files, data, or citations
- Known constraints and approval boundaries
- Quality bar or acceptance criteria

If key inputs are missing, label assumptions and confidence. Do not invent tools, access, facts, policies, or authority.

## Workflow

Follow this sequence:

1. Compare output against the original brief and acceptance criteria
2. Separate supported claims from unsupported claims and hallucination risk
3. Check for missing edge cases, unsafe recommendations, and boundary overreach
4. Score usability: can a busy leader act on this now?
5. Return accept/revise/reject verdict with specific fixes

Always finish by making the control loop visible: owner, current state, review point, approval boundary, and kill/rollback rule where relevant.

## Output Format

Use this structure:

```markdown
# Agent Output Review

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

- Agent output review
- Evidence gap list
- Safety and boundary findings
- Accept/revise/reject verdict
- Fix instructions

See `assets/output-template.md` for a reusable version.

## Human Decision Boundary

The agent may prepare, structure, evaluate, monitor, and recommend. The agent must not cross these boundaries:

- Do not rubber-stamp because the prose is polished
- Do not accept claims without evidence when action risk is high
- Human leader owns final acceptance and downstream use

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

- Eval-driven skill development from Agent Skills docs
- AI assurance and human-in-the-loop review patterns
- Kahneman decision hygiene: separate evidence from judgment

For the shared methodology spine, see `../../docs/SOURCE-SPINE.md`.
