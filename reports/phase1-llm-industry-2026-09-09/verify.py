"""Validate report structure, source identity and PDF text/link integrity."""
from pathlib import Path
import hashlib, json, re
from urllib.parse import unquote
from pypdf import PdfReader
import pdfplumber
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent.parent
pdf=HERE/'report.pdf'
reader=PdfReader(pdf)
manifest=json.loads((HERE/'data/source-manifest.json').read_text())
source_ids=[x['id'] for x in manifest]
labels=(HERE/'reference-labels.tex').read_text()
assert len(source_ids)==len(set(source_ids))
for i,sid in enumerate(source_ids,1):
 assert 'refnum@'+sid+r'\endcsname{'+str(i)+'}' in labels
hash_count=0
for source in manifest:
 for entry in source['files']:
  p=ROOT/entry['path']
  if source['id']=='EXT-QC': p=ROOT/'knowledge-base/reference/2026-llm-quant/quantaalpha-code/files'/entry['path']
  assert p.is_file(),str(p)
  assert hashlib.sha256(p.read_bytes()).hexdigest()==entry['sha256'],str(p)
  hash_count+=1
actual_urls=[]
for page in reader.pages:
 for ann in page.get('/Annots',[]):
  a=ann.get_object().get('/A',{})
  if a.get('/S')=='/URI': actual_urls.append(str(a.get('/URI')))
expected={unquote(s['url']) for s in manifest}
actual={unquote(s) for s in actual_urls}
assert expected==actual,(expected-actual,actual-expected)
text='\n'.join(page.extract_text() or '' for page in reader.pages)
for phrase in ['减少对易方达','4分','5分','用户要求','旧评分','已恢复','用户保存PDF','FUND-']:
 assert phrase not in text,phrase
assert '\ufffd' not in text
log=(HERE/'build/main.log').read_text()
for phrase in ['Overfull','Missing character','undefined references','undefined on input']:
 assert phrase not in log,phrase
cohort=json.loads((HERE/'data/cohort.json').read_text())
land=(HERE/'landscape.tex').read_text()
for company in cohort:
 assert f"{company['aum_cny_100m']:,.2f}" in land, company
coords=[]
with pdfplumber.open(pdf) as doc:
 for i,p in enumerate(doc.pages):
  chars=p.chars
  outside=[c for c in chars if c['x0'] < 0 or c['x1'] > p.width+0.5 or c['top'] < 0 or c['bottom'] > p.height+0.5]
  assert not outside,(i+1,outside[:3])
  coords.append({'physical_page':i+1,'characters':len(chars),'text_bbox':[round(min(c['x0'] for c in chars),2),round(min(c['top'] for c in chars),2),round(max(c['x1'] for c in chars),2),round(max(c['bottom'] for c in chars),2)]})
result={'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'physical_pages':len(reader.pages),'numbered_pages':len(reader.pages)-1,'source_entries':len(manifest),'hashed_files_verified':hash_count,'external_urls_verified':len(actual),'cohort_values_verified':len(cohort),'forbidden_process_phrases_absent':True,'latex_critical_warnings_absent':True,'page_text_bounds':coords,'visual_review':'See qa/review.md; this script does not assert visual correctness.'}
(HERE/'qa/checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='page_text_bounds'},ensure_ascii=False,indent=2))
