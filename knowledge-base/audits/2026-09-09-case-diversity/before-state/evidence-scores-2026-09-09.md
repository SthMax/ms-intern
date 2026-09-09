# 基金公司工作流资料评分 — 2026-09-09

> 同日量化研究新增论文与代码，详见[专项报告](quant-research-2026-09-09.md)；因数据、版本和输出链仍需复核，本轮未调整21家公司分数。

研究者判断，依据当前已入库资料；不更改原始来源证据等级。评分衡量材料对复制同类工作流的帮助，不评价公司真实AI能力或投资业绩。

## 评分口径

按用户原始标准：5分须完整可复制工作流、详细技术、代码、成果与展望；4分为完整可复制工作流和详细技术但没有代码；3分为流程仍不完整但有部分技术与场景；2分为只有场景/使用情况、无实现细节；1分为泛泛介绍。

每家公司取目前最好的一条有明确边界的工作流，不把多个独立项目的组件拼成4/5分。4分为**文档级可重建同类原型**，不代表已实测、能复制原公司生产系统或复现其收益/效率；必须有明确输入、处理步骤、输出及关键校验，不能只凭架构图、模型品牌或组件数量给4分。2分材料中可以出现“多模态/大模型”等能力名称，这不等于已经披露实现细节。

2026-09-09重点检索后，已取得易方达署名论文、提示词及公开代码；原先“当前档案没有公司代码”的判断已更新。[重点研究与5分缺口](focused-research-2026-09-09.md)；[更新前评分快照](../audits/2026-09-09-focused-company-research/before-state/evidence-scores-2026-09-09.md)。

**分布：4分2家（易方达、南方）、3分17家、2分2家（广发、永赢）、1分和5分各0家。** 样本本就筛选了有具体AI披露的公司，分布不能外推全行业。

## 逐家公司

| 公司 | 分数 | 最有参考价值的工作流及技术 | 得分理由／缺什么 | 依据 |
|---|---:|---|---|---|
| [易方达](COMP-002-efund.md) | **4（原3）** | MENTOR按周滚动的事件提取、预测、行业排序、教师反馈及文本策略更新；论文算法、完整Prompt和评价指标齐备 | 可重建同类研究原型；无MENTOR代码，完整授权数据未公开。另有官方查询客户端、SLAG和比赛代码，各自存在范围或复现缺口，暂不认定严格5分。 | [FUND-113](../sources/FUND-113/original.md) · [FUND-114](../sources/FUND-114/original.md) · [代码及边界](focused-research-2026-09-09.md) |
| [华夏](COMP-001-chinaamc.md) | **3** | 飞翼固收投研、组合优化、交易要素识别与执行接口；另有LLM采购；因子/优化/解析流程、QTrade/iDeal/X-BOND接口；LLM安全网关供应商公告 | 主要是广义AI/量化平台；LLM应用部分仍有展望，采购记录不能补足LLM运行工作流。 | [FUND-402](../sources/FUND-402/original.md) · [FUND-001](../sources/FUND-001/original.md) · [FUND-002](../sources/FUND-002/original.md) |
| [广发](COMP-004-gf-fund.md) | **2** | 智能理财助理：基金/账户查询、持仓诊断、产品问答；协议提到DeepSeek、Qwen和检索增强，但未展开实现 | 有明确服务范围与使用限制；只有模型名称和功能概念，没有数据处理、检索编排或技术接口说明。 | [FUND-009](../sources/FUND-009/original.md) |
| [富国](COMP-003-fullgoal.md) | **3** | 本地模型处理研报、市场观点生成和RAG知识问答；Ray、ClickHouse、SpringCloud；本地LLM、Prompt摘要、向量检索与来源引用 | 可借鉴局部技术链，但模型、切分/召回/排序配置、Prompt样例和完整输入输出规格不齐。 | [FUND-007](../sources/FUND-007/original.md) |
| [南方](COMP-007-southern.md) | **4** | 小喃同学：受控NL2SQL查询与结果解释；表描述/字段注释→选表Agent→SQL生成→权限字段过滤→语法/执行计划检查及分页→查询→解释；另有API/RAG/Python沙箱与分级权限 | 4分仅针对该查询子流程的文档级可复制性；可以用样表和可替换LLM重建原型。生产模型、真实业务接口和效果复现实验仍缺，不能把整个交易系统视为已复现。 | [FUND-200](../sources/FUND-200/original.md) |
| [汇添富](COMP-009-china-universal.md) | **3** | 智汇风险平台：托管邮件抽取、条款问答与规则溯源；现金宝AI服务；DeepSeek-R1/QianWen、FastAPI、Flink/Doris、规则审批和回归测试 | 系统架构较详，但具体邮件字段/模板、Prompt、规则映射及LLM评价流程不完整；平台耗时指标不能替代LLM效果。 | [FUND-220](../sources/FUND-220/original.md) · [FUND-221](../sources/FUND-221/original.md) · [FUND-222](../sources/FUND-222/original.md) · [FUND-225](../sources/FUND-225/original.md) |
| [景顺长城](COMP-014-invesco-great-wall.md) | **3** | 研报/纪要处理、代码辅助、知识库与量化研究；媒体提到本地DeepSeek、OCR/Embedding/Rerank/语音及Skills/MCP | 技术栈和场景有线索，但缺公司技术原件、单条任务的处理顺序、参数/输入输出与验证材料。 | [FUND-090](../sources/FUND-090/original.md) · [FUND-250](../sources/FUND-250/original.md) · [FUND-251](../sources/FUND-251/original.md) · [FUND-254](../sources/FUND-254/original.md) |
| [嘉实](COMP-011-harvest.md) | **3** | ESG文本抽取、评分更新与负面新闻监测；超级嘉贝AI信息工具；数据源、清洗/质检、规则评分、股票月更/债券季更；AI/ML/NLP | 有数据工作流和治理细节，缺模型/抽取规则和实现配置；不能由这些材料确认基础LLM部署。 | [FUND-304](../sources/FUND-304/original.md) · [FUND-307](../sources/FUND-307/original.md) · [FUND-317](../sources/FUND-317/original.md) |
| [博时](COMP-008-bosera.md) | **3** | DeepSeek投研观点抽取、研发辅助，BSBox企业智能体；Ascend与私有DeepSeek部署；LLM观点抽取；沙箱和审计的进一步报道 | 场景/模型/硬件线索明确；缺具体Agent编排、Prompt/检索、接口契约及独立评价；BSBox控制细节还需公司原件。 | [FUND-210](../sources/FUND-210/original.md) · [FUND-211](../sources/FUND-211/original.md) · [FUND-214](../sources/FUND-214/original.md) |
| [鹏华](COMP-012-penghua.md) | **3** | 投研资讯抽取与标签、营销物料审核、舆情识别预警；Prompt版本/评测中台、RAG切分/嵌入/检索、知识图谱、PSG网关；7类71规则 | 接近4分，但71条规则、审核Prompt、模型/召回配置和最终复核流程未完整公开，不能靠规则数量复现审核。 | [FUND-308](../sources/FUND-308/original.md) |
| [招商](COMP-018-china-merchants.md) | **3** | AI门户、投研摘要/会议纪要、客服与法规知识问答；DeepSeek-R1/QWQ-32B、本地模型编排；小招X与知识库；AI/OCR/RPA分工 | 有模型、集成与流程构建线索；未给出单一工作流从数据到产出的完整细节，且现为媒体转载材料。 | [FUND-351](../sources/FUND-351/original.md) · [FUND-350](../sources/FUND-350/original.md) |
| [国泰](COMP-015-guotai.md) | **3** | 组合平台中的文档RAG及交易要素NER；Atlas800/910B、MindSpore/CANN；DeepSeek RAG；正则→BERT→BiLSTM→CRF→校验 | 技术栈和算法路线较详；缺实体/关系标注规范、训练/推理配置、检索配置和输入输出样例，暂不足4分。 | [FUND-403](../sources/FUND-403/original.md) |
| [永赢](COMP-019-maxwealth.md) | **2** | 安全GPT邮件钓鱼识别与分级处置；提到意图理解、多模态检测和工具调度，未展开实现 | 有具体使用场景及公司报告效果，但技术仍为能力描述；缺模型、附件/链接处理流程、判定阈值与处置规则。 | [FUND-352](../sources/FUND-352/original.md) |
| [工银瑞信](COMP-013-icbc-credit-suisse.md) | **3** | FundGPT文档对比、标书生成、会议转写及投研推荐；私有语言/多模态/语音/Embedding模型群；微调/聚类/Embedding；数据平台及合作方 | 有模块与分工，缺单条业务的完整接口、输入输出、Prompt和验收规则；平台多年节约不能归到LLM。 | [FUND-312](../sources/FUND-312/original.md) · [FUND-316](../sources/FUND-316/original.md) · [FUND-314](../sources/FUND-314/extractor-recovered.md) · [FUND-315](../sources/FUND-315/extractor-recovered.md) |
| [天弘](COMP-010-tianhong.md) | **3** | FinAgent盈利驱动分解、观点汇总、资讯/事件解释；Think、THAI GPU池化、弘思RAG、智搜、MCP工具及输入/输出护栏 | 服务框架和用途清楚，但自研组件内部实现、Agent动作规格、数据/计算样例和评测协议不足。 | [FUND-300](../sources/FUND-300/original.md) |
| [中欧](COMP-020-china-europe.md) | **3** | 投研要素表智能助手、信息检索与报告撰写；金融场景微调、分布式采集/API、多Agent采集→分析→汇总；100多个Skill | 有局部技术和工作步骤，缺要素表schema、Skill清单、微调/Prompt、质量校验及完整流程；约60%/50%仍是公司归属数据。 | [FUND-354](../sources/FUND-354/original.md) · [FUND-356](../sources/FUND-356/original.md) |
| [华安](COMP-016-huaan.md) | **3** | 灵思：债券报告、FOF尽调、传真录入和披露预检；本地Qwen/DeepSeek-R1加API、SFT；Faiss/Milvus/Neo4j、Whisper/FunASR/OCR | 组件多且架构详细，缺单条任务从数据到报告的输入输出模板、Prompt、路由及校验配置，暂不足完整复现。 | [FUND-150](../sources/FUND-150/original.md) |
| [华泰柏瑞](COMP-021-huatai-pinebridge.md) | **3** | 数据→研究→模型→组合→复盘；文本信号加工与风控辅助；五层架构、文本检索/摘要/实体识别、规则硬约束加人工风险决策 | 有处理环节及部分技术，但无模型/接口/配置和样例；自主研究智能体是未来图景，不能拿来补齐现有流程。 | [FUND-359](../sources/FUND-359/original.md) |
| [兴证全球](COMP-005-industrial-securities-global.md) | **3** | 千询/兴宝：询价、对手匹配、聊天转交易要素和指令；QTrade、LRU、Oracle Data Guard、Kafka；保留交易员/经理操作环节 | 业务链条较完整，但模型、要素schema、Prompt与接口协议未展开；还不能仅按材料重建。 | [FUND-011](../sources/FUND-011/original.md) |
| [平安](COMP-017-pingan.md) | **3** | AI青蚨：文档/纪要→知识库→检索→有引用的观点摘要→研究员复核；分段/去噪/实体、向量+关键词、query扩展、rerank、低温度及输入输出过滤 | 流程描述较完整，但缺模型/Embedding/切分/融合配置、规则及实际样例，尚不能按文重建；实施证据以媒体报道为主。 | [FUND-160](../sources/FUND-160/original.md) · [FUND-161](../sources/FUND-161/original.md) |
| [大成](COMP-006-dacheng.md) | **3** | 固收平台：交易语义要素识别、指令与清算衔接；千问2.5、NLP、Flink/SpringCloud/Vue、O32集成 | 系统应用和部分组件明确，但LLM子流程、字段规范、模型参数/Prompt及独立效果缺失。 | [FUND-013](../sources/FUND-013/original.md) |

## 为什么南方可给4分，而多数仍是3分

FUND-200第4–7页给出了一个可独立重建的受控NL2SQL子流程：读取表/字段元数据，按语义选表，用SQL模板生成查询，对无权限字段过滤，语法/执行计划校验与分页限制，执行查询，再分析和解释结果；终端、角色、网络、二次确认/令牌、脱敏等控制也有位置。样例提到持仓表及trade_date。可先用脱敏样表和可替换的LLM重建这种查询原型。

4分不授予“整套小喃交易执行系统”，更不表示40%节时已经复验；真实接口、生产模型、权限政策与系统效果仍需验证。若把“可复制”定义成按现成参数直接复现原公司系统和数字，则南方也应降为3分，本报告没有采用这一更强含义。

鹏华的71条审核规则没有完整规则文本；国泰的NER没有标注体系/训练配置；华安缺具体报告生成的输入输出/Prompt/路由；富国缺RAG的关键配置和样例。它们有可借鉴技术设计，不能据此宣称已交付完整复现材料。

## 资料深度与证据可靠性分开

景顺长城、招商、中欧、华泰柏瑞、平安的技术/工作流描述可以得到3分，但公司实施一手证据仍有缺口。华泰微信原刊已恢复，只改变可读性和出处链；它仍是记者叙述。官方公告/协议也不会因来源可靠就自动得到4分。

华夏的飞翼和嘉实ESG案例包含传统量化/AI/NLP，不等同于已验证基础LLM；国泰的BERT-BiLSTM-CRF交易抽取与DeepSeek RAG是不同链条。易方达ima安装/API Key步骤是用户使用流程，不等同于内部EFundGPT工程实现。

建议优先把南方NL2SQL、鹏华材料审核、国泰交易要素抽取、华安报告/质检、富国研报RAG各整理成一张“输入→处理→输出→人工校验”表。缺失处标注待核，不自行补成公司已经披露的技术方案。

[机器可读评分、逐源定位和文本哈希](evidence-scores-2026-09-09.json)。这些分数是本轮研究者判断，可随新增技术文档或复现结果调整。
