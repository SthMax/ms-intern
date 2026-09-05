# Onshore Fund Manager AI/LLM Landscape

**Phase 1 — Weeks 1–2.** [Final plan](../../PROJECT_PLAN.md) ·
[Week 2 plan](../../weekly/week-02-plan.md) · [Initial synthesis](synthesis-2026-09-06.md).

Batch cut-off: **6 September 2026**. Six distinct managers with primary-source
disclosures, seven initiatives, and ten additional candidates. Human review is
pending. This is an initial evidence sample, not a census or adoption-rate survey.

## Company and asset-size database

AUM amounts below are reported broader/group totals unless otherwise stated.
One 亿元 = RMB 100 million. Size bands are descriptive classifications of each
reported figure, not a common-date public-fund ranking.

| Company ID | Company / Chinese legal name | Entity eligibility source | AUM value and unit | AUM metric / entity scope | As-of date | Size source ID | Asset-size category / basis | Evidence state |
|---|---|---|---|---|---|---|---|---|
| COMP-001 | [ChinaAMC / 华夏基金管理有限公司](COMP-001-chinaamc.md) | FUND-003 profile/business identity | >RMB 3tn | Total managed assets; not separately public funds | 2025-06-30 | FUND-003 | Reported broader AUM ≥RMB 1tn | verified-primary; older observation |
| COMP-002 | [E Fund / 易方达基金管理有限公司](COMP-002-efund.md) | FUND-004 case / FUND-005 company identity | >RMB 4.1tn | Fund manager and subordinate institutions | 2025-12-31 | FUND-005 | Reported group AUM ≥RMB 1tn | verified-primary |
| COMP-003 | [Fullgoal / 富国基金管理有限公司](COMP-003-fullgoal.md) | FUND-007 case / FUND-008 profile | RMB 19,573亿元 (1.9573tn) | Total incl. pensions/accounts/subsidiaries/advisory; public funds separately 13,521亿元 | 2025-12-31 | FUND-008 | Reported broader AUM ≥RMB 1tn | verified-primary |
| COMP-004 | [GF Fund / 广发基金管理有限公司](COMP-004-gf-fund.md) | FUND-010 profile/business qualifications | >RMB 2tn | Total managed assets; not separately public funds | 2025-12-31 | FUND-010 | Reported broader AUM ≥RMB 1tn | verified-primary |
| COMP-005 | [Industrial Securities Global / 兴证全球基金管理有限公司](COMP-005-industrial-securities-global.md) | FUND-011 case / FUND-012 company identity | RMB 8,333.11亿元 (0.833311tn) | Footnote names manager and capital-management subsidiary | 2026-03-31 | FUND-012 | Reported group AUM RMB 0.5tn–<1tn | verified-primary |
| COMP-006 | [Dacheng / 大成基金管理有限公司](COMP-006-dacheng.md) | FUND-014 profile/business qualifications | >RMB 7,000亿元 (>0.7tn) | Total AUM; public funds separately >4,600亿元 | 2025-12-31 | FUND-014 | Unassigned interval: only a lower bound is disclosed | verified-primary |

Company identity and public-fund activity were checked through profiles and case
descriptions. A current CSRC licence-register cross-check remains a follow-up.
“Top tier” and the required minimum company count remain undefined in the brief.

## Initiative database

| Initiative ID | Company ID | AI / LLM type | Use case | Function | Stage | Technology / model | Technology partner | Disclosed outcome | Disclosure date | Primary source IDs | Evidence state / note |
|---|---|---|---|---|---|---|---|---|---|---|---|
| INIT-001 | COMP-001 | LLM security tooling | LLM security gateway | technology platform / security | procurement completed | Model not disclosed | 北京世纪东凌科技开发有限公司, winning supplier | Procurement award; operational results not disclosed | 2025-12-31 | FUND-001 | verified-primary; not proof of live deployment |
| INIT-002 | COMP-001 | LLM cloud services | Supplier solicitation | technology platform | announcement | Model not disclosed | Not selected/disclosed in inspected page | Solicitation only | 2026-02-05 | FUND-002 | verified-primary; detailed attachment not used |
| INIT-003 | COMP-002 | LLM + deep learning | Integrated index-business platform | research / marketing / trading; platform also supports risk | production (case-reported) | LULU self-developed framework; base model not disclosed | External partner not disclosed | About 1,000 internal users / 300+ daily active; whole-platform figures | PDF date not stated | FUND-004 | verified-primary; LLM-specific benefit not isolated |
| INIT-004 | COMP-003 | Local LLM + RAG | Research parsing, market views, knowledge-based service | research / client service | production (case-reported) | Local LLM unnamed; Ray, ClickHouse, SpringCloud | Self-developed platform; external model partner not disclosed | Reported research workflow >1 week to <3h; not independently validated | PDF date not stated | FUND-007 | verified-primary; reported outcome |
| INIT-005 | COMP-004 | LLM + retrieval augmentation | Financial information/QA assistant | client service / information support | unclear (official service documented) | DeepSeek / Qwen families | Model origins credited; implementation contract not disclosed | Service scope documented; ROI not disclosed | Document date not stated | FUND-009 | verified-primary; availability/topology not tested |
| INIT-006 | COMP-005 | AI / large-model-assisted workflow | Qianxun / Xingbao fixed-income platform | trading / research / risk support | production (case-reported) | Model unnamed; Qtrade integration, LRU, Oracle Data Guard, Kafka | External model partner not disclosed | About 3h saved/trader/day and >50% more inquiry conversations, reported | PDF date not stated | FUND-011 | verified-primary; human execution roles remain |
| INIT-007 | COMP-006 | NLP + Qwen-family model | Transaction-element recognition in fixed-income platform | trading; broader platform research/risk/operations | production (case-reported) | 千问 2.5; Flink, SpringCloud, Vue2.0; O32 integration | Cooperation vendor unnamed | Platform across 10 first-level / 14 second-level units; not LLM-only ROI | PDF date not stated | FUND-013 | verified-primary |

A function attached to a mixed platform is not proof that the LLM performs every
function. No autonomous-trading or regulatory-approval claim is made.
Technology component, model origin, integration endpoint, and contractual partner
are recorded as different things.

## Candidates and coverage

See [the ten-company candidate queue](candidate-queue.md) and its source trail.

| Metric | Requirement / basis | Current |
|---|---|---|
| Distinct verified company disclosures | Brief's numerical minimum still missing | 6 |
| Additional candidate companies | Not included in verified count | 10 |
| Companies with sourced AUM | Scope/date/lower bounds visible | 6 |
| Companies with separately sourced public-fund AUM | Fullgoal and Dacheng | 2 |
| Primary-source initiatives | One company can have multiple initiatives | 7 |
| Human-reviewed company evidence | Actual completed checks | 0 |

## Next verification priorities

1. Expand comparable public-fund AUM at a common cut-off.
2. Trace candidate company reports to originals; do not count media reposts twice.
3. Retrieve publication dates for AMAC cases and the GF agreement if available.
4. Locate a clearly evidenced compliance-review use case rather than treating all
   IT security/ordinary controls as LLM compliance checking.
5. Manually audit source passages and reconcile the eventual company minimum.
