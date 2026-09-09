from pathlib import Path
import json,hashlib,re,ast,collections,subprocess
from urllib.parse import unquote
root=Path(__file__).resolve().parents[3];kb=root/'knowledge-base';audit=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
def check(name,passed,detail):checks.append(dict(name=name,passed=bool(passed),detail=detail))
idx=json.loads((kb/'reading-index.json').read_text());ids=[r['source_id'] for r in idx['records']];regids=re.findall(r'^\| ((?:FUND|REG)-\d+) \|',(kb/'source-register.md').read_text(),re.M)
check('source identity and uniqueness',len(ids)==115 and len(set(ids))==115 and sorted(ids)==sorted(regids),{'index':len(ids),'register':len(regids)})
roles=dict(collections.Counter(r['collection_role'] for r in idx['records']));states=dict(collections.Counter(r['evidence_state'] for r in idx['records']))
check('counts',roles==idx['counts'] and roles=={'main':107,'supporting':4,'redirect':4}, {'roles':roles,'evidence_states':states})
missing=[r['source_id'] for r in idx['records'] if not (kb/r['metadata_path']).exists() or (r.get('reading_path') and not (kb/r['reading_path']).exists())]
check('indexed paths',not missing,missing)
baseline=json.loads((audit/'baseline-source-hashes.json').read_text());bad=[p for p,h in baseline.items() if not (kb/p).exists() or sha(kb/p)!=h]
check('previous source bytes unchanged',not bad,{'files':len(baseline),'changes':bad})
count=0;python_count=0;bad=[];syntax=[]
for d in [kb/'sources/FUND-121',kb/'reference/quant-methods/rd-agent-code']:
 a=json.loads((d/'archive.json').read_text());tree={x['path']:x for x in json.loads((d/'tree.json').read_text())['tree']}
 for f in a['files']:
  p=d/'files'/f['path'];b=p.read_bytes();count+=1
  gitsha=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
  if sha(p)!=f['sha256'] or gitsha!=f['git_blob_sha'] or tree[f['path']]['sha']!=gitsha:bad.append(str(p))
  if p.suffix=='.py':
   python_count+=1
   try:ast.parse(p.read_text())
   except SyntaxError as e:syntax.append(str(e))
check('selected repository bytes and Git blobs',not bad,{'files':count,'failures':bad})
check('Python syntax only',not syntax,{'files':python_count,'errors':syntax})
bad=[]
for d in [kb/f'sources/FUND-{n}' for n in [120,121,122]]+[kb/'reference/quant-methods/rd-agent-quant']:
 m=json.loads((d/'metadata.json').read_text())
 if sha(d/m['raw_file'])!=m['sha256'] or sha(d/m['text_file'])!=m['reading_sha256']:bad.append(str(d))
check('new source metadata hashes',not bad,bad)
score=json.loads((kb/'companies/evidence-scores-2026-09-09.json').read_text());check('company scores unchanged',score['counts']=={'1':0,'2':2,'3':17,'4':2,'5':0} and len(score['records'])==21,score['counts'])
paths=[kb/'companies/quant-research-2026-09-09.md',kb/'reference/quant-methods/README.md',audit/'README.md',kb/'source-register.md',kb/'sources/README.md']+[kb/f'sources/FUND-{n}/original.md' for n in [120,121,122]]
missing=[];n=0
for p in paths:
 for link in re.findall(r'\]\(([^\s)]+)\)',p.read_text()):
  if re.match(r'[a-zA-Z][\w+.-]*:|#',link):continue
  link=unquote(link.split('#')[0]);n+=1
  if not (p.parent/link).exists() and link!='verification.json':missing.append({'file':str(p.relative_to(kb)),'link':link})
check('research/integration local links',not missing,{'checked':n,'missing':missing})
p=subprocess.run(['git','diff','--check'],cwd=root,capture_output=True,text=True);check('tracked diff whitespace',p.returncode==0,p.stdout+p.stderr)
result=dict(date='2026-09-09',passed=all(x['passed'] for x in checks),checks=checks,scope='Archival, static syntax and integration validation; not a runtime backtest, financial-data-rights approval or independently reproduced performance.')
(audit/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False,indent=2))
