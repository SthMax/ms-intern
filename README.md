# MSIM China On-Premise LLM Feasibility Study

Local research workspace for the two-month internship. The
[final, mentor-confirmed project plan](PROJECT_PLAN.md) controls project scope.
Derived schedules and templates must follow it.

## Confirmed phases

| Phase | Timing | Deliverables |
|---|---|---|
| 1 — Industry research | Weeks 1–2 | Onshore fund-company AI/LLM database; regulatory and model risk management (MRM)/CSRC summary |
| 2 — Technical feasibility | Weeks 3–5 | Survey of 5–8 open-source LLMs; on-premise reference architecture; one-model proof of concept on a local GPU workstation |
| 3 — Cost-benefit and recommendations | Weeks 6–8 | Three-year on-premise versus commercial API TCO; 3–5 pilot candidates with ROI metrics; final report and roadmap with 2–5 concrete proposals |

COD is the infrastructure used in MSIM. MRM means model risk management.
The confirmed plan also requires a reusable financial NLP evaluation framework
covering named-entity recognition, financial question answering, and
multi-document summarization.

## Current work: Week 2, 7–11 September 2026

The Friday, 11 September presentation covers Phase 1: the company landscape and
regulatory/MRM/CSRC research, emphasizing data privacy, model interpretability,
and outsourcing restrictions.

Use [the Week 2 execution plan](weekly/week-02-plan.md) for daily work,
deliverables, acceptance criteria, and unresolved inputs. Use
[the checkpoint outline](presentation/deck-outline.md) for presentation structure.

The supplied final brief still omits the number after “at least” in the company
target. Research can proceed; the count requirement remains unconfirmed.
As of the 6 September repository review, the knowledge base contains templates
and no verified external research findings.

## Research and version control

- Keep findings in the Markdown [knowledge base](knowledge-base/README.md), with
  source IDs, direct links, and exact locations that a reviewer can check.
- Keep supplied project context, verified source content, and researcher analysis
  distinguishable. The final plan itself is not evidence of industry adoption.
- Use public information for the landscape and public regulatory work. Handle
  internal requirements according to the user's stated confidentiality constraints.
- Do not store confidential internal documents, client/position data, credentials,
  or personal data in this repository.
- Internal MRM and other Morgan Stanley requirements require authorized internal
  evidence; public guidance cannot establish unpublished firm policy.
- Git is backed up to the public [SthMax/ms-intern](https://github.com/SthMax/ms-intern)
  repository. Releases package finalized research reports, presentations and
  selected model references for sharing.

## Current deliverables

The September 2026 delivery bundle contains:

- [Industry research report](reports/phase1-llm-industry-2026-09-09/report.pdf)
- [Presentation with speaker notes](presentation/phase1-llm-industry-2026-09-10/output/fund-llm-industry-2026-09-11-final.pptx)
- [DeepSeek-V4.1-Flash technical report](knowledge-base/models/deepseek-v4.1-flash/technical-report/DeepSeek_V41_Tech_Report.pdf)
- [DeepSeek architecture and KV Cache analysis, in Chinese](knowledge-base/models/deepseek-v4.1-flash/analysis/DeepSeek_V4_1_Flash_Architecture_and_KV_Cache_Guide_ZH.pdf)

## Repository map

| Location | Purpose |
|---|---|
| [PROJECT_PLAN.md](PROJECT_PLAN.md) | Final approved project brief and mentor clarifications |
| [Research tools](RESEARCH_TOOLS.md) | Tested MCP/tool inventory, research routing, and remaining setup gaps |
| [knowledge-base/README.md](knowledge-base/README.md) | Evidence workflow |
| [Company index](knowledge-base/companies/index.md) | Phase 1 database, candidates, coverage |
| [Regulatory index](knowledge-base/regulation/index.md) | Phase 1 provision map and MRM/internal questions |
| [Model evaluation](knowledge-base/models/benchmark-plan.md) | Phase 2 survey and reusable benchmark framework |
| [Proof-of-concept plan](knowledge-base/models/poc-plan.md) | Phase 2 local GPU execution record template |
| [Reference architecture](knowledge-base/infrastructure/reference-architecture.md) | Phase 2 hardware/software/security specification template |
| [TCO model](knowledge-base/infrastructure/tco-model.md) | Phase 3 three-year on-premise/API comparison |
| [Pilot scorecard](knowledge-base/pilots/scorecard.md) | Phase 3 selection, ROI, and proposal template |
| [Week 1 record](weekly/week-01.md) | Historical setup and corrections |
| [Week 2 plan](weekly/week-02-plan.md) | Current execution plan |
| [Repository alignment review](weekly/repo-alignment-review-2026-09-06.md) | Whole-repository review against the final brief |
