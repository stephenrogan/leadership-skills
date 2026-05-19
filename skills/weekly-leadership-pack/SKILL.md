---
name: weekly-leadership-pack
description: Synthesizes the weekly leadership picture across metrics, risks, people, customers, priorities, and decisions into a one-page operating brief. Use before weekly business reviews, leadership team meetings, Monday planning, or Friday retrospectives.
license: MIT
compatibility: Agent Skills compatible clients. No special tools required; optional file access helps when reading notes, docs, or metrics.
metadata:
  author: Stephen Rogan
  version: "1.0.0"
  tier: tier-1-manager-os
  role: Sensemaker and operator
  cadence: weekly
---

# Weekly Leadership Pack

## Overview

Use this skill to support the leader as **Sensemaker and operator**. A weekly narrative that shows what changed, what matters, what is stuck, and what decisions are required.

This skill is HUMAN+ by design: the agent prepares the work, but the human leader owns judgment, relationship, accountability, and final decisions.

## When to Use

Run this skill when:

- Weekly leadership review is due
- Metrics exist but the story is unclear
- The team is busy but decision requirements are hidden

Do not use it as a substitute for legal, HR, finance, security, medical, or executive approval. If the workflow affects employment, compensation, customer commitments, external messaging, or sensitive personal data, prepare the packet and stop for human review.

## Inputs

Ask for or gather:

- Forecast, risk, performance, capacity, VOC, and process updates
- Prior weekly commitments
- Current priorities and decision log
- Known customer or people escalations

If inputs are missing, proceed with explicit assumptions and label confidence. Do not invent private context, motives, or facts.

## Workflow

Follow this sequence:

1. Identify meaningful changes since last week
2. Separate metric movement from explanatory narrative
3. Rank risks by consequence and reversibility
4. Surface decisions required from the leader or exec team
5. Close with owner/date/action follow-through

Before finalizing, run the boundary check: what is evidence, what is interpretation, what is a recommendation, and what must remain a human decision?

## Output Format

Produce a concise, decision-ready artifact using this structure:

```markdown
# Weekly Leadership Pack

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

- One-page weekly pack
- Top 5 risks/opportunities
- Decision queue
- Open-loop tracker
- Suggested meeting agenda

See `assets/output-template.md` for a reusable version.

## Human Decision Boundary

The agent may prepare, synthesize, compare, draft, and track. The agent must not cross these boundaries:

- Do not invent explanations for metric movement
- Do not turn every weak signal into a crisis
- Leader owns narrative, escalation, and prioritisation

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

- Grove: managerial output through teams
- Operating review best practices
- Decision-log and action-log practices

For the shared methodology spine, see `../../docs/SOURCE-SPINE.md`.
