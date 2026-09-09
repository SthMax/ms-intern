# 基金公司LLM应用与本地部署前期研究

Phase 1 行业报告，资料截止2026-09-09。供mentor与量化部门讨论。

- [PDF报告](report.pdf)
- [LaTeX主文件](main.tex)
- [编译脚本](build.sh)
- [来源清单与原件哈希](data/source-manifest.json)
- [样本规模数据](data/cohort.json) / [研究基线与计数口径](data/report-manifest.json)
- [校验与审阅记录](qa/review.md)

## 内容与定位

报告按仓库根目录的 `PROJECT_PLAN.md`（2026-09-06 mentor确认版）撰写，覆盖当前Phase 1的公司规模、应用场景、技术及合作方，以及隐私、解释性/MRM和外包要求。四个重点方向为投研推理、受控数据查询、知识问答与合规审核、LLM-assisted quant。

国内公司案例以2026年披露为主；2025 MENTOR明确作为历史技术补充。海外资管、学术任务和QuantaAlpha等公开框架不并入国内部署统计。材料评分针对指定工作流；公司报告效果未独立复现。本报告不代表完成本地部署、5–8模型比较、三年TCO或内部合规审批。

现有研究已在撰写前提交：`e51e4c9b93bd03c17f869c2f10027fa8061f9eae`。报告新增文件与该研究基线分开，原始文章、代码快照和法规原件未修改。

## 编译

在macOS上安装有XeLaTeX/latexmk的TeX Live或MacTeX后运行：

```bash
./build.sh
```

本次使用TeX Live 2026、XeLaTeX及latexmk。字体为macOS自带Songti SC和Heiti SC，以及TeX Live的TeX Gyre Pagella/Heros。中文字体已子集嵌入PDF，接收者阅读PDF无需安装字体。源码使用系统字体路径，移到非macOS机器时需在 `preamble.tex` 改为当地可用的中文字体。

`build.sh`把最终PDF复制到本目录 `report.pdf`。图表由TikZ/PGFPlots生成，无需网络或API。`references.tex`、`figures/aum.tex`已随源码提供，不需要访问知识库即可编译。

如需从仓库知识库重新生成引用清单及规模图：

```bash
python3 prepare.py
./build.sh
```

`prepare.py`只读知识库，写入报告目录；不抓取新网页、不调用模型。原始数据的来源/时点变化应先在知识库形成新版本，再更新本报告截止日与基线。

## 文件结构

- `main.tex`：正文、图表、结构和报告结论。
- `preamble.tex`：中文字体、颜色、链接和版式。
- `landscape.tex`：21家公司摘要表。
- `references.tex`：自动生成的49项实际引用来源。
- `figures/aum.tex`：从同口径规模数据生成的矢量图。
- `data/`：规模样本、基线计数、来源ID/URL/原件哈希。
- `qa/`：审阅结论和校验JSON；渲染图片/抽取文本仅作本地中间文件。
- `build/`：编译日志和辅助文件，忽略git跟踪。

报告共24个物理页，含封面；正文页码从执行摘要的1开始，至来源目录的23。中文文本可搜索、可复制；引用可跳转来源目录，目录含外部原始链接。
