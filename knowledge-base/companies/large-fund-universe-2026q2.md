# Large-Fund Research Universe — 2026 Q2 Screen

<!-- original-language-provenance:start -->
> [!important] 原文与研究者分析分离
> 本页保留的英文正文、分类及表格是研究者撰写的摘要、整理或分析，不是来源原文。请先阅读下方逐源链接中的原语言文本；中文来源保留中文，原本为英文的来源保留英文。本次未将英文摘要反译为所谓“中文原文”。
> 来源的一手／转载／媒体／供应商属性及证据限制仍按原登记保留；保存原文不等于核实全部研究结论。人工核验仍待完成。

## 原语言来源档案（逐源）

档案中的 `original.md` 是机械提取文本；页面排版、表格和提取缺失以下载文件为准。无法确认正文的响应不作为原文提供，详见元数据。来源标题沿用登记表，仅作定位。

| 来源 ID | 登记标题 | 原登记证据状态 | 原语言正文／下载文件／记录 |
|---|---|---|---|
| FUND-090 | 多家公募完成DeepSeek-R1版本的私有化部署 应用于多个核心业务场景 | candidate | [原语言正文](../sources/FUND-090/original.md) · [下载文件](../sources/FUND-090/source.html) · [元数据与限制](../sources/FUND-090/metadata.json) · [登记网址](https://www.chnfund.com/article/ARb3b8504a-126c-79fa-d5a0-3a17f32955bc) |
| FUND-400 | 公募非货规模最新座次出炉，万亿公募增至3家，中段座次重排 | candidate | [原语言正文](../sources/FUND-400/original.md) · [下载文件](../sources/FUND-400/source.html) · [元数据与限制](../sources/FUND-400/metadata.json) · [登记网址](https://www.cls.cn/detail/2432695) |
| FUND-401 | 基金管理机构非货币公募基金月均规模（20家）（2024年三季度） | verified-primary | [原语言正文](../sources/FUND-401/original.md) · [下载文件](../sources/FUND-401/source.pdf) · [元数据与限制](../sources/FUND-401/metadata.json) · [登记网址](https://www.amac.org.cn/sjtj/datastatistics/assetmanagementdata/smzg_ywpm/202411/P020241106606145403776.pdf) |

## 研究者摘要／分析（保留原有正文）

**以下为研究者摘要/分析，不是原文。** 原有事实表述、引用定位、证据状态和局限一并保留，供对照原文复核。
<!-- original-language-provenance:end -->

Research date: **6 September 2026**. This replaces disclosure-led sampling as the
main selection method: establish a large-manager universe, then investigate each
manager's actual AI/LLM use. E Fund is the mentor-prioritized deep case.

## Selection rule and source quality

Use the **top 20 managers in one published 2026-Q2 non-money public-fund AUM
table, excluding ETF feeder-fund value**, as a transparent screening cohort.
This is a research choice, not the mentor's still-missing numerical minimum.

**FUND-400:** [CLS original report, 21 July 2026](https://www.cls.cn/detail/2432695),
opening section and [embedded ranking table](https://image.cls.cn/images/20260721/Aw37CDawlh_718x1396.png).
The original article and image were inspected. The ranking remains
**secondary, screening-only evidence**; underlying provider data have not been
independently reconstructed. Values and rank are reported as that source presents
them, without merging other publishers' different tables.

**FUND-401:** [AMAC original 2024-Q3 table](https://www.amac.org.cn/sjtj/datastatistics/assetmanagementdata/smzg_ywpm/202411/P020241106606145403776.pdf),
PDF page 1, provides an older primary-source check of large-manager membership.
It measures **quarterly mean non-money public-fund AUM after removing duplicate
counting**. It is not a 2026 ranking and cannot be used to calculate growth from
the current quarter-end numbers.

Non-money AUM captures scale relevant to this research; it is not a measure of
active-management quality or AI sophistication. Tianhong remains in the cohort
despite its large money-market business. Earlier Dacheng work is retained as a
supplementary case outside this reported top 20.

## Universe and work coverage

AUM unit: **RMB 亿元 (100 million)**. 2026 column is quarter-end; 2024 column is
quarterly mean. Do not subtract them or rank mixed company-profile/group AUM.

| Reported 2026-Q2 rank | Manager | 2026-Q2 non-money AUM, feeders excluded | Historical AMAC 2024-Q3 monthly-mean AUM | Company ID | Research status |
|---|---|---:|---:|---|---|
| 1 | 易方达 / E Fund | 17029.86 | 12,307.21 | COMP-002 | Primary: dedicated EFundGPT / business / engineering deep dive |
| 2 | 华夏 / ChinaAMC | 11987.79 | 10,556.94 | COMP-001 | Primary: LLM procurement and operational AI platform context |
| 3 | 广发 / GF Fund | 10355.25 | 7,887.25 | COMP-004 | Primary: official LLM customer-service terms |
| 4 | 富国 / Fullgoal | 9889.56 | 6,104.70 | COMP-003 | Primary: detailed local-LLM/RAG case |
| 5 | 南方 / Southern | 7856.35 | 5,944.50 | COMP-007 | Primary: 小喃 agents and official customer AI terms |
| 6 | 汇添富 / China Universal | 7719.67 | 4,795.50 | COMP-009 | Primary: risk-platform LLM and CashPlus services |
| 7 | 景顺长城 / Invesco Great Wall | 7465.45 | 3,881.23 | COMP-014 | Candidate adoption; primary identity/AUM only |
| 8 | 嘉实 / Harvest | 6911.96 | 6,597.56 | COMP-011 | Primary AI/NLP; specific foundation LLM unverified |
| 9 | 博时 / Bosera | 6386.18 | 5,676.68 | COMP-008 | Primary: private DeepSeek and BSBox |
| 10 | 鹏华 / Penghua | 6366.21 | 4,225.31 | COMP-012 | Primary: private model matrix and review assistants |
| 11 | 招商 / China Merchants | 6276.62 | 5,503.59 | COMP-018 | Candidate: detailed reporting; primary implementation unresolved |
| 12 | 国泰 / Guotai | 6238.11 | 3,436.59 | COMP-015 | Primary: DeepSeek RAG and distinct BERT NLP |
| 13 | 永赢 / Maxwealth | 5332.53 | 3,201.66 | COMP-019 | Primary: operational LLM mail-security case |
| 14 | 工银瑞信 / ICBC Credit Suisse | 5006.18 | 3,695.00 | COMP-013 | Primary: FundGPT and named vendor roles |
| 15 | 天弘 / Tianhong | 4824.03 | 3,430.85 | COMP-010 | Primary: FinAgent / Think / THAI |
| 16 | 中欧 / China Europe | 4687.70 | 2,868.79 | COMP-020 | Candidate: traced company-account media reprint |
| 17 | 华安 / Hua An | 4632.07 | 3,419.19 | COMP-016 | Primary: CCF technical case for 灵思 |
| 18 | 华泰柏瑞 / Huatai-PineBridge | 4459.62 | 4,878.41 | COMP-021 | Candidate: detailed narrative report; primary unresolved |
| 19 | 兴证全球 / Industrial Securities Global | 3751.87 | 2,647.51 | COMP-005 | Primary: Qianxun / Xingbao workflow |
| 20 | 平安 / Ping An | 3447.69 | Not in this historical top 20 | COMP-017 | Candidate: AI青蚨 / review-platform reporting |

All 20 managers now have case/search dossiers in the current
[company index](index.md): 15 have primary initiative evidence and 5 remain
candidate/unresolved for adoption. A manager remains in the universe even where its
AI/LLM evidence is unresolved. Absence of a qualifying source is not evidence
of no adoption.

## What deeper case research must establish

For each priority manager, record dated evidence for: named workflow/product;
model version and deployment if disclosed; data/retrieval architecture; technology
partner role; integration and human checks; reported result and its baseline;
and what is still unknown. Distinguish modern LLMs from earlier AI/NLP, fund
managers from their bank/broker parents, and open-source origin from a contract.

## Screening evidence and unresolved leads

- China Merchants / Maxwealth / China Europe / Invesco Great Wall: deployment
  claims in industry interviews remain leads until an original company or
  technical disclosure is found (existing FUND-090 and additional sources in the
  root research batch).
- Hua An: the company-hosted news article remains secondary; a separate original
  CCF technical case now supplies primary operational evidence.
- Huatai-PineBridge and Ping An: current interviews describe concrete workflows;
  original team/technical documents remain the next step.
- Exact legal entity and available official company AUM are recorded in each
  completed company note; missing comparable AUM stays visible. These observations
  are separate from this source-attributed rank.

This file defines research coverage. It does not certify the rank provider's raw
data, an industry's adoption rate, or a production system's effectiveness.
