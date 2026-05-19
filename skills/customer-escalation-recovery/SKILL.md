---
name: customer-escalation-recovery
description: Builds an executive customer escalation recovery brief with timeline, commitments, stakeholders, risk exposure, root-cause hypotheses, response plan, and approval-required concessions. Use for major customer escalations, renewal threats, executive complaints, or service failures.
license: MIT
compatibility: Agent Skills compatible clients. No special tools required; optional file access helps when reading notes, docs, or metrics.
metadata:
  author: Stephen Rogan
  version: "1.0.0"
  tier: tier-4-strategic-influence
  role: Customer risk and trust restorer
  cadence: event-driven
---

# Customer Escalation Recovery

## Overview

Use this skill to support the leader as **Customer risk and trust restorer**. A recovery plan that restores control, clarity, and trust without making unauthorized promises.

This skill is HUMAN+ by design: the agent prepares the work, but the human leader owns judgment, relationship, accountability, and final decisions.

## When to Use

Run this skill when:

- Customer escalation is executive-visible
- Renewal, expansion, or reputation is at risk
- Internal teams disagree on cause or next action

Do not use it as a substitute for legal, HR, finance, security, medical, or executive approval. If the workflow affects employment, compensation, customer commitments, external messaging, or sensitive personal data, prepare the packet and stop for human review.

## Inputs

Ask for or gather:

- Customer/account history and contract context
- Issue timeline and prior commitments
- Internal owners, blockers, and root-cause hypotheses
- Customer stakeholders and desired outcome

If inputs are missing, proceed with explicit assumptions and label confidence. Do not invent private context, motives, or facts.

## Workflow

Follow this sequence:

1. Reconstruct chronology and separate facts from claims
2. Identify customer impact, business exposure, and trust damage
3. Map internal owners and decision blockers
4. Draft recovery plan with immediate, corrective, and preventive actions
5. Flag any concession, promise, legal, or commercial statement requiring approval

Before finalizing, run the boundary check: what is evidence, what is interpretation, what is a recommendation, and what must remain a human decision?

## Output Format

Produce a concise, decision-ready artifact using this structure:

```markdown
# Customer Escalation Recovery

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

- Escalation brief
- Customer response draft
- Internal owner map
- Recovery plan
- Approval-required items

See `assets/output-template.md` for a reusable version.

## Human Decision Boundary

The agent may prepare, synthesize, compare, draft, and track. The agent must not cross these boundaries:

- Do not send customer messages automatically
- Do not promise concessions, refunds, timelines, legal positions, or roadmap commitments
- Leader owns external communication and commercial tradeoffs

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

- Service recovery principles
- Moments of Truth customer experience thinking
- Executive escalation practices

For the shared methodology spine, see `../../docs/SOURCE-SPINE.md`.
