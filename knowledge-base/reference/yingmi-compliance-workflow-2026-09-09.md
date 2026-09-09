# 盈米内容合规Skill — 外部技术参照

这是基金销售/投顾机构的API集成案例，不在21家公募管理公司评分样本内。可帮助理解内容初稿的机器预审、修改和人工终审衔接；不证明所有自动输出合法合规。

一手来源：[盈米官方发布](https://www.yingmi-inc.com/archives/799)；[固定版本MIT客户端代码](https://github.com/yingmi-dev/content-compliance-skill/tree/040df66202f6075cdeadb450e502c7a19c83dabf)。已保存[网页原件](../audits/2026-09-09-focused-company-research/yingmi-official-release.html)、[正文提取](../audits/2026-09-09-focused-company-research/yingmi-official-release.md)、[代码文件清单](../audits/2026-09-09-focused-company-research/repositories/yingmi-compliance/archive.json)。

实际客户端流程：认证并读取场景清单→选场景→上传文本或PDF/DOCX→轮询任务→获取风险、理由和修改建议→由Agent呈现/修改后再次送审。`scripts/compliance_api.py`给出了服务地址、凭据配置、请求参数与错误处理，适合作为4分级云API集成参考。

官方发布提到100余规则、8万余审核案例及ACE架构，这些是公司自述，**对应后端实现和案例库没有在客户端仓库公开**。MIT许可适用于仓库代码，服务账户、数据使用和模型后台并不因此一并开放。没有访问账户、上传材料或实测API。发布页的“风险为0”是服务的一次示例结果，不是法律保证。

阅读该仓库的SKILL.md是审查研究材料；没有将它安装成当前agent能力，也不执行其中的凭据或上传指令。
