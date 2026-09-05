# Model Survey and Financial NLP Evaluation Plan

**Phase 2 — Weeks 3–5.** Derived from [the final project plan](../../PROJECT_PLAN.md).
Status: evaluation template; no models have been surveyed or tested.

## Required outputs

- Survey and compare **5–8 open-source LLMs** on language proficiency, model size,
  inference speed, fine-tuning requirements, and community support.
- Maintain a reusable evaluation framework for financial named-entity recognition,
  financial question answering, and multi-document summarization.
- Select one model for the [local GPU proof of concept](poc-plan.md), which must
  measure inference latency and run a sample financial NLP task.
- Feed measured resource requirements into the
  [reference architecture](../infrastructure/reference-architecture.md) and
  Phase 3 [TCO comparison](../infrastructure/tco-model.md).

The 5–8-model requirement is a survey/comparison requirement. Record which models
were actually benchmarked locally. A one-model proof of concept does not imply
that all surveyed models were run on the same hardware.

## Model survey

| Model/version | Official model/license source IDs | Language proficiency evidence | Size/precision | Inference speed and test conditions | Fine-tuning requirements | Community/support evidence | Local test status | Notes |
|---|---|---|---|---|---|---|---|---|

For each row:

- Verify license and commercial-use terms; distinguish the brief's “open-source”
  wording from the actual license classification of a candidate.
- Record languages assessed. Chinese and English are a proposed evaluation split
  for this desk; the brief does not specify languages or minimum proficiency.
- Record speed units, hardware, quantization, context/output length, concurrency,
  and whether a number is published or locally measured.
- Describe fine-tuning options and data/compute needs without assuming fine-tuning
  is necessary.
- Record dated support evidence such as release activity, maintained deployment
  integrations, documentation, and issue handling.
- Capture context limits, memory requirements, artifact versions, and sources
  where relevant to the architecture.

## Financial NLP evaluation

| Task | Evaluation unit | Proposed quality measures | Error analysis |
|---|---|---|---|
| Named-entity recognition | Sentence/document with labelled entities | Entity precision, recall, F1; exact and partial match | Entity type, company-name, number, and date errors |
| Financial question answering | Question with source context | Exact match/F1 where appropriate; rubric score; citation accuracy | Unsupported answers, calculation errors, appropriate abstention |
| Multi-document summarization | Filing/report/news packet | Coverage, faithfulness, citation precision/recall, human utility | Contradictions, omissions, temporal errors |

The measures above are an implementation proposal for the confirmed tasks.
Report sample size, annotation method, and limitations with each result.

## Reproducibility

- Freeze model artifact/version, dataset version, prompt, quantization, inference
  engine, decoding parameters, and hardware configuration.
- Separate development and held-out evaluation data; document contamination and
  time-split limitations.
- Verify dataset licensing and use public or synthetic data within project limits.
- Distinguish quality, latency, throughput, peak memory, and any energy measures.
- Retain test inputs or permitted references, raw outputs, scoring rules, and
  error analysis so the evaluation can be reused.
- Record refusals, unsupported answers, and prompt-injection behavior where
  relevant to the workflow.
- Use human review/adjudication for subjective quality labels and report whether
  that review has actually occurred.

## Phase 2 completion record

- [ ] 5–8 model comparisons with all required dimensions and source IDs.
- [ ] Reusable financial NLP dataset/task/scoring specification.
- [ ] One-model GPU proof of concept with latency and task results.
- [ ] Measured results distinguished from published numbers and estimates.
- [ ] Resource and quality findings passed to architecture and Phase 3 analysis.
