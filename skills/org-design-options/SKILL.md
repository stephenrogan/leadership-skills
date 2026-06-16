---
name: org-design-options
description: "Generates organisation design options with strategy fit, customer segmentation, capacity, spans, roles, tradeoffs, transition risks, and communication implications. Use when growth, churn, margin, coverage, or strategy changes require rethinking team structure."
license: MIT
compatibility: "Agent Skills compatible clients. No special tools required; optional file access helps when reading notes, docs, or metrics."
metadata:
  author: Stephen Rogan
  version: "1.0.0"
  tier: tier-4-strategic-influence
  role: Org architect
  cadence: quarterly or event-driven
---

# Org Design Options

## Overview

Use this skill to support the leader as **Org architect**. A set of org design options with explicit tradeoffs instead of a single overconfident structure.

This skill is human-led by design: the agent prepares the work, but the human leader owns judgment, relationship, accountability, and final decisions.

## When to Use

Run this skill when:

- Current structure no longer fits strategy or scale
- Coverage, capacity, or customer experience is breaking
- Leader needs options before changing roles or reporting lines

Do not use it as a substitute for legal, HR, finance, security, medical, or executive approval. If the workflow affects employment, compensation, customer commitments, external messaging, or sensitive personal data, prepare the packet and stop for human review.

## Inputs

Ask for or gather:

- Strategic priorities and customer segments
- Current org, roles, capacity, and performance
- Customer economics and risk profile
- Constraints, transition timing, and talent realities

If inputs are missing, proceed with explicit assumptions and label confidence. Do not invent private context, motives, or facts.

## Workflow

Follow this sequence:

1. Clarify design principles and non-goals
2. Generate 2-4 viable models, including status quo if credible
3. Assess each model for customer impact, manager load, cost, risk, and reversibility
4. Identify transition risks, communications, and sequencing
5. Recommend decision questions rather than pretending the spreadsheet decides

Before finalizing, run the boundary check: what is evidence, what is interpretation, what is a recommendation, and what must remain a human decision?

## Output Format

Produce a concise, decision-ready artifact using this structure:

```markdown
# Org Design Options

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

- Org design option set
- Tradeoff matrix
- Transition risk map
- Decision questions
- Communication implications

See `assets/output-template.md` for a reusable version.

## Human Decision Boundary

The agent may prepare, synthesize, compare, draft, and track. The agent must not cross these boundaries:

- Do not decide reporting lines, layoffs, compensation, or people moves
- Do not hide human impact behind efficiency language
- Executive leader owns design choice and sequencing

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

- Operating model and org design principles
- Grove: leverage and managerial output
- Leadership Pipeline role-scope transitions

For the shared methodology spine, see `../../docs/SOURCE-SPINE.md`.
