# MSIM China On-Premise LLM Feasibility Study

Local research workspace for an internship project evaluating the feasibility of
on-premise LLM deployment for MSIM China/COD and surveying publicly disclosed
AI/LLM initiatives among onshore mutual fund managers.

## Objective hierarchy

The **primary and secondary objectives cover the full two-month internship**.
They are not the deliverables for next Friday.

Across the internship, the project will evaluate technical, financial, and
regulatory feasibility; survey peer adoption; identify suitable pilots; benchmark
open-source models; and estimate production-grade on-premise TCO.

The immediate deliverable is the **Week 1–2 checkpoint presentation on Friday,
11 September 2026**, limited to:

1. A structured database of the required number of onshore mutual fund companies
   that have publicly disclosed AI/LLM initiatives, categorized by asset size,
   use case, and technology partner. The number is missing from the supplied
   brief and remains to be confirmed.
2. A source-grounded summary of key regulatory texts/filings and MRM/CSRC
   guidance, emphasizing data privacy, model interpretability/governance, and
   outsourcing restrictions.

Pilot selection, model benchmarking, infrastructure sizing, and TCO belong to
later internship workstreams and should appear next Friday only as roadmap items,
not as Week 1–2 deliverables or completed analysis.

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
  pilots/          Later internship: use-case risk/value assessment
  models/          Later internship: financial NLP benchmark design
  infrastructure/  Later internship: deployment architecture and TCO
  templates/       Reusable evidence-note template
presentation/      Slide storyline and later deck artifacts
weekly/            Work log and checkpoints
```
