# Example: Decision Memo

Skill: `decision-memo`
Data: synthetic

## Messy input

The enterprise team is split on whether to move named CSM coverage into a pooled model for sub-500k ARR accounts. Finance wants capacity relief. Sales is worried about renewal risk. CS leaders think named ownership is inconsistent anyway. Nobody agrees on whether this is a cost move, a segmentation move, or a service-quality move.

## Generic prompt baseline

> You should weigh the pros and cons of pooled CSM coverage. Pooled models can increase efficiency, but named ownership can improve relationships. Consider customer impact, team capacity, and revenue risk before making the decision.

Problem: accurate but useless. No owner, no decision shape, no assumptions, no dissent, no revisit trigger.

## Skill-shaped output

# Decision Memo: Enterprise Coverage Model

## Decision required

Should sub-500k ARR enterprise accounts move from named CSM ownership to pooled coverage for the next two quarters?

Decision owner: VP Customer Success  
Deadline: 15 July 2026  
Revisit trigger: renewal risk, response-time breach, or expansion pipeline drop above agreed threshold

## Evidence and signals

Facts:

- Named CSM coverage is inconsistent across the segment.
- Finance needs capacity relief this quarter.
- Sales expects relationship continuity for late-stage renewal support.

Interpretations:

- The current model may be creating the appearance of premium coverage without reliable execution.
- The risk is not pooled coverage by itself. The risk is moving to pooled coverage without clear escalation rules.

Missing context:

- Renewal rate by ARR band
- Support response-time baseline
- Expansion pipeline by coverage model
- Customer sentiment for accounts proposed for pooled coverage

## Options

| Option | Upside | Downside | Reversibility |
|---|---|---|---|
| Keep named ownership | Lower relationship disruption | Capacity problem remains | High |
| Full pooled coverage | Maximum capacity relief | Renewal/support risk | Medium |
| Hybrid by risk tier | Balances capacity and risk | Requires clear rules | High |

## Recommendation

Run a two-quarter hybrid model.

Move low-risk sub-500k accounts to pooled coverage. Keep named ownership for renewal-window, escalation, strategic logo, or expansion-active accounts.

## Dissent to preserve

Sales concern is valid if pooled coverage means no named escalation owner during renewal windows. The design must include named commercial escalation even if day-to-day service is pooled.

## Human decisions required

- Approve the coverage model
- Approve risk-tier criteria
- Approve customer-facing language if coverage changes are communicated
- Accept renewal and relationship risk

## Follow-up

Owner: VP Customer Success  
First review: 30 days after pilot start  
Success signals: capacity relief, no material renewal slippage, stable response time, clear escalation compliance

## Why this is better

The skill output turns vague debate into a decision record. It names the owner, deadline, options, reversibility, missing evidence, dissent, and human approval boundary.
