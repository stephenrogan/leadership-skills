# Example: Agent Command Center

Skill: `agent-command-center`
Data: synthetic

## Messy input

A leader has eight agent workflows running: research, content drafting, QA, forecast notes, escalation prep, hiring screen summaries, meeting prep, and docs maintenance. Nobody knows which are stale, which can publish, which need approval, and which are duplicating effort.

## Generic prompt baseline

> Create a dashboard to track agents, owners, statuses, risks, and next steps.

Problem: it asks for visibility but does not define control, approval, risk, or rollback.

## Skill-shaped output

# Agent Command Center

## Objective

Create one weekly control surface for active agent workflows so the leader can see state, risk, owner, approval boundary, and next decision.

## Current state

| Workflow | State | Owner | Risk | Approval boundary | Next decision |
|---|---|---|---|---|---|
| Research | Running | Strategy lead | Medium | No external citations without source check | Keep, narrow, or pause topic scan |
| Content drafting | Pending review | Marketing lead | High | No publishing without human approval | Approve draft queue or reject |
| QA | Running | Engineering lead | Medium | No production changes without PR review | Fix defects or file backlog |
| Forecast notes | Stale | Revenue ops | High | No forecast changes from agent-only interpretation | Kill or refresh source data |
| Escalation prep | Pending approval | CS lead | High | No customer sends or concessions | Approve response strategy |
| Hiring screen summaries | Running | People lead | High | No candidate decision from agent summary | Define evidence rubric |
| Meeting prep | Healthy | Chief of staff | Low | Human owns agenda and decisions | Continue |
| Docs maintenance | Duplicate | Ops lead | Low | No public docs updates without review | Merge with QA docs workflow |

## Immediate actions

1. Pause stale forecast workflow until source data is refreshed.
2. Merge docs maintenance into QA docs workflow.
3. Add explicit approval metadata to content and escalation workflows.
4. Require hiring summaries to cite interview evidence and avoid recommendation-only decisions.

## Review cadence

Weekly 20-minute command-center review:

- What shipped?
- What is blocked?
- What needs approval?
- What is stale or duplicative?
- What should be killed?

## Human decision boundary

Agents can prepare, classify, summarize, and flag. The human leader owns publishing, customer communication, hiring decisions, forecast changes, access, autonomy increases, and production changes.

## Why this is better

The skill output makes the control loop visible. It does not just track agents. It names owners, risk, approval boundaries, stale work, duplication, and kill decisions.
