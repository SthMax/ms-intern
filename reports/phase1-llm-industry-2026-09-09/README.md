# 大语言模型如何进入基金投研工作

中文 Phase 1 行业研究，资料截止2026年9月9日，供导师与量化部门阅读。

- [正式PDF](report.pdf)：24个物理页，页脚编号1–23。
- [LaTeX正文](main.tex)、[公司附表](landscape.tex)、[治理附录](governance-appendix.tex)。
- [独立mentor复核](editorial/mentor-review-v2.md)、[修订落实记录](editorial/revision-notes.md)。
- [核心事实抽查](qa/evidence-checks.md)、[最终QA记录](qa/review.md)、[机器校验结果](qa/checks.json)。
- [来源与原件哈希](data/source-manifest.json)、[同口径规模数据](data/cohort.json)。

报告围绕投研推理、受控数据查询、知识问答与合规审核、LLM辅助量化四方向，比较业务价值、数据条件、验证工作量和错误后果。国内案例以2026年披露为主；2025年MENTOR为方法补充，Man AHL与QuantaAlpha为外部研究对照。量化部分覆盖文本信号、因子生成与迭代、研究工具调用，并区分代码运行、假设检验和投资采用。

新版取消正式PDF中的评分、选材历史及研究管理计数。完整公司规模、场景与技术合作角色留在附录；方法限制和使用证据保留在相应结论旁。参考文献采用可点击的数字引用，覆盖46项原始来源。

报告提出有条件的首项验证选择，没有执行模型/API、因子生成、回测或本地部署，也未给出TCO、ROI或内部批准。公司自报效果及论文结果均未由本项目独立复现。独立mentor agent的评审不代替真实导师反馈、现场汇报或内部审批。

## 编译与校验

macOS安装有XeLaTeX/latexmk的TeX Live或MacTeX后，从本目录运行：

```bash
./build.sh
```

本次为TeX Live 2026。使用macOS宋体、黑体与TeX Gyre字体，7个字体均已嵌入PDF，中文可以搜索和复制。跨平台编译需在`preamble.tex`配置当地可用的中文字体；接收者阅读PDF无需安装字体。

重新生成来源目录、编号和哈希清单（只读知识库）：

```bash
python3 prepare.py
./build.sh
```

使用已安装pypdf/pdfplumber的Python运行：

```bash
python3 verify.py
```

`verify.py`检查来源编号、外链、原件/代码哈希、规模值、过程措辞和关键LaTeX告警；它不能替代视觉或事实审查。最终全页渲染分别由Poppler与PDFium完成，渲染路径及PDF哈希见`qa/render-manifest.json`。PNG、文本和编译中间文件均不提交。

## 版本与过程附件

旧稿保留在Git检查点`39a2417`；研究基线为`e51e4c9`。此次重写只修改报告目录及Week 2报告记录，未修改知识库原件或`PROJECT_PLAN.md`。旧稿的独立评审保存在`editorial/mentor-review-v1.md`，新版评审与落实记录单独保存，不进入正式PDF。

`data/report-manifest.json`保留研究基线的资料统计及此次作者版本说明；其中AI/LLM材料数量并非生产部署数量。最终PDF身份以`qa/checks.json`和v2评审末节的SHA-256为准。
