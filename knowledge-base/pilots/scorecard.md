# Pilot Use-Case Scorecard

> **Later internship workstream:** retained as scaffolding for the two-month
> secondary objectives. It is not a Week 1–2 checkpoint deliverable.

## Scoring method

Score each factor from 1 (least favorable) to 5 (most favorable). For risks, 5
means lower risk/easier control. Keep the raw evidence and assumptions beside the
score; the number alone is not a finding.

| Criterion | Weight | Question |
|---|---:|---|
| Business value | 20% | How much analyst time or decision quality could improve? |
| Data safety | 20% | Can the pilot use public, synthetic, or low-sensitivity data? |
| Failure containment | 15% | Is output advisory, reversible, and reviewed before use? |
| Evaluation clarity | 15% | Can quality be measured against a defensible reference? |
| Governance simplicity | 15% | Is the control/approval path comparatively clear? |
| Technical feasibility | 10% | Can a small approved environment deliver adequate quality? |
| Adoption fit | 5% | Does it fit an existing desk workflow with little disruption? |

Weighted score = sum of `(score / 5) × weight`.

## Candidate comparison

| Use case | Value | Data safety | Failure containment | Evaluation | Governance | Feasibility | Adoption | Weighted result | Key evidence / assumptions |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Earnings-call summarization from public transcripts |  |  |  |  |  |  |  |  |  |
| Research drafting assistant |  |  |  |  |  |  |  |  |  |
| Public financial-news sentiment |  |  |  |  |  |  |  |  |  |
| Coding assistant for model development |  |  |  |  |  |  |  |  |  |
| Compliance pre-check for fund materials/outputs |  |  |  |  |  |  |  |  |  |

## Initial safety boundary to test

A first pilot should preferably use public or synthetic inputs, remain outside
order execution and regulated client communications, provide citations or source
spans, require human approval, record model/version/settings, and have a simple
fallback to the existing workflow. This is a proposed design principle, not a
statement of policy approval.
