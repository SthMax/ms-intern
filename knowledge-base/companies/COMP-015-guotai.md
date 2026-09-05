---
company_id: COMP-015
evidence_state: verified-primary
evidence_scope: Original AI/LLM project disclosure; current screening rank is secondary
accessed: 2026-09-06
reviewed_by: Codex
human_check_status: pending
---

# Guotai / 国泰基金管理有限公司

## Why this manager is in scope

Guotai is in the reported 2026-Q2 large-fund screen (rank 12; non-money public-fund
AUM RMB 6,238.11亿元 excluding ETF feeders, FUND-400). Keep that source-attributed
screen separate from primary AUM confirmation. AMAC's older 2024-Q3 official
table records 3,436.59亿元 of quarterly-mean non-money AUM (FUND-401); the two
period/metric definitions cannot be used for a growth calculation.

An official 30 March 2026 notice for 294 funds' annual reports establishes current
public-fund-manager activity (FUND-405). It does not supply aggregate AUM.

## Verifiable platform details

FUND-403 is an original company project case hosted by AMAC. Physical PDF page
is printed page + 1. The PDF is undated; no precise production launch is inferred.

| Area | Source disclosure | Locator |
|---|---|---|
| Hardware | Huawei Atlas800, Ascend 910B NPU, Kunpeng 920 CPU | PDF p. 4 / printed p. 3 |
| Runtime | MindSpore and CANN; serving/unified model management layer | PDF p. 4 |
| Data/application stack | Hadoop/CDH, ETL, SpringCloud/Java, Nacos, Vue/jQuery | PDF pp. 5, 7 |
| Document RAG | Table/image recognition and a vision-language conversion route; vectors and graph data feed retrieval | Figure 3, PDF p. 6 |
| Generative model | **DeepSeek模型** is labelled at the answer-generation node of Figure 3 | PDF p. 6, visually checked |
| Transaction NLP | Regex preprocessing → BERT → BiLSTM → CRF, joint entity/relation extraction, post-checks | PDF p. 6 text and Figure 4 p. 7 |
| Control design | Permission controls and review rules for business flow/output; traceability and contingency arrangements | PDF pp. 8, 10 |

The DeepSeek label is in the diagram and was absent from plain text extraction.
No specific DeepSeek version, parameter count, accelerator quantity, inference
benchmark or implementation contract is given. Hardware/framework names disclose
components; they do not establish the scope of a paid Huawei contract.

The transaction NLP pipeline is not the same mechanism as generative DeepSeek
RAG. It is particularly useful to distinguish these methods when examining
financial named-entity extraction.

## Reported outcomes and limits

The case describes production use across investment/trading, risk/compliance and
operations. It reports portfolio work moving from hours to minutes, without a
specified benchmark task, observation window or isolated LLM effect (PDF p. 8).
The wider platform's efficiency and investment claims are not causal LLM ROI.

Private hardware does not establish an air gap, and described permission rules
are not independent evidence of tested control effectiveness. No internal MSIM
policy or deployment approval is inferred.

## Source trail

- **FUND-403** — [『基金行业金融科技获奖成果宣传活动』国泰基金：基金组合管理平台建设](https://www.amac.org.cn/xwfb/hydt/202601/P020260202337808791393.pdf). Complete text read; Figure 3 and surrounding NLP pipeline on PDF p. 6 visually inspected.
- **FUND-405** — [国泰基金管理有限公司旗下部分基金2025年年度报告提示性公告](https://st.gtfund.com/GSGG/2026/03/30/828175006116.PDF). Dated 2026-03-30; PDF p. 1.
- **FUND-400/401** — [Size-screening evidence and definitions](large-fund-universe-2026q2.md).

Human review remains pending. Next: obtain the exact deployed model, task-specific
quality/latency metrics, current official comparable AUM and dated system release.
