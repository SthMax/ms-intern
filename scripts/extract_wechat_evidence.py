"""Use the installed WeChat converter on already saved HTML, without networking.

Keeps source bytes, attribution, date and missing-image references. This does
not fetch blocked pages or make a cleaned file into an original source.
"""
import argparse
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path
from urllib.parse import urljoin

from bs4 import BeautifulSoup


def convert(input_html, source_url, output, selector):
    data = input_html.read_bytes()
    soup = BeautifulSoup(data, 'html.parser')
    body = soup.select_one(selector)
    if body is None or len(body.get_text(strip=True)) < 50:
        raise ValueError('Substantive article container absent; refuse to archive a challenge or error as an article.')
    output.mkdir(parents=True, exist_ok=False)
    (output / 'raw-source.html').write_bytes(data)
    skill = Path.home() / '.codex/skills/wechat-article-to-md-skill/scripts/wechat_article_pipeline.py'
    spec = importlib.util.spec_from_file_location('wechat_evidence_converter', skill)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)

    def deny_network(*args, **kwargs):
        raise RuntimeError('This preservation step is strictly offline.')

    module.requests.sessions.Session.request = deny_network
    image_urls = []

    class KeepImageReference:
        def register(self, source):
            target = urljoin(source_url, source)
            image_urls.append(target)
            return target

    title_node = soup.select_one('#activity-name, .rich_media_title, h1')
    title = title_node.get_text(' ', strip=True) if title_node else (soup.title.get_text(strip=True) if soup.title else input_html.stem)
    account = soup.select_one('#js_name, .profile_nickname')
    authors = [n.get_text(' ', strip=True) for n in soup.select('#js_author_name, .rich_media_meta_text')
               if n.get_text(strip=True) and n.get_text(strip=True) != '原创']
    date = soup.select_one('#publish_time, time')
    provenance = list(dict.fromkeys(
        n.get_text(' ', strip=True) for n in soup.find_all(['p', 'em', 'span'])
        if len(n.get_text(' ', strip=True)) < 500
        and re.search(r'以下文章来源于|内容转载自|来源[:：]|作者[:：]', n.get_text(' ', strip=True))))
    # Preserve all visible article wording; only ignore executable/style content.
    for element in body.select('script, style, noscript'):
        element.decompose()
    parser = module.HTMLToMarkdownParser(KeepImageReference())
    parser.ignore_tags = {'script', 'style', 'noscript'}
    parser.feed(str(body))
    markdown = parser.get_markdown()
    markdown = module._fix_table_separators(module._fix_orphan_blockquotes(module._fix_orphan_list_markers(markdown)))
    normalize = lambda s: re.sub(r'[\s*`_]+', '', s)
    markdown_text = re.sub(r'\[([^\]]*)\]\([^)]+\)', r'\1', markdown)
    missing = []
    for element in body.find_all(['p', 'li', 'td', 'th', 'h1', 'h2', 'h3']):
        text = normalize(element.get_text('', strip=True))
        if text and text not in normalize(markdown_text):
            missing.append(element.get_text(' ', strip=True))
    metadata = {
        'source_url': source_url, 'input_file': str(input_html.resolve()),
        'title': title, 'account_as_displayed': account.get_text(' ', strip=True) if account else None,
        'author_strings_as_displayed': authors,
        'published_as_displayed': date.get_text(' ', strip=True) if date else None,
        'provenance_strings': provenance,
        'raw_sha256': hashlib.sha256(data).hexdigest(),
        'converter_sha256': hashlib.sha256(skill.read_bytes()).hexdigest(),
        'method': 'Offline use of installed WeChat HTML-to-Markdown parser; lossy noise cleaner and network downloader not invoked',
        'article_selector': selector, 'missing_paragraphs': missing,
        'images': [{'url': u, 'downloaded': False} for u in image_urls],
        'text_check': 'pass' if not missing else 'needs_review',
        'human_check_status': 'pending', 'network_used': False,
        'limits': 'Text check does not validate figure contents, table spans, article authenticity, or substantive claims. Remote image references are kept, not downloaded.',
    }
    header = (f'# {title}\n\n> 阅读副本；不是原始文件。来源语言和文字保留，未翻译。'
              '图片未下载，链接仍保留；请核对图片／表格及原始文件。\n\n'
              f'[原始HTML](raw-source.html) · [提取记录](metadata.json) · [来源网址]({source_url})\n\n---\n\n')
    (output / 'reading.md').write_text(header + markdown)
    (output / 'metadata.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'output': str(output), 'text_check': metadata['text_check'], 'missing_paragraphs': len(missing), 'images_not_downloaded': len(image_urls)}, ensure_ascii=False))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input_html', type=Path)
    parser.add_argument('--source-url', required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--selector', default='#js_content')
    args = parser.parse_args()
    convert(args.input_html, args.source_url, args.output, args.selector)
