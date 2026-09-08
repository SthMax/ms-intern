---
company_id: COMP-010
evidence_state: verified-primary
accessed: 2026-09-06
reviewed_by: Codex research subagent
human_check_status: pending
---

# Tianhong / 天弘基金管理有限公司

<!-- original-language-provenance:start -->
> [!important] 原文与研究者分析分离
> 本页保留的英文正文、分类及表格是研究者撰写的摘要、整理或分析，不是来源原文。请先阅读下方逐源链接中的原语言文本；中文来源保留中文，原本为英文的来源保留英文。本次未将英文摘要反译为所谓“中文原文”。
> 来源的一手／转载／媒体／供应商属性及证据限制仍按原登记保留；保存原文不等于核实全部研究结论。人工核验仍待完成。

## 原语言来源档案（逐源）

档案中的 `original.md` 是机械提取文本；页面排版、表格和提取缺失以下载文件为准。无法确认正文的响应不作为原文提供，详见元数据。来源标题沿用登记表，仅作定位。

| 来源 ID | 登记标题 | 原登记证据状态 | 原语言正文／下载文件／记录 |
|---|---|---|---|
| FUND-300 | 『基金行业金融科技发展奖』天弘基金：基于大模型的 FinAgent 金融智能体系统 | verified-primary | [原语言正文](../sources/FUND-300/original.md) · [下载文件](../sources/FUND-300/source.pdf) · [元数据与限制](../sources/FUND-300/metadata.json) · [登记网址](https://www.amac.org.cn/xwfb/hydt/202601/P020260202337562370809.pdf) |
| FUND-301 | 行业动态 | verified-primary | [原语言正文](../sources/FUND-301/original.md) · [下载文件](../sources/FUND-301/source.html) · [元数据与限制](../sources/FUND-301/metadata.json) · [登记网址](https://www.amac.org.cn/xwfb/hydt/index_6.html) |
| FUND-302 | 公司介绍 | unresolved | 浏览器已核实并保存原文片段（非整页） · [元数据与限制](../sources/FUND-302/metadata.json) · [登记网址](https://www.thfund.com.cn/about/company) · [本次恢复记录](../sources/FUND-302/recovery.json) |

## 研究者摘要／分析（保留原有正文）

**以下为研究者摘要/分析，不是原文。** 原有事实表述、引用定位、证据状态和局限一并保留，供对照原文复核。
<!-- original-language-provenance:end -->

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

## Asset-size evidence — browser recovery, 7 September 2026

The official company profile was opened successfully in the internal browser.
Its [original Chinese paragraph](../sources/FUND-302/browser-recovered.md) reports,
as of **31 March 2026**, total AUM **12,258.54亿元**, public-fund AUM
**12,048.15亿元**, and non-money public-fund AUM **4,348.45亿元**.
The total explicitly includes special-account AUM **165.31亿元** and subsidiary
Tianhong Innovation special-business AUM **45.08亿元**. These date/scope-specific
figures do not replace the separate Q2 screening rank. The relevant DOM paragraph
is saved; a full offline page export was unsupported. Human review is pending.

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
