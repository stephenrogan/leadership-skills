---
name: performance-cycle
description: "Assembles fair performance review or improvement-cycle material by organizing evidence against role expectations, strengths, gaps, support actions, and follow-up criteria. Use for review cycles, repeated misses, growth plans, or performance concern preparation."
license: MIT
compatibility: "Agent Skills compatible clients. No special tools required; optional file access helps when reading notes, docs, or metrics."
metadata:
  author: Stephen Rogan
  version: "1.0.0"
  tier: tier-3-people-and-org
  role: Fairness and standards operator
  cadence: quarterly or event-driven
---

# Performance Cycle

## Overview

Use this skill to support the leader as **Fairness and standards operator**. A balanced evidence packet that supports fair human judgment without automating employment decisions.

This skill is HUMAN+ by design: the agent prepares the work, but the human leader owns judgment, relationship, accountability, and final decisions.

## When to Use

Run this skill when:

- Review cycle is approaching
- Repeated performance issue needs structured evidence
- Promotion, growth plan, or performance concern needs clarity

Do not use it as a substitute for legal, HR, finance, security, medical, or executive approval. If the workflow affects employment, compensation, customer commitments, external messaging, or sensitive personal data, prepare the packet and stop for human review.

## Inputs

Ask for or gather:

- Role expectations and goals
- Outcome evidence and examples
- Feedback history and prior commitments
- Support provided and context constraints

If inputs are missing, proceed with explicit assumptions and label confidence. Do not invent private context, motives, or facts.

## Workflow

Follow this sequence:

1. Map evidence to role expectations and goals
2. Separate pattern from isolated incident
3. Balance strengths, gaps, context, and support actions
4. Draft review language that is specific and behaviour-based
5. Define follow-up criteria and manager-owned next steps

Before finalizing, run the boundary check: what is evidence, what is interpretation, what is a recommendation, and what must remain a human decision?

## Output Format

Produce a concise, decision-ready artifact using this structure:

```markdown
# Performance Cycle

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

- Performance evidence packet
- Strength/gap summary
- Growth or improvement plan draft
- Fairness check

See `assets/output-template.md` for a reusable version.

## Human Decision Boundary

The agent may prepare, synthesize, compare, draft, and track. The agent must not cross these boundaries:

- Do not make ratings, compensation, PIP, termination, or legal recommendations
- Do not label potential or character from partial data
- Manager and HR own employment decisions

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

- Google re:Work performance management resources
- Radical Candor: direct and caring feedback
- HBR performance review fairness principles

For the shared methodology spine, see `../../docs/SOURCE-SPINE.md`.
