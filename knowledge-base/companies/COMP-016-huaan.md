---
company_id: COMP-016
evidence_state: verified-primary
research_cutoff: 2026-09-06
accessed: 2026-09-06
reviewed_by: Codex
human_check_status: pending
---

# Hua An / 华安基金管理有限公司

<!-- original-language-provenance:start -->
> [!important] 原文与研究者分析分离
> 本页保留的英文正文、分类及表格是研究者撰写的摘要、整理或分析，不是来源原文。请先阅读下方逐源链接中的原语言文本；中文来源保留中文，原本为英文的来源保留英文。本次未将英文摘要反译为所谓“中文原文”。
> 来源的一手／转载／媒体／供应商属性及证据限制仍按原登记保留；保存原文不等于核实全部研究结论。人工核验仍待完成。

## 原语言来源档案（逐源）

档案中的 `original.md` 是机械提取文本；页面排版、表格和提取缺失以下载文件为准。无法确认正文的响应不作为原文提供，详见元数据。来源标题沿用登记表，仅作定位。

| 来源 ID | 登记标题 | 原登记证据状态 | 原语言正文／下载文件／记录 |
|---|---|---|---|
| FUND-150 | 2025 CCF企业数字化发展推荐案例集 — 华安基金管理有限公司——华安“灵思”AI智能创新平台 | verified-primary | [原语言正文](../sources/FUND-150/original.md) · [下载文件](../sources/FUND-150/source.pdf) · [元数据与限制](../sources/FUND-150/metadata.json) · [登记网址](https://edc-book.ccf.org.cn/%E3%80%8A2025CCF%E4%BC%81%E4%B8%9A%E6%95%B0%E5%AD%97%E5%8C%96%E5%8F%91%E5%B1%95%E6%8E%A8%E8%8D%90%E6%A1%88%E4%BE%8B%E9%9B%86%E3%80%8B.pdf) |
| FUND-151 | 2025 CCF企业数字化发展优秀案例评选结果公示 | verified-primary | [原语言正文](../sources/FUND-151/original.md) · [下载文件](../sources/FUND-151/source.html) · [元数据与限制](../sources/FUND-151/metadata.json) · [登记网址](https://www.ccf.org.cn/Focus/2025-10-11/849374.shtml) |
| FUND-152 | 华安基金完成DeepSeek私有化部署 | candidate | [原语言正文](../sources/FUND-152/original.md) · [下载文件](../sources/FUND-152/source.html) · [元数据与限制](../sources/FUND-152/metadata.json) · [登记网址](https://www.cs.com.cn/tzjj/jjdt/202502/t20250214_6474446.html) |

## 研究者摘要／分析（保留原有正文）

**以下为研究者摘要/分析，不是原文。** 原有事实表述、引用定位、证据状态和局限一并保留，供对照原文复核。
<!-- original-language-provenance:end -->

Hua An's 灵思 AI platform is documented in an original six-page company case
published by the China Computer Federation (CCF). It supplies concrete model,
workflow and architecture details beyond the earlier DeepSeek news report.

## Primary case: 灵思 AI智能创新平台

**FUND-150** — [2025 CCF企业数字化发展推荐案例集](https://edc-book.ccf.org.cn/%E3%80%8A2025CCF%E4%BC%81%E4%B8%9A%E6%95%B0%E5%AD%97%E5%8C%96%E5%8F%91%E5%B1%95%E6%8E%A8%E8%8D%90%E6%A1%88%E4%BE%8B%E9%9B%86%E3%80%8B.pdf),
PDF pp. 23–28 / printed pp. 18–23. Case submitter: 华安基金管理有限公司.
Publication day is unstated; 2025 is the edition year.

| Evidence | Exact locator |
|---|---|
| Local Qwen/DeepSeek-R1 alongside Wenxin/DeepSeek APIs; SFT and prompt optimization for 华安GPT | Printed p. 20, 技术前沿性 / 完全自研化 |
| Four layers: compute, models, AI platform, applications; resource/service monitoring and Agent management | Printed p. 20, Figure 4-1 |
| Bond/convertible reports, FOF diligence from speech transcripts, counter-document entry, disclosure prechecks and risk-indicator extraction | Printed p. 21, Figure 4-2 and preceding paragraph |
| Diagram names Faiss, Milvus, Neo4j, Whisper/FunASR and OCR components | Printed p. 22, Figure 4-3; components, not proven supplier contracts |
| Company-reported daily-active share >50%, >80% of counter faxes using intelligent entry, and two days' report work completed in five minutes | Printed p. 23, 降本增效; measurement protocol absent |

The case also reports public-fund AUM above **RMB 6,900亿元** at **2024-12-31**
(printed p. 18). This is a historical public-fund lower bound, not a current
rank or a bounded size interval.

The original CCF [selection notice](https://www.ccf.org.cn/Focus/2025-10-11/849374.shtml)
(FUND-151; 2025-10-11) lists Hua An in **入围案例, row 6**, separately from
全国优秀案例. Do not relabel this as a national-winner award. The notice establishes
case identity and the public review stage, not regulatory approval.

## Interpretation and limits

Stage: internal operational use reported in the case, with further development
planned. The local/API routes coexist; the document does not identify which
data classes or tasks use each route. It does not establish that all data stays
on-premise. Checkpoint sizes, quantization, GPUs, inference engine, procurement
contracts and per-request costs are not disclosed.

The report-generation claim has no workload definition, sample size or independent
quality audit. Preserve the stated comparison; do not calculate a universal
speedup or infer staff/cost savings. The separate “2026年前” process targets on
printed p. 19 are not achieved results. Platform monitoring and prechecks do not
establish that model outputs can authorize compliance decisions.

## Secondary provenance retained

The [company-hosted DeepSeek article](https://www.huaan.com.cn/news/2025-02-17/225869_1.shtml)
explicitly says **来源: 中国证券报** and opens with a reporter attribution. Its
[newspaper original](https://www.cs.com.cn/tzjj/jjdt/202502/t20250214_6474446.html)
(FUND-152; 2025-02-14 13:11) attributes late-2023 platform initiation,
DeepSeek integration and >90% QA accuracy to Hua An. Keep the exact chronology
and accuracy figure supplementary: CCF independently supplies primary deployment
detail, but not a validation dataset for that percentage.

## Verification record

Codex read all six case pages and inspected full-page renders, including figures,
on 2026-09-06. The CCF cover and HTML notice date/category were checked. The
original media report and Hua An mirror were opened and their provenance compared.
Human review is pending. [Batch source register](research-batches/2026-09-06-huaan-pingan-sources.md).

Next checks: verify current comparable AUM, source-specific routing/data controls,
model configurations, and the time/accuracy measurement protocol. Company size
screening is documented separately in [the large-manager universe](large-fund-universe-2026q2.md).
