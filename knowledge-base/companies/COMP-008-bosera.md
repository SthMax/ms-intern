---
company_id: COMP-008
evidence_state: verified-primary
accessed: 2026-09-06
reviewed_by: Codex research subagent
human_check_status: pending
---

# Bosera / 博时基金管理有限公司

## Verified initiatives

### Privately deployed LLMs and research-text extraction

**FUND-210** is an original article with the explicit byline **博时基金管理有限公司**,
published on China Securities Journal's website on 9 March 2025. It is therefore
a first-person company disclosure carried by a publisher, rather than an
independently measured result. AMAC's later copy credits that newspaper and is
not a second independent observation.

The article reports private deployment of DeepSeek-v1/v2 on Ascend servers from
2024 and implementation of R1 in 2025, for research, investment-advisory and
software-development workflows. These model names follow the company's wording;
no checkpoint, parameter count, precision, accelerator model/count or inference
engine is disclosed. Distillation/fine-tuning for financial agents is described
as exploration.

Its research system combines machine-learning factor allocation, neural-network
factor discovery and **LLM extraction of views from research reports**. The
reported 95% extraction accuracy lacks a test set, sample size, scoring protocol
and external validation. Separately reported 10–20% annualized excess returns
concern the machine-learning allocation component and a core stock pool; they
must not be presented as LLM alpha, audited fund returns or a transferable ROI.
The company describes displaying intermediate model processes, factor/sector
distributions and involving investment professionals in monitoring/iteration.

### BSBox enterprise agent platform

**FUND-211**, an official investor-relations article dated 14 July 2026, confirms
an AI Lab established in 2023 and a self-developed BSBox enterprise intelligent
service platform introduced in April 2026. It reports broad AI use across
research, marketing, risk, operations and development, without per-workflow
adoption or reliability measurements.

**FUND-214** is further reporting of chairman Zhang Dong's 29 May speech by the
forum's own organizer. It describes sandbox isolation, full-chain auditing,
private compute/models, market tracking, information/research synthesis and
automated email delivery of investment suggestions, with minutes-level task
completion. This is a useful detailed lead, but the original speech or an
official company control specification is still needed; those controls are not
promoted into the verified implementation row solely from the reporter's text.

## Technology relationships

DeepSeek is a model origin; Ascend is a named hardware family. Neither by itself
establishes a paid co-development relationship. **FUND-212**, a 4 October 2024
China Merchants Group article explicitly sourced to Bosera, identifies
cooperation with the China Computer Federation and Alibaba Cloud to organize a
financial-industry LLM competition. That substantiates a competition/ecosystem
relationship, not use of Alibaba Cloud to host confidential production data.

## Asset size

**FUND-213**, live official company profile inspected on 6 September 2026, states
at **30 June 2026**:

| Metric | Company-reported value | Scope limitation |
|---|---|---|
| Public-fund AUM excluding money-market funds | **Over RMB 699.3 billion** (逾6,993亿元) | Whether ETF feeder funds are excluded is not stated; do not equate with rankings that exclude them. |
| Total AUM | **Over RMB 1,735.3 billion** (逾17,353亿元) | Broader than public funds; includes the management activities described in the profile. |

The Exa cached profile still displayed 31 March 2026. These values were checked
against direct live official HTML, not the stale extraction.

## Source trail and review

- **FUND-210** — [博时基金：人工智能技术锻造AI投资创新引擎](https://www.cs.com.cn/tzjj/jjdt/202503/t20250309_6478371.html). Company-authored original, 2025-03-09 12:12; opening deployment paragraph; “AI驱动” and “生态融合” sections.
- **FUND-211** — [廿八载价值深耕，博时基金奋进高质量发展新征程](https://www.bosera.com/column/infoDetail.do?classid=00020002000200020003&infoid=2974324). Official company article, 投资者关系部, 2026-07-14 13:24:21; paragraph beginning 数字金融深度融合.
- **FUND-212** — [致敬75周年丨博时基金以金融创新为翼助力经济高质量发展](https://www.cmhk.com/main/xwzx/jtjx/content/1842100685282906114_1842100685295489025.html). China Merchants Group, news source 博时基金, 2024-10-04; “砺剑新质生产力” section.
- **FUND-213** — [公司简介](https://www.bosera.com/column/index.do?classid=00020002000200010001). Undated live profile, 2026-06-30 AUM paragraph.
- **FUND-214** — [博时基金董事长张东：把握“十五五”财富管理新趋势，运用AI助力高质量发展](https://www.chnfund.com/article/AR0510706e-d2be-f4c8-f7f4-3a218e3f33d9). 中国基金报 reporter 方丽, 2026-05-31; final section and paragraphs beginning 今年4月初 and 张东介绍. Detailed controls retained as candidate claims pending original speech/company specification.

Agent inspected the cited webpage passages and bylines; official Bosera pages
required direct HTML retrieval because the search/browser extractor returned
errors. Human checks remain pending. Model performance, realized savings,
control effectiveness and integration contracts were not independently tested.
