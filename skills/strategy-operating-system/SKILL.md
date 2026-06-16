---
name: strategy-operating-system
description: "Turns strategy into an operating system with priorities, bets, decision calendar, metrics, operating cadence, owner map, risks, and kill criteria. Use for quarterly planning, annual planning, strategic resets, or converting executive direction into management rhythm."
license: MIT
compatibility: "Agent Skills compatible clients. No special tools required; optional file access helps when reading notes, docs, or metrics."
metadata:
  author: Stephen Rogan
  version: "1.0.0"
  tier: tier-4-strategic-influence
  role: Strategy-to-execution architect
  cadence: quarterly with weekly review
---

# Strategy Operating System

## Overview

Use this skill to support the leader as **Strategy-to-execution architect**. A strategy operating plan that connects ambition to cadence, ownership, evidence, and hard tradeoffs.

This skill is human-led by design: the agent prepares the work, but the human leader owns judgment, relationship, accountability, and final decisions.

## When to Use

Run this skill when:

- Strategy exists as slides but not operating motion
- Quarterly or annual planning is underway
- Priorities are too many, vague, or disconnected from cadence

Do not use it as a substitute for legal, HR, finance, security, medical, or executive approval. If the workflow affects employment, compensation, customer commitments, external messaging, or sensitive personal data, prepare the packet and stop for human review.

## Inputs

Ask for or gather:

- Strategic goals and constraints
- Current performance, risks, capacity, VOC, and economics
- Leadership team ownership and dependencies
- Existing rituals and decision forums

If inputs are missing, proceed with explicit assumptions and label confidence. Do not invent private context, motives, or facts.

## Workflow

Follow this sequence:

1. Translate strategy into 3-5 priority bets and explicit non-goals
2. Define leading and lagging metrics for each bet
3. Map owners, decision forums, and review cadence
4. Set risk watchlist and kill/pivot criteria
5. Create weekly/monthly/quarterly operating rhythm

Before finalizing, run the boundary check: what is evidence, what is interpretation, what is a recommendation, and what must remain a human decision?

## Output Format

Produce a concise, decision-ready artifact using this structure:

```markdown
# Strategy Operating System

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

- Strategy operating system brief
- Priority stack
- Decision calendar
- Cadence map
- Kill criteria

See `assets/output-template.md` for a reusable version.

## Human Decision Boundary

The agent may prepare, synthesize, compare, draft, and track. The agent must not cross these boundaries:

- Do not confuse synthesis with strategic choice
- Do not add priorities without cuts
- Leader owns strategy, resourcing, and tradeoffs

Stop and ask for explicit approval before sending messages, changing employment status, making customer promises, publishing, sharing sensitive information, or committing budget/resources.

## Quality Bar

A strong output for this skill:

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

- OKR and operating cadence practices
- Good Strategy/Bad Strategy principles
- Decision and operating review methods

For the shared methodology spine, see `../../docs/SOURCE-SPINE.md`.
