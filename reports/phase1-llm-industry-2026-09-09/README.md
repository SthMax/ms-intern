# 基金公司LLM应用调研

当前版本按用户确认的汇报口吻改写，资料截止2026年9月9日。

- [PDF报告](report.pdf)：21个物理页，页脚编号1–20。
- [LaTeX正文](main.tex)、[表A](landscape.tex)、[法规附录](governance-appendix.tex)。
- [本次修改说明](editorial/narrative-revision.md)、[当前PDF检查记录](qa/review.md)。
- [来源与原件哈希](data/source-manifest.json)、[同口径规模数据](data/cohort.json)、[机器校验结果](qa/checks.json)。

报告从同业已经开展的应用出发，先用行业概览介绍表A，再依次讨论投研分析、数据查询、知识问答与合规审核、LLM辅助量化，最后结合监管文件说明本地探索需要确认的条件。表A汇总20家主要样本和大成补充案例，保留公司规模、实际应用、技术和合作信息；所有表格均按正式阅读需要重新表述。

国内材料以2026年披露为主；2025年MENTOR作为方法补充，Man AHL和QuantaAlpha作为外部研究对照。公司自报效果与论文结果保留具体条件，说明性例子与实际披露分开。尚未开展模型/API实验、本地部署、回测复现或TCO/ROI测算。

## 编译与校验

macOS安装有XeLaTeX/latexmk的TeX Live或MacTeX后，从本目录运行：

```bash
./build.sh
```

本次使用TeX Live 2026，以及macOS宋体、黑体和TeX Gyre字体。中文可搜索和复制，接收者阅读PDF无需另装字体。跨平台编译时需在`preamble.tex`指定当地可用的中文字体。

如需根据知识库重新生成来源目录、编号和哈希清单：

```bash
python3 prepare.py
./build.sh
```

使用已安装pypdf/pdfplumber的Python进行机器校验：

```bash
python3 verify.py
```

来源目录包含46项实际引用，机器校验核对117个原件或代码文件哈希以及20家公司的规模值。当前PDF经过全页渲染检查；渲染版本和路径见`qa/render-manifest.json`。PNG、抽取文本和编译中间文件不提交。

## 历史版本与评审

- `39a2417`：首次独立mentor评审前的旧稿。
- `fc2cf1d`：按两轮独立评审完成的业务版报告。
- `0b85429`：本次叙述方式讨论前的检查点。

`editorial/mentor-review-v1.md`、`editorial/mentor-review-v2.md`和`editorial/revision-notes.md`是此前版本的历史评审与修改记录，未被改写，也不表示独立mentor代理已审阅本次版本。本次以用户认可的摘要和章节样稿为依据，修改记录另见`editorial/narrative-revision.md`。

研究基线`e51e4c9`中的原始材料及确认的`PROJECT_PLAN.md`保持不变。`data/report-manifest.json`中的研究管理数量不是公司生产部署数量。当前PDF身份以`qa/checks.json`中的SHA-256为准。
