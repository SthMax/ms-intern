# 2026年、三方向、部署解耦的定向研究

用户最终确认①LLM因子生成/筛选/迭代，②文本→量化信号，③研究Agent调用数据/代码/回测。基金案例优先，2026材料优先；API方案可用，本地加分。结果见[当前矩阵](../../companies/quant-research-2026-09-09.md)。

## 新增资料

- FUND-215：博时BSBox，2026-04-30，新浪基金刊载。原HTML与正文入库；保留风险提示和编辑信息，去掉末尾MACD推广与APP广告。仍为媒体/公司归属陈述，未认定完整量化回测闭环。
- FUND-323：Man Group/Man AHL AlphaTrend，2026-02-11，公司原文及流程图。本文档下载入口返回HTML落地页，已按`download-response.html`保留，未冒充PDF。改为保存可直接读取的完整文章HTML和原始Figure 1，图已视觉核对；没有通过修改身份/地区来获取额外权限。
- FUND-324：Two Sigma，2026-07-09，Ben Wellington署名文章。保留正文，去掉页面反应按钮与Spotify嵌入；未抓取音频，文章只是研究观点，不是4分实现。
- 外部参考：QuantaAlpha当前23页PDF（日期2026-05-19）及固定commit的30份代码/Prompt/配置；CogAlpha35页ACL 2026正式论文（早期预印本2025）。不计为国内基金部署项目。资料在[reference/2026-llm-quant](../../reference/2026-llm-quant/README.md)。

## 日期与范围审查

富国FUND-007的具体PDF链接在AMAC列表中对应2026-01-19，中信建投FUND-321对应2026-01-20；保存[匹配列表](amac-fullgoal-date/matched-listing.json)和HTML，未把文件路径日期当作发表日期。

FUND-251仍是2026-08-20中国基金报记者调研，不因多家公司发声就变成多份独立公司原件。华泰柏瑞未来自主Agent图景与当前文本处理分开；招商传统神经网络量化平台、未指明LLM的量化“哨兵”、匿名基金经理的AI使用均不补技术分。

BlackRock Macro Decoder内容相关，但未确认2026发表日，页脚2026与“as of Dec 2025”不能当发表日期，未纳入新增2026主案例。DeepFund/RD-Agent的2025论文不因2026仓库活动变成新论文。ChatGLM2/旧FinGPT/AlphaFin方案已从当前推荐撤回，旧笔记保存在`before-state/`。

## 实现与归因审查

QuantaAlpha明确以LLM生成、修复和验证因子，传统LightGBM/回测是下游评价，因此在用户范围内；读取了模型端配置、表达式/代码一致性、实验/回测配置和轨迹演化。论文结果是因子池结果，不是单因子收益。本轮未验证完整市场数据许可或运行环境；README的MIT徽章没有被当成独立许可文件。

Man Group公开了研究流程、一个Prompt、三类对照实验和模型比较，但缺完整节点Prompt/代码/工具契约，因此标“接近4”，不拔高。其历史模拟不是2026实际投资业绩。

原122来源顶层原件/提取/元数据SHA在[baseline-source-hashes.json](baseline-source-hashes.json)，本轮未改旧原文。新来源与索引、代码hash/语法、当前链接及文档边界核查见[verification.json](verification.json)。未运行模型/API、代码生成、回测、部署或发送信息；最终report未开始写。

当前125个正式来源：112主阅读、9辅助、4来源链；88一手、35候选、2未解决。原21家样本与历史评分不变；海外材料分开标记。
