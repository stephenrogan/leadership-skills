---
name: conflict-mediation-prep
description: "Prepares a neutral conflict mediation plan by separating facts, interpretations, interests, stakes, possible agreements, conversation structure, and follow-up commitments. Use when two people, teams, or functions are stuck in recurring tension or blame."
license: MIT
compatibility: "Agent Skills compatible clients. No special tools required; optional file access helps when reading notes, docs, or metrics."
metadata:
  author: Stephen Rogan
  version: "1.0.0"
  tier: tier-3-people-and-org
  role: Conflict de-escalator
  cadence: event-driven
---

# Conflict Mediation Prep

## Overview

Use this skill to support the leader as **Conflict de-escalator**. A mediation prep brief that helps the leader reduce heat and get to interests, commitments, and next behaviour.

This skill is HUMAN+ by design: the agent prepares the work, but the human leader owns judgment, relationship, accountability, and final decisions.

## When to Use

Run this skill when:

- Conflict is slowing work or damaging trust
- Two sides describe the same situation differently
- Leader needs to mediate without becoming partisan

Do not use it as a substitute for legal, HR, finance, security, medical, or executive approval. If the workflow affects employment, compensation, customer commitments, external messaging, or sensitive personal data, prepare the packet and stop for human review.

## Inputs

Ask for or gather:

- Narratives from each side
- Known facts and disputed interpretations
- Desired outcomes and constraints
- History of prior attempts to resolve

If inputs are missing, proceed with explicit assumptions and label confidence. Do not invent private context, motives, or facts.

## Workflow

Follow this sequence:

1. Separate facts, stories, interests, and asks
2. Name common goal and cost of unresolved conflict
3. Draft neutral opening and conversation rules
4. Generate questions that reveal interests and tradeoffs
5. Define agreement, follow-up, and escalation path

Before finalizing, run the boundary check: what is evidence, what is interpretation, what is a recommendation, and what must remain a human decision?

## Output Format

Produce a concise, decision-ready artifact using this structure:

```markdown
# Conflict Mediation Prep

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

- Conflict canvas
- Neutral mediation agenda
- Question guide
- Agreement summary template

See `assets/output-template.md` for a reusable version.

## Human Decision Boundary

The agent may prepare, synthesize, compare, draft, and track. The agent must not cross these boundaries:

- Do not adjudicate serious HR, harassment, legal, or safety issues
- Do not force false equivalence when facts are clear
- Leader decides whether to mediate, escalate, or involve HR/legal

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

- Getting to Yes: interests over positions
- Crucial Conversations
- HBR conflict management practices

For the shared methodology spine, see `../../docs/SOURCE-SPINE.md`.
