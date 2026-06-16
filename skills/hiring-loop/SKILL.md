---
name: hiring-loop
description: "Creates a structured hiring loop with role scorecard, competencies, interview plan, question bank, evidence rubric, debrief packet, and bias checks. Use when opening a role, designing interviews, consolidating feedback, or preparing a hire/no-hire debrief."
license: MIT
compatibility: "Agent Skills compatible clients. No special tools required; optional file access helps when reading notes, docs, or metrics."
metadata:
  author: Stephen Rogan
  version: "1.0.0"
  tier: tier-3-people-and-org
  role: Team builder
  cadence: per role or candidate loop
---

# Hiring Loop

## Overview

Use this skill to support the leader as **Team builder**. A hiring loop that evaluates evidence against role needs instead of vibes and recency bias.

This skill is human-led by design: the agent prepares the work, but the human leader owns judgment, relationship, accountability, and final decisions.

## When to Use

Run this skill when:

- New or replacement role is approved
- Interview loop needs design
- Candidate feedback is scattered or inconsistent

Do not use it as a substitute for legal, HR, finance, security, medical, or executive approval. If the workflow affects employment, compensation, customer commitments, external messaging, or sensitive personal data, prepare the packet and stop for human review.

## Inputs

Ask for or gather:

- Role outcomes and competencies
- Must-have and nice-to-have requirements
- Interview notes and scorecards
- Team gaps and ramp expectations

If inputs are missing, proceed with explicit assumptions and label confidence. Do not invent private context, motives, or facts.

## Workflow

Follow this sequence:

1. Define role outcomes before interview questions
2. Map each interview to competencies and evidence needed
3. Create behavioural questions and score rubric
4. Consolidate debrief evidence by competency
5. Flag missing evidence, inconsistencies, and possible bias

Before finalizing, run the boundary check: what is evidence, what is interpretation, what is a recommendation, and what must remain a human decision?

## Output Format

Produce a concise, decision-ready artifact using this structure:

```markdown
# Hiring Loop

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

- Role scorecard
- Interview loop plan
- Question bank
- Debrief packet
- Evidence-gap and bias checklist

See `assets/output-template.md` for a reusable version.

## Human Decision Boundary

The agent may prepare, synthesize, compare, draft, and track. The agent must not cross these boundaries:

- Do not make final hire/no-hire or compensation decision
- Do not infer protected characteristics or cultural fit vaguely
- Hiring manager owns final judgment and legal compliance

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

- Google re:Work structured interviewing
- Laszlo Bock, Work Rules!
- Structured interview validity research

For the shared methodology spine, see `../../docs/SOURCE-SPINE.md`.
