# 原文保全：全部变更表 / Complete change table

> 后续更新：本文保留初轮审计快照。八个来源的最新浏览器／深搜结果见[来源恢复报告](../2026-09-07-source-recovery/README.md)。

Date: 2026-09-07. Requested audit performed by a **low-effort subagent**; separate medium-effort agents remediated company and regulatory notes while the parent downloaded and checked source originals.

Baseline: **56 files** (44 translated/paraphrased, 11 raw internal authored documents, 1 not verifiable); **101 sources** (91 translated/paraphrased, 10 not verifiable). No complete external original was saved at baseline. “Translated” includes summaries; four English originals were summarized in English, not translated from Chinese. “Raw internal” is not an external-source archive.

After: **93 registered publications archived in original language; 8 originals unavailable.** Readable reposts still carry upstream provenance gaps. Human verification and broad legal/status/outcome verification remain pending.

## Summary of changes

| 范围 | 数量 | 改动 |
|---|---:|---|
| 原始来源 | 93 | 下载原始PDF/HTML，保存原语言机械提取及SHA-256/时间/网址/方法 |
| 未取得原文 | 8 | 保存错误／重定向／挑战响应或失败记录，不伪装为原文 |
| 监管证据笔记 | 12 | 用73处逐字原语言摘录替换英文来源摘要；保留并标明研究者分析 |
| 公司目录下文件 | 34 | 新增逐源原文链接；英文正文明确标为研究者摘要／分析 |
| 监管索引与综合分析 | 2 | 明确研究者编写属性，链接原文档案 |
| 知识库说明、证据模板、来源登记表 | 3 | 原语言保全规则、来源文件/元数据字段，全部101来源添加存档状态与链接 |
| 原内部规划模板 | 5 | 无需替换：是内部创作，不是外文来源的替代文本 |
| ChinaAMC/E Fund动态AUM | 2来源 | 新捕获页面的日期/数值已变化；现值更新，旧观察标记无历史存档，未回溯核实 |
| 提取修复 | 7来源 | REG012压缩解码；FUND103/107/221/162提取遗漏；FUND211内嵌图像拆出；REG011跨页定位 |
| 工具与审计记录 | 见下表 | 新增来源归档工具、全量前后审计、逐文件变化清单 |

## Unavailable sources — these cannot currently be verified from their originals

| Source | 登记标题 | 本次结果 |
|---|---|---|
| [FUND-093](../../sources/FUND-093/metadata.json) | 亮相2026中国国际金融展 嘉实基金解构数字金融智能化跃迁 | Registered article redirects to generic FX168 news portal; expected Harvest article absent |
| [FUND-109](../../sources/FUND-109/metadata.json) | 🧧易方达基金 × ima首发基金研选Skill：从获取信息到分析判断，助你走通决策闭环 — title from mirror only | Challenge/error text: 环境异常 |
| [FUND-302](../../sources/FUND-302/metadata.json) | 公司介绍 | HTTP 200 anti-bot challenge (var arg1), not company-profile content |
| [FUND-310](../../sources/FUND-310/metadata.json) | AI算力服务器采购项目招标文件 | Registered PDF redirects to Penghua homepage; browser independently confirmed homepage rather than cited PDF |
| [FUND-314](../../sources/FUND-314/metadata.json) | 【专访】工银瑞信CIO王建：2026金融大模型与智能体，从野蛮生长到合规落地、价值凸显 | curl: (35) LibreSSL SSL_connect: SSL_ERROR_SYSCALL in connection to www.fintechinchina.com:443 |
| [FUND-315](../../sources/FUND-315/metadata.json) | 工银瑞信首席信息官王建：自立自强 数智融合 工银瑞信数智化发展回顾与展望 | curl: (35) LibreSSL SSL_connect: SSL_ERROR_SYSCALL in connection to fintechinchina.com:443 |
| [FUND-356](../../sources/FUND-356/metadata.json) | 中欧基金窦玉明：AI赋能时代，「三化」协同夯实长期业绩根基 | Challenge/error text: 环境异常 |
| [FUND-359](../../sources/FUND-359/metadata.json) | Linked source for 华泰柏瑞量化团队：“人机协同”迈入深水区，AI投研构筑长期护城河; destination title not retrieved | Challenge/error text: 环境异常 |

FUND-108/355/358 are readable mirrors of inaccessible upstream source chains; FUND-222 retains unresolved first-publication provenance. These limits are separate from whether their saved text is raw. FUND-091, previously a search-only lead, now has a readable archived article; its candidate evidence status was not upgraded. FUND-093's HTTP200 generic portal was rejected as the wrong article. FUND-302's HTTP200 JavaScript challenge was rejected as non-content.

## Every baseline file

| File | Before category | Action | Result / exact change |
|---|---|---|---|
| [knowledge-base/README.md](../../README.md) | raw | Modified | 新增原语言优先存档规范和审计入口 |
| [knowledge-base/companies/COMP-001-chinaamc.md](../../companies/COMP-001-chinaamc.md) | translated | Modified | 新增原语言来源表和研究者摘要／分析标识；注明动态AUM快照变化及历史核验缺口 |
| [knowledge-base/companies/COMP-002-efund.md](../../companies/COMP-002-efund.md) | translated | Modified | 新增原语言来源表和研究者摘要／分析标识；注明动态AUM快照变化及历史核验缺口 |
| [knowledge-base/companies/COMP-003-fullgoal.md](../../companies/COMP-003-fullgoal.md) | translated | Modified | 新增原语言来源表和研究者摘要／分析标识 |
| [knowledge-base/companies/COMP-004-gf-fund.md](../../companies/COMP-004-gf-fund.md) | translated | Modified | 新增原语言来源表和研究者摘要／分析标识 |
| [knowledge-base/companies/COMP-005-industrial-securities-global.md](../../companies/COMP-005-industrial-securities-global.md) | translated | Modified | 新增原语言来源表和研究者摘要／分析标识 |
| [knowledge-base/companies/COMP-006-dacheng.md](../../companies/COMP-006-dacheng.md) | translated | Modified | 新增原语言来源表和研究者摘要／分析标识 |
| [knowledge-base/companies/COMP-007-southern.md](../../companies/COMP-007-southern.md) | translated | Modified | 新增原语言来源表和研究者摘要／分析标识 |
| [knowledge-base/companies/COMP-008-bosera.md](../../companies/COMP-008-bosera.md) | translated | Modified | 新增原语言来源表和研究者摘要／分析标识 |
| [knowledge-base/companies/COMP-009-china-universal.md](../../companies/COMP-009-china-universal.md) | translated | Modified | 新增原语言来源表和研究者摘要／分析标识 |
| [knowledge-base/companies/COMP-010-tianhong.md](../../companies/COMP-010-tianhong.md) | translated | Modified | 新增原语言来源表和研究者摘要／分析标识 |
| [knowledge-base/companies/COMP-011-harvest.md](../../companies/COMP-011-harvest.md) | translated | Modified | 新增原语言来源表和研究者摘要／分析标识 |
| [knowledge-base/companies/COMP-012-penghua.md](../../companies/COMP-012-penghua.md) | translated | Modified | 新增原语言来源表和研究者摘要／分析标识 |
| [knowledge-base/companies/COMP-013-icbc-credit-suisse.md](../../companies/COMP-013-icbc-credit-suisse.md) | translated | Modified | 新增原语言来源表和研究者摘要／分析标识 |
| [knowledge-base/companies/COMP-014-invesco-great-wall.md](../../companies/COMP-014-invesco-great-wall.md) | translated | Modified | 新增原语言来源表和研究者摘要／分析标识 |
| [knowledge-base/companies/COMP-015-guotai.md](../../companies/COMP-015-guotai.md) | translated | Modified | 新增原语言来源表和研究者摘要／分析标识 |
| [knowledge-base/companies/COMP-016-huaan.md](../../companies/COMP-016-huaan.md) | translated | Modified | 新增原语言来源表和研究者摘要／分析标识 |
| [knowledge-base/companies/COMP-017-pingan.md](../../companies/COMP-017-pingan.md) | translated | Modified | 新增原语言来源表和研究者摘要／分析标识 |
| [knowledge-base/companies/COMP-018-china-merchants.md](../../companies/COMP-018-china-merchants.md) | translated | Modified | 新增原语言来源表和研究者摘要／分析标识 |
| [knowledge-base/companies/COMP-019-maxwealth.md](../../companies/COMP-019-maxwealth.md) | translated | Modified | 新增原语言来源表和研究者摘要／分析标识 |
| [knowledge-base/companies/COMP-020-china-europe.md](../../companies/COMP-020-china-europe.md) | translated | Modified | 新增原语言来源表和研究者摘要／分析标识 |
| [knowledge-base/companies/COMP-021-huatai-pinebridge.md](../../companies/COMP-021-huatai-pinebridge.md) | not verifiable | Modified | 新增原语言来源表和研究者摘要／分析标识 |
| [knowledge-base/companies/candidate-queue.md](../../companies/candidate-queue.md) | raw | Modified | 新增原语言来源表和研究者摘要／分析标识 |
| [knowledge-base/companies/efund-llm-deep-dive.md](../../companies/efund-llm-deep-dive.md) | translated | Modified | 新增原语言来源表和研究者摘要／分析标识 |
| [knowledge-base/companies/index.md](../../companies/index.md) | raw | Modified | 新增原语言来源表和研究者摘要／分析标识；注明动态AUM快照变化及历史核验缺口 |
| [knowledge-base/companies/large-fund-synthesis-2026-09-06.md](../../companies/large-fund-synthesis-2026-09-06.md) | translated | Modified | 新增原语言来源表和研究者摘要／分析标识 |
| [knowledge-base/companies/large-fund-universe-2026q2.md](../../companies/large-fund-universe-2026q2.md) | translated | Modified | 新增原语言来源表和研究者摘要／分析标识 |
| [knowledge-base/companies/research-batches/2026-09-06-efund-sources.md](../../companies/research-batches/2026-09-06-efund-sources.md) | translated | Modified | 新增原语言来源表和研究者摘要／分析标识 |
| [knowledge-base/companies/research-batches/2026-09-06-huaan-pingan-sources.md](../../companies/research-batches/2026-09-06-huaan-pingan-sources.md) | translated | Modified | 新增原语言来源表和研究者摘要／分析标识 |
| [knowledge-base/companies/research-batches/2026-09-06-invesco-great-wall-sources.md](../../companies/research-batches/2026-09-06-invesco-great-wall-sources.md) | translated | Modified | 新增原语言来源表和研究者摘要／分析标识 |
| [knowledge-base/companies/research-batches/2026-09-06-large-funds-national-sources.md](../../companies/research-batches/2026-09-06-large-funds-national-sources.md) | translated | Modified | 新增原语言来源表和研究者摘要／分析标识 |
| [knowledge-base/companies/research-batches/2026-09-06-large-funds-south-sources.md](../../companies/research-batches/2026-09-06-large-funds-south-sources.md) | translated | Modified | 新增原语言来源表和研究者摘要／分析标识 |
| [knowledge-base/companies/research-batches/2026-09-06-remaining-large-funds-sources.md](../../companies/research-batches/2026-09-06-remaining-large-funds-sources.md) | translated | Modified | 新增原语言来源表和研究者摘要／分析标识 |
| [knowledge-base/companies/research-batches/2026-09-06-root-large-funds-sources.md](../../companies/research-batches/2026-09-06-root-large-funds-sources.md) | translated | Modified | 新增原语言来源表和研究者摘要／分析标识 |
| [knowledge-base/companies/synthesis-2026-09-06.md](../../companies/synthesis-2026-09-06.md) | translated | Modified | 新增原语言来源表和研究者摘要／分析标识 |
| [knowledge-base/infrastructure/reference-architecture.md](../../infrastructure/reference-architecture.md) | raw | Unchanged | 未改动：内部原创计划／模板，无外部原文需要替换 |
| [knowledge-base/infrastructure/tco-model.md](../../infrastructure/tco-model.md) | raw | Unchanged | 未改动：内部原创计划／模板，无外部原文需要替换 |
| [knowledge-base/models/benchmark-plan.md](../../models/benchmark-plan.md) | raw | Unchanged | 未改动：内部原创计划／模板，无外部原文需要替换 |
| [knowledge-base/models/poc-plan.md](../../models/poc-plan.md) | raw | Unchanged | 未改动：内部原创计划／模板，无外部原文需要替换 |
| [knowledge-base/pilots/scorecard.md](../../pilots/scorecard.md) | raw | Unchanged | 未改动：内部原创计划／模板，无外部原文需要替换 |
| [knowledge-base/regulation/REG-001-generative-ai-interim-measures.md](../../regulation/REG-001-generative-ai-interim-measures.md) | translated | Modified | 来源摘要替换为逐字原语言摘录；新增原始文件／提取／元数据链接；分析独立标注 |
| [knowledge-base/regulation/REG-002-personal-information-protection-law.md](../../regulation/REG-002-personal-information-protection-law.md) | translated | Modified | 来源摘要替换为逐字原语言摘录；新增原始文件／提取／元数据链接；分析独立标注 |
| [knowledge-base/regulation/REG-003-csrc-information-technology-management.md](../../regulation/REG-003-csrc-information-technology-management.md) | translated | Modified | 来源摘要替换为逐字原语言摘录；新增原始文件／提取／元数据链接；分析独立标注 |
| [knowledge-base/regulation/REG-004-network-data-security-regulations.md](../../regulation/REG-004-network-data-security-regulations.md) | translated | Modified | 来源摘要替换为逐字原语言摘录；新增原始文件／提取／元数据链接；分析独立标注 |
| [knowledge-base/regulation/REG-005-csrc-network-information-security.md](../../regulation/REG-005-csrc-network-information-security.md) | translated | Modified | 来源摘要替换为逐字原语言摘录；新增原始文件／提取／元数据链接；分析独立标注 |
| [knowledge-base/regulation/REG-006-cross-border-data-provisions.md](../../regulation/REG-006-cross-border-data-provisions.md) | translated | Modified | 来源摘要替换为逐字原语言摘录；新增原始文件／提取／元数据链接；分析独立标注 |
| [knowledge-base/regulation/REG-007-fed-sr-26-2-replacement.md](../../regulation/REG-007-fed-sr-26-2-replacement.md) | translated | Modified | 来源摘要替换为逐字原语言摘录；新增原始文件／提取／元数据链接；分析独立标注 |
| [knowledge-base/regulation/REG-008-fed-mrm-guidance-scope.md](../../regulation/REG-008-fed-mrm-guidance-scope.md) | translated | Modified | 来源摘要替换为逐字原语言摘录；新增原始文件／提取／元数据链接；分析独立标注 |
| [knowledge-base/regulation/REG-009-amac-llm-standard-publication.md](../../regulation/REG-009-amac-llm-standard-publication.md) | translated | Modified | 来源摘要替换为逐字原语言摘录；新增原始文件／提取／元数据链接；分析独立标注 |
| [knowledge-base/regulation/REG-010-amac-llm-application-standard.md](../../regulation/REG-010-amac-llm-application-standard.md) | translated | Modified | 来源摘要替换为逐字原语言摘录；新增原始文件／提取／元数据链接；分析独立标注 |
| [knowledge-base/regulation/REG-011-amac-explainability-research.md](../../regulation/REG-011-amac-explainability-research.md) | translated | Modified | 来源摘要替换为逐字原语言摘录；新增原始文件／提取／元数据链接；分析独立标注 |
| [knowledge-base/regulation/REG-012-standardization-law.md](../../regulation/REG-012-standardization-law.md) | translated | Modified | 来源摘要替换为逐字原语言摘录；新增原始文件／提取／元数据链接；分析独立标注 |
| [knowledge-base/regulation/index.md](../../regulation/index.md) | raw | Modified | 新增研究者编写声明及原文目录链接 |
| [knowledge-base/regulation/synthesis-2026-09-06.md](../../regulation/synthesis-2026-09-06.md) | translated | Modified | 新增研究者编写声明及原文目录链接 |
| [knowledge-base/source-register.md](../../source-register.md) | raw | Modified | 全部101来源添加原文存档／失败记录；同步两项动态AUM和REG011页码 |
| [knowledge-base/templates/evidence-note.md](../../templates/evidence-note.md) | raw | Modified | 新增来源语言、原始文件、提取、SHA-256和获取字段；原文与摘要分栏 |

## Every registered source — before/after and all generated artifacts

The table lists all files created per source, including failed responses. Metadata distinguishes downloaded original bytes from extraction and records pending human review.

| Source | Before | After | 原语言 | 全部新增档案文件 | 限制／修正 |
|---|---|---|---|---|---|
| REG-001 | translated | raw | Chinese | [metadata.json](../../sources/REG-001/metadata.json) · [original.md](../../sources/REG-001/original.md) · [source.html](../../sources/REG-001/source.html) | 原登记来源类型和核验范围保留；人工核验待完成 |
| REG-002 | translated | raw | Chinese | [metadata.json](../../sources/REG-002/metadata.json) · [original.md](../../sources/REG-002/original.md) · [source.html](../../sources/REG-002/source.html) | 原登记来源类型和核验范围保留；人工核验待完成 |
| REG-003 | translated | raw | Chinese | [metadata.json](../../sources/REG-003/metadata.json) · [original.md](../../sources/REG-003/original.md) · [source.html](../../sources/REG-003/source.html) | 原登记来源类型和核验范围保留；人工核验待完成 |
| REG-004 | translated | raw | Chinese | [metadata.json](../../sources/REG-004/metadata.json) · [original.md](../../sources/REG-004/original.md) · [source.html](../../sources/REG-004/source.html) | 原登记来源类型和核验范围保留；人工核验待完成 |
| REG-005 | translated | raw | Chinese | [metadata.json](../../sources/REG-005/metadata.json) · [original.md](../../sources/REG-005/original.md) · [source.pdf](../../sources/REG-005/source.pdf) | 原登记来源类型和核验范围保留；人工核验待完成 |
| REG-006 | translated | raw | Chinese | [metadata.json](../../sources/REG-006/metadata.json) · [original.md](../../sources/REG-006/original.md) · [source.html](../../sources/REG-006/source.html) | 原登记来源类型和核验范围保留；人工核验待完成 |
| REG-007 | translated | raw | English | [metadata.json](../../sources/REG-007/metadata.json) · [original.md](../../sources/REG-007/original.md) · [source.html](../../sources/REG-007/source.html) | 原登记来源类型和核验范围保留；人工核验待完成 |
| REG-008 | translated | raw | English | [metadata.json](../../sources/REG-008/metadata.json) · [original.md](../../sources/REG-008/original.md) · [source.html](../../sources/REG-008/source.html) | 原登记来源类型和核验范围保留；人工核验待完成 |
| REG-009 | translated | raw | Chinese | [metadata.json](../../sources/REG-009/metadata.json) · [original.md](../../sources/REG-009/original.md) · [source.html](../../sources/REG-009/source.html) | 原登记来源类型和核验范围保留；人工核验待完成 |
| REG-010 | translated | raw | Chinese | [metadata.json](../../sources/REG-010/metadata.json) · [original.md](../../sources/REG-010/original.md) · [source.pdf](../../sources/REG-010/source.pdf) | Some pages have little/no text; inspect original PDF for images, charts, tables and scans. |
| REG-011 | translated | raw | Chinese | [metadata.json](../../sources/REG-011/metadata.json) · [original.md](../../sources/REG-011/original.md) · [source.pdf](../../sources/REG-011/source.pdf) | 原登记来源类型和核验范围保留；人工核验待完成 |
| REG-012 | translated | raw | Chinese | [metadata.json](../../sources/REG-012/metadata.json) · [original.md](../../sources/REG-012/original.md) · [source.html](../../sources/REG-012/source.html) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-001 | translated | raw | Chinese | [metadata.json](../../sources/FUND-001/metadata.json) · [original.md](../../sources/FUND-001/original.md) · [source.pdf](../../sources/FUND-001/source.pdf) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-002 | translated | raw | Chinese | [metadata.json](../../sources/FUND-002/metadata.json) · [original.md](../../sources/FUND-002/original.md) · [source.html](../../sources/FUND-002/source.html) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-003 | translated | raw | Chinese | [metadata.json](../../sources/FUND-003/metadata.json) · [original.md](../../sources/FUND-003/original.md) · [source.html](../../sources/FUND-003/source.html) | Current capture: 2025 year-end total including subsidiaries >RMB3.2tn. Prior 2025Q2 >RMB3tn observation lacks a preserved historical snapshot and is not reverified here. |
| FUND-004 | translated | raw | Chinese | [metadata.json](../../sources/FUND-004/metadata.json) · [original.md](../../sources/FUND-004/original.md) · [source.pdf](../../sources/FUND-004/source.pdf) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-005 | translated | raw | Chinese | [metadata.json](../../sources/FUND-005/metadata.json) · [original.md](../../sources/FUND-005/original.md) · [source.html](../../sources/FUND-005/source.html) | Current capture: 2026June-end EFund and subordinate institutions >RMB4.3tn. Prior 2025YE >RMB4.1tn observation lacks a preserved historical snapshot and is not reverified here. |
| FUND-006 | translated | raw | Chinese | [metadata.json](../../sources/FUND-006/metadata.json) · [original.md](../../sources/FUND-006/original.md) · [source.html](../../sources/FUND-006/source.html) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-007 | translated | raw | Chinese | [metadata.json](../../sources/FUND-007/metadata.json) · [original.md](../../sources/FUND-007/original.md) · [source.pdf](../../sources/FUND-007/source.pdf) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-008 | translated | raw | Chinese | [metadata.json](../../sources/FUND-008/metadata.json) · [original.md](../../sources/FUND-008/original.md) · [source.html](../../sources/FUND-008/source.html) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-009 | translated | raw | Chinese | [metadata.json](../../sources/FUND-009/metadata.json) · [original.md](../../sources/FUND-009/original.md) · [source.pdf](../../sources/FUND-009/source.pdf) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-010 | translated | raw | Chinese | [metadata.json](../../sources/FUND-010/metadata.json) · [original.md](../../sources/FUND-010/original.md) · [source.html](../../sources/FUND-010/source.html) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-011 | translated | raw | Chinese | [metadata.json](../../sources/FUND-011/metadata.json) · [original.md](../../sources/FUND-011/original.md) · [source.pdf](../../sources/FUND-011/source.pdf) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-012 | translated | raw | Chinese | [metadata.json](../../sources/FUND-012/metadata.json) · [original.md](../../sources/FUND-012/original.md) · [source.html](../../sources/FUND-012/source.html) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-013 | translated | raw | Chinese | [metadata.json](../../sources/FUND-013/metadata.json) · [original.md](../../sources/FUND-013/original.md) · [source.pdf](../../sources/FUND-013/source.pdf) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-014 | translated | raw | Chinese | [metadata.json](../../sources/FUND-014/metadata.json) · [original.md](../../sources/FUND-014/original.md) · [source.html](../../sources/FUND-014/source.html) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-090 | translated | raw | Chinese | [metadata.json](../../sources/FUND-090/metadata.json) · [original.md](../../sources/FUND-090/original.md) · [source.html](../../sources/FUND-090/source.html) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-091 | not verifiable | raw | Chinese | [metadata.json](../../sources/FUND-091/metadata.json) · [original.md](../../sources/FUND-091/original.md) · [source.html](../../sources/FUND-091/source.html) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-092 | translated | raw | Chinese | [metadata.json](../../sources/FUND-092/metadata.json) · [original.md](../../sources/FUND-092/original.md) · [source.pdf](../../sources/FUND-092/source.pdf) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-093 | not verifiable | not verifiable | Chinese | [metadata.json](../../sources/FUND-093/metadata.json) · [retrieval-response.html](../../sources/FUND-093/metadata.json) · [retrieval-response.md](../../sources/FUND-093/metadata.json) | Registered article redirects to generic FX168 news portal; expected Harvest article absent |
| FUND-100 | translated | raw | Chinese | [metadata.json](../../sources/FUND-100/metadata.json) · [original.md](../../sources/FUND-100/original.md) · [source.html](../../sources/FUND-100/source.html) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-101 | translated | raw | Chinese | [metadata.json](../../sources/FUND-101/metadata.json) · [original.md](../../sources/FUND-101/original.md) · [source.pdf](../../sources/FUND-101/source.pdf) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-102 | translated | raw | Chinese | [metadata.json](../../sources/FUND-102/metadata.json) · [original.md](../../sources/FUND-102/original.md) · [source.pdf](../../sources/FUND-102/source.pdf) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-103 | translated | raw | Chinese | [full-visible-text.txt](../../sources/FUND-103/full-visible-text.txt) · [metadata.json](../../sources/FUND-103/metadata.json) · [original.md](../../sources/FUND-103/original.md) · [source.html](../../sources/FUND-103/source.html) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-104 | translated | raw | Chinese | [metadata.json](../../sources/FUND-104/metadata.json) · [original.md](../../sources/FUND-104/original.md) · [source.pdf](../../sources/FUND-104/source.pdf) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-105 | translated | raw | Chinese | [metadata.json](../../sources/FUND-105/metadata.json) · [original.md](../../sources/FUND-105/original.md) · [source.html](../../sources/FUND-105/source.html) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-106 | translated | raw | English | [metadata.json](../../sources/FUND-106/metadata.json) · [original.md](../../sources/FUND-106/original.md) · [source.html](../../sources/FUND-106/source.html) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-107 | translated | raw | Chinese | [full-visible-text.txt](../../sources/FUND-107/full-visible-text.txt) · [metadata.json](../../sources/FUND-107/metadata.json) · [original.md](../../sources/FUND-107/original.md) · [source.html](../../sources/FUND-107/source.html) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-108 | not verifiable | raw | Chinese | [metadata.json](../../sources/FUND-108/metadata.json) · [original.md](../../sources/FUND-108/original.md) · [source.html](../../sources/FUND-108/source.html) | 原登记为候选／二手材料；保存该页面不升级部署证据; 所链上游微信原文未获取，转载原始链仍有缺口 |
| FUND-109 | not verifiable | not verifiable | Chinese | [metadata.json](../../sources/FUND-109/metadata.json) · [retrieval-response.html](../../sources/FUND-109/retrieval-response.html) · [retrieval-response.txt](../../sources/FUND-109/retrieval-response.txt) | Challenge/error text: 环境异常 |
| FUND-110 | translated | raw | Chinese | [metadata.json](../../sources/FUND-110/metadata.json) · [original.md](../../sources/FUND-110/original.md) · [source.html](../../sources/FUND-110/source.html) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-111 | translated | raw | Chinese | [metadata.json](../../sources/FUND-111/metadata.json) · [original.md](../../sources/FUND-111/original.md) · [source.html](../../sources/FUND-111/source.html) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-112 | translated | raw | Chinese | [metadata.json](../../sources/FUND-112/metadata.json) · [original.md](../../sources/FUND-112/original.md) · [source.html](../../sources/FUND-112/source.html) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-150 | translated | raw | Chinese | [metadata.json](../../sources/FUND-150/metadata.json) · [original.md](../../sources/FUND-150/original.md) · [source.pdf](../../sources/FUND-150/source.pdf) | Some pages have little/no text; inspect original PDF for images, charts, tables and scans. |
| FUND-151 | translated | raw | Chinese | [metadata.json](../../sources/FUND-151/metadata.json) · [original.md](../../sources/FUND-151/original.md) · [source.html](../../sources/FUND-151/source.html) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-152 | translated | raw | Chinese | [metadata.json](../../sources/FUND-152/metadata.json) · [original.md](../../sources/FUND-152/original.md) · [source.html](../../sources/FUND-152/source.html) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-160 | translated | raw | Chinese | [metadata.json](../../sources/FUND-160/metadata.json) · [original.md](../../sources/FUND-160/original.md) · [source.html](../../sources/FUND-160/source.html) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-161 | translated | raw | Chinese | [metadata.json](../../sources/FUND-161/metadata.json) · [original.md](../../sources/FUND-161/original.md) · [source.html](../../sources/FUND-161/source.html) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-162 | translated | raw | Chinese | [full-visible-text.txt](../../sources/FUND-162/metadata.json) · [metadata.json](../../sources/FUND-162/metadata.json) · [original.md](../../sources/FUND-162/original.md) · [source.html](../../sources/FUND-162/source.html) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-200 | translated | raw | Chinese | [metadata.json](../../sources/FUND-200/metadata.json) · [original.md](../../sources/FUND-200/original.md) · [source.pdf](../../sources/FUND-200/source.pdf) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-201 | translated | raw | Chinese | [metadata.json](../../sources/FUND-201/metadata.json) · [original.md](../../sources/FUND-201/original.md) · [source.html](../../sources/FUND-201/source.html) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-202 | translated | raw | Chinese | [metadata.json](../../sources/FUND-202/metadata.json) · [original.md](../../sources/FUND-202/original.md) · [source.html](../../sources/FUND-202/source.html) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-203 | translated | raw | Chinese | [metadata.json](../../sources/FUND-203/metadata.json) · [original.md](../../sources/FUND-203/original.md) · [source.html](../../sources/FUND-203/source.html) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-210 | translated | raw | Chinese | [metadata.json](../../sources/FUND-210/metadata.json) · [original.md](../../sources/FUND-210/original.md) · [source.html](../../sources/FUND-210/source.html) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-211 | translated | raw | Chinese | [embedded-image-1.jpg](../../sources/FUND-211/embedded-image-1.jpg) · [metadata.json](../../sources/FUND-211/metadata.json) · [original.md](../../sources/FUND-211/original.md) · [source.html](../../sources/FUND-211/source.html) | Embedded base64 image moved to local image asset for readability; original HTML unchanged. |
| FUND-212 | translated | raw | Chinese | [metadata.json](../../sources/FUND-212/metadata.json) · [original.md](../../sources/FUND-212/original.md) · [source.html](../../sources/FUND-212/source.html) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-213 | translated | raw | Chinese | [metadata.json](../../sources/FUND-213/metadata.json) · [original.md](../../sources/FUND-213/original.md) · [source.html](../../sources/FUND-213/source.html) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-214 | translated | raw | Chinese | [metadata.json](../../sources/FUND-214/metadata.json) · [original.md](../../sources/FUND-214/original.md) · [source.html](../../sources/FUND-214/source.html) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-220 | translated | raw | Chinese | [metadata.json](../../sources/FUND-220/metadata.json) · [original.md](../../sources/FUND-220/original.md) · [source.pdf](../../sources/FUND-220/source.pdf) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-221 | translated | raw | Chinese | [full-visible-text.txt](../../sources/FUND-221/full-visible-text.txt) · [metadata.json](../../sources/FUND-221/metadata.json) · [original.md](../../sources/FUND-221/original.md) · [source.html](../../sources/FUND-221/source.html) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-222 | not verifiable | raw | Chinese | [metadata.json](../../sources/FUND-222/metadata.json) · [original.md](../../sources/FUND-222/original.md) · [source.html](../../sources/FUND-222/source.html) | 原登记为候选／二手材料；保存该页面不升级部署证据; 属于转载；首发来源／日期仍未确认 |
| FUND-223 | translated | raw | Chinese | [metadata.json](../../sources/FUND-223/metadata.json) · [original.md](../../sources/FUND-223/original.md) · [source.html](../../sources/FUND-223/source.html) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-224 | translated | raw | Chinese | [metadata.json](../../sources/FUND-224/metadata.json) · [original.md](../../sources/FUND-224/original.md) · [source.html](../../sources/FUND-224/source.html) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-225 | translated | raw | English | [metadata.json](../../sources/FUND-225/metadata.json) · [original.md](../../sources/FUND-225/original.md) · [source.pdf](../../sources/FUND-225/source.pdf) | English source; some Chinese corporate-name glyphs are malformed in PDF extraction. Consult original PDF for these names. |
| FUND-250 | translated | raw | Chinese | [metadata.json](../../sources/FUND-250/metadata.json) · [original.md](../../sources/FUND-250/original.md) · [source.html](../../sources/FUND-250/source.html) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-251 | translated | raw | Chinese | [metadata.json](../../sources/FUND-251/metadata.json) · [original.md](../../sources/FUND-251/original.md) · [source.html](../../sources/FUND-251/source.html) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-252 | translated | raw | Chinese | [metadata.json](../../sources/FUND-252/metadata.json) · [original.md](../../sources/FUND-252/original.md) · [source.html](../../sources/FUND-252/source.html) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-253 | translated | raw | Chinese | [metadata.json](../../sources/FUND-253/metadata.json) · [original.md](../../sources/FUND-253/original.md) · [source.pdf](../../sources/FUND-253/source.pdf) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-254 | translated | raw | Chinese | [metadata.json](../../sources/FUND-254/metadata.json) · [original.md](../../sources/FUND-254/original.md) · [source.html](../../sources/FUND-254/source.html) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-255 | translated | raw | Chinese | [metadata.json](../../sources/FUND-255/metadata.json) · [original.md](../../sources/FUND-255/original.md) · [source.html](../../sources/FUND-255/source.html) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-300 | translated | raw | Chinese | [metadata.json](../../sources/FUND-300/metadata.json) · [original.md](../../sources/FUND-300/original.md) · [source.pdf](../../sources/FUND-300/source.pdf) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-301 | translated | raw | Chinese | [metadata.json](../../sources/FUND-301/metadata.json) · [original.md](../../sources/FUND-301/original.md) · [source.html](../../sources/FUND-301/source.html) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-302 | not verifiable | not verifiable | Chinese | [metadata.json](../../sources/FUND-302/metadata.json) · [retrieval-response.html](../../sources/FUND-302/retrieval-response.html) · [retrieval-response.txt](../../sources/FUND-302/retrieval-response.txt) | HTTP 200 anti-bot challenge (var arg1), not company-profile content |
| FUND-304 | translated | raw | Chinese | [metadata.json](../../sources/FUND-304/metadata.json) · [original.md](../../sources/FUND-304/original.md) · [source.pdf](../../sources/FUND-304/source.pdf) | Some pages have little/no text; inspect original PDF for images, charts, tables and scans. |
| FUND-305 | translated | raw | Chinese | [metadata.json](../../sources/FUND-305/metadata.json) · [original.md](../../sources/FUND-305/original.md) · [source.html](../../sources/FUND-305/source.html) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-306 | translated | raw | Chinese | [metadata.json](../../sources/FUND-306/metadata.json) · [original.md](../../sources/FUND-306/original.md) · [source.html](../../sources/FUND-306/source.html) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-307 | translated | raw | Chinese | [metadata.json](../../sources/FUND-307/metadata.json) · [original.md](../../sources/FUND-307/original.md) · [source.html](../../sources/FUND-307/source.html) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-308 | translated | raw | Chinese | [metadata.json](../../sources/FUND-308/metadata.json) · [original.md](../../sources/FUND-308/original.md) · [source.pdf](../../sources/FUND-308/source.pdf) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-309 | translated | raw | Chinese | [metadata.json](../../sources/FUND-309/metadata.json) · [original.md](../../sources/FUND-309/original.md) · [source.html](../../sources/FUND-309/source.html) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-310 | not verifiable | not verifiable | Chinese | [metadata.json](../../sources/FUND-310/metadata.json) · [retrieval-response.html](../../sources/FUND-310/retrieval-response.html) · [retrieval-response.txt](../../sources/FUND-310/retrieval-response.txt) | Registered PDF redirects to Penghua homepage; browser independently confirmed homepage rather than cited PDF |
| FUND-312 | translated | raw | Chinese | [metadata.json](../../sources/FUND-312/metadata.json) · [original.md](../../sources/FUND-312/original.md) · [source.pdf](../../sources/FUND-312/source.pdf) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-313 | translated | raw | Chinese | [metadata.json](../../sources/FUND-313/metadata.json) · [original.md](../../sources/FUND-313/original.md) · [source.html](../../sources/FUND-313/source.html) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-314 | translated | not verifiable | Chinese | [metadata.json](../../sources/FUND-314/metadata.json) | curl: (35) LibreSSL SSL_connect: SSL_ERROR_SYSCALL in connection to www.fintechinchina.com:443 |
| FUND-315 | not verifiable | not verifiable | Chinese | [metadata.json](../../sources/FUND-315/metadata.json) | curl: (35) LibreSSL SSL_connect: SSL_ERROR_SYSCALL in connection to fintechinchina.com:443 |
| FUND-316 | translated | raw | Chinese | [metadata.json](../../sources/FUND-316/metadata.json) · [original.md](../../sources/FUND-316/original.md) · [source.pdf](../../sources/FUND-316/source.pdf) | Some pages have little/no text; inspect original PDF for images, charts, tables and scans. |
| FUND-317 | translated | raw | Chinese | [metadata.json](../../sources/FUND-317/metadata.json) · [original.md](../../sources/FUND-317/original.md) · [source.html](../../sources/FUND-317/source.html) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-350 | translated | raw | Chinese | [metadata.json](../../sources/FUND-350/metadata.json) · [original.md](../../sources/FUND-350/original.md) · [source.html](../../sources/FUND-350/source.html) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-351 | translated | raw | Chinese | [metadata.json](../../sources/FUND-351/metadata.json) · [original.md](../../sources/FUND-351/original.md) · [source.html](../../sources/FUND-351/source.html) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-352 | translated | raw | Chinese | [metadata.json](../../sources/FUND-352/metadata.json) · [original.md](../../sources/FUND-352/original.md) · [source.pdf](../../sources/FUND-352/source.pdf) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-353 | translated | raw | Chinese | [metadata.json](../../sources/FUND-353/metadata.json) · [original.md](../../sources/FUND-353/original.md) · [source.html](../../sources/FUND-353/source.html) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-354 | translated | raw | Chinese | [metadata.json](../../sources/FUND-354/metadata.json) · [original.md](../../sources/FUND-354/original.md) · [source.html](../../sources/FUND-354/source.html) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-355 | translated | raw | Chinese | [metadata.json](../../sources/FUND-355/metadata.json) · [original.md](../../sources/FUND-355/original.md) · [source.html](../../sources/FUND-355/source.html) | 原登记为候选／二手材料；保存该页面不升级部署证据; 所链上游微信原文未获取，转载原始链仍有缺口 |
| FUND-356 | translated | not verifiable | Chinese | [metadata.json](../../sources/FUND-356/metadata.json) · [retrieval-response.html](../../sources/FUND-356/retrieval-response.html) · [retrieval-response.txt](../../sources/FUND-356/retrieval-response.txt) | Challenge/error text: 环境异常 |
| FUND-357 | translated | raw | Chinese | [metadata.json](../../sources/FUND-357/metadata.json) · [original.md](../../sources/FUND-357/original.md) · [source.html](../../sources/FUND-357/source.html) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-358 | not verifiable | raw | Chinese | [metadata.json](../../sources/FUND-358/metadata.json) · [original.md](../../sources/FUND-358/original.md) · [source.html](../../sources/FUND-358/source.html) | 原登记为候选／二手材料；保存该页面不升级部署证据; 所链上游微信原文未获取，转载原始链仍有缺口 |
| FUND-359 | not verifiable | not verifiable | Chinese | [metadata.json](../../sources/FUND-359/metadata.json) · [retrieval-response.html](../../sources/FUND-359/retrieval-response.html) · [retrieval-response.txt](../../sources/FUND-359/retrieval-response.txt) | Challenge/error text: 环境异常 |
| FUND-400 | translated | raw | Chinese | [metadata.json](../../sources/FUND-400/metadata.json) · [original.md](../../sources/FUND-400/original.md) · [source.html](../../sources/FUND-400/source.html) | 原登记为候选／二手材料；保存该页面不升级部署证据 |
| FUND-401 | translated | raw | Chinese | [metadata.json](../../sources/FUND-401/metadata.json) · [original.md](../../sources/FUND-401/original.md) · [source.pdf](../../sources/FUND-401/source.pdf) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-402 | translated | raw | Chinese | [metadata.json](../../sources/FUND-402/metadata.json) · [original.md](../../sources/FUND-402/original.md) · [source.pdf](../../sources/FUND-402/source.pdf) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-403 | translated | raw | Chinese | [metadata.json](../../sources/FUND-403/metadata.json) · [original.md](../../sources/FUND-403/original.md) · [source.pdf](../../sources/FUND-403/source.pdf) | 原登记来源类型和核验范围保留；人工核验待完成 |
| FUND-405 | translated | raw | Chinese | [metadata.json](../../sources/FUND-405/metadata.json) · [original.md](../../sources/FUND-405/original.md) · [source.pdf](../../sources/FUND-405/source.pdf) | 原登记来源类型和核验范围保留；人工核验待完成 |

## Workflow and audit artifacts

| File | Action / purpose |
|---|---|
| [archive_sources.py](../../../scripts/archive_sources.py) | Download/retain registered public sources without translation; successful archives are immutable on retries |
| [Original-source index](../../sources/README.md) | All101 sources, usable originals vs failures, provenance caveats |
| [file-audit-before.md](file-audit-before.md) | All56 baseline files, classifications and reasons |
| [source-audit-before.md](source-audit-before.md) | All101 baseline sources, classifications and verification gaps |
| [audit-before.json](audit-before.json) | Baseline hashes, original source rows and machine-readable classifications |
| [source-audit-after.json](source-audit-after.json) | All101 current source classifications and artifact paths |
| [company-remediation.md](company-remediation.md) | All34 changed company files; exact AUM corrections |
| [regulatory-remediation.md](regulatory-remediation.md) | All12 changed regulatory notes; excerpt ranges and extraction limits |
| [file-changes.md](file-changes.md) | Exhaustive modified/new-file inventory |
| [validation.json](validation.json) | Final completeness, hash, local-link and verbatim-excerpt checks |
| [changes.md](changes.md) | This consolidated full change table |

Original project-level README.md and RESEARCH_TOOLS.md changes predated this task and were not edited. No remote publication or commit was performed by this audit.
