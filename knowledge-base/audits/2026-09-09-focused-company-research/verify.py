from pathlib import Path
import json,hashlib,subprocess,re,ast,collections
from urllib.parse import unquote
root=Path(__file__).resolve().parents[3];kb=root/'knowledge-base';audit=Path(__file__).resolve().parent
checks=[]
def add(name,passed,detail): checks.append(dict(name=name,passed=bool(passed),detail=detail))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
idx=json.loads((kb/'reading-index.json').read_text()); ids=[r['source_id'] for r in idx['records']]
regids=re.findall(r'^\| ((?:FUND|REG)-\d+) \|',(kb/'source-register.md').read_text(),re.M)
add('register/index identities',len(ids)==112 and len(set(ids))==112 and sorted(ids)==sorted(regids),{'index':len(ids),'register':len(regids)})
add('roles',idx['counts']==dict(collections.Counter(r['collection_role'] for r in idx['records'])),idx['counts'])
missing=[r['source_id'] for r in idx['records'] if (r.get('reading_path') and not (kb/r['reading_path']).exists()) or (r.get('available_text') and not r.get('reading_path')) or not (kb/r['metadata_path']).exists()]
add('all indexed files exist',not missing,missing)
old=json.loads((audit/'before-state/evidence-scores-2026-09-09.json').read_text());new=json.loads((kb/'companies/evidence-scores-2026-09-09.json').read_text())
changed=[a['company'] for a,b in zip(old['records'],new['records']) if a!=b]
add('only E Fund score record changes',changed==['易方达'] and len(new['records'])==21 and new['counts']=={'1':0,'2':2,'3':17,'4':2,'5':0},changed)
bad=[]
for r in new['records']:
 for s in r['sources']:
  if sha(kb/s['reading_path'])!=s['reading_sha256']:bad.append(s['source_id'])
add('score evidence hashes',not bad,bad)
raw_bad=[]
for pstr in subprocess.check_output(['git','ls-tree','-r','--name-only','HEAD','knowledge-base/sources'],cwd=root,text=True).splitlines():
 p=root/pstr
 if re.match(r'knowledge-base/sources/(FUND|REG)-\d+/(?:source\.[^/]+|original\.md|metadata\.json)$',pstr):
  original=subprocess.check_output(['git','show','HEAD:'+pstr],cwd=root)
  if not p.exists() or p.read_bytes()!=original:raw_bad.append(pstr)
add('historical raw/extracted/metadata byte preservation',not raw_bad,raw_bad)
files=0;hash_bad=[];syntax_bad=[];pycount=0
manifests=[kb/f'sources/FUND-{n}/repository/archive.json' for n in [115,117,118,119]]+[audit/'repositories/yingmi-compliance/archive.json']
for manifest in manifests:
 m=json.loads(manifest.read_text());tree=json.loads((manifest.parent/'tree.json').read_text());tree_paths={x['path']:x for x in tree['tree']}
 for f in m['files']:
  p=manifest.parent/'files'/f['path'];files+=1
  if sha(p)!=f['sha256'] or tree_paths[f['path']]['sha']!=f['git_blob_sha']:hash_bad.append(str(p))
  if p.suffix=='.py':
   pycount+=1
   try:ast.parse(p.read_text())
   except SyntaxError as e:syntax_bad.append({'path':str(p),'error':str(e)})
add('downloaded repository files match hashes/tree',not hash_bad,{'files':files,'failures':hash_bad})
add('Python AST syntax (not runtime)',not syntax_bad,{'files':pycount,'failures':syntax_bad})
metabad=[]
for n in range(113,120):
 d=kb/f'sources/FUND-{n}';m=json.loads((d/'metadata.json').read_text())
 if sha(d/m['raw_file'])!=m['sha256'] or sha(d/m['text_file'])!=m['reading_sha256']:metabad.append(n)
add('new company source metadata hashes',not metabad,metabad)
paths=[kb/'companies/focused-research-2026-09-09.md',kb/'companies/evidence-scores-2026-09-09.md',kb/'reference/yingmi-compliance-workflow-2026-09-09.md',audit/'README.md',audit/'search-log.md',kb/'sources/README.md',kb/'source-register.md']
paths += [kb/f'sources/FUND-{n}/original.md' for n in range(113,120)]
missing_links=[];count=0
for p in paths:
 for link in re.findall(r'\]\(([^\s)]+)\)',p.read_text()):
  if re.match(r'[a-zA-Z][\w+.-]*:|#',link):continue
  link=unquote(link.split('#')[0]);count+=1
  if not (p.parent/link).exists() and link!='verification.json':missing_links.append({'file':str(p.relative_to(kb)),'target':link})
add('current research/integration local links',not missing_links,{'checked':count,'missing':missing_links})
proc=subprocess.run(['git','diff','--check'],cwd=root,text=True,capture_output=True)
add('tracked diff whitespace',proc.returncode==0,proc.stdout+proc.stderr)
result={'date':'2026-09-09','passed':all(x['passed'] for x in checks),'checks':checks,'limits':'File/syntax/integration checks; not a full runtime reproduction, legal approval, or independently verified investment performance.'}
(audit/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False,indent=2))
