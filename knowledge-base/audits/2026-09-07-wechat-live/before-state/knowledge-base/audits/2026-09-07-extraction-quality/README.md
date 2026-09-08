# Extraction quality, analysis impact and WeChat skill evaluation

2026-09-07. This report addresses the user's concern about poor raw-page quality and request to install/test a WeChat article skill.

## Does poor extraction hurt the analysis?

**Yes, when information is omitted, reordered or misattributed.** A page full of navigation, CSS or scripts can still be a faithful raw byte capture, but it is not a good reading copy. A tidy Markdown file can be worse evidence if it silently removes source credits, figures, qualifiers or dates. A checksum establishes byte integrity, not semantic completeness or source authenticity.

The prior “93 raw sources / hashes passed” finding was an archival integrity result, not a claim that all93 extractions were publication-ready or that every research conclusion was revalidated. Human source review and broader legal-status review remain pending.

| Issue observed in this project | Potential analytical effect | Current treatment |
|---|---|---|
| English source summaries without saved originals | Hard to check legal modality, scope and attribution | Original files preserved where obtained; regulatory notes now contain source-language excerpts |
| EFund CIO speech/Tencent customer listing omitted by generic extraction | Understates or loses adoption evidence | Earlier full-text extraction repaired; EFund speech now has a cleaner reading copy |
| REG-008 footnote numbering shifted and body duplicated | Misreads which scope exclusion a footnote qualifies | Regulatory note explicitly preserves actual footnote content and labels extraction numbering; human review still required |
| Figures or scanned pages with little extracted text | Misses architecture/control evidence or measurement definitions | Original PDFs retained; text-only extraction is not sufficient for figure-based claims |
| Live AUM profile changed since previous observation | Mixes dates or backdates new figures | Current/historical observations separated; common-date ranking unchanged |
| Repost attribution removed by cleaning | Mistakes a repost for independent primary disclosure | Provenance retained separately and in article body; candidate status not automatically upgraded |
| Missing images silently removed | Conceals evidence gaps | Reading-copy metadata lists every image; references are kept; reachable saved-page images downloaded |

### Narrow claim checks performed now

These checks confirm wording in saved source material, not independent measurement or whole-project validity:

- FUND-102, original PDF page8:100多项AIGC应用 wording present; not100 independent models/deployments.
- FUND-200, original PDF page8:40% reduction refers to日均操作耗时; not general portfolio performance or isolated LLM ROI.
- FUND-308, original PDF page6:91% is建议采纳率; not accuracy.
- FUND-103:EFundGPT/LoRA wording retained, including“也许”in the future staffing statement; not evidence of realized headcount reduction.

[Machine-readable spot checks](claim-spot-checks.json). These spot checks did not identify a reversal of the selected claims, but do not establish that the entire analysis is unaffected.

## Installed skill and comparison

Installed **wechat-article-to-md-skill** from [Yui-cx/wechat-article-to-md-skill](https://github.com/Yui-cx/wechat-article-to-md-skill), pinned to revision `41f1ed58a9c74e8c61ffbe8f3290c0d13e5ff759`. Installed path: `/Users/sthmax/.codex/skills/wechat-article-to-md-skill`. The installed script and SKILL.md matched the reviewed bytes. Codex can discover it on the user's next turn.

| Candidate inspected | Evidence from code/docs | Selection |
|---|---|---|
| Yui-cx/wechat-article-to-md-skill | Standalone Python pipeline; complete article conversion; image downloads; table/list handling; optional cleaned HTML | Best fit among these inspected candidates, subject to preservation safeguards; not a proven universal performance winner |
| cathyzhang0905/wechat-article-reader | Code truncates text to15,000 characters and images to5; docs describe a different8,000-character limit; fallback can return raw HTML prefix | Rejected for evidence preservation |
| ppx123-web/claude-config/wechat-article-fetcher | Interest-ranked digest workflow with tailored AI topics, filtering and summaries | Poor fit for faithful source archives |

### Installed upstream reader: offline test results

No network requests were made by these tests. The synthetic fixture is labelled test data and is not a research source.

| Test | Upstream result |
|---|---|
| Long-text ending and numeric qualifiers | Retained |
| 宜 / 不得 wording | Retained |
| Original-source attribution line | Removed by noise cleaning |
| Author separate from account | Failed: account name returned as author |
| Publication date in structured metadata | Absent |
| Missing image reference | Removed |
| `--save-html` equals untouched original response | False: it saves reconstructed/cleaned HTML |

Therefore, stock output must **not** replace the raw archive or automatically qualify as verified evidence. [Test results](skill-test.json).

## Local preservation step and actual reading copies

Added [extract_wechat_evidence.py](../../../scripts/extract_wechat_evidence.py). It uses the installed skill's converter only on saved HTML, with all networking disabled. It preserves input bytes; separates author/account/date metadata; retains provenance and missing-image links; skips the lossy noise cleaner; and compares paragraph text before/after conversion. Failed article-container checks reject error pages. Raw archives are not overwritten.

[Preservation fixture checks](preservation-test.json) passed for unchanged bytes, attribution, separate author/account, date, image references, long-text ending, qualifiers and no-network operation. This is not a visual or substantive validation of every table/image.

| Actual saved source | Cleaner reading copy | Saved images |
|---|---|---:|
| FUND-103 EFund CIO speech, original SZU host | [reading.md](../../sources/FUND-103/reading-copy/reading.md) | 1/1 |
| FUND-108 EFund ima article, Sina mirror | [reading.md](../../sources/FUND-108/reading-copy/reading.md) | 16/16 |
| FUND-355 China Europe article, Sina mirror | [reading.md](../../sources/FUND-355/reading-copy/reading.md) | 5/5 |
| FUND-358 Huatai-PineBridge article, Sina mirror | [reading.md](../../sources/FUND-358/reading-copy/reading.md) | 1/1 |

All four passed the mechanical paragraph-text check. The23 image files came from the independently accessible Sina/SZU publications, not from newly fetched WeChat articles. Article text and images remain publisher content, not analysis instructions. These new reading copies do not change repost provenance.

Example local use:

```bash
.venv-research/bin/python scripts/extract_wechat_evidence.py saved-article.html \
  --source-url 'ORIGINAL_SOURCE_URL' --output output/new-article
```

Dependencies are in the ignored project `.venv-research/`; the upstream skill remains unchanged. The offline wrapper uses Beautiful Soup plus the installed converter. It is for readable evidence copies, not access-policy bypass.

## Live WeChat retrieval status

**No newly blocked WeChat article was fetched with this skill.** A previous internal-browser safety rejection explicitly prohibited using indirect execution or other tools to achieve that blocked access. Installing a reader does not override that restriction. Tests used saved files and a synthetic fixture, with networking disabled. The existing WeChat challenge response still contains no article, and was not converted into false evidence.

The [source-recovery report](../2026-09-07-source-recovery/README.md) remains the record of live access limitations. The distinction is **agent access blocked / original not inspected**, not an assertion that WeChat articles are intrinsically unverifiable. A legitimately saved article supplied locally can be processed with the preservation step.

## Working evidence rule

Before a headline claim is used in the presentation, locate its exact source passage, inspect relevant tables/images, check the date and attribution, and distinguish reported metrics from measured effects. Clean reading copies assist this review; they are not its substitute. Do not infer an all-clear for the remaining corpus from file hashes or these sampled checks.
