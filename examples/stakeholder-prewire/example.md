# Example: Stakeholder Prewire

Skill: `stakeholder-prewire`
Data: synthetic

## Messy input

Ops wants to change the onboarding handoff. Sales thinks it will slow deals. CS thinks the current handoff creates bad customer expectations. Product wants cleaner implementation data but does not want another meeting. The VP wants the proposal approved in next week's leadership meeting.

## Generic prompt baseline

> Meet with stakeholders before the meeting, understand objections, and tailor the message to each group.

Problem: true, but it does not tell the leader who to speak to, in what order, or what decision each person needs to make.

## Skill-shaped output

# Stakeholder Prewire Plan: Onboarding Handoff Change

## Decision to prepare

Approve a revised onboarding handoff that improves implementation readiness without creating unnecessary sales friction.

## Stakeholder map

| Stakeholder | Likely concern | Needed from them | Prewire angle |
|---|---|---|---|
| Sales lead | Deal slowdown | Agreement on minimum required fields | This reduces post-sale rework, not sales control |
| CS lead | Expectation mismatch | Support for stricter customer-ready criteria | This prevents false starts and renewal risk |
| Product lead | Meeting load | Agreement on data fields and async review | Cleaner implementation data without extra ceremony |
| Ops lead | Process adoption | Owner for rollout and measurement | Make the change operational, not theoretical |

## Conversation sequence

1. CS lead first: confirm current customer pain and failure examples.
2. Sales lead second: identify the smallest handoff standard that does not block good deals.
3. Product lead third: get async agreement on implementation data fields.
4. Ops lead last: turn agreement into rollout plan and adoption measure.

## Likely objections

- "This will slow deals."  
  Response: only fields tied to implementation readiness are required. Anything else gets cut.

- "This creates another process."  
  Response: the current hidden process already exists as rework. This makes it visible.

## Leadership meeting ask

Approve a 30-day pilot with minimum handoff fields, named exception path, and weekly adoption review.

## Human decision boundary

The agent can prepare the influence plan and language. The human leader owns stakeholder conversations and final commitment.

## Why this is better

The skill output turns vague alignment advice into a sequence, objection map, decision ask, and approval boundary.
