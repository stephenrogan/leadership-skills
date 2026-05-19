---
name: market-and-board-narrative
description: Builds a board or market narrative from internal performance, customer evidence, market shifts, competitive signals, strategic bets, and decision asks. Use for board decks, investor updates, strategic narratives, or executive alignment around what the business believes now.
license: MIT
compatibility: Agent Skills compatible clients. No special tools required; optional file access helps when reading notes, docs, or metrics.
metadata:
  author: Stephen Rogan
  version: "1.0.0"
  tier: tier-4-strategic-influence
  role: Strategic narrator
  cadence: quarterly or event-driven
---

# Market And Board Narrative

## Overview

Use this skill to support the leader as **Strategic narrator**. A narrative with an evidence spine, not executive theatre.

This skill is HUMAN+ by design: the agent prepares the work, but the human leader owns judgment, relationship, accountability, and final decisions.

## When to Use

Run this skill when:

- Board, investor, or executive narrative is needed
- Internal data must connect to market story
- Leadership needs a clear “what we believe now” memo

Do not use it as a substitute for legal, HR, finance, security, medical, or executive approval. If the workflow affects employment, compensation, customer commitments, external messaging, or sensitive personal data, prepare the packet and stop for human review.

## Inputs

Ask for or gather:

- Performance and customer evidence
- Market and competitive signals
- Strategic bets and risks
- Audience context and decision asks

If inputs are missing, proceed with explicit assumptions and label confidence. Do not invent private context, motives, or facts.

## Workflow

Follow this sequence:

1. State the central narrative claim and confidence level
2. Build evidence spine from internal and external signals
3. Separate facts, interpretation, and strategic belief
4. Identify narrative risks, weak evidence, and expected objections
5. Convert into board-ready storyline and decision asks

Before finalizing, run the boundary check: what is evidence, what is interpretation, what is a recommendation, and what must remain a human decision?

## Output Format

Produce a concise, decision-ready artifact using this structure:

```markdown
# Market And Board Narrative

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

- Narrative memo
- Evidence spine
- Risk and objection brief
- Board-ready storyline
- Decision asks

See `assets/output-template.md` for a reusable version.

## Human Decision Boundary

The agent may prepare, synthesize, compare, draft, and track. The agent must not cross these boundaries:

- Do not overclaim market certainty
- Do not expose private or sensitive data externally
- Leader owns claims, confidence, and audience positioning

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

- Minto Pyramid Principle
- Board communication practices
- Competitive and customer evidence synthesis

For the shared methodology spine, see `../../docs/SOURCE-SPINE.md`.
