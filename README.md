# Leadership Skills

World-class Agent Skills for leadership and management workflows, built to the [Agent Skills](https://agentskills.io/home) format.

This repo packages leadership work into reusable, compatible agent skills. The point is not to automate leadership. The point is to automate the preparation, synthesis, memory, drafting, and follow-through around leadership so humans can spend more time on judgment, trust, courage, coaching, and influence.

## Structure

```text
skills/
  <skill-name>/
    SKILL.md
    references/framework.md
    assets/output-template.md
    evals/evals.json
scripts/
  validate_repo.py
tests/
  test_validate_repo.py
QA-REPORT.md
```

Every skill is a folder containing `SKILL.md` with Agent Skills YAML frontmatter and Markdown instructions. Each skill also includes references, output templates, and eval prompts.


## Quickstart

1. Pick the skill that matches the leadership job.
2. Load the skill folder in any Agent Skills-compatible client.
3. Give the agent the live context: notes, metrics, prior decisions, stakeholder list, or meeting goal.
4. Ask for the specific artifact, not generic advice.
5. Review the human decision boundary before using or sending anything.

Example prompt:

```text
Use skills/decision-memo. We need to decide whether to move enterprise renewals from named CSM ownership to pooled coverage. Build the decision memo with options, tradeoffs, assumptions, dissent, and revisit criteria. Do not make the final decision.
```

Example boundary prompt:

```text
Use skills/feedback-conversation-prep. Prepare the conversation, but do not decide whether this becomes a formal HR action.
```

## Skill tiers

### Tier 1: Manager OS

Frequent workflows that make managers better every week.

- `manager-one-on-one-prep`
- `feedback-conversation-prep`
- `delegation-brief`
- `staff-meeting-designer`
- `weekly-leadership-pack`

### Tier 2: Leadership Judgment

Decision quality, influence, and executive communication.

- `decision-memo`
- `premortem-runner`
- `stakeholder-prewire`
- `executive-update-brief`
- `change-cascade`

### Tier 3: People and Org

Sensitive talent, performance, team health, and org resilience workflows.

- `performance-cycle`
- `onboarding-ramp`
- `talent-calibration`
- `succession-coverage-map`
- `hiring-loop`
- `team-health-pulse`
- `conflict-mediation-prep`

### Tier 4: Strategic Influence

Large-blast-radius strategy, org, customer, and board narrative workflows.

- `org-design-options`
- `customer-escalation-recovery`
- `strategy-operating-system`
- `market-and-board-narrative`
- `leadership-learning-loop`


### Tier 5: Mega Manager

AI-native management workflows for leaders managing portfolios of humans, agents, workflows, memory, evals, and governance.

- `agent-workforce-architecture`
- `agent-delegation-brief`
- `agent-output-review`
- `agent-command-center`
- `agent-performance-management`
- `context-memory-ops`
- `agent-risk-governance`
- `human-agent-team-design`
- `agent-eval-design`
- `agent-improvement-backlog`

## Leadership boundary

All skills obey the same boundary:

- Agent does: gather, synthesize, structure, draft, simulate, monitor, and prepare.
- Human does: decide, communicate, manage emotions, make people decisions, send external messages, approve commitments, and own consequences.

## QA

Run the full validation suite:

```bash
python3 scripts/validate_repo.py
python3 -m unittest discover -s tests -v
```

The validator checks Agent Skills format, metadata constraints, required sections, eval coverage, safety guardrails, template/reference presence, and mechanical quality gates.
