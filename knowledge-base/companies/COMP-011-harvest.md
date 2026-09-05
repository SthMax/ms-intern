---
company_id: COMP-011
evidence_state: verified-primary
accessed: 2026-09-06
reviewed_by: Codex research subagent
human_check_status: pending
---

# Harvest / 嘉实基金管理有限公司

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
