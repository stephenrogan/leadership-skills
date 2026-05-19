---
name: executive-update-brief
description: "Creates an executive-ready update brief with headline narrative, evidence, risks, decisions needed, owner asks, and anticipated questions. Use for exec staff updates, QBRs, board prep, steering meetings, or when leaders need concise upward communication."
license: MIT
compatibility: "Agent Skills compatible clients. No special tools required; optional file access helps when reading notes, docs, or metrics."
metadata:
  author: Stephen Rogan
  version: "1.0.0"
  tier: tier-2-leadership-judgment
  role: Executive communicator
  cadence: weekly, monthly, or event-driven
---

# Executive Update Brief

## Overview

Use this skill to support the leader as **Executive communicator**. A brief that tells executives what changed, why it matters, and what decision or support is needed.

This skill is HUMAN+ by design: the agent prepares the work, but the human leader owns judgment, relationship, accountability, and final decisions.

## When to Use

Run this skill when:

- Executive update is due
- A metric moved and needs explanation
- Leader needs support, air cover, or a decision from above

Do not use it as a substitute for legal, HR, finance, security, medical, or executive approval. If the workflow affects employment, compensation, customer commitments, external messaging, or sensitive personal data, prepare the packet and stop for human review.

## Inputs

Ask for or gather:

- Metrics and trend changes
- Strategic context and prior commitments
- Risks, mitigations, and decision asks
- Audience priorities and likely questions

If inputs are missing, proceed with explicit assumptions and label confidence. Do not invent private context, motives, or facts.

## Workflow

Follow this sequence:

1. Start with the executive headline, not background
2. Support every claim with evidence or mark it as hypothesis
3. Separate update, risk, and decision ask
4. Add anticipated questions and crisp answers
5. End with owner, timeline, and requested decision

Before finalizing, run the boundary check: what is evidence, what is interpretation, what is a recommendation, and what must remain a human decision?

## Output Format

Produce a concise, decision-ready artifact using this structure:

```markdown
# Executive Update Brief

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

- Executive brief
- Decision ask block
- Risk/mitigation summary
- FAQ and objection prep

See `assets/output-template.md` for a reusable version.

## Human Decision Boundary

The agent may prepare, synthesize, compare, draft, and track. The agent must not cross these boundaries:

- Do not over-polish weak evidence into certainty
- Do not make external claims or commitments
- Leader owns tone, accountability, and sensitive framing

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

- Barbara Minto, Pyramid Principle
- Amazon narrative memo practice
- Executive communication best practices

For the shared methodology spine, see `../../docs/SOURCE-SPINE.md`.
