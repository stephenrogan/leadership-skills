---
name: premortem-runner
description: Runs a structured pre-mortem for a plan, initiative, launch, reorg, or strategic bet by imagining failure, identifying causes, leading indicators, mitigations, owners, and pause or kill criteria. Use before committing to meaningful change.
license: MIT
compatibility: Agent Skills compatible clients. No special tools required; optional file access helps when reading notes, docs, or metrics.
metadata:
  author: Stephen Rogan
  version: "1.0.0"
  tier: tier-2-leadership-judgment
  role: Risk thinker
  cadence: event-driven
---

# Premortem Runner

## Overview

Use this skill to support the leader as **Risk thinker**. A realistic failure map before the failure happens.

This skill is HUMAN+ by design: the agent prepares the work, but the human leader owns judgment, relationship, accountability, and final decisions.

## When to Use

Run this skill when:

- Initiative is about to launch
- Plan has optimistic assumptions
- Failure would be expensive, reputational, or hard to reverse

Do not use it as a substitute for legal, HR, finance, security, medical, or executive approval. If the workflow affects employment, compensation, customer commitments, external messaging, or sensitive personal data, prepare the packet and stop for human review.

## Inputs

Ask for or gather:

- Plan summary and success criteria
- Timeline, dependencies, and owners
- Known risks and assumptions
- Stakeholder concerns

If inputs are missing, proceed with explicit assumptions and label confidence. Do not invent private context, motives, or facts.

## Workflow

Follow this sequence:

1. State the future failure in plain language
2. Generate operational, people, customer, technical, and political failure modes
3. Rank by likelihood, impact, detectability, and reversibility
4. Define leading indicators and mitigations
5. Set pause, rollback, or kill criteria

Before finalizing, run the boundary check: what is evidence, what is interpretation, what is a recommendation, and what must remain a human decision?

## Output Format

Produce a concise, decision-ready artifact using this structure:

```markdown
# Premortem Runner

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

- Pre-mortem brief
- Failure-mode register
- Mitigation plan
- Leading indicators
- Pause/kill criteria

See `assets/output-template.md` for a reusable version.

## Human Decision Boundary

The agent may prepare, synthesize, compare, draft, and track. The agent must not cross these boundaries:

- Do not confuse cynicism with risk management
- Do not block action because risk exists
- Leader decides what risk to accept

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

- Gary Klein, HBR: Performing a Project Premortem
- Risk register practices
- Change management readiness checks

For the shared methodology spine, see `../../docs/SOURCE-SPINE.md`.
