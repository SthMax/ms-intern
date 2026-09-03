# MSIM China On-Premise LLM Feasibility Study

Local research workspace for an internship project evaluating the feasibility of
on-premise LLM deployment for MSIM China/COD and surveying publicly disclosed
AI/LLM initiatives among onshore mutual fund managers.

## Immediate deliverable

Prepare a source-auditable presentation for **Friday, 11 September 2026**.
The first-week deliverable is deliberately narrower than the full internship
topic:

1. A database of at least 15 onshore mutual fund companies with verified public
   AI/LLM disclosures.
2. A regulatory and internal-policy evidence map, clearly separating public law
   from Morgan Stanley internal requirements.
3. A ranked shortlist of low-risk quant-research pilots.
4. A proposed model benchmark and TCO methodology, with assumptions clearly
   labelled rather than presented as completed results.
5. A 10–12 slide management presentation.

See [PROJECT_PLAN.md](PROJECT_PLAN.md) for scope and schedule and
[knowledge-base/README.md](knowledge-base/README.md) for the evidence workflow.

## Repository rules

- This repository is local-only. Do not add a remote without explicit approval.
- Use public information for the external landscape and public regulatory work.
- Do not copy confidential Morgan Stanley documents, client information,
  positions, research data, credentials, or personal data into this repository.
- Internal MRM, security, architecture, procurement, and compliance requirements
  must be supplied or confirmed by authorized Morgan Stanley stakeholders.
- A factual claim is not presentation-ready until it has a source-register entry
  and a manually verifiable citation.

## Structure

```text
knowledge-base/
  companies/       Public AI/LLM initiative evidence
  regulation/      Public rules and internal-policy questions
  pilots/          Use-case risk/value assessment
  models/          Financial NLP benchmark design
  infrastructure/  Deployment architecture and TCO method
  templates/       Reusable evidence-note template
presentation/      Slide storyline and later deck artifacts
weekly/            Work log and checkpoints
```

