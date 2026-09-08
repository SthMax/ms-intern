---
company_id: COMP-011
evidence_state: verified-primary
accessed: 2026-09-06
reviewed_by: Codex research subagent
human_check_status: pending
---

# Harvest / 嘉实基金管理有限公司

<!-- source-recovery-followup -->
> 2026-09-07 后续恢复：FUND-093原FX168链接仍失效；FUND-317嘉实官网同题文章已获取，可作为该事件的直接公司来源。 详见[恢复报告](../audits/2026-09-07-source-recovery/README.md)。

<!-- original-language-provenance:start -->
> [!important] 原文与研究者分析分离
> 本页保留的英文正文、分类及表格是研究者撰写的摘要、整理或分析，不是来源原文。请先阅读下方逐源链接中的原语言文本；中文来源保留中文，原本为英文的来源保留英文。本次未将英文摘要反译为所谓“中文原文”。
> 来源的一手／转载／媒体／供应商属性及证据限制仍按原登记保留；保存原文不等于核实全部研究结论。人工核验仍待完成。

## 原语言来源档案（逐源）

档案中的 `original.md` 是机械提取文本；页面排版、表格和提取缺失以下载文件为准。无法确认正文的响应不作为原文提供，详见元数据。来源标题沿用登记表，仅作定位。

| 来源 ID | 登记标题 | 原登记证据状态 | 原语言正文／下载文件／记录 |
|---|---|---|---|
| FUND-304 | 嘉实基金2025可持续投资报告 | verified-primary | [原语言正文](../sources/FUND-304/original.md) · [下载文件](../sources/FUND-304/source.pdf) · [元数据与限制](../sources/FUND-304/metadata.json) · [登记网址](https://www.jsfund.cn/ueditor/jsp/upload/file/20260331/1774939300245008932.pdf) |
| FUND-305 | 认识嘉实 | verified-primary | [原语言正文](../sources/FUND-305/original.md) · [下载文件](../sources/FUND-305/source.html) · [元数据与限制](../sources/FUND-305/metadata.json) · [登记网址](https://www.jsfund.cn/main/AboutHarvest/KnowJiashi/index.shtml) |
| FUND-306 | 加入我们—嘉实招聘 | verified-primary | [原语言正文](../sources/FUND-306/original.md) · [下载文件](../sources/FUND-306/source.html) · [元数据与限制](../sources/FUND-306/metadata.json) · [登记网址](https://www.jsfund.cn/main/AboutHarvest/JoinUs/index.shtml) |
| FUND-307 | 从春山可望到E路生花，嘉实基金第二届超级指数节成功举办 | verified-primary | [原语言正文](../sources/FUND-307/original.md) · [下载文件](../sources/FUND-307/source.html) · [元数据与限制](../sources/FUND-307/metadata.json) · [登记网址](https://www.jsfund.cn/main/a/20260316/484107.shtml) |
| FUND-317 | 亮相2026中国国际金融展，嘉实基金解构数字金融智能化跃迁 | verified-primary | [原语言正文](../sources/FUND-317/original.md) · [下载文件](../sources/FUND-317/source.html) · [元数据与限制](../sources/FUND-317/metadata.json) · [登记网址](https://www.jsfund.cn/main/a/20260617/484163.shtml) |

## 研究者摘要／分析（保留原有正文）

**以下为研究者摘要/分析，不是原文。** 原有事实表述、引用定位、证据状态和局限一并保留，供对照原文复核。
<!-- original-language-provenance:end -->

## Research conclusion

Harvest's official **2025 sustainable-investment report** verifies an operational
AI/ML/NLP ESG research and risk-monitoring system. This is a concrete internal
AI application. The report does **not** establish a foundation LLM or its
on-premise deployment, so Harvest must be counted separately from verified LLM
deployments. The company also discloses an AI-assisted ETF information tool,
**超级嘉贝**, giving a second verified application in investor services.

## Application, data and controls

| Item | Narrow company disclosure | FUND-304 locator |
|---|---|---|
| Users / ownership | ESG Research and Solutions team works with the Data Lab and investment/technology colleagues | PDF pp. 27, 30 / printed pp. 17, 20 |
| Data processing | AI, machine learning and NLP support ESG information extraction; sources include public authorities, financial media, NGOs and associations | PDF p. 30 / printed p. 20 |
| Research / risk use | ESG screening, issuer research, portfolio analysis and adverse-news alerts integrated into internal investment workflows | PDF pp. 28–30 / printed pp. 18–20 |
| Update process | Equity ESG data undergo cleaning, quality checks, processing and score checks before monthly updates; bond scores update quarterly | PDF p. 30 / printed p. 20 |
| Scoring | Quantified inputs are scored using established rules | PDF p. 30 / printed p. 20 |
| Coverage at 2025-12-31 | 5,453 A-share companies; 2,600 Hong Kong companies; 5,376 bond issuers | PDF p. 30 / printed p. 20 |

Coverage is an observable reported output of the wider ESG system. It is not
LLM accuracy, person-hours saved, or proof that AI alone caused the coverage.
Rules-based scoring and explicit quality checks are useful governance details;
they do not independently validate the extraction models.

No named external implementation partner, model family/version, parameter size,
serving framework, vector database, hosting location or GPU configuration is
established by the report. Data Lab is an internal collaboration, not an external
vendor. Wind distribution of ESG scores does not make Wind the model supplier.

## Asset size

The official profile reports **RMB 18,034+亿元** in total assets managed at
2025 year-end (RMB 1.8034+ trillion; FUND-305, headline and 2025-12 timeline).
This is **total management scope**, not public-fund-only AUM. The same page
attributes a fifth-place 2025 non-money public-fund ranking to Galaxy Securities;
the underlying Galaxy table was not verified here.

The profile extraction contains a separate obsolete 2021 section with
RMB 14,000+亿元. Use the explicitly dated 2025 section; never merge the two.
The 2025 report independently states total AUM above RMB 1.8 trillion.

## Investor services and AI governance

The official 16 March 2026 event report identifies AI-supported information
processing in the **找机会** module of 超级嘉贝 (FUND-307, paragraph beginning
“超级工具上”). The mini-program was launched in March 2025; the source describes
subsequent AI enhancement. This supports an investor-service AI application;
model family, hosting, active-user figures and quantified benefit are absent.

The official 17 June 2026 account of CIO Liu Wei's speech says Harvest has
established a unified internal AI capability platform (FUND-317, 观点二).
The CIO describes human confirmation of investment/risk decisions, system
records and responsibility boundaries. These are published governance positions,
not an independently verified inventory of implemented controls. The same speech's
future architecture recommendations must not be described as already deployed.

## LLM-specific leads still open

An official recruitment page advertises financial-model training/fine-tuning,
distributed training, quantized deployment and agent-development work. This is
evidence of recruitment requirements, not a deployed model; the original HTML
was inspected (FUND-306, 人工智能分析师). Media reports of 2026 investment
workflow AI provide leads, but do not supply a verified model/hosting disclosure.
The company's ETF marketing about AI-sector investments is excluded from
internal adoption evidence.

## Verification and source trail

Codex downloaded the original official PDF, extracted relevant pages and
visually checked PDF p. 30, including counts and update cadence. The company
profile was opened through Exa extraction; official articles and recruitment HTML
were opened directly. Human checking remains pending.
Report publication date is not inferred from the URL's upload date.

- **FUND-304** — [嘉实基金2025可持续投资报告](https://www.jsfund.cn/ueditor/jsp/upload/file/20260331/1774939300245008932.pdf). Official company report; reporting period 2025; publication date not independently established.
- **FUND-305** — [认识嘉实](https://www.jsfund.cn/main/AboutHarvest/KnowJiashi/index.shtml). Official live profile; 2025-12-31 AUM, with older duplicate content separately visible in extraction.
- **FUND-306** — [加入我们—嘉实招聘](https://www.jsfund.cn/main/AboutHarvest/JoinUs/index.shtml). Official recruitment page; undated; AI analyst role verified in original HTML; do not count as deployment.
- **FUND-307** — [从春山可望到E路生花，嘉实基金第二届超级指数节成功举办](https://www.jsfund.cn/main/a/20260316/484107.shtml). Company-authored article, 2026-03-16; 超级工具上 paragraph.
- **FUND-317** — [亮相2026中国国际金融展，嘉实基金解构数字金融智能化跃迁](https://www.jsfund.cn/main/a/20260617/484163.shtml). Company-authored article, 2026-06-17; 观点二 and 观点三 distinguish existing platform, governance position and future design.
