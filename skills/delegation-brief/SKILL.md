---
name: delegation-brief
description: "Converts fuzzy delegation into a crisp ownership brief with outcome, context, constraints, decision rights, checkpoints, risks, and success criteria. Use when handing work to a direct report, project owner, team lead, or cross-functional partner."
license: MIT
compatibility: "Agent Skills compatible clients. No special tools required; optional file access helps when reading notes, docs, or metrics."
metadata:
  author: Stephen Rogan
  version: "1.0.0"
  tier: tier-1-manager-os
  role: Leverage builder
  cadence: event-driven
---

# Delegation Brief

## Overview

Use this skill to support the leader as **Leverage builder**. A delegation brief that prevents rework, micromanagement, and unclear authority.

This skill is HUMAN+ by design: the agent prepares the work, but the human leader owns judgment, relationship, accountability, and final decisions.

## When to Use

Run this skill when:

- A leader is holding work someone else should own
- A task has been delegated but expectations are vague
- A project needs explicit decision rights and checkpoints

Do not use it as a substitute for legal, HR, finance, security, medical, or executive approval. If the workflow affects employment, compensation, customer commitments, external messaging, or sensitive personal data, prepare the packet and stop for human review.

## Inputs

Ask for or gather:

- Desired outcome and why it matters
- Deadline, constraints, and dependencies
- Owner capability and task-relevant maturity
- Decision rights and escalation threshold

If inputs are missing, proceed with explicit assumptions and label confidence. Do not invent private context, motives, or facts.

## Workflow

Follow this sequence:

1. Define the outcome, not the activity list
2. State non-negotiables, constraints, and known risks
3. Choose an authority level: recommend, decide within bounds, or fully own
4. Set checkpoint cadence based on risk and owner readiness
5. Write success criteria and escalation rules

Before finalizing, run the boundary check: what is evidence, what is interpretation, what is a recommendation, and what must remain a human decision?

## Output Format

Produce a concise, decision-ready artifact using this structure:

```markdown
# Delegation Brief

## Situation
[Brief context and why this workflow is being run.]

## Evidence and Signals
- Fact:
- Pattern:
- Hypothesis, confidence:

## Recommended Focus
1. [Highest leverage focus]
2. [Second focus]
3. [Third focus, optional]

## Working Artifact
[Agenda, memo, brief, plan, map, script, or tracker depending on the workflow.]

## Human Decisions Required
- [Decision/action the agent must not take.]

## Follow-Up
- Owner:
- Date:
- Success signal:
```

Expected deliverables:

- Delegation brief
- Decision-rights statement
- Checkpoint plan
- Definition of done

See `assets/output-template.md` for a reusable version.

## Human Decision Boundary

The agent may prepare, synthesize, compare, draft, and track. The agent must not cross these boundaries:

- Do not delegate accountability the leader legally or ethically owns
- Do not hide risk or ambiguity from the owner
- Leader chooses authority level and remains accountable for the system

Stop and ask for explicit approval before sending messages, changing employment status, making customer promises, publishing, sharing sensitive information, or committing budget/resources.

## Quality Bar

A world-class output for this skill:

- Separates facts, interpretations, hypotheses, and recommendations.
- Names uncertainty and missing context instead of hiding it.
- Produces an artifact a busy leader can use immediately.
- Reduces avoidance, ambiguity, rework, or decision drift.
- Makes the human judgment boundary visible.
- Includes concrete follow-up with owner, date, and success signal where applicable.

## Failure Modes

Watch for these mistakes:

- Overconfident claims from thin notes or sentiment.
- Generic management advice with no artifact.
- Automating sensitive judgment instead of preparing it.
- Producing too many options without a recommended default.
- Treating leadership as text generation rather than accountability.

## References

- Andy Grove, High Output Management: task-relevant maturity
- RACI/DACI decision-rights practice
- The Coaching Habit: ask before telling

For the shared methodology spine, see `../../docs/SOURCE-SPINE.md`.
