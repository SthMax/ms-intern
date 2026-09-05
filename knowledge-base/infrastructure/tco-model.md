# Three-Year TCO — On-Premise versus Commercial APIs

**Phase 3 — Weeks 6–8.** The three-year comparison horizon and API alternative are
confirmed in [the final project plan](../../PROJECT_PLAN.md).
Status: calculation framework; no quotes, prices, or cost results recorded.

Compare production-grade on-premise deployment with commercial LLM API
consumption. The brief lists OAI, Anthropic, and DeepSeek as examples.
Provider inclusion in the comparison does not establish internal approval,
service availability, or suitability for a particular data class.

## Shared comparison basis

Use the same workload, output-quality threshold, service level, currency,
price date, and tax treatment across options. Connect on-premise capacity to the
[Phase 2 architecture](reference-architecture.md) and measured proof of concept.

| Input | Unit / definition | Low | Base | High | Source / assumption |
|---|---|---|---|---|---|
| Analysis horizon | 3 years / 36 months — confirmed | 3 | 3 | 3 | Final project plan |
| Users and peak concurrency | Users | | | | |
| Annual workload and growth | Tasks/year; growth by year | | | | |
| Input/output tokens | Tokens/task, including retries | | | | |
| Quality and human review | Accepted-task criteria; review minutes | | | | |
| Service hours / availability | Hours/year; target % | | | | |
| Inference latency | Seconds under stated load | | | | |
| Retained data / traffic | GB stored and transferred | | | | |
| Currency, FX, tax | Currency and valuation date | | | | |

## On-premise costs

| Component | Cost driver | Timing | Source ID / assumption |
|---|---|---|---|
| GPU servers, spares, and capacity | Server/GPU count and configuration | Upfront / refresh | |
| CPU, memory, storage, networking | Architecture specification | Upfront / refresh | |
| Rack and facility integration | Space, installation, power | Mixed | |
| Electricity | IT kWh, facility overhead, tariff | Annual | |
| Cooling | PUE or separately priced facility charge | Annual | |
| Software, commercial licenses, and support | Node/user/model terms | Mixed | |
| Maintenance | Support contracts and repair assumptions | Annual | |
| Security, monitoring, backup, recovery | Required controls and architecture | Mixed | |
| Implementation and model validation | Person-months | Upfront / changes | |
| Operations and governance personnel | FTE, release and evaluation effort | Annual | |

## Commercial API costs

| Component | Cost driver | Required evidence |
|---|---|---|
| Input and output consumption | Separate token volumes and prices | Dated provider prices with units and currency |
| Volume-based pricing | Usage tiers, discounts, commitments, minimums | Published terms or clearly labelled indicative quote |
| Cache / batch terms | Eligible volumes and separate rates | Applicable provider terms; no automatic discount assumption |
| Data egress and transfer | Billable GB by direction and service | Provider/network terms; mark unknown or not applicable with a reason |
| Security premiums | Incremental enterprise/private connectivity, isolation, retention, audit or contractual controls | Priced feature/quote or explicit scenario assumption |
| Platform integration and support | Gateway, application, retrieval, observability, support | Architecture and staffing assumptions |
| Review and governance | Validation, human review, monitoring, change management | Comparable effort assumptions to on-premise |

Do not assume a provider charges egress fees or security premiums. Record a
sourced charge, a justified non-applicable entry, or an unknown input requiring
sensitivity analysis. Avoid counting an included feature again as a premium.

## Calculation method

- Annual IT energy = average IT load in kW × operating hours.
- Facility energy = IT energy × PUE, where this method matches facility charging.
- Electricity cost = facility energy × tariff. Do not add cooling again if PUE
  or a facility charge already includes it.
- Annual API consumption cost = sum across billed input/output/cache/batch/volume
  categories of quantity × applicable price, plus relevant commitments/minimums.
- Three-year on-premise TCO = upfront implementation and capex + year 1, 2, and 3
  operating costs + refresh/contingency assumptions.
- Three-year API TCO = upfront integration + year 1, 2, and 3 consumption,
  transfer, security, platform, personnel, and governance costs.
- Cost per accepted task = three-year TCO / accepted tasks over the same period.

Model each year separately to capture growth, utilization, price changes, and
staffing. Report low/base/high scenarios and break-even volume where the inputs
support it. Keep cash TCO separate from depreciation or discounted-value views.

## Phase 3 output

A traceable three-year comparison, sensitivity table, major cost drivers, and
limitations. Link the model to the pilot proposal effort/cost/ROI assumptions
and the final report.
