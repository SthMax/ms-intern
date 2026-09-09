# 本地LLM目标的定向研究 — 2026-09-09

用户强调项目目标为本地部署LLM并通过其能力完成实际任务，前述三个LLM量化方向保持。结果见[任务/代码/部署证据](../../models/local-llm-poc-evidence-2026-09-09.md)。本轮不是实际GPU部署或最终report写作。

## 正式新增与来源处理

- FUND-321：AMAC刊载中信建投基金7页原始公司案例，物理第6页私有化部署措辞已视觉核对。是样本外补充，不改原21家统计，不自动升4分。
- FUND-322：AMAC2025年第4期总201期《基金行业人工智能大模型应用及建设探索》，14页，末页明确联博基金技术部陈慧卿供稿。是行业建设研究，不认证联博实际部署全文所有模块。
- 原件与提取已移到sources/FUND目录，本目录原metadata记录`relocated_to`。
- 外部参考位于[reference/local-llm](../../reference/local-llm/README.md)：AlphaQT-Bench、AlphaFin、FinGPT论文/代码。两个仓库固定commit，选取18份代码/文档/notebook及许可；不计为基金实施证据。

## 检索路径及未升级项

定向查询覆盖公司＋本地/私有化/RAG/Prompt、天弘平野演讲与基金行业建设文章、开源LLM金融文本任务、LLM因子实现评价。主要原始入口：AMAC、CCF、ACL Anthology、arXiv、作者GitHub组织和Hugging Face模型/数据卡。

天弘FCon分享的原始站点直接取文受限，未再次尝试绕过；使用搜索返回的演讲片段作定位，已入库FUND-300仍为主要公司出处。招聘、基金持仓公司讲AI、机构调研对象的技术以及“智能”但未证实LLM的交易机器人均没有用来提分。

AlphaQT-Bench全文核出云端OpenRouter调用，以及所列毫秒耗时是生成代码执行；未当作本地LLM测量。AlphaFin已读本地模型加载、Embedding/FAISS、Prompt、Top-K与返回链；发现UI模式和实现不完全对应、动态日期影响复现等限制。FinGPT已读本地任务notebook与SETUP，发现7B基座/13B adapter混用示例，不能原样采用。

AlphaFin HF数据卡可读，标注Apache-2.0，但预览混有一般新闻，未整库下载/入库；模型卡对应ChatGLM2-6B与PEFT 0.5.0。资料“公开”与我们的数据选择/使用权、正确性分别判断。

## 验证

原120个来源顶层原件/阅读/元数据哈希保存在[baseline-source-hashes.json](baseline-source-hashes.json)，旧文件未改。新原件PDF提取保留语言与页号；视觉核对中信建投第6页、AlphaQT第16页完整Prompt。其余方法页文本审查，不宣称逐页视觉复核。

代码只作静态阅读，notebook只解析JSON并导出代码，没有运行单元、模型、生成程序、训练、账户操作或交易。最终检查见[verification.json](verification.json)。当前122个正式来源为109主阅读、9辅助、4来源链；86一手、34候选、2未解决，历史评分本轮不变。
