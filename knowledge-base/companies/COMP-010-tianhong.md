---
company_id: COMP-010
evidence_state: verified-primary
accessed: 2026-09-06
reviewed_by: Codex research subagent
human_check_status: pending
---

# Tianhong / 天弘基金管理有限公司

## Research conclusion

Tianhong has a detailed original AMAC-hosted case for its **FinAgent financial
agent system**, including the self-developed **Think** model, **THAI** inference
platform, **弘思 3.0** financial RAG and **智搜 2.0** search. The case describes
operational research and distribution workflows. This is considerably stronger
evidence than a generic announcement that a fund company is exploring AI.

AMAC's [industry index](https://www.amac.org.cn/xwfb/hydt/index_6.html)
dates the linked case **19 January 2026** (FUND-301). The PDF itself has no
publication date; the two facts are kept separate. The case says self-development
began in 2023 (FUND-300, PDF p. 4 / printed p. 3).

## Verifiable application and architecture details

| Item | Narrow disclosure | Locator in FUND-300 |
|---|---|---|
| Model and serving | Think financial model; THAI supports pooled GPUs and concurrent inference | PDF p. 5 / printed p. 4 |
| Retrieval and tools | 弘思 3.0 RAG, 智搜 2.0 search, financial calculation tools, Wind and Tonghuashun interfaces, MCP tool connectivity | PDF p. 5 / printed p. 4 |
| Research | Earnings-driver decomposition from financial statements, with macro/industry context | PDF p. 6 / printed p. 5 |
| Marketing | Fund-manager viewpoint summaries assembled from roadshow notes, comments and periodic reports; industry weekly views; daily market briefs | PDF pp. 7–9 / printed pp. 6–8 |
| Risk / service | Event interpretation and customer-adviser conversation practice | PDF pp. 10–11 / printed pp. 9–10 |
| Disclosed safeguards | Input screening, human-feedback alignment, output review, key-fact cross-checks and traceable references | PDF pp. 5–6 / printed pp. 4–5 |

Wind and Tonghuashun are named data/tool interfaces, **not verified model
implementation contractors**. Self-development does not establish that every
component or training base is proprietary. The case does not identify the
base-model lineage, parameter counts, GPU quantities, inference engine, vector
database product, data-centre location, or internet-egress design.

## Reported outcomes and interpretation limits

The case reports manual data organisation/calculation for earnings-driver
decomposition shrinking from days to minutes (PDF p. 6), and one partner bank's
advisers' daily information-gathering time from 2–3 hours to 15 minutes
(PDF p. 9). These are company-case claims with limited sample/methodology detail.
They are useful questions for later pilot design, not transferable ROI estimates.

The source also claims a 12% advantage over GPT-4o in a financial evaluation
(PDF p. 5). Dataset, model version, scoring and replication materials are absent;
**do not use this as a validated model benchmark**. Claims of avoiding investor
redemptions or investment losses do not establish causal AI performance.

The named guardrails establish what the case says was designed. They do not
prove that every output is faithful, that controls were independently tested,
or that a regulator approved the deployment.

## Asset-size evidence

The size-first research universe is maintained separately. A current,
same-date public-fund-only AUM figure has not yet been verified in this note.
The official profile is [公司介绍](https://www.thfund.com.cn/about/company);
any broad company/subsidiary AUM must remain distinct from public-fund AUM.

## Verification and source trail

Codex downloaded the original AMAC PDF and inspected all text pages with pypdf;
PDF pp. 5–6 were rendered for visual checking of the technical claims and
controls. Human checking remains pending. No internal system was accessed.

- **FUND-300** — [『基金行业金融科技发展奖』天弘基金：基于大模型的 FinAgent 金融智能体系统](https://www.amac.org.cn/xwfb/hydt/202601/P020260202337562370809.pdf). Original company case hosted by AMAC; operational claims and self-reported outcomes.
- **FUND-301** — [行业动态](https://www.amac.org.cn/xwfb/hydt/index_6.html). Original AMAC index; linked case listed as 2026-01-19. Pagination can change.

## Follow-up verification targets

Identify the training base and model licence; obtain explicit hosting/egress
disclosure; locate benchmark methodology and measured user coverage; verify
same-date public-fund AUM. These gaps do not negate the disclosed applications.
