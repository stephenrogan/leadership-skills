---
name: decision-memo
description: "Creates a concise decision memo with context, decision required, options, tradeoffs, assumptions, dissent, recommendation, owner, and revisit criteria. Use when a leadership decision has ambiguity, cross-functional impact, material risk, or is likely to be reopened later."
license: MIT
compatibility: "Agent Skills compatible clients. No special tools required; optional file access helps when reading notes, docs, or metrics."
metadata:
  author: Stephen Rogan
  version: "1.0.0"
  tier: tier-2-leadership-judgment
  role: Decision architect
  cadence: event-driven
---

# Decision Memo

## Overview

Use this skill to support the leader as **Decision architect**. A decision-ready memo that makes tradeoffs explicit and prevents decision amnesia.

This skill is HUMAN+ by design: the agent prepares the work, but the human leader owns judgment, relationship, accountability, and final decisions.

## When to Use

Run this skill when:

- Material decision needs to be made
- Teams keep re-litigating the same choice
- Options, constraints, or ownership are unclear

Do not use it as a substitute for legal, HR, finance, security, medical, or executive approval. If the workflow affects employment, compensation, customer commitments, external messaging, or sensitive personal data, prepare the packet and stop for human review.

## Inputs

Ask for or gather:

- Decision statement and context
- Options considered
- Data, constraints, risks, and dependencies
- Stakeholders and dissenting views

If inputs are missing, proceed with explicit assumptions and label confidence. Do not invent private context, motives, or facts.

## Workflow

Follow this sequence:

1. Write the decision as a question with owner and deadline
2. Limit options to 2-4 real choices, including status quo if relevant
3. For each option, state upside, downside, cost, reversibility, and second-order effect
4. Name assumptions and what would change the decision
5. Record recommendation, dissent, final decision, and revisit trigger

Before finalizing, run the boundary check: what is evidence, what is interpretation, what is a recommendation, and what must remain a human decision?

## Output Format

Produce a concise, decision-ready artifact using this structure:

```markdown
# Decision Memo

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

- One-page decision memo
- Options/tradeoff table
- Assumption and dissent log
- Decision record

See `assets/output-template.md` for a reusable version.

## Human Decision Boundary

The agent may prepare, synthesize, compare, draft, and track. The agent must not cross these boundaries:

- Do not make the final decision unless explicitly asked and authorized
- Do not hide uncertainty to make the memo cleaner
- Human leader owns values, risk appetite, and accountability

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

- Amazon narrative memo practice
- Kahneman/Sibony/Sunstein, Noise: decision hygiene
- Atlassian DACI decision practice

For the shared methodology spine, see `../../docs/SOURCE-SPINE.md`.
