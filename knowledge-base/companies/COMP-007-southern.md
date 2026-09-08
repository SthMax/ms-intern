---
company_id: COMP-007
evidence_state: verified-primary
accessed: 2026-09-06
reviewed_by: Codex research subagent
human_check_status: pending
---

# Southern Asset Management / 南方基金管理股份有限公司

<!-- original-language-provenance:start -->
> [!important] 原文与研究者分析分离
> 本页保留的英文正文、分类及表格是研究者撰写的摘要、整理或分析，不是来源原文。请先阅读下方逐源链接中的原语言文本；中文来源保留中文，原本为英文的来源保留英文。本次未将英文摘要反译为所谓“中文原文”。
> 来源的一手／转载／媒体／供应商属性及证据限制仍按原登记保留；保存原文不等于核实全部研究结论。人工核验仍待完成。

## 原语言来源档案（逐源）

档案中的 `original.md` 是机械提取文本；页面排版、表格和提取缺失以下载文件为准。无法确认正文的响应不作为原文提供，详见元数据。来源标题沿用登记表，仅作定位。

| 来源 ID | 登记标题 | 原登记证据状态 | 原语言正文／下载文件／记录 |
|---|---|---|---|
| FUND-200 | 『基金行业金融科技获奖成果宣传活动』南方基金：基于多智能体协同的交易助理 | verified-primary | [原语言正文](../sources/FUND-200/original.md) · [下载文件](../sources/FUND-200/source.pdf) · [元数据与限制](../sources/FUND-200/metadata.json) · [登记网址](https://www.amac.org.cn/xwfb/hydt/202601/P020260202337849876845.pdf) |
| FUND-201 | 南方基金电子直销用户服务协议 | verified-primary | [原语言正文](../sources/FUND-201/original.md) · [下载文件](../sources/FUND-201/source.html) · [元数据与限制](../sources/FUND-201/metadata.json) · [登记网址](https://wap.southernfund.com/mweb/agreement/xieyi_register_v2.html) |
| FUND-202 | 华泰证券股份有限公司 | verified-primary | [原语言正文](../sources/FUND-202/original.md) · [下载文件](../sources/FUND-202/source.html) · [元数据与限制](../sources/FUND-202/metadata.json) · [登记网址](https://app.cnstock.com/zzb/zgzqb/html/2026-03/31/nw.D110000zgzqb_20260331_1-B071.htm) |
| FUND-203 | 拥抱AI，南方基金ETFirst Skill重塑指数投资服务生态 | candidate | [原语言正文](../sources/FUND-203/original.md) · [下载文件](../sources/FUND-203/source.html) · [元数据与限制](../sources/FUND-203/metadata.json) · [登记网址](https://finance.sina.com.cn/wm/2026-07-08/doc-inihatty8088729.shtml) · [微信原刊及核对](../sources/wechat-articles/README.md) |

## 研究者摘要／分析（保留原有正文）

**以下为研究者摘要/分析，不是原文。** 原有事实表述、引用定位、证据状态和局限一并保留，供对照原文复核。
<!-- original-language-provenance:end -->

## Verified initiatives

### Multi-agent trading assistant: 小喃同学

**FUND-200** is a company case submission hosted by AMAC, listed on 23 January
2026. The current 11-page PDF uses **小喃同学**. The older search-indexed PDF
uses 小南 and now returns 404; use the working source below. Physical PDF pages
are one greater than printed page numbers because of its added cover.

| Dimension | Disclosure and locator |
|---|---|
| Use case | Trading workflow assistance: natural-language queries, bond screening, inquiry, instructions and internal-system operations. PDF pp. 4–8, sections II–III. |
| Implementation | A fine-tuned, unnamed LLM decomposes tasks; a scheduler invokes API, SQL, retrieval and custom/Python executors. SQL agents select tables, write and check queries, and explain results. PDF pp. 4–6. |
| Retrieval and integration | RAG, FAQ and search are combined; Elasticsearch is named. Wind is an external information source and IDeal an integration platform. These mentions do not establish procurement contracts. PDF pp. 7–9. |
| Human and access controls | Terminal, role and network jointly determine access. High-sensitivity instructions require internal-network PC use, senior role, a second user confirmation and token authentication. Medium-sensitivity actions have dynamic passwords/confirmation; lower-sensitivity results filter sensitive fields. Python uses a sandbox. PDF pp. 4, 6. |
| Stage | The conclusion says the assistant has entered production use; opening language also describes an early pilot. Record **company-reported production**, with no precise go-live date. PDF pp. 2, 10–11. |
| Missing | Model name, parameter count, GPU configuration, inference engine, deployment topology, model-evaluation sample and independent control testing. |

The company reports 40% less daily trader operation time and potential release
of over 1,000 person-days annually; reverse-repurchase operation time falls by
one third (PDF p. 8, III.1). No observation window, staffing denominator or
controlled baseline is supplied. These are system-level reported efficiencies,
not isolated LLM effects, realized headcount savings, or audited ROI.

The report discusses TradingAgents as background research. It does **not** say
Southern deployed that framework. Architecture logos are illustrative integration
labels, not sufficient evidence of technology partnerships. Its especially large
daily transaction-volume claim has ambiguous scope and is excluded from the
comparison.

### Customer AI assistant in official service terms

**FUND-201**, section III.2 of Southern's electronic direct-sales service
agreement, names the open-source Tongyi Qianwen model and a Southern-specific
knowledge base. Disclosed services cover fund/product/manager searches, market
information, business rules and platform-use questions. The agreement says
responses undergo content-compliance processing and cautions that generated
answers may be wrong or incomplete; generated-content labels are addressed in
III.5. It identifies Alibaba DAMO as the model origin, without establishing a
commercial partner, model version, hosting location or real-time human review.
Publication and launch dates are not printed. Stage: **service documented in
official terms; live usage not tested**.

## Asset size

**FUND-202**, Huatai Securities' annual-report summary as published on the
newspaper's disclosure page, reports Southern's **31 December 2025 public-fund
AUM of RMB 1,512.566 billion (15,125.66亿元)** and total AUM of
**RMB 2,827.868 billion (28,278.68亿元)**. The public-fund figure includes money
funds; it is not the same metric as the separate non-money/ETF-feeder-excluded
screening cohort. The two figures describe Southern, not Huatai's consolidated
asset-management AUM.

## Further leads, not verified adoption facts

**FUND-203** describes ETFirst Skill within the 首趋E指 mini-program, with
natural-language ETF/index queries and an external-assistant/API-key connection.
Its source link has now been archived from the 中国基金报 WeChat account
(2026-07-08 17:04:16 Asia/Shanghai, HTML ct). The three-step configuration and
AI-content risk notice match the Sina body. An original Southern-authored
disclosure or public product documentation has not yet been located. This is a candidate for follow-up, not evidence that confidential desk
data can safely be sent to an external assistant.

## Source trail and review

- **FUND-200** — [『基金行业金融科技获奖成果宣传活动』南方基金：基于多智能体协同的交易助理](https://www.amac.org.cn/xwfb/hydt/202601/P020260202337849876845.pdf). Original company case, AMAC host. [AMAC listing](https://www.amac.org.cn/xwfb/hydt/index_3.html) dates it 2026-01-23; PDF revision date not stated. All 11 pages extracted; complete physical pp. 5–8 visually inspected, including Figures 1–2, permissions and reported efficiencies. The PDF skill was used for visual checks.
- **FUND-201** — [南方基金电子直销用户服务协议](https://wap.southernfund.com/mweb/agreement/xieyi_register_v2.html). Undated official terms, III.1–2 and III.5. Direct live HTML inspected: Exa's extracted copy omitted the AI section, so the narrower extraction was not relied upon.
- **FUND-202** — [华泰证券股份有限公司](https://app.cnstock.com/zzb/zgzqb/html/2026-03/31/nw.D110000zgzqb_20260331_1-B071.htm). Annual-report-summary disclosure, 中国证券报 B071, 2026-03-31; second section, investment-management business, paragraph naming 南方基金. The summary is signed 2026-03-30. Exact AUM paragraph and annual reporting period checked in direct HTML.
- **FUND-203** — [拥抱AI，南方基金ETFirst Skill重塑指数投资服务生态](https://finance.sina.com.cn/wm/2026-07-08/doc-inihatty8088729.shtml). 2026-07-08 media-distribution lead; upstream 中国基金报 WeChat original now archived and compared in the [WeChat archive](../sources/wechat-articles/README.md). Publisher recovery does not make it a Southern-authored deployment record.

Two other working AMAC copies linked from the same listing,
[copy A](https://www.amac.org.cn/xwfb/hydt/202605/P020260507641128700604.pdf) and
[copy B](https://www.amac.org.cn/xwfb/hydt/202605/P020260507634384177787.pdf),
were retrieved and have identical extracted full text to FUND-200. They are
duplicates, not independent corroboration; their URL dates are not treated as
publication dates.

Review was by an agent on 6 September 2026. Human verification remains pending;
company assertions of safety or regulatory compliance are not independently
established by an award submission or service agreement.
