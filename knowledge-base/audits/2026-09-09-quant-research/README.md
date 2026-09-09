# 量化专项检索与审查 — 2026-09-09

用户新增量化偏好，本轮纳入纯量化ML和LLM辅助量化研发。[研究报告](../../companies/quant-research-2026-09-09.md)给出方向、来源归因及具体代码问题。

新增正式来源FUND-120–122：Label Horizon论文v5、官方日频demo、易方达合著Alpha mining综述。微软RD-Agent论文/代码在[外部方法目录](../../reference/quant-methods/README.md)，不混入基金管理公司样本或公司分数。

当前115个正式来源：107主阅读、4辅助、4来源链；82一手、31候选/二手、2未解决。21家公司评分本轮未变。旧重点研究审计中的112来源数为其完成时快照，本轮另建记录，不改写该历史结果。

## 搜索及来源处理

代表查询：`E Fund quantitative LLM factor`、`EFundAI label-horizon-paradox`、`基金 因子 大模型 github`、`A survey on large language model-based alpha mining`、`Microsoft RD-Agent quantitative finance`、`中欧基金 优化器 上海交通大学`。

- Label Horizon：官方EFundAI README→论文arXiv条目→v5原PDF；[ICML下载目录](https://icml.cc/Downloads/2026)核题名，原PDF第1页核单位及会议信息。OpenReview要求浏览器验证，ICML单篇页打开失败，未绕过验证；均未用失败页证明论文内容。
- Alpha mining：期刊[JZUS条目](https://jzus.zju.edu.cn/iparticle.php?doi=10.1631/FITEE.2500386)及[HEP原PDF](https://journal.hep.com.cn/fitee/EN/PDF/10.1631/FITEE.2500386)。综述引用文献只作检索线索，不自动归入易方达项目。
- RD-Agent：[作者arXiv论文](https://arxiv.org/abs/2505.15155v2)、[微软仓库](https://github.com/microsoft/RD-Agent)、[官方文档](https://rdagent.readthedocs.io/en/latest/scens/quant_agent_fin.html)。搜索得到的DeepWiki和第三方项目只用于定位，没有替代源码。
- BlackRock AlphaAgents：搜索出现第三方“论文实现”仓库，未确认官方实现，未收入当前优先代码集。
- 中欧/华泰柏瑞/富国：重新读取已入库原语言材料；未因媒体提到求解器、速度或AI能力就升级4/5分。

GitHub REST树API触发限流；使用公开Git仓库只读获取（无checkout），按固定commit从git对象中选取文件。Label Horizon取33个文件，RD-Agent取44个；源码不执行、不安装、不递归获取子模块。没有获取数据、秘密配置、账户凭据或付费内容。临时Git存储不是知识库正文，不递归入库。

## 审查范围

3份PDF原件共85页：FUND-120为30页、FUND-122为13页，外部RD-Agent为42页。使用pypdf提取并清除非打印控制字符，保留原PDF与哈希；数学排版以PDF为准。渲染了Label Horizon第1页、综述第4页、RD-Agent第3及24页；视觉核对前两者及RD-Agent第24页，未声称逐页视觉核对。

静态核查了标签构造、BLO输出、回测读取路径、默认Qlib配置和反馈链。已确认的关键边界见研究报告：

- Label Horizon是独立公开demo，不能逐项代替论文实验；BLO输出λ，收益回测读取逐h基线alpha；跨分段标签及简化执行需检查。
- RD-Agent当前默认test回测结果会参与自适应反馈；论文交易成本/执行措辞与代码要定版对齐。不能将当前代码反推为论文全部实验的真实运行配置。
- 不直接采纳“3天永远最佳”“收益翻倍”“低API费用就是总成本”等推广性结论。

旧112个来源的324份顶层原件/阅读文本/元数据逐文件哈希保存在[baseline-source-hashes.json](baseline-source-hashes.json)，用于确保这轮未动原件。新源文件和77份代码/文档的hash/tree一致性、Python语法、索引和链接检查见[verification.json](verification.json)。检查脚本[verify.py](verify.py)可重跑；它不执行下载代码或交易逻辑。
