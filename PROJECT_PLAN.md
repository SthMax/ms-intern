# Project Plan

## 1. Scope hierarchy

### Two-month internship: primary objective

Evaluate the technical, financial, and regulatory feasibility of deploying
open-source or commercial LLMs on-premise within MSIM China/COD infrastructure,
including model selection, hardware requirements, data security, and compliance
with applicable Morgan Stanley internal requirements, CSRC guidance, and other
applicable Chinese regulatory requirements.

### Two-month internship: secondary objectives

1. Survey AI/LLM adoption among top-tier Chinese fund houses, including disclosed
   use cases, technology stacks/partners, maturity, and observed outcomes.
2. Identify high-impact, low-risk quant-research pilot applications, including
   earnings-call summarization, drafting assistance, financial-news sentiment,
   model-building “vibe coding,” and automated compliance checking for “fund
   outcomes” (the meaning of that phrase in the notes must be confirmed).
3. Benchmark open-source LLMs on financial named-entity recognition, financial
   question answering, and multi-document summarization.
4. Estimate production-grade on-premise TCO, including GPU servers, electricity,
   cooling, maintenance, and personnel.

### Week 1–2 checkpoint: presentation on 11 September 2026

The checkpoint covers only the two targets supplied by the mentor:

1. Compile a structured database of **at least [number to be confirmed]** onshore
   mutual fund companies with publicly disclosed AI/LLM initiatives, categorized
   by asset size, use case (`research`, `trading`, `risk`, `marketing`,
   `compliance`, and other clearly labelled categories), and technology partner.
2. Summarize key regulatory texts/filings and MRM/CSRC guidance on AI use in
   financial institutions, emphasizing data privacy, model
   interpretability/governance, and outsourcing restrictions.

The checkpoint may show the full internship roadmap, but it must not imply that
pilot selection, model benchmarking, architecture sizing, or TCO estimation were
assigned for completion in Week 1–2.

## 2. Week 1–2 deliverables

### A. Onshore fund-company database

- Required number of qualifying managers once the missing threshold is confirmed.
- Asset-size value accompanied by metric/scope, as-of date, and source.
- Each initiative tagged by use case, maturity, disclosed technology/model/partner,
  and evidence strength.
- At least one public primary source for every presentation-grade initiative.
- Separate reserve/candidate list for weak, vague, or not-yet-verified disclosures.
- Summary charts/tables that do not erase differences in AUM definitions or
  initiative maturity.

### B. Regulatory and governance summary

- Source register containing issuer, exact title, publication/effective/status
  dates, official URL, relevant provision, scope, and caveat.
- Thematic synthesis focused on privacy/data governance, interpretability/model
  governance, and outsourcing/third-party restrictions.
- Clear separation among binding law/rules, regulator guidance, consultation or
  draft material, industry interpretation, and internal Morgan Stanley policy.
- Applicability questions and operational implications explicitly labelled as
  analysis, not quoted legal requirements.
- MRM meaning, source set, and authorized internal owner confirmed rather than
  inferred.

### C. Checkpoint presentation

- Concise main deck covering methods, company landscape, regulatory themes,
  limitations, and next steps.
- Evidence appendix with company-level entries and regulatory source matrix.
- Claim-level source IDs and manually testable links.
- No legal conclusion and no claim about undisclosed peer systems.

## 3. Proposed two-month sequence

This sequence is a planning proposal, not a restatement of mentor-assigned weekly
targets. It should be adjusted after mentor feedback.

| Internship phase | Primary focus | Intended output |
|---|---|---|
| Weeks 1–2 | Peer landscape and regulatory/MRM/CSRC evidence | Structured database and checkpoint presentation |
| Week 3 | Use-case analysis | Ranked pilot candidates with value, risk, and control requirements |
| Week 4 | Model/deployment feasibility design | Open-source/commercial candidate screen, architecture options, security boundary, hardware-sizing assumptions |
| Weeks 5–6 | Model selection and financial NLP benchmarking | Reproducible benchmark results and model shortlist |
| Week 7 | Hardware sizing and financial feasibility | Low/base/high TCO using an agreed horizon and documented sensitivities |
| Week 8 | Integrated assessment | Technical/financial/regulatory feasibility, recommendations, roadmap, and final report/deck |

Workstreams may overlap when dependencies require it, but their final outputs
remain aligned to the full two-month objectives.

## 4. Schedule to the Week 1–2 checkpoint

| Date | Focus | Exit criterion |
|---|---|---|
| Fri 4 Sep | Correct scope, schemas, evidence protocol, candidate universe | Two-month objectives separated from checkpoint targets |
| Mon 7 Sep | Discover company disclosures and authoritative regulatory corpus | Candidates/source records logged; primary sources prioritized |
| Tue 8 Sep | Verify companies, initiatives, AUM definitions, and partners | Required company threshold progressing with weak entries quarantined |
| Wed 9 Sep | Complete company verification and extract regulatory provisions | Database and evidence notes substantially complete |
| Thu 10 Sep | Synthesize findings, build deck, perform citation/applicability audit | Every material claim traceable; uncertainty visible |
| Fri 11 Sep | Final review and checkpoint presentation | Main deck and evidence appendix ready |

## 5. Week 1–2 research questions

### Peer landscape

1. Which onshore mutual fund managers have made a concrete public AI/LLM
   disclosure?
2. What was disclosed: exploration, partnership, procurement, pilot, deployed
   capability, or measured outcome?
3. Which business function and technology partner/model were explicitly named?
4. What asset-size measure is available, for what entity and date?
5. What does each source establish, and what remains unknown?

### Regulation and governance

1. Which authoritative instruments potentially govern the intended institutional
   use of AI/LLMs?
2. What do the exact provisions say about data/privacy, model governance or
   explainability, and outsourcing/third parties?
3. What is binding, effective, sector-specific, or merely guidance/draft?
4. What applicability questions require confirmation by Legal, Compliance,
   Privacy, InfoSec, MRM, or Third-Party Risk?
5. Which requirements come from internal Morgan Stanley policy and therefore
   cannot be reconstructed from public sources?

## 6. Inputs to confirm with the mentor

- The missing minimum number of onshore fund companies.
- The intended universe: all licensed onshore mutual fund managers or a defined
  “top-tier” subset, and the preferred asset-size measure.
- Whether “MRM” means Morgan Stanley Model Risk Management, generic model-risk
  management, or a particular internal document set.
- What “COD” denotes in this project and the infrastructure boundary it implies.
- Whether the landscape includes broad AI initiatives or only LLM/generative-AI
  initiatives, and what qualifies as a public disclosure.
- Which internal policies may be consulted, summarized, or cited, and where those
  notes are permitted to be stored.
- Which instruments “regulatory filings” refers to, which authorities beyond CSRC
  are in scope, and the research information cut-off date.
- Presentation audience, duration, expected language, and appendix depth.
- Whether 11 September is the formal end-of-Week-2 checkpoint.

## 7. Later-stage decision frame

The full internship should not assume that self-hosting is automatically the most
compliant or economical answer. Later work will compare open-weight on-premise,
approved dedicated commercial deployment, and narrower non-general-purpose
approaches against confirmed internal and regulatory constraints.

## 8. Definition of done for any finding

A finding is usable only when its scope, date, provenance, evidence state, and
limitations are recorded. Regulatory conclusions require review by an authorized
legal/compliance stakeholder; this project is research, not legal advice.
