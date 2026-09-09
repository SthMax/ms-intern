"""Build auditable, deterministic report inputs from the committed knowledge base."""
from pathlib import Path
import json, hashlib, re
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent

def esc(s):
    return ''.join({'\\':r'\textbackslash{}','&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_','{':r'\{','}':r'\}','~':r'\textasciitilde{}','^':r'\textasciicircum{}'}.get(c,c) for c in str(s))

def url(s):
    return str(s).replace('%',r'\%').replace('#',r'\#')

cohort=json.loads((HERE/'data/cohort.json').read_text())
fig=[r'\begin{tikzpicture}',r'\begin{axis}[xbar,width=15.8cm,height=13.8cm,xmin=0,xmax=19500,',r'ytick={1,...,20},yticklabels={'+','.join(esc(x['company']) for x in cohort)+r'},y dir=reverse,',r'ymin=0.25,ymax=20.75,bar width=9pt,axis x line*=bottom,axis y line*=left,y axis line style={draw=none},',r'xtick={0,5000,10000,15000},scaled x ticks=false,xticklabel style={/pgf/number format/fixed,/pgf/number format/1000 sep={,}},',r'xmajorgrids=true,grid style={linegray},tick style={draw=none},',r'xlabel={2026年二季度末非货公募规模（亿元人民币）},',r'tick label style={font=\small},label style={font=\small},',r'nodes near coords,point meta=x,nodes near coords style={font=\scriptsize,anchor=west,/pgf/number format/fixed,/pgf/number format/precision=0,/pgf/number format/1000 sep={,}}]',r'\addplot[fill=teal,draw=none] coordinates {'+' '.join(f"({x['aum_cny_100m']},{x['rank']})" for x in cohort)+r'};',r'\end{axis}',r'\end{tikzpicture}']
(HERE/'figures/aum.tex').write_text('\n'.join(fig)+'\n')

# Locators and date descriptions are report-specific annotations, separate from raw metadata.
refs={
'FUND-001':('2025-12-31；历史采购证据','采购公告；不证明验收或完整LLM部署'),
'FUND-004':('2026年1月协会案例；PDF未注明修订日期','指数业务一体化平台；平台指标与LLM效果须分开'),
'FUND-007':('2026-01-19协会目录；PDF未注明日期','PDF第8–9页；本地RAG、市场观点与因子辅助评价'),
'FUND-009':('协议未注明发布日期','大模型技术名称与服务协议；不据URL月份认定发布日期'),
'FUND-011':('2026年1月协会案例；PDF未注明日期','千询固收交易平台；NLP与基础LLM需区分'),
'FUND-013':('2026年1月协会案例；PDF未注明日期','固收平台中的Qwen2.5交易要素提取'),
'FUND-109':('2026-07-24','微信原刊；基金研选Skill产品说明'),
'FUND-113':('2025，26(10)；历史技术补充','PDF第5–9、13–14页；MENTOR方法、实验与数据边界'),
'FUND-114':('2025；MENTOR官方补充材料','PDF第1–5页，尤其第2–3页Prompt'),
'FUND-115':('代码快照；不推断发布日期','固定提交1058e1b；公开查询客户端与配置缺口'),
'FUND-116':('无日期帮助文档；2026-09-09归档','PDF第8–10页查询示例；非服务端代码'),
'FUND-119':('NLPCC 2026共享任务；仓库快照','固定提交4744a77；研究基线、Prompt、数据及回测客户端'),
'FUND-150':('2025版案例集；历史补充','华安“灵思”；本地与API混合平台'),
'FUND-160':('2026-02-06','中国证券报；平安AI青蚨报道'),
'FUND-200':('2026-01-23协会目录；PDF未注明修订日期','PDF第4–8页，尤其第5–6页NL2SQL及权限检查'),
'FUND-215':('2026-04-30','博时BSBox报道；工具与运行环境'),
'FUND-220':('2026-01-27协会目录；PDF未注明修订日期','PDF第5–11页，尤其第7页图2；LLM与规则平台边界'),
'FUND-251':('2026-08-20','中国基金报20家调研；媒体/公司归属陈述，不替代技术原件'),
'FUND-300':('2026-01-19协会目录；PDF未注明日期','PDF第4–7页；FinAgent分层与业务拆解'),
'FUND-304':('2025报告期；发布日期未独立确认','嘉实可持续投资报告；AI/NLP不自动等于LLM'),
'FUND-308':('2026-01-27协会目录；PDF未注明日期','PDF第3–6页；Prompt治理、RAG与营销材料审核'),
'FUND-312':('2026-01-21协会目录；PDF未注明日期','工银瑞信养老金运营管理平台'),
'FUND-316':('2023报告期；历史合作证据','恒生电子可持续发展报告；FundGPT相关合作方'),
'FUND-321':('2026年1月协会案例；PDF未注明日期','中信建投基金本地LLM平台；扩展样本'),
'FUND-323':('2026-02-11','Man AHL；原文流程图与三组研究想法实验'),
'FUND-324':('2026-07-09','Two Sigma；文本特征研究观点，缺少完整实现'),
'FUND-352':('2026-07-01协会目录；PDF未注明日期','永赢安全GPT邮件反钓鱼；非投研量化系统'),
'FUND-356':('2026-06-01','微信原刊；中欧Skills与投研协作披露'),
'FUND-359':('2026-09-03','微信原刊、用户保存PDF；文本处理实践与Agent展望分开'),
'FUND-400':('2026-07-21','财联社；2026Q2非货公募规模，剔除ETF联接基金'),
'FUND-403':('2026年1月协会案例；PDF未注明日期','国泰组合平台；DeepSeek与传统NER模块分开'),
}
for i in range(1,17):
    sid=f'REG-{i:03d}'
    p=ROOT/'knowledge-base/sources'/sid/'metadata.json'
    if p.exists():
        d=json.loads(p.read_text());refs[sid]=(d.get('published','见官方原文'),'具体条款及适用条件见报告第9节；法律状态核验记录见监管复核底稿')

# Only publish references cited by the authored report.
tex='\n'.join(p.read_text() for p in HERE.glob('*.tex') if p.name not in {'references.tex','landscape.tex'})
used=set(re.findall(r'\\src\{([^}]+)\}',tex))
used.update(re.findall(r'\\refsource\{([^}]+)\}',tex))
landscape_path=HERE/'landscape.tex'
if landscape_path.exists(): used.update(re.findall(r'\\src\{([^}]+)\}',landscape_path.read_text()))
manifest=[]; entries=[]
for sid in sorted(used):
    if sid in refs:
        folder=ROOT/'knowledge-base/sources'/sid
        m=json.loads((folder/'metadata.json').read_text())
        date,loc=refs[sid]
        title=m['title'].replace('🧧','')
        link=m['url']
        if sid=='FUND-113': link='https://doi.org/10.1631/FITEE.2500608'
        raw=folder/m.get('raw_file','source.pdf')
        item=dict(id=sid,title=title,issuer=m.get('issuer',''),date_label=date,url=link,locator=loc,metadata_path=str((folder/'metadata.json').relative_to(ROOT)))
        files=[]
        for f in [raw,folder/m.get('text_file','original.md')]:
            if f.is_file(): files.append(dict(path=str(f.relative_to(ROOT)),sha256=hashlib.sha256(f.read_bytes()).hexdigest()))
        item['files']=files
    elif sid=='EXT-QA':
        folder=ROOT/'knowledge-base/reference/2026-llm-quant/quantaalpha'
        title='QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining'
        date='2026；归档PDF封面日期2026-05-19（arXiv v3）'
        loc='23页论文；方法、实验及附录Prompt；作者团队包含高校与研究项目'
        link='https://arxiv.org/abs/2602.07085v3'
        item=dict(id=sid,title=title,date_label=date,url=link,locator=loc,files=[dict(path=str((folder/'source.pdf').relative_to(ROOT)),sha256=hashlib.sha256((folder/'source.pdf').read_bytes()).hexdigest())])
    elif sid=='EXT-QC':
        folder=ROOT/'knowledge-base/reference/2026-llm-quant/quantaalpha-code'
        archive=json.loads((folder/'archive.json').read_text())
        title='QuantaAlpha官方代码选取快照'
        date='固定提交 '+archive['commit'][:12]
        loc='30个选取文件；完整清单及逐文件哈希见archive.json；未执行复现'
        link='https://github.com/QuantaAlpha/QuantaAlpha/tree/'+archive['commit']
        item=dict(id=sid,title=title,date_label=date,url=link,locator=loc,archive_manifest=str((folder/'archive.json').relative_to(ROOT)),commit=archive['commit'],files=archive['files'])
    elif sid=='EXT-AB':
        folder=ROOT/'knowledge-base/reference/local-llm/alphaqt-bench'
        title='AlphaQT-Bench：量化因子代码评价基准'
        date='ACL 2026 Findings'
        loc='16页论文；第16页Prompt及执行、因果、语义、结构评价'
        link='https://aclanthology.org/2026.findings-acl.138/'
        item=dict(id=sid,title=title,date_label=date,url=link,locator=loc,files=[dict(path=str((folder/'source.pdf').relative_to(ROOT)),sha256=hashlib.sha256((folder/'source.pdf').read_bytes()).hexdigest())])
    else:
        raise ValueError(f'Unresolved citation {sid}')
    manifest.append(item)
    entries.append(r'\referenceentry{'+esc(sid)+'}{'+esc(title)+'}{'+esc(date)+'}{'+esc(loc)+'}{'+url(link)+'}')
(HERE/'references.tex').write_text('\n\n'.join(entries)+'\n')
(HERE/'data/source-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(f'Generated AUM chart and {len(manifest)} source references.')
