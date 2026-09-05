# Knowledge Base

This folder holds research findings and their evidence. Project scope is
controlled by [the final project plan](../PROJECT_PLAN.md). Execution is tracked
in [the Week 2 plan](../weekly/week-02-plan.md).

## Phase ownership

| Folder | Phase | Purpose |
|---|---|---|
| companies/ | 1 — Weeks 1–2 | Onshore AI/LLM disclosures, size categories, use cases, partners, and reported outcomes |
| regulation/ | 1 — Weeks 1–2; maintained later | Public regulatory evidence and model risk management questions |
| models/ | 2 — Weeks 3–5 | 5–8-model survey, reusable evaluation framework, one-model GPU proof of concept |
| infrastructure/ | 2 and 3 | Phase 2 reference architecture; Phase 3 three-year on-premise/API TCO |
| pilots/ | 3 — Weeks 6–8 | 3–5 candidates and roadmap with 2–5 concrete proposals |
| templates/ | All | Evidence recording and review |

## Evidence states

- **candidate:** discovered but not checked against the original source.
- **verified-primary:** original primary material was opened and the specific
  claim, identity, date, and location were checked.
- **corroborated:** verified-primary evidence with an additional independent
  supporting source.
- **unresolved:** ambiguous, inaccessible, superseded, or conflicting evidence
  prevents the proposed claim from being verified.

Only verified-primary and corroborated claims may appear as facts in the main
presentation. A primary vendor source supports what the vendor reported; it does
not automatically establish independently measured customer outcomes.

Record who checked the source. Agent inspection and user/manual verification are
separate: use a human-check status and date without implying human review
occurred merely because a link is available.

## Required citation fields

Each source in [source-register.md](source-register.md) needs:

- Stable source ID, exact title, issuer, and source/instrument type.
- Publication date; for rules, effective date and amendment/current status.
- Direct primary URL and access date.
- Relevant article, section, page, or timestamp.
- Narrow supported claim and limitations.
- Evidence state and a link to the detailed evidence note.
- In that note, reviewer/method and human-check status.

Use “not stated” or “not yet verified” for absent or unresolved dates. Never infer
an effective date or legal force from the publication date or document title.

## Workflow

1. Log a candidate and its discovery source.
2. Open the original source and check the exact claim and its context.
3. Save an evidence note using [the template](templates/evidence-note.md), then
   update the source register and relevant index.
4. Record findings as research proceeds, so slides never become the only record.
5. Keep source wording, interpretation, and open applicability questions explicit.
6. Before presentation release, follow every material claim's links to the
   original passage; record reviewer and result.
7. Update counts and report unresolved/manual-review items honestly.

The overview supplied in the final project plan is project context, not a
verified industry research finding. Source its claims before reusing them as
evidence.

## Citation discipline

- Prefer authoritative Chinese originals; translations are aids.
- Search snippets and reposts may support discovery, not legal conclusions.
- Distinguish law/rules, regulator guidance, drafts, industry material, vendor
  claims, and internal requirements.
- Verify instrument status and applicability separately.
- Keep quotations short and exact; retain section/page pointers for manual review.
- Record AUM unit, metric, entity scope, date, and source. Compare compatible
  measurements and label gaps.
- Distinguish announcement, pilot, and production use.
- Absence of a disclosure does not establish absence of adoption.

## Data handling

Use public information in this repository. Do not place confidential internal,
client, personal, portfolio/position, or licensed research data here without the
user's explicit direction and an authorized storage basis. Track internal-policy
questions without copying restricted text. COD is MSIM's infrastructure; MRM
means model risk management. Those clarifications do not supply architecture
specifications or internal policy content.
