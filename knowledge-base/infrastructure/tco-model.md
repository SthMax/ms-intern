# On-Premise Deployment and TCO Framework

> **Later internship workstream:** retained as scaffolding for the two-month
> primary/secondary objectives. It is not a Week 1–2 checkpoint deliverable.

## Capacity inputs to obtain first

| Input | Unit | Low | Base | High | Source / owner |
|---|---|---:|---:|---:|---|
| Concurrent users | users |  |  |  |  |
| Peak requests | requests/min |  |  |  |  |
| Average input/output length | tokens/request |  |  |  |  |
| Service hours and availability | hours, % |  |  |  |  |
| Target latency | seconds |  |  |  |  |
| Model size/precision | parameters/bits |  |  |  |  |
| Retention/log volume | GB/month |  |  |  |  |
| Growth horizon | years |  |  |  |  |

## Cost model

Use low/base/high scenarios over a horizon to be agreed with the mentor and show
both total cost and cost per useful reviewed task.

| Cost component | Upfront / recurring | Quantity driver | Unit cost source | Low | Base | High |
|---|---|---|---|---:|---:|---:|
| GPU servers and spare capacity | Upfront | Servers/GPUs |  |  |  |  |
| CPU, memory, storage, networking | Upfront | Architecture |  |  |  |  |
| Rack/data-center integration | Mixed | Power/rack units |  |  |  |  |
| Electricity | Recurring | IT kWh × tariff |  |  |  |  |
| Cooling | Recurring | IT energy × PUE adjustment |  |  |  |  |
| Software/support/licenses | Recurring | Nodes/users/models |  |  |  |  |
| Hardware maintenance | Recurring | Support contract or % capex |  |  |  |  |
| Security/monitoring/backup | Mixed | Architecture |  |  |  |  |
| Implementation and validation | Mixed | Person-months |  |  |  |  |
| Ongoing platform operations | Recurring | FTE |  |  |  |  |
| Model evaluation/governance | Recurring | Releases/use cases |  |  |  |  |
| Facility/contingency | Mixed | Scenario assumption |  |  |  |  |

### Core formulas

- `Annual IT energy (kWh) = average IT load (kW) × operating hours`
- `Annual facility energy (kWh) = annual IT energy × PUE`
- `Annual electricity cost = annual facility energy × tariff`
- `Horizon TCO = capex + implementation + (analysis years × recurring annual cost) + contingency`

Avoid double-counting cooling if the facility tariff or chargeback already embeds
it. Treat depreciation/accounting presentation separately from cash TCO.

## Architecture questions

- Is inference isolated from training/fine-tuning?
- Are high availability and disaster recovery required for a pilot?
- How are model artifacts scanned, approved, signed, and promoted?
- Can the system operate with outbound network access disabled?
- Where do prompts, retrieved content, outputs, feedback, and audit logs reside?
- How are access control, secrets, deletion, backup, monitoring, and incident
  response implemented?
- Is remote vendor support possible, and what data/system access would it expose?
