---

> 新增严格LLM候选：[FUND-320知识图谱问答方案](../sources/FUND-320/original.md)，S50明确由LLM结合schema与示例生成图查询并校验重试；原PDF和投产对应待核，尚未提分。

> 2026-09-09定向补查：深交所2024年度结项公告列出FRDC022024123《大模型企业超级助手》，但尚未取得结项报告；评分仍为3。检索路径见[重点研究](focused-research-2026-09-09.md)。
company_id: COMP-012
evidence_state: verified-primary
accessed: 2026-09-06
reviewed_by: Codex research subagent
human_check_status: pending
---

# Penghua / 鹏华基金管理有限公司

<!-- source-recovery-followup -->
> 2026-09-07 后续恢复：FUND-310本次浏览器和深搜仍未取得完整35页招标PDF；只保留索引线索，不用索引规格替代已核验原文。 详见[恢复报告](../audits/2026-09-07-source-recovery/README.md)。

<!-- original-language-provenance:start -->
> [!important] 原文与研究者分析分离
> 本页保留的英文正文、分类及表格是研究者撰写的摘要、整理或分析，不是来源原文。请先阅读下方逐源链接中的原语言文本；中文来源保留中文，原本为英文的来源保留英文。本次未将英文摘要反译为所谓“中文原文”。
> 来源的一手／转载／媒体／供应商属性及证据限制仍按原登记保留；保存原文不等于核实全部研究结论。人工核验仍待完成。

## 原语言来源档案（逐源）

档案中的 `original.md` 是机械提取文本；页面排版、表格和提取缺失以下载文件为准。无法确认正文的响应不作为原文提供，详见元数据。来源标题沿用登记表，仅作定位。

| 来源 ID | 登记标题 | 原登记证据状态 | 原语言正文／下载文件／记录 |
|---|---|---|---|
| FUND-308 | 『基金行业金融科技获奖成果宣传活动』鹏华基金：基于动态思维链的资管业务智能体建设 | verified-primary | [原语言正文](../sources/FUND-308/original.md) · [下载文件](../sources/FUND-308/source.pdf) · [元数据与限制](../sources/FUND-308/metadata.json) · [登记网址](https://www.amac.org.cn/xwfb/hydt/202601/P020260202337850951100.pdf) |
| FUND-309 | 行业动态 | verified-primary | [原语言正文](../sources/FUND-309/original.md) · [下载文件](../sources/FUND-309/source.html) · [元数据与限制](../sources/FUND-309/metadata.json) · [登记网址](https://www.amac.org.cn/xwfb/hydt/index_3.html) |
| FUND-310 | AI算力服务器采购项目招标文件 | unresolved | 完整PDF仍未取得；仅有搜索索引片段 · [元数据与限制](../sources/FUND-310/metadata.json) · [登记网址](https://www.phfund.com.cn/fs/uf/ke/file/20241223/20241223182720.pdf) · [本次恢复记录](../sources/FUND-310/recovery.json) |

## 研究者摘要／分析（保留原有正文）

**以下为研究者摘要/分析，不是原文。** 原有事实表述、引用定位、证据状态和局限一并保留，供对照原文复核。
<!-- original-language-provenance:end -->

## Research conclusion

An original AMAC-hosted case documents Penghua's **基于动态思维链的资管业务智能体**,
with a private model matrix and operational research, marketing-material review
and customer-discussion monitoring applications. AMAC's index dates the linked
case **27 January 2026** (FUND-309); the PDF itself does not state publication date.

## Architecture and applications

| Item | Narrow disclosure | FUND-308 locator |
|---|---|---|
| Infrastructure | Privately deployed model matrix spanning image, speech and dialogue/reasoning; high-performance computing cluster | PDF p. 3 / printed p. 2 |
| Prompt management | Model switching, change history, debugging, evaluation and version release | PDF pp. 3–4 / printed pp. 2–3 |
| Retrieval | Document parsing/cleaning/chunking, embeddings and vector storage; knowledge graph; PSG service gateway upgraded for AI tool access | PDF pp. 4–5 / printed pp. 3–4 |
| Research assistant | A-share filings, news/sentiment and research reports are extracted, tagged and summarized for researchers and fund managers | PDF pp. 5–6 / printed pp. 4–5 |
| Marketing compliance | Review system covers 7 categories and 71 rules, including risk notices, fund facts and performance promotion | PDF p. 6 / printed p. 5 |
| Sentiment assistant | Public product-discussion feeds from Tiantian Fund, Ant and Licaitong; sentiment/intent classification and anomaly alerts for business intervention | PDF p. 7 / printed p. 6 |

The named distribution platforms are data channels, not identified model
vendors. No foundation-model version, parameter count, GPU model/count,
commercial supplier, inference-engine product or vector-database product is
disclosed. “Private deployment” does not by itself establish an air-gapped
network or prohibit every external service call.

## Outcomes and human role

For marketing review the case reports **1,266 documents**, approximately
**60,000 individual checks**, **989 useful revision suggestions** and a **91%
adoption rate** (PDF p. 6). This is suggestion adoption, **not accuracy**;
false negatives, test-set construction and the measurement window are unstated.
The source's claimed approximately 50 checks per document is rounded.

For the sentiment assistant, the business team reports monthly cost savings of
“4.5万” (PDF p. 7). Currency, calculation method and measurement period are not
explicit; do not translate this into a verified RMB ROI estimate.

The case expressly describes human–machine collaboration (PDF p. 8), and alerts
for staff intervention (PDF p. 7). Marketing modifications are suggestions.
It does not publish final sign-off authority or demonstrate autonomous legal
approval. Its “dynamic chain-of-thought” description does not establish faithful
reasoning explanations or independently validated interpretability.

## Asset size and unresolved evidence

Same-date company-origin public-fund AUM is not yet verified in this note;
use the separately sourced size-first universe with its stated metric.

A December 2024 **AI算力服务器采购项目招标文件** appears in indexed search
(FUND-310). Direct download and extraction now return website HTML rather than
the PDF. Keep it unresolved; neither GPU specifications nor completed procurement
can be asserted from the search hit. The operational AMAC case independently
establishes the private model matrix.

## Verification and source trail

Codex downloaded the original AMAC PDF, inspected all text pages and rendered
PDF pp. 6–7 for visual checks of the reported metrics and their qualifiers.
The original AMAC index directly associates the link and date. Human checking
remains pending.

- **FUND-308** — [『基金行业金融科技获奖成果宣传活动』鹏华基金：基于动态思维链的资管业务智能体建设](https://www.amac.org.cn/xwfb/hydt/202601/P020260202337850951100.pdf). Original company case hosted by AMAC; operational disclosures and self-reported metrics.
- **FUND-309** — [行业动态](https://www.amac.org.cn/xwfb/hydt/index_3.html). Original AMAC index; linked case dated 2026-01-27; pagination can change.
- **FUND-310** — [AI算力服务器采购项目招标文件](https://www.phfund.com.cn/fs/uf/ke/file/20241223/20241223182720.pdf). Intended official procurement PDF; current retrieval returns HTML; unresolved.
