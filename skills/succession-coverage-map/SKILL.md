---
name: succession-coverage-map
description: "Maps critical roles, coverage gaps, bench readiness, vacancy risk, ramp time, and development moves for succession and continuity planning. Use for quarterly planning, leadership transitions, key-person risk, or org resilience reviews."
license: MIT
compatibility: "Agent Skills compatible clients. No special tools required; optional file access helps when reading notes, docs, or metrics."
metadata:
  author: Stephen Rogan
  version: "1.0.0"
  tier: tier-3-people-and-org
  role: Org risk manager
  cadence: quarterly or event-driven
---

# Succession Coverage Map

## Overview

Use this skill to support the leader as **Org risk manager**. A coverage map that shows where the organisation is fragile before it breaks.

This skill is human-led by design: the agent prepares the work, but the human leader owns judgment, relationship, accountability, and final decisions.

## When to Use

Run this skill when:

- Key role may become vacant
- Quarterly org planning is due
- Leader suspects single points of failure

Do not use it as a substitute for legal, HR, finance, security, medical, or executive approval. If the workflow affects employment, compensation, customer commitments, external messaging, or sensitive personal data, prepare the packet and stop for human review.

## Inputs

Ask for or gather:

- Critical roles and responsibilities
- Current owners and backup coverage
- Readiness hypotheses and ramp requirements
- Business impact of vacancy or undercoverage

If inputs are missing, proceed with explicit assumptions and label confidence. Do not invent private context, motives, or facts.

## Workflow

Follow this sequence:

1. Identify critical roles by business consequence, not seniority alone
2. Map current owner, backups, and readiness level
3. Estimate vacancy impact and ramp time
4. Define development moves to improve coverage
5. Create contingency actions for high-risk gaps

Before finalizing, run the boundary check: what is evidence, what is interpretation, what is a recommendation, and what must remain a human decision?

## Output Format

Produce a concise, decision-ready artifact using this structure:

```markdown
# Succession Coverage Map

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

- Succession and coverage map
- Key-person risk register
- Development move list
- Contingency plan

See `assets/output-template.md` for a reusable version.

## Human Decision Boundary

The agent may prepare, synthesize, compare, draft, and track. The agent must not cross these boundaries:

- Do not tell people they are successors or not successors
- Do not make reporting-line or employment decisions
- Leader owns confidentiality and career implications

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

- Leadership Pipeline
- Org design and continuity planning practices
- Grove: leverage and managerial output

For the shared methodology spine, see `../../docs/SOURCE-SPINE.md`.
