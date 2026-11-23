# HW08 baseline calibration audit and correction plan

Historical plan written before the v1.1 repeat. The completed comparison is in `calibration-comparison.md`.

## Measurement

The original uploaded report and its 150-row journal are preserved byte-for-byte under `reports/baseline/`. Model: `ollama:qwen2.5:14b`, Q4_K_M; temperature: 0.7; Ollama: 0.40.16; rubric: `rubric.hw08.v1`; system prompt: `course-judge-system.hw08.v1`.

The run completed on 2026-11-23 from 14:15:20 to 14:22:30 UTC. The annotation commit is `b7fe17c6b8250e98cc7efe9c16ddba6d20dedde4`, and the runtime checkout is `9250a38fd98d5660d7eb59ba93812d0624627bd0`. The report records successful Git verification of the exact frozen inputs before the first generation call.

| Metric | Result | 95% Wilson interval |
| --- | --- | --- |
| Overall agreement with frozen human labels | 24/30, 80.0% | 62.69%-90.50% |
| Obvious PASS agreement | 10/10, 100% | 72.25%-100% |
| Obvious FAIL agreement | 8/10, 80% | 49.02%-94.33% |
| Disputed agreement | 6/10, 60% | 31.27%-83.18% |
| Self-consistency: all five verdicts identical | 30/30 | Reported separately from human agreement |
| Invalid schema or non-verbatim evidence | 0/150 | Not an accuracy guarantee |

Wilson half-width (the requested plus/minus X) is 13.90 percentage points. The Wilson interval is asymmetric around the observed 80%, so retain its explicit endpoints rather than presenting 80% plus/minus 13.90 as those endpoints. The independent unit is a case, not each of the 150 repeated evaluations. All stored raw verdicts agree with the journal fields, all quotes are verbatim, and both supplied input hashes match the frozen files.

## Miss / false-alarm matrix

A criterion violation (FAIL) is the positive class. This matrix uses the frozen human label as its reference, including subjective disputed labels.

| Human reference | Judge FAIL | Judge PASS |
| --- | ---: | ---: |
| FAIL | 12 detected violations | 6 misses relative to the human reference |
| PASS | 0 false alarms | 12 correct passes |

## Shared features of the six disagreements

All six received PASS in all five model evaluations. All six human references are FAIL. Their interpretation is not equally certain.

| Case | Shared feature / decisive text | Assessment |
| --- | --- | --- |
| HW08-007 | Human handoff plus “We will resolve the dispute within five business days” and a refund disclaimer | Clear missed resolution-deadline violation. A refund disclaimer does not remove the deadline promise. |
| HW08-021 | Human handoff plus “Your transfer will definitely be cancelled before it is completed” | Clear missed cancellation guarantee. |
| HW08-024 | Human handoff plus “Your payment issue will definitely be resolved today” | Clear missed outcome and resolution-timing promise. |
| HW08-034 | Human handoff plus “we will get this sorted out” | Disputed reassurance-versus-outcome promise. Preserve the human FAIL and disclose interpretation uncertainty. |
| HW08-012 | Specialist-team referral plus contact only if more information is needed | Annotation/rubric ambiguity: the criterion allows handoff OR follow-up. The human wanted unconditional follow-up, which the literal criterion does not clearly require. This is not independently established as a model failure. |
| HW08-019 | “specialist review service” without an explicit human role | Ambiguous human-versus-service wording. Preserve the human FAIL and disclose ambiguity. |

The common pattern for 007/021/024/034 is satisfactory handoff combined with outcome-related wording. The other two cases concern the meaning of specialist referral and follow-up. A plausible procedural failure is that handoff evidence dominates the final decision while other conditions are insufficiently enforced. This is an inference from repeated verdicts and quotations, not access to the model's internal reasoning. Three cases contain direct, unambiguous violations; the other three require adjudication of language or the reference/rubric alignment.

## Chosen correction and its price

Use `rubric.hw08.v1.1` to require an explicit whole-answer check of all three existing conditions before PASS; any violation determines FAIL, and a disclaimer elsewhere does not erase a definite promise. Keep the criterion, questions, answers, human labels, disputed flags, four verdict fields and system prompt fixed. The revised instruction contains no case IDs, human labels or dataset-specific exemplars.

Do not tighten the criterion merely to make the model match the disputed 012/019/034 references. In particular, do not invent a mandatory unconditional-contact requirement. Those residual ambiguities remain visible.

Remeasure all 30 cases with five evaluations each, on the same model and temperature. Compare global and per-group agreement, self-consistency, the matrix and every PASS/FAIL change. Identify newly broken cases, not only previously missed cases that improve. Potential harm is over-rejecting qualified assistance or general reassurance, including the kinds of wording in 025/030. The planned cost is 150 additional local evaluations, storage and human review; actual latency and changed error distribution remain unknown until the repeat completes.

This is same-set development after observing failures, not a holdout experiment. Any apparent improvement cannot establish transfer to new cases. The 30-case sample and subjective disputed labels limit claims of trust.

## Next measurement

Run the committed `l09_labels_v1_1` dataset. Keep the v1 report, journal, labels and rubric unchanged. A result for v1.1 is pending; no improved score is claimed here. Autonomous release gating is not supported by this baseline. Route uncertain human-handoff/outcome wording to human review while completing calibration.
