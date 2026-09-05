# Root research batch — size-first screen, ChinaAMC and Guotai

Cut-off: 6 September 2026. Five new sources: four inspected primary sources and
one secondary ranking used only to select the research cohort. Human checks pending.
The two ranking documents differ in date and measurement method.

| Source ID | Workstream | Organization / issuer | Exact title | Source / instrument type | Published | Effective / status | Direct primary URL | Accessed | Article / section / page | Supports | Evidence state | Evidence-note link / caveat |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FUND-400 | Universe / size | CLS; reporter 吴雨其 | 公募非货规模最新座次出炉，万亿公募增至3家，中段座次重排 | Original financial-media report; secondary underlying AUM data | 2026-07-21 16:57 | 2026-06-30 quarter-end, non-money public funds, ETF feeders excluded | [Article](https://www.cls.cn/detail/2432695) | 2026-09-06 | Opening; 前二十; [ranking image](https://image.cls.cn/images/20260721/Aw37CDawlh_718x1396.png) | Transparent top-20 research screen; table transcribed and visually checked | candidate | [Universe](../large-fund-universe-2026q2.md); source inspected but underlying dataset not independently reconstructed; screening only |
| FUND-401 | Universe / size | AMAC | 基金管理机构非货币公募基金月均规模（20家）（2024年三季度） | Official association statistics | Not printed; data period 2024 Q3 | Historical quarterly-mean measure, duplicate counting removed | [Original](https://www.amac.org.cn/sjtj/datastatistics/assetmanagementdata/smzg_ywpm/202411/P020241106606145403776.pdf) | 2026-09-06 | PDF p. 1, all rows and two footnotes | Historical primary-source membership/scale anchor | verified-primary | [Universe](../large-fund-universe-2026q2.md); not current ranking or comparable endpoint for growth |
| FUND-402 | Company landscape | ChinaAMC; AMAC host | 『基金行业金融科技获奖成果宣传活动』华夏基金：飞翼固收一体化智能平台 | Original company project case | Not stated in PDF | Operating AI/quant platform; future LLM work separately described | [Original](https://www.amac.org.cn/xwfb/hydt/202602/P020260202337823336223.pdf) | 2026-09-06 | PDF pp. 2–8; methods, outcomes, outlook | Named operational fixed-income platform, parsing/algorithm workflows and qualified metrics | verified-primary | [ChinaAMC](../COMP-001-chinaamc.md); platform started 2020, not proof of LLM launch then |
| FUND-403 | Company landscape | Guotai; AMAC host | 『基金行业金融科技获奖成果宣传活动』国泰基金：基金组合管理平台建设 | Original company project case | Not stated in PDF | Company-reported operating platform | [Original](https://www.amac.org.cn/xwfb/hydt/202601/P020260202337808791393.pdf) | 2026-09-06 | PDF pp. 4–8, 10; Figure 3 p. 6 | Atlas/Ascend stack, DeepSeek-labelled RAG, BERT-BiLSTM-CRF extraction and controls | verified-primary | [Guotai](../COMP-015-guotai.md); exact DeepSeek version and isolated effect not disclosed |
| FUND-405 | Company identity | Guotai | 国泰基金管理有限公司旗下部分基金2025年年度报告提示性公告 | Official signed fund-report notice | 2026-03-30 | 294 funds' FY2025 reports announced | [Original](https://st.gtfund.com/GSGG/2026/03/30/828175006116.PDF) | 2026-09-06 | PDF p. 1 | Public-fund manager identity/activity | verified-primary | [Guotai](../COMP-015-guotai.md); fund count is not AUM |

## Integration proposals

- Add one ChinaAMC operating AI/quant platform row for Feiyi, distinct from its
  existing LLM gateway/cloud procurements. Do not present all Feiyi functions or
  its 2020 start as LLM deployment.
- Add one Guotai integrated-platform row, with both the DeepSeek RAG and
  BERT-BiLSTM-CRF components described. Do not count every component as a separate
  company or deployment.
- Keep the 2026 current-ranking evidence as secondary screening-only. Retain
  managers with unresolved AI evidence in the universe to avoid selection bias.
