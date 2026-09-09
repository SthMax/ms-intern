# Report verification — 2026-09-09

Status: authored report and artifact checks complete; mentor/independent human approval remains pending.

## Project scope and evidence review

- Re-read the full mentor-confirmed `PROJECT_PLAN.md` before authoring. This artifact delivers the Phase 1 landscape and privacy/interpretability/outsourcing synthesis. It does not claim the Phase 2 deployment/model comparison or Phase 3 TCO/ROI work is complete.
- Preserved the pre-report research in `e51e4c9b93bd03c17f869c2f10027fa8061f9eae`. Compared the final working changes with that baseline: report files are new; the only existing authored file changed is the Week 2 execution plan. Knowledge-base raw articles, PDFs, code snapshots and the confirmed project plan remain unchanged.
- Reconciled source records (125), source states (88/35/2), reading roles (112/9/4), the 20-company AUM cohort plus Dacheng supplement, and mixed AI/LLM primary evidence counts. No source count or workflow count is presented as a production deployment count.
- Checked the uniform AUM definition and 20 values against the frozen cohort. Bar labels round only for display; source data and company table preserve two decimals.
- Kept E Fund MENTOR explicitly dated 2025. Kept 2026 research tasks, Man Group institutional research and QuantaAlpha external code separate from domestic production deployment claims.
- Checked Southern's reported 40% daily-operation time reduction and Penghua's 1,266 documents / approximately 60,000 checks / 989 suggestions / 91% adoption against originals. Adoption is not accuracy; platform time savings are not isolated LLM gains or MSIM ROI.
- Removed Danlan from the concise ICBC partner row because the row's selected source directly supports Hundsun Juyuan, ICBC Technology and Zhipu AI; additional historical partner evidence would need its own citation.
- Preserved the regulatory review's legal-force and applicability boundaries, including conditional GenAI scope, important-system outsourcing, AMAC group-standard status and the 2026 Fed guidance scope. The report uses the archived official AMAC material and earlier same-day status review; its announcement timed out during the additional report-authoring access attempt. This is not an internal compliance approval.

## Artifact checks

- Built using the LaTeX compile skill with TeX Live 2026 / XeLaTeX / latexmk, then verified the standalone `build.sh` path.
- Final output: **24 physical pages**, including cover; **23 numbered pages**, **9 figures**, **15 numbered tables**, **49 source entries**.
- All 49 external source URLs embedded in the PDF match the report source manifest. Referenced local originals and all 30 selected QuantaAlpha code files match recorded SHA-256 hashes.
- All source IDs resolve; no unresolved references, missing-glyph or overfull-box warnings in the final LaTeX log. Cover page anchors disabled to prevent duplicate page-1 destinations.
- Replaced Fandol with explicitly embedded macOS Songti/Heiti fonts after finding the initial output failed CJK rendering/extraction with the available reader stack. Final Chinese text extracts correctly and is searchable.
- Rendered all pages with Poppler and visually reviewed them. Fixed omitted AUM y-axis labels and title-bar contrast. The bundled Poppler renderer displayed inconsistent header/footers on some pages, so also rendered and inspected the entire final PDF with independent PDFium; headers, page numbers, body text and chart labels are present. Text coordinates were checked independently with pdfplumber.
- Inspected every final page, with detailed checks of the dense company table, AUM chart, workflow figures, governance tables and reference pages. No clipping, collisions, missing labels or incomplete rows found in the final PDFium review.
- Latest PDF SHA-256 and machine checks are in `checks.json`. Rendered page PNGs are local QA intermediates ignored by git.

No model/API call, factor generation, backtest, local model deployment, internal outreach or legal approval was performed as part of report authoring.
