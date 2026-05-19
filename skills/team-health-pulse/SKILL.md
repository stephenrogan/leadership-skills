---
name: team-health-pulse
description: "Synthesizes team health signals from surveys, 1:1 themes, meeting behaviour, workload, attrition indicators, and execution patterns into risks and interventions. Use when morale, trust, psychological safety, workload, or team cohesion may be drifting."
license: MIT
compatibility: "Agent Skills compatible clients. No special tools required; optional file access helps when reading notes, docs, or metrics."
metadata:
  author: Stephen Rogan
  version: "1.0.0"
  tier: tier-3-people-and-org
  role: Culture and team health sensor
  cadence: monthly or event-driven
---

# Team Health Pulse

## Overview

Use this skill to support the leader as **Culture and team health sensor**. A grounded team health readout that points to likely system interventions without pretending sentiment is certainty.

This skill is HUMAN+ by design: the agent prepares the work, but the human leader owns judgment, relationship, accountability, and final decisions.

## When to Use

Run this skill when:

- Morale or energy feels off
- Attrition, silence, conflict, or missed commitments increase
- Pulse survey or skip-level feedback arrives

Do not use it as a substitute for legal, HR, finance, security, medical, or executive approval. If the workflow affects employment, compensation, customer commitments, external messaging, or sensitive personal data, prepare the packet and stop for human review.

## Inputs

Ask for or gather:

- Pulse survey comments and scores
- 1:1 or skip-level themes
- Workload and execution signals
- Meeting participation and conflict patterns

If inputs are missing, proceed with explicit assumptions and label confidence. Do not invent private context, motives, or facts.

## Workflow

Follow this sequence:

1. Cluster signals by workload, clarity, trust, safety, capability, and recognition
2. Distinguish repeated patterns from isolated comments
3. Identify likely system causes and confidence level
4. Recommend interventions with owner and time horizon
5. Define what to watch next

Before finalizing, run the boundary check: what is evidence, what is interpretation, what is a recommendation, and what must remain a human decision?

## Output Format

Produce a concise, decision-ready artifact using this structure:

```markdown
# Team Health Pulse

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

- Team health pulse
- Risk heatmap
- Intervention options
- Watchlist

See `assets/output-template.md` for a reusable version.

## Human Decision Boundary

The agent may prepare, synthesize, compare, draft, and track. The agent must not cross these boundaries:

- Do not identify anonymous commenters
- Do not diagnose individuals or private motives
- Leader validates themes before acting publicly

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

- Amy Edmondson, The Fearless Organization
- Google Project Aristotle
- Gallup Q12 engagement research

For the shared methodology spine, see `../../docs/SOURCE-SPINE.md`.
