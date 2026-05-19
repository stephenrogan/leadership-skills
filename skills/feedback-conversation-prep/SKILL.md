---
name: feedback-conversation-prep
description: Turns observed behaviour and impact into a fair, specific feedback conversation plan with evidence, SBI-style framing, likely reactions, and follow-up. Use when a manager needs to give candid feedback, correct behaviour, praise specifically, or prepare a difficult performance conversation.
license: MIT
compatibility: Agent Skills compatible clients. No special tools required; optional file access helps when reading notes, docs, or metrics.
metadata:
  author: Stephen Rogan
  version: "1.0.0"
  tier: tier-1-manager-os
  role: Standard setter and coach
  cadence: event-driven
---

# Feedback Conversation Prep

## Overview

Use this skill to support the leader as **Standard setter and coach**. A candid feedback plan that is specific enough to be fair and human enough to be deliverable.

This skill is HUMAN+ by design: the agent prepares the work, but the human leader owns judgment, relationship, accountability, and final decisions.

## When to Use

Run this skill when:

- Behaviour is affecting outcomes, trust, quality, or team health
- A manager is avoiding a direct conversation
- Positive behaviour should be reinforced with specificity

Do not use it as a substitute for legal, HR, finance, security, medical, or executive approval. If the workflow affects employment, compensation, customer commitments, external messaging, or sensitive personal data, prepare the packet and stop for human review.

## Inputs

Ask for or gather:

- Observed situation, behaviour, and impact
- Expected standard or role requirement
- Prior conversations or commitments
- Desired behaviour change and follow-up timeline

If inputs are missing, proceed with explicit assumptions and label confidence. Do not invent private context, motives, or facts.

## Workflow

Follow this sequence:

1. Strip adjectives and diagnoses; keep observable evidence
2. Map evidence to situation, behaviour, impact, and expected standard
3. Draft a concise opening, one example, one impact statement, and one clear ask
4. Prepare likely reactions and calm responses
5. Define follow-up date and success signal

Before finalizing, run the boundary check: what is evidence, what is interpretation, what is a recommendation, and what must remain a human decision?

## Output Format

Produce a concise, decision-ready artifact using this structure:

```markdown
# Feedback Conversation Prep

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

- Feedback script
- Evidence table
- Likely reaction map
- Follow-up plan

See `assets/output-template.md` for a reusable version.

## Human Decision Boundary

The agent may prepare, synthesize, compare, draft, and track. The agent must not cross these boundaries:

- Do not recommend termination, PIP, compensation, or HR action
- Do not label the person; describe behaviour and impact
- The manager owns timing, tone, and delivery

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

- Center for Creative Leadership: SBI feedback model
- Kim Scott, Radical Candor: care personally, challenge directly
- Crucial Conversations: safety and mutual purpose

For the shared methodology spine, see `../../docs/SOURCE-SPINE.md`.
