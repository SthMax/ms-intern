# 外部量化方法参考

本目录是研究机构的技术参考，不计入21家基金管理公司、公司实施案例数或主来源ID统计。

## RD-Agent-Quant

- [作者论文](https://arxiv.org/abs/2505.15155v2)，本地[42页PDF](rd-agent-quant/source.pdf)、[原语言提取](rd-agent-quant/original.md)、[元数据](rd-agent-quant/metadata.json)。第1页单位为微软亚洲研究院及CMU/HKUST/Oxford；论文为NeurIPS 2025版本。
- [固定版本官方仓库](https://github.com/microsoft/RD-Agent/tree/32b3d395e73d9db5eee3fe9063d69aec0fdc83bd)，本地[README](rd-agent-code/files/README.md)、[44个选取文件manifest](rd-agent-code/archive.json)、[完整树目录](rd-agent-code/tree.json)。仅选取量化工作流相关源码/配置/文档，不是全仓库镜像。
- 已读量化主循环、因子runner与反馈、Qlib策略/成本配置、论文方法/实验/Prompt/局限。详见[量化研究报告](../../companies/quant-research-2026-09-09.md)。

它提供接近5分的技术材料，但当前代码版本与论文实验版本没有逐一对应，名为test的回测结果会进入搜索反馈，论文成本/执行文字也存在不一致。技术完整度与独立样本外效果须分别判断；本轮没有安装、调用模型或运行生成代码，没有据此推荐实际交易。
