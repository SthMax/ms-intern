# Financial NLP Benchmark Plan

## Decision goal

Determine whether candidate models are sufficiently accurate, reproducible,
controllable, and economical for shortlisted workflows—not which model wins a
generic leaderboard.

## Candidate task families

| Task | Example evaluation unit | Primary metrics | Risk-oriented checks |
|---|---|---|---|
| Financial named-entity recognition | Chinese/English sentence or document | Entity precision, recall, F1; exact and partial match | Entity type confusion, numeric/date errors |
| Financial question answering | Question plus approved source context | Exact match/F1 or rubric score; citation accuracy | Unsupported answer rate, abstention quality |
| Multi-document summarization | Small filing/report/news packet | Coverage, faithfulness, citation precision/recall, human utility | Contradictions, omitted caveats, temporal errors |

## Experimental controls

- Freeze dataset version, model artifact/version, quantization, inference engine,
  prompt, decoding parameters, retrieval settings, and hardware.
- Separate public/synthetic development data from a held-out evaluation set.
- Use double review or adjudication for subjective labels.
- Report confidence intervals where the sample supports them.
- Measure Chinese and English performance separately.
- Test refusal/abstention and prompt-injection behavior, not only helpfulness.
- Record latency, throughput, peak memory, input/output length, and energy where
  measurement is available.

## Candidate model screening fields

| Model/version | License verified | Chinese finance fit | Context length verified | Deployment format | Hardware tested | Quality results | Operational/security notes | Source IDs |
|---|---|---|---|---|---|---|---|---|

Model names and specifications will be added only after checking current official
model cards, licenses, and deployment documentation.

## Dataset acceptance checks

- License and commercial-use terms verified.
- No confidential, client, personal, licensed-research, or future-leaking content.
- Time split prevents look-ahead where relevant.
- Annotation protocol and error analysis documented.
- Dataset represents the intended Chinese financial language and document types.

