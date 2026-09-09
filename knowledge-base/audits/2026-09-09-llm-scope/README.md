# 用户明确LLM范围后的纠正

用户指出前轮工银两项是传统ML/深度学习，要求仍聚焦LLM。纠正后的[入选表](../../companies/llm-report-scope-2026-09-09.md)为报告选择依据。

- 工银从传统ML材料得到的3→4上调撤回；记录恢复自前轮上调前快照，不重新臆测原分数。
- FUND-120/121/226/318/319转辅助，设置`llm_report_eligibility=excluded_non_llm`；原件及阅读文本保留。当前119旧来源加1新候选，共120条：107主阅读、9辅助、4来源链。
- 21家历史底表混有广义AI材料，现明确不等同严格LLM排名；确认的4分LLM公司为易方达、南方。
- 新增鹏华CN120804142A，FUND-320：S50明确LLM调用，方法涉及schema/示例约束、Cypher生成、校验重试与图查询。仅得说明书镜像，未取得PDF、附图或部署证明，保持candidate，不升级评分。
- InfoQ天弘分享由搜索返回部分内容，直接HTTP获取451；汇添富评测B版镜像404。未绕过限制、未将失败响应当正文、未依据这些线索提分。此前汇添富A版的镜像仍在上轮审计。

修正前当前笔记/评分/索引在`before-state/`。旧原件与阅读文本的SHA-256记录在[original-byte-baseline.json](original-byte-baseline.json)，元数据角色变更属于本轮授权修正。原始论文、专利的技术价值保留，但不再用于填LLM报告缺口。

元数据、来源ID、评分恢复、分类、当前笔记链接与原件字节检查见[verification.json](verification.json)。本轮没有运行模型或代码、没有编写最终report。
