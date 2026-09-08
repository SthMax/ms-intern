"""Offline quality check of the installed reader; deliberately makes no requests."""
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'knowledge-base/audits/2026-09-07-extraction-quality'
SKILL = Path('/Users/sthmax/.codex/skills/wechat-article-to-md-skill')
spec = importlib.util.spec_from_file_location('reviewed_wechat', SKILL / 'scripts/wechat_article_pipeline.py')
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)


def deny_network(*args, **kwargs):
    raise AssertionError('Offline quality check must not make a network request')


module.requests.sessions.Session.request = deny_network
OUT.mkdir(parents=True, exist_ok=True)
fixture = '''<!doctype html><html><head><title>研究证据质量测试</title></head><body>
<div id="img-content"><h1 class="rich_media_title">研究证据质量测试</h1>
<span class="rich_media_meta rich_media_meta_text">曹雯璟</span>
<a id="js_name">示例基金公众号</a><em id="publish_time">2026-05-31</em>
<div id="js_content"><p>以下文章来源于中国基金报，作者曹雯璟</p>
<p>建议采纳率为91%，并非准确率；结果未经独立验证。</p>
<p>宜保留来源引用；未经同意不得向第三方提供数据。</p>
<table><tr><th>指标</th><th>数值</th></tr><tr><td>建议采纳率</td><td>91%</td></tr></table>
<img src="https://example.invalid/chart.png" alt="统计口径图">
<p>''' + ('长文完整性测试。' * 2500) + '''全文结束标记。</p>
</div></div><div id="js_pc_qr_code">网页导航</div></body></html>'''
(OUT / 'synthetic-fixture.html').write_text(fixture)
pipeline = module.WeChatArticlePipeline()
article = pipeline.extract_article(fixture, 'https://example.invalid/local-fixture')


class MissingImage:
    def register(self, source):
        return 'missing-image.png'


parser = module.HTMLToMarkdownParser(MissingImage())
parser.feed(article.content_html)
before = parser.get_markdown()
after, formatting = module.format_markdown(before, OUT)
(OUT / 'synthetic-before-cleanup.md').write_text(before)
(OUT / 'synthetic-after-cleanup.md').write_text(after)
checks = {
    'long_article_end_retained': '全文结束标记。' in after,
    'numeric_qualifier_retained': '91%，并非准确率' in after,
    'modal_and_negation_retained': '宜保留来源引用；未经同意不得' in after,
    'source_credit_retained': '以下文章来源于中国基金报' in after,
    'author_extracted_correctly': article.author == '曹雯璟',
    'publication_date_metadata_present': hasattr(article, 'published') or hasattr(article, 'published_at'),
    'missing_image_reference_retained': 'missing-image.png' in after,
    'save_html_is_unmodified_original': pipeline.build_clean_html(article) == fixture,
}
challenge = (ROOT / 'knowledge-base/sources/FUND-109/retrieval-response.html').read_text()
failed_article = pipeline.extract_article(challenge, 'https://example.invalid/saved-error-response')
result = {
    'network_used': False,
    'skill': str(SKILL),
    'upstream_revision': '41f1ed58a9c74e8c61ffbe8f3290c0d13e5ff759',
    'script_sha256': hashlib.sha256((SKILL / 'scripts/wechat_article_pipeline.py').read_bytes()).hexdigest(),
    'checks': checks,
    'returned_author': article.author,
    'formatting_summary': formatting,
    'saved_challenge_title': failed_article.title,
    'synthetic_input_characters': len(fixture),
    'synthetic_output_characters': len(after),
    'interpretation': 'Synthetic/offline conversion test only; not live WeChat retrieval or a corpus-wide analysis validation.',
}
(OUT / 'skill-test.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(result, ensure_ascii=False, indent=2))
