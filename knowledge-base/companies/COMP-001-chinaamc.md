---
company_id: COMP-001
evidence_state: verified-primary
accessed: 2026-09-06
reviewed_by: Codex
human_check_status: pending
award_pdf_sha256: e111c0969036c3fd2935fd4d477ab477211d6f2dd56d1e988eb507d5e298a6b8
---

# ChinaAMC / 华夏基金管理有限公司

<!-- original-language-provenance:start -->
> [!important] 原文与研究者分析分离
> 本页保留的英文正文、分类及表格是研究者撰写的摘要、整理或分析，不是来源原文。请先阅读下方逐源链接中的原语言文本；中文来源保留中文，原本为英文的来源保留英文。本次未将英文摘要反译为所谓“中文原文”。
> 来源的一手／转载／媒体／供应商属性及证据限制仍按原登记保留；保存原文不等于核实全部研究结论。人工核验仍待完成。

## 原语言来源档案（逐源）

档案中的 `original.md` 是机械提取文本；页面排版、表格和提取缺失以下载文件为准。无法确认正文的响应不作为原文提供，详见元数据。来源标题沿用登记表，仅作定位。

> [!warning] 动态网页已变化：2026-09-07获取快照与历史观察不同
> FUND-003：本次网页快照写明截至2025年末管理资产规模超3.2万亿元人民币，页面脚注明确总管理规模含子公司。旧笔记中的2025年二季度末超3万亿元是此前观察，未保存对应历史页面，本次快照不能重新核实该历史数值。
> 上述均为较宽资产管理口径，不能直接替代2026-Q2非货公募筛选排名；本次不调整筛选排名。

| 来源 ID | 登记标题 | 原登记证据状态 | 原语言正文／下载文件／记录 |
|---|---|---|---|
| FUND-001 | 关于华夏基金管理有限公司采购结果的公告 | verified-primary | [原语言正文](../sources/FUND-001/original.md) · [下载文件](../sources/FUND-001/source.pdf) · [元数据与限制](../sources/FUND-001/metadata.json) · [登记网址](https://www.chinaamc.com/upload/resources/file/2025/12/31/442744.pdf) |
| FUND-002 | 华夏基金管理有限公司大模型云服务项目潜在供应商征集公告 | verified-primary | [原语言正文](../sources/FUND-002/original.md) · [下载文件](../sources/FUND-002/source.html) · [元数据与限制](../sources/FUND-002/metadata.json) · [登记网址](https://www.chinaamc.com/c/2026-02-05/926147.shtml) |
| FUND-003 | 公司概览 | verified-primary | [原语言正文](../sources/FUND-003/original.md) · [下载文件](../sources/FUND-003/source.html) · [元数据与限制](../sources/FUND-003/metadata.json) · [登记网址](https://www.chinaamc.com/jgb/gyhx/gsgl/) |
| FUND-402 | 『基金行业金融科技获奖成果宣传活动』华夏基金：飞翼固收一体化智能平台 | verified-primary | [原语言正文](../sources/FUND-402/original.md) · [下载文件](../sources/FUND-402/source.pdf) · [元数据与限制](../sources/FUND-402/metadata.json) · [登记网址](https://www.amac.org.cn/xwfb/hydt/202602/P020260202337823336223.pdf) |

## 研究者摘要／分析（保留原有正文）

**以下为研究者摘要/分析，不是原文。** 原有事实表述、引用定位、证据状态和局限一并保留，供对照原文复核。
<!-- original-language-provenance:end -->

## Verified disclosures

- **LLM security gateway:** the 31 December 2025 procurement award names
  北京世纪东凌科技开发有限公司 as winning supplier. The row distinguishes
  candidates from the winner. Stage: procurement completed, operational
  deployment not established. Function: technology platform/security.
- **LLM cloud-service solicitation:** the 5 February 2026 official title establishes
  an active procurement initiative. No winning supplier or deployment follows
  from that title. Stage: announcement; function: technology platform.

The award's [publication page](https://www.chinaamc.com/c/2025-12-31/920510.shtml)
supplies its date. The cloud solicitation attachment was located but its detailed
requirements have not been used as findings.

## Deeper operational case: 飞翼 fixed-income platform

**FUND-402** describes the Feiyi platform begun in 2020 and subsequently used in
production for fixed-income research and trading. It combines factor/strategy
research, portfolio optimisation, transaction-element recognition, reconciliation
and electronic execution interfaces (physical PDF pp. 2–7; printed pp. 1–6).
QTrade/iDeal and X-BOND are workflow/data interfaces, not evidence of a model
supplier contract. Linear/discrete programming and algorithmic backtesting are
not automatically LLM functions.

The case reports three blocks, eight subsystems, 20+ modules, and support for
trillion-yuan-scale fixed-income portfolios. Its >100 spot-bond trades per person
per day and near-zero execution-error description concern the integrated
platform; no isolated LLM measurement or independent error audit is supplied.

The outlook (PDF p. 8) discusses further LLM application in research-resource
reuse and information extraction. Do not label the platform's 2020 construction
as an LLM launch, or infer a foundation-model version from generic AI wording.
This case deepens the operational context alongside the two verified LLM
procurements, without proving those procurements powered Feiyi.

## Asset size

The FUND-003 snapshot retrieved on 7 September 2026 reports managed assets
above RMB 3.2 trillion at 2025 year-end; its footnote includes subsidiaries.
This is broader managed assets, not standalone public-fund AUM. The earlier
research observation was above RMB 3 trillion at 2025 Q2-end. That historical
page was not archived, and the current snapshot does not reverify it.

## Assessment and limits

This is concrete evidence of procurement and a named supplier. It does not
establish model choice, system acceptance, performance, cloud location, or the
firm's general data policy. The security-gateway award PDF was inspected visually
to verify row/column alignment. Human review pending.

## Source trail

- **FUND-402** — [『基金行业金融科技获奖成果宣传活动』华夏基金：飞翼固收一体化智能平台](https://www.amac.org.cn/xwfb/hydt/202602/P020260202337823336223.pdf). Original company case hosted by AMAC; complete PDF text inspected, material outcomes/outlook pages checked. Publication date not stated.

- **FUND-001** — [关于华夏基金管理有限公司采购结果的公告](https://www.chinaamc.com/upload/resources/file/2025/12/31/442744.pdf). Company procurement award; 2025-12-31. Locator: PDF p. 1, 大模型安全网关 row; publication page dated 2025-12-31.
- **FUND-002** — [华夏基金管理有限公司大模型云服务项目潜在供应商征集公告](https://www.chinaamc.com/c/2026-02-05/926147.shtml). Company procurement solicitation; 2026-02-05. Locator: Page title and date.
- **FUND-003** — [公司概览](https://www.chinaamc.com/jgb/gyhx/gsgl/). Company profile / AUM; current archived snapshot: 2025 year-end, total includes subsidiaries. Earlier unarchived observation: 2025 Q2. Current locator: 管理规模领先; 数据来源 footnote.
