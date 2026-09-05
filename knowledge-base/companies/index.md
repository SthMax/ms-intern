# Onshore Fund Manager AI/LLM Landscape

**Phase 1 — Weeks 1–2.** See [the final plan](../../PROJECT_PLAN.md) and
[Week 2 execution plan](../../weekly/week-02-plan.md).
Status at 6 September: no companies or initiatives verified.

## Inclusion and counting

Include an entity in the verified set when a public primary source identifies a
concrete AI/LLM initiative and its identity as an onshore mutual fund manager is
supported. General statements about AI remain candidates.

Count distinct legal fund-management entities, not products, subsidiaries outside
the agreed universe, or repeated initiative rows. “Top tier” and the company-count
threshold are not defined in the supplied brief; record coverage and the working
selection method transparently.

## Company and asset-size database

| Company ID | Company / Chinese legal name | Entity eligibility source | AUM value and unit | AUM metric / entity scope | As-of date | Size source ID | Asset-size category / basis | Evidence state |
|---|---|---|---|---|---|---|---|---|

Use stable IDs such as `COMP-001`. Record both currency and magnitude. Size
categories/rankings need an explicit, consistent basis; retain raw size metrics
when dates or definitions are not comparable. Do not mix group AUM, total managed
assets, public-fund AUM, and non-money-market AUM in an unqualified ranking.

## Initiative database

| Initiative ID | Company ID | AI / LLM type | Use case | Function | Stage | Technology / model | Technology partner | Disclosed outcome | Disclosure date | Primary source IDs | Evidence state / note |
|---|---|---|---|---|---|---|---|---|---|---|---|

Required function categories are `research`, `trading`, `risk`, `marketing`,
and `compliance`. Supplemental tags may include `client service`, `operations`,
`technology platform`, and `other`. Multi-tag initiatives where justified.

Stage values: `announcement`, `research`, `proof of concept`, `pilot`,
`limited deployment`, `production`, `unclear`.

Record the AI/LLM distinction from the disclosure. Use “not disclosed” for absent
partner, model, deployment, or outcome details. Observed/reported outcomes
support the full project's secondary objective; an undisclosed outcome does not
by itself exclude an otherwise qualifying Phase 1 company.

## Candidate queue

| Candidate company | Discovery source | Eligibility / evidence gap | Next verification action | Status |
|---|---|---|---|---|

## Coverage tracker

| Metric | Requirement / basis | Current |
|---|---|---|
| Distinct verified companies | Minimum omitted in final brief; await number | 0 |
| Candidate companies | Discovery queue; excluded from verified count | 0 |
| Companies with sourced AUM | Record coverage and any gaps | 0 |
| Verified initiatives | May exceed distinct company count | 0 |
| Human-reviewed company evidence | Actual completed checks | 0 |

## Interpretation guardrails

- Preserve source attribution for vendor statements and quantitative benefits.
- Partnership does not establish production deployment.
- Named models, partners, deployment topology, and outcomes require explicit
  support.
- Lack of disclosure does not establish lack of adoption.
- Store detailed evidence notes here and link them through
  [the source register](../source-register.md).
