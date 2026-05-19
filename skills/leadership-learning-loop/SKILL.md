---
name: leadership-learning-loop
description: Runs a leadership learning loop by reviewing decisions, outcomes, missed signals, behaviour patterns, system failures, and commitments for improvement. Use after failed decisions, incidents, missed forecasts, team friction, or monthly leadership retrospectives.
license: MIT
compatibility: Agent Skills compatible clients. No special tools required; optional file access helps when reading notes, docs, or metrics.
metadata:
  author: Stephen Rogan
  version: "1.0.0"
  tier: tier-4-strategic-influence
  role: Reflective system improver
  cadence: weekly, monthly, or post-incident
---

# Leadership Learning Loop

## Overview

Use this skill to support the leader as **Reflective system improver**. A leadership retro that turns outcomes into sharper judgment and better systems.

This skill is HUMAN+ by design: the agent prepares the work, but the human leader owns judgment, relationship, accountability, and final decisions.

## When to Use

Run this skill when:

- Decision or initiative did not produce expected outcome
- Team incident, missed forecast, or escalation occurred
- Leader wants to identify repeated personal or system patterns

Do not use it as a substitute for legal, HR, finance, security, medical, or executive approval. If the workflow affects employment, compensation, customer commitments, external messaging, or sensitive personal data, prepare the packet and stop for human review.

## Inputs

Ask for or gather:

- Decision records and assumptions
- Outcome data and timeline
- Feedback, meeting notes, and incident facts
- Leader commitments and operating norms

If inputs are missing, proceed with explicit assumptions and label confidence. Do not invent private context, motives, or facts.

## Workflow

Follow this sequence:

1. Reconstruct what was believed, decided, and expected
2. Compare outcome to assumptions and leading indicators
3. Identify missed signals, delayed conversations, and system gaps
4. Separate personal leadership behaviour from structural failure
5. Create one behaviour commitment and one system fix

Before finalizing, run the boundary check: what is evidence, what is interpretation, what is a recommendation, and what must remain a human decision?

## Output Format

Produce a concise, decision-ready artifact using this structure:

```markdown
# Leadership Learning Loop

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

- Leadership retro
- Missed-signal analysis
- Behaviour commitment
- System fix list
- Follow-up check date

See `assets/output-template.md` for a reusable version.

## Human Decision Boundary

The agent may prepare, synthesize, compare, draft, and track. The agent must not cross these boundaries:

- Do not turn reflection into self-flagellation or blame theatre
- Do not infer private psychology
- Leader owns self-awareness and behaviour change

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

- After-action review practices
- Double-loop learning
- Psychological safety and blameless retro principles

For the shared methodology spine, see `../../docs/SOURCE-SPINE.md`.
