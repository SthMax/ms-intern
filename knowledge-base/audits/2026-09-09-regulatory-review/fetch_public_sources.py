"""Preserve official public review evidence; do not overwrite prior REG originals."""
from pathlib import Path
from urllib.request import Request, urlopen
from html.parser import HTMLParser
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
AUDIT = Path(__file__).resolve().parent
SOURCES = [
    ('REG-013', '中华人民共和国网络安全法（2025年修正）', 'https://www.cac.gov.cn/2025-12/29/c_1768735112911946.htm', 'NPC Standing Committee; CAC official reproduction', 'PRC law', '2025-10-28', '2026-01-01 amendment commencement', 'Articles 2, 20, 23, 27, 33, 39, 42'),
    ('REG-014', '中华人民共和国数据安全法', 'https://www.cac.gov.cn/2021-06/11/c_1624994566919140.htm', 'NPC Standing Committee; CAC official reproduction', 'PRC law', '2021-06-10', '2021-09-01', 'Articles 2–3, 21, 27, 29–32, 36, 55'),
    ('REG-015', '个人信息保护合规审计管理办法', 'https://www.cac.gov.cn/2025-02/14/c_1741233507681519.htm', 'CAC', 'Departmental rule; Order 18', '2025-02-12', '2025-05-01', 'Articles 2–6, 20; attached audit guidelines'),
    ('REG-016', '人工智能生成合成内容标识办法', 'https://www.cac.gov.cn/2025-03/14/c_1743654684782215.htm', 'CAC, MIIT, MPS, NRTA', 'Joint administrative normative document', '2025-03-07', '2025-09-01', 'Articles 2, 4–6, 9–12, 14'),
]
SUPPLEMENTAL = [
    ('cybersecurity-amendment', 'https://www.cac.gov.cn/2025-10/29/c_1763461514768457.htm'),
    ('csrc-it-status-text', 'https://www.csrc.gov.cn/csrc/c106256/c1653896/content.shtml'),
    ('csrc-network-security-status', 'https://neris.csrc.gov.cn/falvfagui/rdqsHeader/mainbody?navbarId=3&secFutrsLawId=7b2fd48915564f939041a34bf3555939'),
    ('amac-standard-notice', 'https://www.amac.org.cn/xwfb/xhyw/202604/t20260403_27458.html'),
    ('amac-standard-current', 'https://www.amac.org.cn/xwfb/xhyw/202604/P020260429638714694502.pdf'),
    ('amac-research-current', 'https://www.amac.org.cn/hyyj/sy/202604/P020260408624258724685.pdf'),
    ('eo14148-rescission', 'https://www.whitehouse.gov/presidential-actions/2025/01/initial-rescissions-of-harmful-executive-orders-and-actions/'),
    ('senate-ai-moratorium', 'https://www.commerce.senate.gov/press/dem/release/senate-strikes-ai-moratorium-from-budget-reconciliation-bill-in-overwhelming-99-1-vote-2025-7/'),
    ('algorithm-recommendation-rules', 'https://www.cac.gov.cn/2022-01/04/c_1642894606364259.htm'),
    ('deep-synthesis-rules', 'https://www.cac.gov.cn/2022-12/11/c_1672221949354811.htm'),
    ('hk-genai-guidelines', 'https://www.digitalpolicy.gov.hk/tc/our_work/data_governance/policies_standards/ethical_ai_framework/doc/HK_Generative_AI_Technical_and_Application_Guideline_tc.pdf'),
]

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__(); self.parts = []; self.skip = 0
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style', 'noscript'): self.skip += 1
        if tag in ('p', 'div', 'h1', 'h2', 'h3', 'br', 'li', 'tr'): self.parts.append('\n')
    def handle_endtag(self, tag):
        if tag in ('script', 'style', 'noscript'): self.skip = max(0, self.skip - 1)
        if tag in ('p', 'div', 'li', 'tr'): self.parts.append('\n')
    def handle_data(self, data):
        if not self.skip: self.parts.append(data)
    def text(self):
        return '\n\n'.join(line.strip() for line in ''.join(self.parts).splitlines() if line.strip())

def fetch(item, primary=False):
    key, title, url, *rest = item if primary else (item[0], item[0], item[1])
    dest = ROOT / 'knowledge-base' / 'sources' / key if primary else AUDIT / 'evidence' / key
    dest.mkdir(parents=True, exist_ok=True)
    meta = {'source_id':key, 'title':title, 'url':url, 'retrieved_at':datetime.now(timezone.utc).isoformat(), 'human_check_status':'pending'}
    try:
        with urlopen(Request(url, headers={'User-Agent':'Mozilla/5.0'}), timeout=35) as response:
            raw = response.read(); content_type = response.headers.get('Content-Type','')
            meta.update(http_status=response.status, final_url=response.url, content_type=content_type)
        ext = 'pdf' if raw.startswith(b'%PDF') else 'html'
        rawname = f'source.{ext}'; (dest/rawname).write_bytes(raw)
        meta.update(sha256=hashlib.sha256(raw).hexdigest(), byte_count=len(raw), raw_file=rawname)
        if ext == 'html':
            doc = raw.decode('utf-8', errors='replace')
            parser = TextExtractor(); parser.feed(doc); body = parser.text()
            extraction = 'Python HTMLParser; scripts/styles removed; full visible text with navigation retained'
            if primary and '【打印】【纠错】\n\n' in body:
                body = body.split('【打印】【纠错】\n\n', 1)[1].split('\n\n关闭\n\n', 1)[0]
                extraction = 'Python HTMLParser; full article after CAC print controls and before closing/footer; site navigation omitted; no translation'
        else:
            from pypdf import PdfReader
            reader = PdfReader(dest/rawname)
            body = '\n\n'.join(f'## PDF page {n}\n\n{page.extract_text() or ""}' for n,page in enumerate(reader.pages,1))
            meta['page_count'] = len(reader.pages); extraction = 'pypdf page-by-page; no OCR or translation'
        if primary:
            issuer, typ, published, effective, locator = rest
            meta.update(issuer=issuer, source_type=typ, published=published, effective=effective, locator=locator, evidence_state='verified-primary', archive_status='raw', verification_scope='Official text retrieved; relevant provisions and targeted status searches reviewed; institution-specific applicability and human approval remain pending')
        meta.update(text_file='original.md', extraction_method=extraction, extracted_characters=len(body))
        prefix=f'# {key} — 原始来源提取文本\n\n- 标题：{title}\n- 官方网址：{url}\n- 获取：{meta["retrieved_at"]}\n- 原件：[{rawname}]({rawname})\n- SHA-256：`{meta["sha256"]}`\n\n> 机械提取的原语言文本；可能含导航、换行及PDF阅读顺序差异。未翻译、未改写，以原件为准。\n\n---\n\n'
        (dest/'original.md').write_text(prefix+body+'\n')
        meta['extracted_text_sha256']=hashlib.sha256((dest/'original.md').read_bytes()).hexdigest()
    except Exception as exc:
        meta['retrieval_error']=f'{type(exc).__name__}: {exc}'
    (dest/'metadata.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
    return {'source_id':key, 'http_status':meta.get('http_status'), 'bytes':meta.get('byte_count'), 'error':meta.get('retrieval_error')}

if __name__ == '__main__':
    jobs=[(s,True) for s in SOURCES]+[(s,False) for s in SUPPLEMENTAL]
    with ThreadPoolExecutor(max_workers=4) as pool:
        results=list(pool.map(lambda args: fetch(*args),jobs))
    (AUDIT/'retrieval-results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(results,ensure_ascii=False,indent=2))
