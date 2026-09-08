"""Archive registered public sources without translating or rewriting their text.

Run with the bundled Python (pypdf), curl and defuddle. Downloaded bytes are
authoritative; original.md is a convenience extraction, not a layout replica.
"""
import argparse
import concurrent.futures
import datetime
import hashlib
import html.parser
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "knowledge-base/sources"


def sources():
    result = []
    for line in (ROOT / "knowledge-base/source-register.md").read_text().splitlines():
        if not re.match(r"\| (?:REG|FUND)-\d+ \|", line):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        assert len(cells) == 13, (cells[0], len(cells))
        urls = re.findall(r"\]\((https?://[^)]+)\)", cells[7])
        assert urls, cells[0]
        result.append(dict(source_id=cells[0], issuer=cells[2], title=cells[3],
                           source_type=cells[4], published=cells[5], url=urls[0],
                           locator=cells[9], evidence_state=cells[11], caveat=cells[12]))
    assert len({s['source_id'] for s in result}) == len(result)
    return result


class VisibleText(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.skip = 0
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style', 'noscript'):
            self.skip += 1

    def handle_endtag(self, tag):
        if tag in ('script', 'style', 'noscript'):
            self.skip = max(0, self.skip - 1)
        elif tag in ('p', 'div', 'br', 'li', 'tr', 'h1', 'h2', 'h3'):
            self.parts.append('\n')

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)


def archive(item, force=False):
    dest = ARCHIVE / item['source_id']
    dest.mkdir(parents=True, exist_ok=True)
    meta_path = dest / 'metadata.json'
    if meta_path.exists():
        existing = json.loads(meta_path.read_text())
        # An archived original is immutable. --force only retries failed records.
        if not force or existing.get('archive_status') == 'raw':
            return existing
    meta = dict(item, retrieved_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                human_check_status='pending', archive_status='not_verifiable',
                verification_scope='Retrieval and original-language preservation only; no new legal or outcome validation.')
    response = dest / 'response.bin'
    proc = subprocess.run(['curl', '-L', '--compressed', '--max-time', '50', '--connect-timeout', '15',
                           '--max-filesize', '60000000', '--silent', '--show-error',
                           '-A', 'Mozilla/5.0', '-o', str(response),
                           '-w', '%{json}', item['url']], capture_output=True, text=True)
    try:
        info = json.loads(proc.stdout)
    except json.JSONDecodeError:
        info = {}
    meta.update(http_status=info.get('http_code'), final_url=info.get('url_effective'),
                content_type=info.get('content_type'), curl_exit=proc.returncode)
    content = ''
    if proc.returncode or info.get('http_code', 0) >= 400 or not response.exists():
        meta['failure'] = proc.stderr.strip() or f"HTTP {info.get('http_code')}"
    else:
        data = response.read_bytes()
        meta.update(sha256=hashlib.sha256(data).hexdigest(), byte_count=len(data))
        if data.startswith(b'%PDF-'):
            raw = dest / 'source.pdf'
            response.replace(raw)
            meta['raw_file'] = raw.name
            try:
                from pypdf import PdfReader
                reader = PdfReader(raw)
                pages = [p.extract_text() or '' for p in reader.pages]
                meta['page_count'] = len(pages)
                meta['empty_text_pages'] = [i+1 for i, p in enumerate(pages) if len(p.strip()) < 30]
                content = '\n\n'.join(f'## PDF page {i+1}\n\n{p}' for i, p in enumerate(pages))
                meta['extraction_method'] = 'pypdf page-by-page; no OCR or translation'
                meta['archive_status'] = 'raw'
                if meta['empty_text_pages']:
                    meta['extraction_limit'] = 'Some pages have little/no text; inspect original PDF for images, charts, tables and scans.'
            except Exception as exc:
                meta.update(archive_status='raw', extraction_limit=str(exc))
        else:
            raw = dest / 'source.html'
            response.replace(raw)
            meta['raw_file'] = raw.name
            ct = info.get('content_type') or ''
            charset = re.search(r'charset\s*=\s*[\"\x27]?([a-zA-Z0-9_-]+)', ct)
            if not charset:
                charset = re.search(r'charset\s*=\s*[\"\x27]?([a-zA-Z0-9_-]+)', data[:20000].decode('ascii', errors='ignore'))
            encoding = charset.group(1).lower() if charset else 'utf-8'
            if encoding in ('gb2312', 'gbk'):
                encoding = 'gb18030'
            try:
                decoded = data.decode(encoding)
            except (UnicodeDecodeError, LookupError):
                try:
                    decoded = data.decode('utf-8')
                    encoding = 'utf-8'
                except UnicodeDecodeError:
                    decoded = data.decode('gb18030', errors='replace')
                    encoding = 'gb18030 with replacement'
            meta['decoded_encoding'] = encoding
            # Defuddle reads UTF-8 files; raw bytes above remain untouched.
            normalized = dest / '.extraction-input.html'
            normalized.write_text(decoded)
            extraction = subprocess.run(['defuddle', 'parse', str(normalized), '--md'],
                                        capture_output=True, text=True, timeout=40)
            normalized.unlink()
            content = extraction.stdout.strip() if extraction.returncode == 0 else ''
            meta['extraction_method'] = 'Defuddle Markdown from archived HTML; no translation'
            parser = VisibleText()
            parser.feed(decoded)
            visible = re.sub(r'\n[ \t]*\n+', '\n\n', ''.join(parser.parts)).strip()
            (dest / 'full-visible-text.txt').write_text(visible + '\n')
            meta['full_visible_text_file'] = 'full-visible-text.txt'
            if len(content) < 150 and len(visible) > len(content):
                content = visible
                meta['extraction_method'] = 'HTML visible-text fallback, including possible navigation; no translation'
            blocked = re.search(r'Access Denied|Just a moment|验证码|环境异常|安全验证|verify you are human|页面不存在|网页不存在|页面无法访问|该内容已被发布者删除|该内容已删除|var arg1=', content[:8000], re.I)
            if len(content.strip()) < 150 or blocked:
                meta['failure'] = ('Challenge/error text: ' + blocked.group(0)) if blocked else 'No substantive article text in response; may require browser rendering.'
            else:
                meta['archive_status'] = 'raw'
    if content:
        chinese = len(re.findall(r'[\u4e00-\u9fff]', content))
        meta['text_language'] = 'Chinese' if chinese > 100 else 'English or other (check source)'
        meta['extracted_characters'] = len(content)
        if meta['archive_status'] == 'raw':
            intro = (f"# {item['source_id']} — 原文 / Original-language source\n\n"
                     f"- 登记标题 / Registered title: {item['title']}\n"
                     f"- 原始网址 / Original URL: {item['url']}\n"
                     f"- 获取时间 / Retrieved: {meta['retrieved_at']}\n"
                     f"- 原始文件 / Downloaded bytes: [{meta['raw_file']}]({meta['raw_file']})\n"
                     f"- 定位 / Cited locator: {item['locator']}\n"
                     f"- SHA-256: `{meta['sha256']}`\n\n"
                     "> 下文为机械提取的来源原语言文本，未翻译、未改写。版式、图表、脚注及提取缺失以原始文件为准。网页提取可能包含导航或省略动态内容。\n"
                     "> This is an extraction, not a new translation or an assurance that every prior research claim is verified. Original publisher/reprint status is unchanged; human review remains pending.\n\n---\n\n")
            (dest / 'original.md').write_text(intro + content + '\n')
            meta['text_file'] = 'original.md'
        else:
            (dest / 'retrieval-response.txt').write_text(content)
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + '\n')
    return meta


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ids', nargs='*')
    parser.add_argument('--force', action='store_true', help='Retry failed records; never overwrite archived originals')
    args = parser.parse_args()
    selected = [s for s in sources() if not args.ids or s['source_id'] in args.ids]
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        futures = {pool.submit(archive, s, args.force): s for s in selected}
        for future in concurrent.futures.as_completed(futures):
            item = futures[future]
            try:
                result = future.result()
                print(item['source_id'], result['archive_status'], result.get('failure', ''), flush=True)
            except Exception as exc:
                print(item['source_id'], 'ERROR', str(exc), flush=True)


if __name__ == '__main__':
    main()
