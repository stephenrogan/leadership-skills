---
name: stakeholder-prewire
description: "Builds a stakeholder prewire plan with influence map, likely objections, conversation sequence, audience-specific framing, decision asks, and alignment tracker. Use before cross-functional proposals, executive decisions, process changes, or politically sensitive initiatives."
license: MIT
compatibility: "Agent Skills compatible clients. No special tools required; optional file access helps when reading notes, docs, or metrics."
metadata:
  author: Stephen Rogan
  version: "1.0.0"
  tier: tier-2-leadership-judgment
  role: Organisational influencer
  cadence: event-driven
---

# Stakeholder Prewire

## Overview

Use this skill to support the leader as **Organisational influencer**. A prewire plan that gets alignment before the meeting instead of hoping the meeting creates it.

This skill is HUMAN+ by design: the agent prepares the work, but the human leader owns judgment, relationship, accountability, and final decisions.

## When to Use

Run this skill when:

- Decision requires people who do not report to the leader
- A proposal could trigger objections or territorial conflict
- Exec meeting should not be the first time stakeholders hear the idea

Do not use it as a substitute for legal, HR, finance, security, medical, or executive approval. If the workflow affects employment, compensation, customer commitments, external messaging, or sensitive personal data, prepare the packet and stop for human review.

## Inputs

Ask for or gather:

- Proposal or decision memo
- Stakeholder list and influence levels
- Known incentives, objections, and dependencies
- Desired decision and fallback options

If inputs are missing, proceed with explicit assumptions and label confidence. Do not invent private context, motives, or facts.

## Workflow

Follow this sequence:

1. Map stakeholders by influence, impact, support, and likely concern
2. Sequence conversations from allies to blockers to decision-makers
3. Tailor the message to each stakeholder’s incentives and risk lens
4. Prepare objection responses and concessions that do not violate principles
5. Track alignment status and unresolved issues

Before finalizing, run the boundary check: what is evidence, what is interpretation, what is a recommendation, and what must remain a human decision?

## Output Format

Produce a concise, decision-ready artifact using this structure:

```markdown
# Stakeholder Prewire

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

- Stakeholder map
- Prewire sequence
- Conversation briefs
- Objection response guide
- Alignment tracker

See `assets/output-template.md` for a reusable version.

## Human Decision Boundary

The agent may prepare, synthesize, compare, draft, and track. The agent must not cross these boundaries:

- Do not manipulate or misrepresent tradeoffs
- Do not promise concessions without approval
- Human leader owns relationship capital and live negotiation

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

- Michael Watkins, The First 90 Days: stakeholder mapping
- Influence without authority practices
- Minto Pyramid Principle for structured persuasion

For the shared methodology spine, see `../../docs/SOURCE-SPINE.md`.
