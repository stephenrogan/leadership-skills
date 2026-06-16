# Security and Privacy

Leadership workflows often involve sensitive people, customer, strategy, and performance context. Treat this repo as public-safe infrastructure only. Do not add real confidential data.

## Supported versions

The `main` branch is the supported version until tagged releases are introduced.

## Data rules

Do not commit:

- real employee names or performance details
- real customer names, account health, commercial terms, or escalations
- private employer context
- private meeting notes or transcripts
- credentials, tokens, secrets, or API keys
- legal, HR, medical, or financial advice presented as definitive instruction

Examples, evals, and fixtures must be synthetic or clearly redacted.

## Reporting a vulnerability or sensitive-data issue

Open a private security advisory if available, or contact the repository owner directly. Do not open a public issue containing secrets, private data, or exploit details.

## Agent safety boundary

The skills are designed for preparation and decision support. They must not instruct an agent to independently:

- terminate, discipline, or diagnose a person
- make compensation, hiring, legal, or HR decisions
- send external messages or customer commitments without approval
- publish sensitive information
- grant access, change production systems, or spend budget without authorization

If a skill output could affect people, customers, reputation, legal/compliance exposure, or money, the agent should prepare the packet and stop for human approval.
