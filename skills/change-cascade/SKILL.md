---
name: change-cascade
description: "Plans how to communicate and operationalize a change through managers and teams, including rationale, audience impact, FAQ, resistance risks, adoption measures, and reinforcement cadence. Use for process, policy, tooling, org, or strategy changes."
license: MIT
compatibility: "Agent Skills compatible clients. No special tools required; optional file access helps when reading notes, docs, or metrics."
metadata:
  author: Stephen Rogan
  version: "1.0.0"
  tier: tier-2-leadership-judgment
  role: Change leader
  cadence: event-driven with weekly monitoring
---

# Change Cascade

## Overview

Use this skill to support the leader as **Change leader**. A change cascade that makes the why clear, the impact concrete, and adoption measurable.

This skill is HUMAN+ by design: the agent prepares the work, but the human leader owns judgment, relationship, accountability, and final decisions.

## When to Use

Run this skill when:

- New process, policy, tool, org model, or strategy needs rollout
- Managers need consistent talking points
- Change risk is more about adoption than design

Do not use it as a substitute for legal, HR, finance, security, medical, or executive approval. If the workflow affects employment, compensation, customer commitments, external messaging, or sensitive personal data, prepare the packet and stop for human review.

## Inputs

Ask for or gather:

- Change rationale and desired outcomes
- Impacted audiences and manager layers
- Timeline, training needs, and adoption metrics
- Known objections and risks

If inputs are missing, proceed with explicit assumptions and label confidence. Do not invent private context, motives, or facts.

## Workflow

Follow this sequence:

1. Clarify what is changing, why now, and what is not changing
2. Map audience impacts and likely concerns
3. Create message cascade: exec, managers, teams, individual contributors
4. Define enablement, reinforcement, and feedback loops
5. Set adoption metrics and rollback/escalation triggers

Before finalizing, run the boundary check: what is evidence, what is interpretation, what is a recommendation, and what must remain a human decision?

## Output Format

Produce a concise, decision-ready artifact using this structure:

```markdown
# Change Cascade

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

- Change narrative
- Cascade plan
- Manager talking points
- FAQ
- Adoption monitor

See `assets/output-template.md` for a reusable version.

## Human Decision Boundary

The agent may prepare, synthesize, compare, draft, and track. The agent must not cross these boundaries:

- Do not pretend change has no cost
- Do not send communications without approval
- Leader owns empathy, timing, and firmness

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

- John Kotter, Leading Change
- Prosci ADKAR concepts
- Atlassian change and team playbooks

For the shared methodology spine, see `../../docs/SOURCE-SPINE.md`.
