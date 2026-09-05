# Repository Alignment Review — 6 September 2026

## Basis and coverage

Reviewed all **13 existing project files**, including the hidden `.gitignore`,
against the user-supplied [final confirmed plan](../PROJECT_PLAN.md).
The working tree was clean at review start and no Git remote was configured.
No external sources or completed research artifacts existed.

This review updates planning, schemas, and future-work templates. It does not
perform the Week 2 research, technical tests, or cost analysis.

## Findings and corrections

| File | Finding before review | Correction / result |
|---|---|---|
| [PROJECT_PLAN.md](../PROJECT_PLAN.md) | Earlier derived plan and provisional Weeks 3–8 sequence | Replaced with the supplied final brief; confirmed text retained with normalized Markdown; final status and mentor clarifications recorded |
| [README.md](../README.md) | Incomplete phase details and no three-year API comparison | Summarizes all three confirmed phases, new quantities, definitions, current status, and Week 2 navigation |
| [weekly/week-01.md](week-01.md) | Mixed historical setup with future Week 2 work; MRM unresolved | Historical record updated with final-plan adoption; open execution moved to Week 2; MRM/COD clarifications closed |
| [presentation/deck-outline.md](../presentation/deck-outline.md) | Phase 1 focus broadly aligned, but roadmap and definitions needed updating | Retains Phase 1 storyline; links confirmed phase dates, evidence audit, and derived Week 2 plan |
| [knowledge-base/README.md](../knowledge-base/README.md) | Evidence protocol aligned, but phase ownership/provenance could be clearer | Adds phase mapping and distinction between supplied overview, source verification, and actual human checks |
| [source-register.md](../knowledge-base/source-register.md) | Dummy example row and no explicit instrument-type/note-link fields | Removes dummy row, records zero sources, adds source/instrument type and evidence-note linkage |
| [evidence-note.md](../knowledge-base/templates/evidence-note.md) | Missing reviewer/method and explicit human-check fields | Adds provenance, human-check status, and current-status verification basis |
| [companies/index.md](../knowledge-base/companies/index.md) | One wide table obscured company versus initiative count and AUM classification | Separates entity and initiative records; explicit size unit/basis, AI/LLM distinction, source links, candidate queue, and count method |
| [regulation/index.md](../knowledge-base/regulation/index.md) | MRM meaning still marked TBC; source type/legal force not explicit | Records confirmed terminology, focuses on three required themes, adds instrument type/legal force and source-versus-interpretation fields |
| [models/benchmark-plan.md](../knowledge-base/models/benchmark-plan.md) | Generic later-phase benchmark; no 5–8 comparison or required survey dimensions | Assigns Weeks 3–5; adds all survey dimensions and links reusable evaluation and GPU proof of concept |
| [infrastructure/tco-model.md](../knowledge-base/infrastructure/tco-model.md) | On-premise-only framework; horizon unconfirmed | Assigns Weeks 6–8; fixes horizon at three years and adds commercial API, volume pricing, egress, security-premium, and comparison assumptions |
| [pilots/scorecard.md](../knowledge-base/pilots/scorecard.md) | Generic later-phase scoring; lacked confirmed counts and proposal economics | Assigns Weeks 6–8; 3–5 candidates and 2–5 final proposals, with explicit complexity/risk, effort, cost, impact, and ROI fields |
| [.gitignore](../.gitignore) | Existing local/privacy exclusions fit the project | Reviewed; no change needed |

## Missing supporting documents added

| New file | Requirement addressed |
|---|---|
| [Week 2 plan](week-02-plan.md) | Daily execution, deliverables, acceptance criteria, research workflow, open inputs, and Friday review |
| [Reference architecture](../knowledge-base/infrastructure/reference-architecture.md) | Phase 2 hardware, GPU cluster, storage, networking, inference engine, vector database, orchestration, and security specification |
| [Local GPU proof of concept](../knowledge-base/models/poc-plan.md) | Phase 2 one-model deployment, inference latency, sample financial task, and reproduction record |
| This review | File-by-file alignment findings and disposition |

## Final-plan traceability

| Confirmed requirement | Repository implementation |
|---|---|
| Phase 1 — Weeks 1–2 | Company/regulatory indexes, source/evidence protocol, Week 2 plan and checkpoint outline |
| Phase 2 — Weeks 3–5 | 5–8-model survey, architecture specification, and one-model GPU proof-of-concept templates |
| Phase 3 — Weeks 6–8 | Three-year on-premise/API TCO; pilot candidates/proposals; final-report handoff |
| Financial NLP benchmarks | NER, financial QA, and multi-document summarization evaluation specification |
| Five expected outcomes | Knowledge base; architecture; TCO comparison; proposal roadmap; reusable evaluation framework |
| COD and MRM clarifications | Final plan, README, regulatory index, knowledge-base guidance, and Week 2 plan |

## Remaining wording and execution gaps

- The company-count number is still absent in the confirmed brief. It remains
  open; the former assistant-selected 15 is not reinstated.
- “Top tier” and the preferred AUM metric/cut-off remain unspecified. Week 2
  records its selection/comparison method.
- The model survey's “language proficiency” does not name languages or thresholds.
  The model template labels Chinese/English assessment as a working proposal.
- “Fund outcomes” needs operational definition when developing Phase 3 pilots.
- Phase 3's 3–5 candidates and the expected outcome's 2–5 proposals are retained
  as distinct stages: final proposals are developed from the candidate set.
- COD/MRM meanings are resolved. Actual infrastructure specifications and
  applicable internal model risk management policy still need evidence.
- Global-industry statements in the supplied overview remain project context
  until independently sourced; no external adoption claims were verified here.

These details do not reopen the confirmed phase scope or prevent Week 2 public
research.

## Verification record

- Reviewed all 13 original files and four new supporting documents.
- Checked 68 local Markdown links across 16 Markdown files; no broken targets.
- Checked Markdown table column consistency; no mismatches.
- Reconciled phase timing, model/pilot counts, three-year horizon, API comparison,
  and COD/MRM terminology with the confirmed brief.
- Corrected whitespace issues found during the diff check.
- Confirmed there is no configured Git remote.
