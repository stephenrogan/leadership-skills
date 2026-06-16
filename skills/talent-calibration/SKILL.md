---
name: talent-calibration
description: "Prepares talent calibration material by assembling performance evidence, scope, growth trajectory, readiness hypotheses, risks, and development actions. Use before talent reviews, promotion discussions, succession conversations, or leadership bench planning."
license: MIT
compatibility: "Agent Skills compatible clients. No special tools required; optional file access helps when reading notes, docs, or metrics."
metadata:
  author: Stephen Rogan
  version: "1.0.0"
  tier: tier-3-people-and-org
  role: Talent developer
  cadence: quarterly or semiannual
---

# Talent Calibration

## Overview

Use this skill to support the leader as **Talent developer**. A calibration packet that improves evidence quality while keeping people judgments human-owned.

This skill is human-led by design: the agent prepares the work, but the human leader owns judgment, relationship, accountability, and final decisions.

## When to Use

Run this skill when:

- Talent review or calibration meeting is scheduled
- Promotion readiness is being debated
- Bench strength and development priorities need clarity

Do not use it as a substitute for legal, HR, finance, security, medical, or executive approval. If the workflow affects employment, compensation, customer commitments, external messaging, or sensitive personal data, prepare the packet and stop for human review.

## Inputs

Ask for or gather:

- Role expectations and scope
- Performance outcomes and behavioural examples
- Development history and feedback
- Business needs and future role requirements

If inputs are missing, proceed with explicit assumptions and label confidence. Do not invent private context, motives, or facts.

## Workflow

Follow this sequence:

1. Compile evidence by outcome, behaviour, scope, and trajectory
2. Identify gaps in evidence before making readiness claims
3. Separate current performance from future potential hypotheses
4. Draft development actions tied to next-scope requirements
5. Flag bias risks and missing perspectives

Before finalizing, run the boundary check: what is evidence, what is interpretation, what is a recommendation, and what must remain a human decision?

## Output Format

Produce a concise, decision-ready artifact using this structure:

```markdown
# Talent Calibration

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

- Talent calibration packet
- Promotion-readiness evidence map
- Development action plan
- Bias and evidence-gap checklist

See `assets/output-template.md` for a reusable version.

## Human Decision Boundary

The agent may prepare, synthesize, compare, draft, and track. The agent must not cross these boundaries:

- Do not assign definitive labels like high/low potential as fact
- Do not decide promotion, rating, pay, or succession status
- Leaders own sponsorship and people decisions

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

- Leadership Pipeline: role transitions and readiness
- HBR talent calibration practices
- Bias-aware performance review practices

For the shared methodology spine, see `../../docs/SOURCE-SPINE.md`.
