---
name: manager-one-on-one-prep
description: "Prepares a manager for high-quality 1:1s by synthesizing prior notes, commitments, performance signals, blockers, career goals, and coaching questions. Use when planning a direct report 1:1, skip-level, coaching check-in, or follow-up conversation."
license: MIT
compatibility: "Agent Skills compatible clients. No special tools required; optional file access helps when reading notes, docs, or metrics."
metadata:
  author: Stephen Rogan
  version: "1.0.0"
  tier: tier-1-manager-os
  role: Coach and context keeper
  cadence: weekly or biweekly
---

# Manager One On One Prep

## Overview

Use this skill to support the leader as **Coach and context keeper**. A focused 1:1 agenda, coaching prompts, open-loop list, and follow-up actions that help the manager show up prepared without outsourcing the relationship.

This skill is HUMAN+ by design: the agent prepares the work, but the human leader owns judgment, relationship, accountability, and final decisions.

## When to Use

Run this skill when:

- Recurring 1:1 or skip-level is due
- A direct report is stuck, quiet, overloaded, or drifting
- Open commitments from prior conversations need follow-through

Do not use it as a substitute for legal, HR, finance, security, medical, or executive approval. If the workflow affects employment, compensation, customer commitments, external messaging, or sensitive personal data, prepare the packet and stop for human review.

## Inputs

Ask for or gather:

- Prior 1:1 notes and action items
- Current priorities, goals, and blockers
- Recent wins, misses, customer/account signals, or peer feedback
- Career goals and development themes

If inputs are missing, proceed with explicit assumptions and label confidence. Do not invent private context, motives, or facts.

## Workflow

Follow this sequence:

1. Build a continuity brief from prior commitments and unresolved topics
2. Separate facts, observed patterns, and hypotheses about energy or performance
3. Choose at most three conversation priorities: execution, development, wellbeing, or decision support
4. Draft coaching questions before advice; include one direct feedback prompt only if evidence is specific
5. Create a follow-up log with owner, date, and success signal

Before finalizing, run the boundary check: what is evidence, what is interpretation, what is a recommendation, and what must remain a human decision?

## Output Format

Produce a concise, decision-ready artifact using this structure:

```markdown
# Manager One On One Prep

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

- 1:1 agenda with sections for check-in, priorities, coaching, decisions, and commitments
- Open-loop tracker
- Suggested coaching questions
- Follow-up summary draft

See `assets/output-template.md` for a reusable version.

## Human Decision Boundary

The agent may prepare, synthesize, compare, draft, and track. The agent must not cross these boundaries:

- Do not infer private motives from thin evidence
- Do not script manipulative or therapeutic language
- The manager chooses what to say, how direct to be, and what commitments to make

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

- Andy Grove, High Output Management: leverage and manager output
- Michael Bungay Stanier, The Coaching Habit: coaching questions before advice
- Google re:Work: manager 1:1 guidance

For the shared methodology spine, see `../../docs/SOURCE-SPINE.md`.
