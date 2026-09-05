# Local GPU Proof-of-Concept Plan

**Phase 2 — Weeks 3–5.** Required by [the final project plan](../../PROJECT_PLAN.md).
Status: plan template; no workstation, deployment, or measurements recorded.

## Confirmed minimum

Deploy **one open-source model on a local GPU workstation**, measure inference
latency, and run a sample financial NLP task. Keep enough configuration and
measurement detail for another researcher to repeat the experiment.

## Execution record

| Item | Value / evidence |
|---|---|
| Model and artifact version | |
| Model selection rationale / survey link | |
| License and source IDs | |
| Workstation GPU/VRAM, CPU, RAM, OS | |
| Driver, inference engine, dependency versions | |
| Precision / quantization | |
| Sample task and dataset / license | |
| Prompt, context/output length, decoding settings | |
| Warm-up, repetitions, concurrency, timing method | |
| Inference latency results and units | |
| Time to first token / throughput, if measured | |
| Peak memory / resource observations | |
| Sample outputs and scoring / error review | |
| Reproduction instructions and execution date | |
| Limitations and open questions | |

Select a sample from the financial NLP tasks in
[the evaluation plan](benchmark-plan.md). Published benchmark figures must be
labelled separately from local measurements.

## Completion checklist

- [ ] Model selection traced to the 5–8-model survey.
- [ ] One model deployed and served on the local GPU workstation.
- [ ] Latency measured under documented conditions.
- [ ] Sample financial NLP task completed with outputs and quality review.
- [ ] Reproduction instructions and limitations recorded.
- [ ] Findings linked to reference architecture and later TCO assumptions.

If the specified workstation is unavailable, record the dependency and continue
survey/evaluation design; do not represent a CPU or API experiment as completion
of the required GPU proof of concept.
