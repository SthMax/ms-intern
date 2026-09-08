---
company_id: COMP-003
evidence_state: verified-primary
accessed: 2026-09-06
reviewed_by: Codex
human_check_status: pending
---

# Fullgoal / 富国基金管理有限公司

<!-- original-language-provenance:start -->
> [!important] 原文与研究者分析分离
> 本页保留的英文正文、分类及表格是研究者撰写的摘要、整理或分析，不是来源原文。请先阅读下方逐源链接中的原语言文本；中文来源保留中文，原本为英文的来源保留英文。本次未将英文摘要反译为所谓“中文原文”。
> 来源的一手／转载／媒体／供应商属性及证据限制仍按原登记保留；保存原文不等于核实全部研究结论。人工核验仍待完成。

## 原语言来源档案（逐源）

档案中的 `original.md` 是机械提取文本；页面排版、表格和提取缺失以下载文件为准。无法确认正文的响应不作为原文提供，详见元数据。来源标题沿用登记表，仅作定位。

| 来源 ID | 登记标题 | 原登记证据状态 | 原语言正文／下载文件／记录 |
|---|---|---|---|
| FUND-007 | 『基金行业金融科技发展奖』富国基金：指数基金智能投资决策系统 | verified-primary | [原语言正文](../sources/FUND-007/original.md) · [下载文件](../sources/FUND-007/source.pdf) · [元数据与限制](../sources/FUND-007/metadata.json) · [登记网址](https://www.amac.org.cn/xwfb/hydt/202601/P020260202337808067241.pdf) |
| FUND-008 | 关于富国 | verified-primary | [原语言正文](../sources/FUND-008/original.md) · [下载文件](../sources/FUND-008/source.html) · [元数据与限制](../sources/FUND-008/metadata.json) · [登记网址](https://www.fullgoal.com.cn/main/AboutFuguo/InvestResearch/index.html) |

## 研究者摘要／分析（保留原有正文）

**以下为研究者摘要/分析，不是原文。** 原有事实表述、引用定位、证据状态和局限一并保留，供对照原文复核。
<!-- original-language-provenance:end -->

## Verified disclosure

AMAC's original project case describes a locally hosted LLM used for research
report parsing, market-view generation, and knowledge-based smart search.
The architecture also names Ray, ClickHouse, SpringCloud, Python, and Rust
(PDF p. 5). These components are disclosed stack elements, not commercial
technology partners.

The local-LLM sections describe prompt-based summarization and RAG with source
references (PDF pp. 8–9). The vector-store name is misspelled “mvlius” in the
document; do not silently assert a particular product/version from that spelling.
The base model/vendor is not disclosed.

The case reports a reduction of a research workflow from over a week to under
three hours (PDF p. 9), but supplies no controlled evaluation sample or attribution
isolating the LLM. Stage: operational application reported by the case.

## Asset size

At 31 December 2025: total RMB **19,573亿元** (1.9573 trillion), public-fund AUM
**13,521亿元** (1.3521 trillion), and public assets excluding money-market and
short-term wealth-management bond funds **8,885亿元**. The total combines public
funds, pensions, segregated accounts, subsidiaries, and advisory business.

## Limits

Retain each metric separately. Platform efficiency claims are reported claims,
not independently audited savings. Relevant local-RAG page inspected visually;
human review pending.

## Source trail

- **FUND-007** — [『基金行业金融科技发展奖』富国基金：指数基金智能投资决策系统](https://www.amac.org.cn/xwfb/hydt/202601/P020260202337808067241.pdf). Original association case publication; Publication date not stated in PDF. Locator: PDF pp. 3, 5, 8–10; printed pp. 2, 4, 7–9.
- **FUND-008** — [关于富国](https://www.fullgoal.com.cn/main/AboutFuguo/InvestResearch/index.html). Company profile / AUM; Undated live page; AUM 2025-12-31. Locator: 关于富国 opening AUM paragraph and scope footnote.
