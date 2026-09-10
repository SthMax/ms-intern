# 基金公司LLM应用调研

当前版本按“模型接收什么、执行什么任务、输出如何使用”重写，采用正式、客观的研究报告表达。修订日期为2026年9月10日，研究资料截止日保持2026年9月9日。

- [PDF报告](report.pdf)：22个物理页，页脚编号1–21。
- [LaTeX正文](main.tex)、[表A](landscape.tex)、[法规附录](governance-appendix.tex)、[实验结果附录](quant-evidence.tex)。
- [本次修改说明与写作参考](editorial/llm-role-revision.md)、[当前PDF检查记录](qa/review.md)。
- [来源与原件哈希](data/source-manifest.json)、[同口径规模数据](data/cohort.json)、[PDF机器校验](qa/checks.json)、[本次对照检查](qa/role-revision-checks.json)。

报告保留投研分析、数据查询、知识问答与合规审核、LLM辅助量化四个方向。行业概览与表A说明基金公司的模型任务和产物；案例正文区分LLM生成内容与工具执行、计算及人工复核。量化章节重点解释文本提取、因子表达式生成与修订，以及研究工具调用，主要收益和风险数字移至附录C。

国内材料以2026年披露为主，2025年MENTOR为方法补充；Man AHL与QuantaAlpha为外部研究对照。未公开的模型字段、提示词和接口不补造细节，说明性输出与公司运行记录明确区分。本次未开展模型/API实验、本地部署、回测复现或TCO/ROI测算，未修改PPT和知识库原件。

## 编译与校验

macOS安装有XeLaTeX/latexmk的TeX Live或MacTeX后，从本目录运行：

```bash
./build.sh
```

当前使用TeX Live 2026、macOS宋体和黑体，以及TeX Gyre字体。中文可搜索和复制，接收者阅读PDF无需另装字体。跨平台编译时需在`preamble.tex`指定当地可用的中文字体。

如需根据知识库重新生成来源目录、编号和哈希清单：

```bash
python3 prepare.py
./build.sh
```

使用已安装pypdf/pdfplumber的Python进行机器校验：

```bash
python3 verify.py
```

当前引用46项来源；机器校验核对117个原件或代码文件哈希、46个外链及20家公司的规模值。PDF经过全页渲染检查，版本和路径见`qa/render-manifest.json`。PNG、抽取文本和编译中间文件不提交。

## 历史版本与评审

- `39a2417`：首次独立mentor评审前的旧稿。
- `fc2cf1d`：按两轮独立评审完成的业务版报告。
- `0b85429`：叙述方式讨论前的检查点。
- `94c1b25`：按当时确认的口吻重写，加入表A概览。
- `98bab07`：局部修正口语措辞。
- `3509381`：本次LLM职责与正式文风修订的基线。

历史mentor评审与编辑记录保持原样，不表示独立mentor代理审阅了当前版本。本次修改记录见`editorial/llm-role-revision.md`。

研究基线`e51e4c9`的原始材料和`PROJECT_PLAN.md`保持不变。`data/report-manifest.json`中的研究管理数量不是公司生产部署数量。当前PDF身份以`qa/checks.json`中的SHA-256为准。
