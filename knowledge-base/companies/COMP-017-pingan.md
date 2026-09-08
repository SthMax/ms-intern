---
company_id: COMP-017
evidence_state: candidate
research_cutoff: 2026-09-06
accessed: 2026-09-06
reviewed_by: Codex
human_check_status: pending
---

# Ping An Fund / 平安基金管理有限公司

<!-- original-language-provenance:start -->
> [!important] 原文与研究者分析分离
> 本页保留的英文正文、分类及表格是研究者撰写的摘要、整理或分析，不是来源原文。请先阅读下方逐源链接中的原语言文本；中文来源保留中文，原本为英文的来源保留英文。本次未将英文摘要反译为所谓“中文原文”。
> 来源的一手／转载／媒体／供应商属性及证据限制仍按原登记保留；保存原文不等于核实全部研究结论。人工核验仍待完成。

## 原语言来源档案（逐源）

档案中的 `original.md` 是机械提取文本；页面排版、表格和提取缺失以下载文件为准。无法确认正文的响应不作为原文提供，详见元数据。来源标题沿用登记表，仅作定位。

| 来源 ID | 登记标题 | 原登记证据状态 | 原语言正文／下载文件／记录 |
|---|---|---|---|
| FUND-160 | 平安基金发布“AI青蚨”：破解数据“沉睡”困局 构建智能投研新范式 | candidate | [原语言正文](../sources/FUND-160/original.md) · [下载文件](../sources/FUND-160/source.html) · [元数据与限制](../sources/FUND-160/metadata.json) · [登记网址](https://www.cs.com.cn/ssgs/gsxl/202602/t20260206_6537131.html) |
| FUND-161 | AI重塑资管业！从千人千面到“价值深耕”，四大机构最新研判 | candidate | [原语言正文](../sources/FUND-161/original.md) · [下载文件](../sources/FUND-161/source.html) · [元数据与限制](../sources/FUND-161/metadata.json) · [登记网址](https://www.chnfund.com/article/ARae630e7e-72d1-f00a-3da7-3a218b519b1b) |
| FUND-162 | 平安基金管理有限公司 | verified-primary | [原语言正文](../sources/FUND-162/original.md) · [下载文件](../sources/FUND-162/source.html) · [元数据与限制](../sources/FUND-162/metadata.json) · [登记网址](https://fund.pingan.com/) |

## 研究者摘要／分析（保留原有正文）

**以下为研究者摘要/分析，不是原文。** 原有事实表述、引用定位、证据状态和局限一并保留，供对照原文复核。
<!-- original-language-provenance:end -->

Status: detailed AI/LLM disclosure leads located, but the underlying original
company/association technical record was not found in this focused pass. Exclude
from primary-only adoption and initiative counts. This is the onshore fund
manager, not Ping An Bank, Ping An Asset Management or the insurance group's
separate AI projects.

The [official fund-manager homepage](https://fund.pingan.com/) (FUND-162) provides
company identity and public-fund products. It is identity evidence, not adoption
evidence. No company-wide AUM figure was verified from it. The current screening
rank is recorded separately in [the large-manager universe](large-fund-universe-2026q2.md).

## AI青蚨: detailed technical lead

**FUND-160** — [平安基金发布“AI青蚨”：破解数据“沉睡”困局 构建智能投研新范式](https://www.cs.com.cn/ssgs/gsxl/202602/t20260206_6537131.html),
China Securities Journal, 2026-02-06 11:28. The feature has media provenance;
the “CIS” marker does not identify a company-author source.

Its “应势而生” section describes RAG over reports/documents/transcripts: text
processing and entities, embeddings, query expansion, dense-plus-keyword retrieval,
reranking and summaries with citations. It reports core-view extraction falling
from 30–60 minutes to under five minutes and mentions an HR assistant.

Its “稳健前行” section describes lower temperature, original-document links,
researcher review before adopting key investment suggestions, input/output
filters, logs and automated checks plus manual sampling. Treat these as reported
controls; their implementation and effectiveness were not inspected. Model family,
vector database, hardware, hosting and retention periods are not specified.

The feature's “seconds” phrasing and under-five-minute workflow comparison need
separate measurement definitions; neither supplies quality-adjusted ROI. Plans
to explore MCP/Skills are future intentions, not existing integrations.

## Named executive's forum comments

**FUND-161** — [AI重塑资管业！从千人千面到“价值深耕”，四大机构最新研判](https://www.chnfund.com/article/ARae630e7e-72d1-f00a-3da7-3a218b519b1b),
China Fund News, 2026-05-31 10:19, describing its 2026-05-29 forum.

In “AI正在重塑资管业的各个环节”, information-technology head 游自强 is
quoted describing AI青蚨, personalized research Agents, automated meeting notes,
daily group-message digests and an AI review platform initially covering
disclosures. Prospectus/contract review is future expansion; the marketing
platform is described as under construction. These stage distinctions should
remain explicit.

This is the event organizer's own reporter-authored Q&A account, with named
participants and photographs. It is stronger than an unattributed repost but
is retained as supplementary deployment evidence under the repository's rule;
the recording or a company-issued transcript is still needed. Do not treat
another participant's technical advice as Ping An's implementation.

## Original-source checks and unresolved items

On 2026-09-06 Codex inspected the official homepage and
[company news directory](https://fund.pingan.com/main/conpanyNews/index.shtml).
Its public frontend's read-only archive query uses `funcNo=520004`, `catalogId=501`.
A query for 青蚨 returned zero records; an unfiltered first page returned current
and historical articles, confirming the endpoint responded. This is a title/archive
search limitation, not evidence that Ping An has made no disclosure.

The archive listed [“平台化”驱动投研质效再升级，平安基金跑出转型加速度](https://fund.pingan.com/main/aV2/20251031/77214.shtml),
dated 2025-10-31, but opening it returned a page containing the site's 404 image.
No adoption claim is extracted from that unavailable body. General web/Exa
company-domain and AMAC searches did not locate an original AI青蚨 case. Similar
February 2026 features across media were not counted as independent measurements.

Next checks: original AI青蚨 release/technical presentation, the forum recording,
deployment configuration and source rights, control tests, current AUM and the
workflow timing/quality protocol. Human check: pending.
[Batch source register](research-batches/2026-09-06-huaan-pingan-sources.md).
