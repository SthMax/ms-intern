# 原始来源恢复报告 / Browser and deeper-search recovery

2026-09-07. Follow-up checks are complete; **not every original is obtainable in this environment**. The distinctions below replace the initial audit's single “unverifiable” label for these eight cases.

## Results for all eight sources

| Source | Material | Current result | What was obtained / what remains | Saved evidence |
|---|---|---|---|---|
| FUND-093 | 嘉实 / FX168 | 官网替代来源已取得 | 原FX168链接仍失效；嘉实自有网站同题稿FUND-317可读并已存档。 | [original.md](../../sources/FUND-317/original.md) · [source.html](../../sources/FUND-317/source.html) · [recovery metadata](../../sources/FUND-093/recovery.json) |
| FUND-109 | 易方达 / 微信 | 仅转载可得，微信原文仍受限 | 浏览器安全策略在打开前拒绝；FUND-108新浪同题署名转载可读。易方达/腾讯站点定向检索未找到可访问同题原文。 | [original.md](../../sources/FUND-108/original.md) · [source.html](../../sources/FUND-108/source.html) · [recovery metadata](../../sources/FUND-109/recovery.json) |
| FUND-302 | 天弘公司介绍 | 浏览器核实，原文段落已保存 | 浏览器正确显示原官网页面。整页导出不支持，保存相关DOM段落和原语言文本；不称为完整页面副本。 | [browser-profile-fragment.html](../../sources/FUND-302/browser-profile-fragment.html) · [browser-recovered.md](../../sources/FUND-302/browser-recovered.md) · [recovery metadata](../../sources/FUND-302/recovery.json) |
| FUND-310 | 鹏华AI服务器招标 | 完整PDF仍未恢复 | 浏览器再次重定向首页；检索可见题名/封面/第6页规格片段，但没有取得35页原始PDF。 | [indexed-discovery.md](../../sources/FUND-310/indexed-discovery.md) · [recovery metadata](../../sources/FUND-310/recovery.json) |
| FUND-314 | 工银瑞信CIO专访 | 原语言正文已通过提取服务恢复 | 精确URL对应文章日期2026-05-27、五个主要部分均可读；浏览器与原始HTML访问失败，正文提取的时效/完整性没有独立保证。 | [extractor-recovered.md](../../sources/FUND-314/extractor-recovered.md) · [recovery metadata](../../sources/FUND-314/recovery.json) |
| FUND-315 | 工银瑞信数智化回顾 | 原语言正文已通过提取服务恢复 | 精确URL对应正文日期2026-03-26，署名来源中国金融电脑。新浪索引副本经下载和浏览器验证为“文章不存在”，已拒绝。 | [extractor-recovered.md](../../sources/FUND-315/extractor-recovered.md) · [retrieval-response.html](../../sources/FUND-315/alternatives/china-financial-computer/retrieval-response.html) · [retrieval-response.md](../../sources/FUND-315/alternatives/china-financial-computer/retrieval-response.md) · [recovery metadata](../../sources/FUND-315/recovery.json) |
| FUND-356 | 中欧 / 微信转载链 | 原报道发布者全文已取得 | 下载中国基金报2026-05-31 19:24原刊文章，署名曹雯璟；微信转载包装页未访问，不宣称两页逐字一致。 | [source.html](../../sources/FUND-356/alternatives/china-fund-news/source.html) · [original.md](../../sources/FUND-356/alternatives/china-fund-news/original.md) · [metadata.json](../../sources/FUND-356/alternatives/china-fund-news/metadata.json) · [recovery metadata](../../sources/FUND-356/recovery.json) |
| FUND-359 | 华泰柏瑞 / 微信原始链 | 仅转载可得，微信原文仍受限 | FUND-358新浪全文可读且署名中国证券报-中证网；精确题名/发行者检索未取得可访问首发正文。 | [original.md](../../sources/FUND-358/original.md) · [source.html](../../sources/FUND-358/source.html) · [recovery metadata](../../sources/FUND-359/recovery.json) |

## What “recovered” means here

- **Tianhong:** correct official page opened in internal browser; a verbatim relevant HTML paragraph is saved. The browser’s whole-page export command is unsupported. Direct HTTP requests still produce a challenge. This is a verified source excerpt, not a full offline webpage.
- **ICBC articles:** exact-URL original-language text recovered from Exa. The service did not provide underlying publisher bytes or establish whether its content was live or cached. The retrieved text is preserved without translation. It is not relabelled as a downloaded original HTML file.
- **China Europe:** the China Fund News publisher’s full HTML and Chinese body are downloaded. The title, byline, 2026-05-31 19:24 date, speech topic, 100+Skill/60%/50% paragraphs and conclusion were located. This is reporter-authored source material, not an independent company implementation record or validated performance test.
- **Harvest:** the missing FX168 record is covered by already archived FUND-317, the fund company’s own titled event account. The missing FX168 bytes were not recovered, and exact text equivalence is not asserted.
- **E Fund / Huatai-PineBridge:** the existing Sina publications remain accessible, attributed mirrors. This pass did not recover the inaccessible upstream WeChat originals.
- **Penghua:** exact-title/URL searches still expose indexed document excerpts, but every attempted full-document route returns a homepage, script shell or retrieval error. No35-page PDF was fabricated from snippets. The procurement lead remains unverified at document level.

## Internal-browser policy restriction

The internal browser rejected FUND-109’s WeChat URL under its site-safety policy **before navigation**. No permission prompt or automatic approval review was attempted. Its rejection explicitly prohibited indirect execution, alternate browsers or other workarounds to that blocked page. None were attempted. The remaining WeChat URLs were not retried as same-site workarounds; instead, independently accessible publisher pages and attributed reposts were investigated.

Ordinary browser access succeeded for Tianhong, confirmed Penghua’s redirect, and confirmed the indexed Sina magazine copy is gone. The prior Fintech in China browser connection failure remains recorded. An extraction service recovered the two Fintech texts without asserting successful browser access.

## Search trail

Exact titles and URLs were searched with built-in web search and Exa, including targeted domains for EFund/Tencent, China Fund News, China Securities Journal/Huatai-PineBridge, Penghua and China Financial Computer. Searches on magazine/fund sites also returned unrelated years or generic product pages; these were rejected as substitutes for the requested publication.

- [Initial exact-title queries](title-search-results.txt)
- [Original-publisher queries](original-publisher-search-results.txt)
- [E Fund official-domain results](efund-official-search-results.json)
- [Huatai-PineBridge exact-title results](huatai-search-results.json)
- [Penghua deeper-search results](penghua-search-results.json)
- [Unmodified extraction-service response](fintech-extraction-response.json)
- [Machine-readable eight-source results](recovery-results.json)
- [Final checks](validation.json)

## Repository changes

| Area | Change |
|---|---|
| Eight original source folders | Added recovery records with exact methods, limitations, alternative URLs and file checksums |
| FUND-302 | Saved original browser DOM paragraph and readable Chinese excerpt |
| FUND-314 / FUND-315 | Saved exact-URL Chinese extractor text; preserved the tool response |
| FUND-356 | Added separately identified original-publisher HTML, Chinese extraction and metadata |
| FUND-315 alternative | Preserved rejected “article does not exist” response; not represented as original |
| FUND-310 | Saved indexed-discovery record with explicit missing-PDF limitation |
| Master register / source archive index | Linked current recovery status while retaining historical evidence-state classifications |
| Company notes referencing these IDs | Added current recovery links and explicit notices for affected dossiers |
| Tianhong AUM paragraph and company index | Recorded browser-verified2026-03-31 total/public/non-money AUM separately from Q2 ranking |
| Prior language audit | Retained as historical snapshot; linked this follow-up |

Human review, regulatory-status checks, and company outcome validation remain pending. No outreach, publication or Git commit was performed.
