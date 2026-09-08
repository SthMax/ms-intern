---
company_id: COMP-009
evidence_state: verified-primary
accessed: 2026-09-06
reviewed_by: Codex research subagent
human_check_status: pending
---

# China Universal / 汇添富基金管理股份有限公司

<!-- original-language-provenance:start -->
> [!important] 原文与研究者分析分离
> 本页保留的英文正文、分类及表格是研究者撰写的摘要、整理或分析，不是来源原文。请先阅读下方逐源链接中的原语言文本；中文来源保留中文，原本为英文的来源保留英文。本次未将英文摘要反译为所谓“中文原文”。
> 来源的一手／转载／媒体／供应商属性及证据限制仍按原登记保留；保存原文不等于核实全部研究结论。人工核验仍待完成。

## 原语言来源档案（逐源）

档案中的 `original.md` 是机械提取文本；页面排版、表格和提取缺失以下载文件为准。无法确认正文的响应不作为原文提供，详见元数据。来源标题沿用登记表，仅作定位。

| 来源 ID | 登记标题 | 原登记证据状态 | 原语言正文／下载文件／记录 |
|---|---|---|---|
| FUND-220 | 『基金行业金融科技获奖成果宣传活动』汇添富基金：智汇投资风险管理平台 | verified-primary | [原语言正文](../sources/FUND-220/original.md) · [下载文件](../sources/FUND-220/source.pdf) · [元数据与限制](../sources/FUND-220/metadata.json) · [登记网址](https://www.amac.org.cn/xwfb/hydt/202601/P020260202337837900594.pdf) |
| FUND-221 | 汇添富现金宝-汇添富基金打造的投资平台 | verified-primary | [原语言正文](../sources/FUND-221/original.md) · [下载文件](../sources/FUND-221/source.html) · [元数据与限制](../sources/FUND-221/metadata.json) · [登记网址](https://apps.apple.com/cn/app/%E6%B1%87%E6%B7%BB%E5%AF%8C%E7%8E%B0%E9%87%91%E5%AE%9D-%E6%B1%87%E6%B7%BB%E5%AF%8C%E5%9F%BA%E9%87%91%E6%89%93%E9%80%A0%E7%9A%84%E6%8A%95%E8%B5%84%E5%B9%B3%E5%8F%B0/id1061838086) |
| FUND-222 | 【汇添富基金副总经理兼首席信息官李骁】汇添富基金数智化赋能的实践与思考——2025年金融科技发展回顾与2026年展望 | candidate | [原语言正文](../sources/FUND-222/original.md) · [下载文件](../sources/FUND-222/source.html) · [元数据与限制](../sources/FUND-222/metadata.json) · [登记网址](https://finance.sina.cn/2026-03-25/detail-inhsffcq0897979.d.html) |
| FUND-223 | AI智能体落地！汇添富直销平台率先接入DeepSeek | candidate | [原语言正文](../sources/FUND-223/original.md) · [下载文件](../sources/FUND-223/source.html) · [元数据与限制](../sources/FUND-223/metadata.json) · [登记网址](https://www.chnfund.com/article/AR3358889b-f3d5-0c09-2763-3a1894ea2603) |
| FUND-224 | 公司介绍 | verified-primary | [原语言正文](../sources/FUND-224/original.md) · [下载文件](../sources/FUND-224/source.html) · [元数据与限制](../sources/FUND-224/metadata.json) · [登记网址](https://www.99fund.com/main/gywm/gsjs/index.shtml) |
| FUND-225 | RESULTS ANNOUNCEMENT FOR THE YEAR ENDED DECEMBER 31, 2025 | verified-primary | [原语言正文](../sources/FUND-225/original.md) · [下载文件](../sources/FUND-225/source.pdf) · [元数据与限制](../sources/FUND-225/metadata.json) · [登记网址](https://www.hkexnews.hk/listedco/listconews/sehk/2026/0327/2026032703598.pdf) |

## 研究者摘要／分析（保留原有正文）

**以下为研究者摘要/分析，不是原文。** 原有事实表述、引用定位、证据状态和局限一并保留，供对照原文复核。
<!-- original-language-provenance:end -->

## Verified initiative: 智汇投资风险管理平台

**FUND-220** is an original company project report hosted by AMAC and listed on
27 January 2026. It has an added cover: physical PDF page = printed page + 1.

| Dimension | Disclosure and locator |
|---|---|
| Specific LLM uses | Extract risk information from custodian-bank emails; answer risk/compliance-clause questions. The system links risk rules to source regulatory, internal-control and contract clauses so users can locate the basis for a block. PDF pp. 5, 10. |
| Models | Figure 2 explicitly labels **DeepSeek-R1** and **QianWen** in the LLM capability layer. Parameter counts, Qwen version and runtime are not disclosed. PDF p. 7; visually inspected because extraction omitted diagram text. |
| Integration | A risk-data mart and seven risk-management modules integrate with the company's investment/trading system. Figure 2 shows Spring Cloud/Java and Python FastAPI services, Flink, Doris, Oracle and centralized login/authentication. These are architecture components, not proof of contracts with their vendors. PDF pp. 4–7. |
| Governance | Business and technology project managers cooperate; rule changes support review/approval; engine regression tests compare each version to reference-day outputs. No separate LLM-validation protocol is specified. PDF pp. 6, 10. |
| Stage | Reported implemented platform with realized workflows; original go-live date not stated. Contract parsing and automatic rule-element filling are explicitly further work. PDF pp. 8–11. |

Company metrics describe the **whole risk platform/engine**: 500-security batch
checks changed from two minutes to two seconds; instruction rules fell from over
9,000 to over 2,500 (PDF pp. 8–9). They do not measure the LLM's accuracy,
incremental speed-up, cost savings or compliance decisions. Hardware and test
conditions are omitted. No evidence supports autonomous legal approval.

## Verified client-service evidence: DeepSeek in 现金宝 and AI帮你看

**FUND-225**, Orient Securities' 2025 annual report filed on HKEX, explicitly
records China Universal's launch of **DeepSeek in CashPlus (现金宝)** in its fund
management business discussion (physical PDF p. 41, printed p. 40). That supports
the named service's existence, without verifying the 671B runtime, local hosting,
or launch date claimed in news articles. **FUND-224**, China Universal's official
company introduction, independently identifies **AI帮你看** among its CashPlus
innovations.

**FUND-221**, the developer's App Store release history, records the 帮你看
report/holdings/fund-analysis features in version **8.97, 26 May 2025**. Version
8.98 repeats the feature text; later versions describe improvements. This proves
a developer-disclosed product feature and release record, not the precise first
launch date, underlying model or measured outcome. The **current** provider is
**汇添富基金销售（上海）有限公司**, described in the listing as a wholly owned
China Universal subsidiary commencing business in 2026. Current operator
identity must not be projected backwards onto the 2025 release. FUND-224 and
FUND-225 establish the manager-level connection independently.

## Deeper leads pending original-publication verification

**FUND-222** reproduces a named first-person article by deputy general manager/
CIO 李骁, credited to《中国金融电脑》2026年第3期. Its live full text was inspected,
but the original magazine page or issue has not yet been obtained. It describes:

- Private and cloud model services used together, an AI innovation committee,
  GPU investment, an enterprise agent platform and tool calls.
- Research QA over reports, meeting minutes and announcements, with source
  tracing and multi-turn dialogue; 智会通 recording/transcription/minutes entering
  the research knowledge base.
- AI-assisted coding, marketing-image generation and promotional-material
  review, plus the 帮你看 service.

These are valuable, attributable leads. Keep the deployment and additional
workflow details **candidate** until original-publication provenance is closed.

**FUND-223**, the March 2025 news report on DeepSeek in 现金宝, adds DeepSeek-R1,
671B deployment, DeepFund team and model-generated report explanations. It is
not a company-hosted original. “DeepFund” also appears as an unrelated media
account and an academic project: those names must not be merged into this fund
manager's technology stack.

## Asset size

**FUND-225**, physical PDF p. 42 (printed p. 41), reports China Universal's
**public-fund AUM excluding money-market funds above RMB 680.0 billion
(6,800亿元) at 31 December 2025**, approximately 37% above the start of the year.
It is a lower bound, not an exact AUM; ETF-feeder treatment is not specified.
The comparative size-screening list is maintained separately. FUND-224 reports
395 public funds at 2025 Q4 but supplies no matching AUM number; fund count is
not used as an asset-size measure.

## Source trail and review

- **FUND-220** — [『基金行业金融科技获奖成果宣传活动』汇添富基金：智汇投资风险管理平台](https://www.amac.org.cn/xwfb/hydt/202601/P020260202337837900594.pdf). Original company case; [AMAC index](https://www.amac.org.cn/xwfb/hydt/index_3.html) date 2026-01-27; no PDF revision date printed. All 11 pages extracted; physical pp. 5, 7, 9–10 visually inspected in full, including model/architecture labels and numerical claims, using the PDF skill.
- **FUND-221** — [汇添富现金宝-汇添富基金打造的投资平台](https://apps.apple.com/cn/app/%E6%B1%87%E6%B7%BB%E5%AF%8C%E7%8E%B0%E9%87%91%E5%AE%9D-%E6%B1%87%E6%B7%BB%E5%AF%8C%E5%9F%BA%E9%87%91%E6%89%93%E9%80%A0%E7%9A%84%E6%8A%95%E8%B5%84%E5%B9%B3%E5%8F%B0/id1061838086). Developer listing on Apple; current provider 汇添富基金销售（上海）有限公司; version 8.97 dated 2025-05-26. Developer/provider, company description and version history checked; operator transition prevents inferring historical legal ownership from today's field.
- **FUND-222** — [【汇添富基金副总经理兼首席信息官李骁】汇添富基金数智化赋能的实践与思考——2025年金融科技发展回顾与2026年展望](https://finance.sina.cn/2026-03-25/detail-inhsffcq0897979.d.html). Sina distribution dated 2026-03-25, source 中国金融电脑; II.1–2 and issue attribution at end. Full live HTML checked; primary magazine issue outstanding.
- **FUND-223** — [AI智能体落地！汇添富直销平台率先接入DeepSeek](https://www.chnfund.com/article/AR3358889b-f3d5-0c09-2763-3a1894ea2603). 中国基金报, 2025-03-11; media-discovery lead for local deployment/model version/DeepFund provenance.
- **FUND-224** — [公司介绍](https://www.99fund.com/main/gywm/gsjs/index.shtml). Undated official company introduction; CashPlus/e-commerce paragraph naming AI帮你看; adjacent public-fund paragraph as of 2025 Q4. Direct HTML decoded from GB18030 and inspected.
- **FUND-225** — [RESULTS ANNOUNCEMENT FOR THE YEAR ENDED DECEMBER 31, 2025](https://www.hkexnews.hk/listedco/listconews/sehk/2026/0327/2026032703598.pdf). Orient Securities/DFZQ, 2026-03-27, includes full Annual Report 2025; physical pp. 41–42 (printed 40–41), Section III, Fund management business. Complete relevant pages text-checked and visually inspected. The [Chinese filing](https://www.hkexnews.hk/listedco/listconews/sehk/2026/0327/2026032703599_c.pdf) has encoding/font-mapping issues in this environment; precise claims were checked in the official English filing. No legal conclusion is based on this translation.

China Universal's public company-news search also links to a media copy of the
March 2025 launch story. This establishes an official navigation trail, but it
does not convert all the media article's technical assertions into independently
verified implementation details. The publisher's own《中国金融电脑》website
was found; its search facility returned “搜索暂停使用”, leaving FUND-222's
original-issue retrieval open.

Reviewed by an agent on 6 September 2026; human checks pending. The original
project report establishes the company's disclosure, not independently audited
ROI, control effectiveness or regulatory approval.
