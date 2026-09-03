# Project Plan

## Decision to support

What should MSIM China investigate next—if anything—to enable useful LLM
workflows while respecting data, security, model-risk, regulatory, outsourcing,
and operational constraints?

The study should not start from an assumption that an on-premise model is always
the compliant answer. It will compare at least three deployment patterns:

1. Fully on-premise/self-hosted open-weight model.
2. Dedicated commercial model deployed in an approved private environment.
3. No general-purpose deployment; narrow deterministic or retrieval-assisted
   tools only.

## Scope

### Primary workstreams

- **Landscape:** verified public disclosures by onshore mutual fund managers.
- **Regulation and governance:** applicable public requirements plus a separate
  checklist for internal Morgan Stanley policy confirmation.
- **Pilots:** value, data sensitivity, failure impact, human review, and ease of
  evaluation for quant-research use cases.
- **Models:** reproducible evaluation of Chinese/English financial tasks.
- **Infrastructure and TCO:** capacity assumptions, architecture options, and
  three-year cost scenarios.

### Explicit non-goals for the first presentation

- A final legal or compliance opinion.
- A production architecture approval.
- Claims about unpublished competitor systems.
- A completed benchmark without access to approved hardware and datasets.
- A precise TCO point estimate before workload, availability, and procurement
  assumptions are confirmed.

## Deliverables

### Week 1: presentation baseline (4–11 September 2026)

- At least 15 qualifying fund managers in the landscape database.
- Every included initiative supported by at least one direct public disclosure;
  secondary sources may help discovery but are not sufficient alone for strong
  claims.
- Regulatory source map with issuing body, document title, publication/effective
  dates, scope, relevant provision, official URL, and interpretation caveat.
- Internal-policy request list for MRM, information security, data classification,
  third-party risk, software licensing, record retention, and human supervision.
- Pilot scorecard and recommended first candidate(s).
- Benchmark and TCO designs; preliminary numbers only where their inputs are
  sourced and sensitivity-tested.
- 10–12 slide deck with claim-level citations.

### Week 2: evidence and feasibility deepening

- Expand and quality-check the company landscape.
- Convert regulatory documents into a controls/implications matrix reviewed by
  an authorized subject-matter expert.
- Run a small benchmark on approved public or synthetic data.
- Obtain indicative hardware/software/support inputs and build low/base/high TCO
  scenarios.
- Refine deployment options, risk register, and pilot implementation plan.

## Working minimum for the missing company count

The brief says “at least [number missing] onshore mutual fund companies.” Until
the manager confirms the intended number, the working minimum is **15 verified
firms**. Keep a larger candidate list so weak or unverifiable entries can be
removed without missing the target.

## Schedule to next Friday

| Date | Focus | Exit criterion |
|---|---|---|
| Fri 4 Sep | Scope, repository, schemas, research protocol | Structure committed locally; ambiguities logged |
| Mon 7 Sep | Public regulatory corpus and internal-policy request list | Core documents inventoried; no unsourced legal claims |
| Tue 8 Sep | Fund-manager landscape | 15 verified firms plus reserve candidates |
| Wed 9 Sep | Pilot ranking, deployment options, benchmark/TCO design | Recommendation logic and assumptions visible |
| Thu 10 Sep | Draft deck, citation audit, challenge session | Every material claim traceable; gaps labelled |
| Fri 11 Sep | Final review and presentation | Deck, appendix, and speaking notes ready |

## Research questions

1. Which workloads are permissible under public requirements and internal policy?
2. Which data may enter each candidate system, at what classification level?
3. Which model/deployment options meet functional quality and operational needs?
4. How will output errors be detected, reviewed, logged, and remediated?
5. What evidence shows peer adoption, and what does it *not* prove?
6. What utilization and service-level assumptions drive cost?
7. What smallest pilot can produce decision-quality evidence without exposing
   sensitive data or automating a regulated decision?

## Manager inputs needed

- Confirm the required number and preferred list of fund managers.
- Confirm whether “MRM” means Morgan Stanley Model Risk Management and identify
  the authorized internal policy owner.
- Confirm permitted sources, browsing/download rules, and whether Chinese public
  documents may be retained locally.
- Provide the intended audience and presentation length.
- Identify approved data classes, infrastructure boundary, procurement currency,
  depreciation horizon, and availability target.
- Confirm whether benchmark execution is expected before 11 September or whether
  a benchmark design is sufficient.

## Definition of done for any finding

A finding is usable only when its scope, date, provenance, evidence status, and
limitations are recorded. Regulatory conclusions also require confirmation by
an authorized legal/compliance stakeholder; this research is not legal advice.

