"""Read-only comparison of the approved cleanup against its pre-cleanup Git snapshot."""
from pathlib import Path
from collections import Counter
import hashlib, json, os, re, subprocess, sys
from urllib.parse import unquote
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[3]
KB = ROOT / 'knowledge-base'
AUDIT = Path(__file__).parent
BASE = '103f14ccbb18509afd013755128618c61f30e6ad'
checks = []
def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)
def before(path):
    return git('show', BASE + ':' + str(path.relative_to(ROOT)))
def old(path):
    return before(path).decode()
def check(name, ok, details=None):
    checks.append({'check': name, 'pass': bool(ok), 'details': details})
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
def body(text):
    return text.split('\n---\n', 1)[-1]
def normalize(text):
    text = re.sub(r'\[([^\]]*)\]\([^)]+\)', r'\1', text)
    return re.sub(r'\s+', '', text)
def pdf_pages(text):
    pieces = re.split(r'(?m)^## PDF page (\d+)\n', text)
    return {int(pieces[i]): pieces[i + 1] for i in range(1, len(pieces), 2)}

tree = {}
for record in git('ls-tree', '-rz', BASE).split(b'\0'):
    if not record: continue
    desc, path = record.split(b'\t', 1)
    tree[path.decode()] = desc.split()[2].decode()
expected_deleted = {'knowledge-base/sources/FUND-093/retrieval-response.md',
                    'knowledge-base/sources/FUND-093/retrieval-response.html',
                    'knowledge-base/sources/FUND-162/full-visible-text.txt'}
deleted = set(git('diff', '--name-only', '--diff-filter=D', BASE).decode().splitlines())
check('Only the three approved disposable files were deleted', deleted == expected_deleted, sorted(deleted))
asset_paths = [p for p in tree if p.startswith('knowledge-base/sources/') and Path(p).suffix.lower() in {'.html', '.pdf', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp'} and p not in expected_deleted]
current_assets = [p if p != 'knowledge-base/sources/FUND-203/source.html' else 'knowledge-base/sources/FUND-203/source.sina.html' for p in asset_paths]
asset_hashes = git('hash-object', '--', *current_assets).decode().splitlines()
asset_errors = [a for a, digest in zip(asset_paths, asset_hashes) if tree[a] != digest]
check('All existing source PDFs, HTML and images preserved byte-for-byte, allowing the documented Sina rename', not asset_errors and len(asset_hashes) == len(asset_paths), {'checked': len(asset_paths), 'mismatches': asset_errors})

# Check article preservation using the before/after text, not just new metadata claims.
p = KB/'sources/FUND-112/original.md'
expected = old(p).split('[MACD金叉信号形成，这些股涨势不错！]', 1)[0].rstrip()+'\n'
check('A2 Buddy body and full risk warning unchanged', p.read_text() == expected)
for sid, sns in {'FUND-110':['a342b90feb23715ad1dbf57efb29bf52'], 'FUND-251':['51c149921742d4593080d0fd9da1a022','b78c51f64886c5cbf7a4ca60fbfd6e50']}.items():
    p=KB/'sources'/sid/'original.md'
    expected='\n'.join(line for line in old(p).splitlines() if not any(sn in line for sn in sns)).rstrip()+'\n'
    check(sid+' only specifically approved recommendation lines removed', p.read_text()==expected)
p=KB/'sources/FUND-359/original.md'
check('Huatai entire article, final paragraph and risk warning unchanged', p.read_text()==old(p).split('\n---\n\n## 原页附属内容',1)[0].rstrip()+'\n')
p=KB/'sources/FUND-221/original.md'
check('CashPlus version history, provider and date unchanged', p.read_text()==old(p).split('你可能还喜欢',1)[0].rstrip()+'\n')
for sid in ['FUND-109','FUND-356']:
    p=KB/'sources'/sid/'original.md';check(sid+' canonical full reading unchanged', p.read_bytes()==before(p))
wp=next((KB/'sources/wechat-articles/WX-004').glob('*/metadata.json'))
wd=json.loads(wp.read_text());wx_text=(wp.parent/wd['markdown_file']).read_text()
check('Southern canonical raw HTML matches the archived WeChat bytes', (KB/'sources/FUND-203/source.html').read_bytes()==(wp.parent/'raw-source.html').read_bytes())
check('Southern canonical reading preserves all WeChat text', normalize(body((KB/'sources/FUND-203/original.md').read_text()))==normalize(body(wx_text)))

p=KB/'sources/FUND-150/original.md';prior=pdf_pages(old(p));selected=pdf_pages(p.read_text())
check('CCF main excerpt is exactly Huaan pages 23–28 with no loss of page text', set(selected)==set(range(23,29)) and all(normalize(selected[n])==normalize(prior[n]) for n in selected))
ref_pages=pdf_pages((KB/'reference/ccf-financial-cases.md').read_text());wanted=set(range(130,137))|set(range(171,176))
check('Two retained financial technical analogues match their original pages', set(ref_pages)==wanted and all(normalize(ref_pages[n])==normalize(prior[n]) for n in wanted))
banned=['温氏执业AI兽医','国家能源集团智慧化学习','智慧家庭全屋全流程','生猪产业链智能互联','船厂起重机监测','压缩机定子智慧检测','中国古壁画数字资源库','山西·文旅云','5G智慧电台']
check('Nine reviewed nonfinancial CCF chapter titles absent from the main excerpt', not any(t in p.read_text() for t in banned))
p=KB/'sources/FUND-405/original.md';pg=pdf_pages(p.read_text());orig=pdf_pages(old(p))
check('Guotai page 1, date, 294 count and risk notice preserved', set(pg)=={1} and normalize(pg[1])==normalize(orig[1]))
p=KB/'sources/FUND-162/metadata.json';m=json.loads(p.read_text());soup=BeautifulSoup((p.parent/'source.html').read_bytes(),'html.parser');v=set(soup.stripped_strings)
check('Ping An identity excerpt values grounded in unchanged HTML', m['excerpt_values']['html_title']==soup.title.get_text(strip=True) and all(x in v for x in m['excerpt_values']['visible_labels']))
for sid in ['FUND-255','FUND-357']:
    p=KB/'sources'/sid/'original.md';ref=(KB/'reference'/f'{sid}.md').read_text()
    source_part=body(ref).split('## 研究者用途与限制（原公司笔记移入）',1)[0]
    check(sid+' full source text preserved in supporting reference', normalize(source_part)==normalize(body(old(p))))
# Verify all unchanged source readers and every regulatory artifact, protecting against off-scope edits.
target_ids={'FUND-093','FUND-108','FUND-110','FUND-112','FUND-150','FUND-162','FUND-203','FUND-221','FUND-251','FUND-255','FUND-355','FUND-357','FUND-358','FUND-359','FUND-405'}
protected=[p for p in tree if (p.startswith('knowledge-base/regulation/') or p.startswith('knowledge-base/models/') or p.startswith('knowledge-base/infrastructure/') or p.startswith('knowledge-base/pilots/') or re.match(r'^knowledge-base/sources/[^/]+/original.md$',p) and p.split('/')[2] not in target_ids)]
errs=[p for p,h in zip(protected,git('hash-object','--',*protected).decode().splitlines()) if tree[p]!=h]
check('Untargeted source readers, regulation, model, architecture and pilot notes unchanged', not errs, {'checked':len(protected),'mismatches':errs})

manifest=json.loads((KB/'reading-index.json').read_text());records=manifest['records'];counts=Counter(r['collection_role'] for r in records)
check('Reading roles are 93 main / 4 supporting / 4 redirects; unique 101 IDs',len(records)==101 and len({r['source_id'] for r in records})==101 and counts=={'main':93,'supporting':4,'redirect':4},dict(counts))
check('All declared reading/metadata paths exist or are explicitly unavailable', all((not r['reading_path'] or (KB/r['reading_path']).is_file()) and (KB/r['metadata_path']).is_file() for r in records))
state_changes=[];hash_errors=[]
for p in (KB/'sources').glob('*/metadata.json'):
    d=json.loads(p.read_text());prev=json.loads(old(p))
    if d.get('evidence_state')!=prev.get('evidence_state'):state_changes.append(d['source_id'])
    if d.get('extracted_text_sha256') and (p.parent/'original.md').exists() and d['extracted_text_sha256']!=sha(p.parent/'original.md'):hash_errors.append(d['source_id'])
    if d.get('reference_text_sha256'):
        ref=(p.parent/d['reference_text']).resolve()
        if d['reference_text_sha256']!=sha(ref):hash_errors.append(d['source_id']+' reference')
check('All source evidence states unchanged',not state_changes,state_changes)
# Report pre-existing stale text hashes separately; only cleanup-introduced mismatches block completion.
new_hash_errors=[sid for sid in hash_errors if sid.split()[0] in target_ids]
check('All changed reading text/reference hashes correct',not new_hash_errors,{'new_mismatches':new_hash_errors,'preexisting_untouched_mismatches':[x for x in hash_errors if x not in new_hash_errors]})
def registry_states(text):
    return {m[1]:m[2] for line in text.splitlines() if (m:=re.match(r'^\| ((?:FUND|REG)-\d+) \|.*\| (verified-primary|candidate|unresolved|corroborated) \|',line))}
p=KB/'source-register.md';check('Master register IDs and evidence states unchanged',registry_states(p.read_text())==registry_states(old(p)))

# Relative-link audit compares current failures with baseline failures; source-page web URLs aren't local files.
def failures(path,text,existing):
    bad=set();text=re.sub(r'```.*?```','',text,flags=re.S)
    for t in re.findall(r'\]\(([^)]+)\)',text):
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',t) or t.startswith(('#','//')):continue
        t=re.sub(r':\d+$','',t.split('#',1)[0]);t=unquote(t.strip('<>'))
        if ' "' in t:t=t.split(' "',1)[0]
        resolved=Path(os.path.normpath(str(path.parent/t)))
        # Absolute website-relative paths in captured source text retain their web origin.
        if t.startswith('/') and not t.startswith(str(ROOT)):continue
        try:key=str(resolved.relative_to(ROOT))
        except ValueError:continue
        if key not in existing:bad.add((str(path.relative_to(ROOT)),t))
    return bad
before_bad=set();after_bad=set()
for p in [p for p in tree if p.startswith('knowledge-base/') and p.endswith('.md')]:
    before_bad |= failures(ROOT/p,old(ROOT/p),set(tree))
current_set={str(p.relative_to(ROOT)) for p in ROOT.rglob('*') if '.git' not in p.parts and '.venv-research' not in p.parts and p.is_file()}
for p in KB.rglob('*.md'):after_bad |= failures(p,p.read_text(),current_set)
new_broken=sorted(after_bad-before_bad)
check('No new broken relative file links',not new_broken,{'new':new_broken,'baseline_existing_count':len(before_bad),'current_existing_count':len(after_bad)})
result=subprocess.run(['git','diff','--check',BASE,'--','.',':(exclude)knowledge-base/sources/FUND-203/source.html'],cwd=ROOT,capture_output=True,text=True)
check('Authored/derived diff whitespace check; byte-preserved raw HTML checked by hashes',result.returncode==0,result.stdout+result.stderr)
report={'baseline_commit':BASE,'result':'pass' if all(c['pass'] for c in checks) else 'needs_fix','checks':checks}
(AUDIT/'verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'result': report['result'], 'checks': len(checks), 'failed': [c for c in checks if not c['pass']]},ensure_ascii=False,indent=2))
sys.exit(0 if report['result']=='pass' else 1)
