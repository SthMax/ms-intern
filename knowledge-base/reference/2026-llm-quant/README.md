# 2026 LLM＋量化框架参考

这些是外部研究材料，不计为基金公司已部署案例。API方案可用，本地化另评；[当前公司与方法矩阵](../../companies/quant-research-2026-09-09.md)。

| 项目 | 原件与代码 | 边界 |
|---|---|---|
| QuantaAlpha | [23页论文](quantaalpha/source.pdf) · [提取](quantaalpha/original.md) · [元数据](quantaalpha/metadata.json) · [官方源码清单](quantaalpha-code/archive.json) | 2026论文，所取PDF日期2026-05-19；代码固定b7ceb27b1001261d7a95b209a963664ae1f8ab23；30份选取文件；未执行，数据/模型/授权未作为已验证处理 |
| CogAlpha | [35页ACL 2026正式论文](cogalpha/source.pdf) · [提取](cogalpha/original.md) · [元数据](cogalpha/metadata.json) | 正式发表2026，早期预印本2025；作者单位含GIM、港大和中移动；未找到完整官方代码，第三方复现不能替代 |
| AlphaQT-Bench | [2026论文](../local-llm/alphaqt-bench/source.pdf) | 量化代码评价协议，非基金部署、非本地LLM实测；完整测试包未取得 |

QuantaAlpha核心链路在`quantaalpha-code/files/quantaalpha/pipeline/`，Prompt在其`prompts/`及`factors/regulator/`，模型端配置在`llm/config.py`，回测配置在`configs/backtest.yaml`。只保存用于研究的源码/配置/Prompt，未下载行情、安装依赖、运行LLM或回测。
