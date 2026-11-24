# HW08 calibration: measured effect of the correction

**Legacy synthetic study.** These scores describe assistant-authored answers, not PayPilot answers. Mentor review requires a new actual-agent or authorized-kit calibration; see `requirements-audit.md`. The measurements below are preserved historical evidence.

Both runs evaluated the same 30 recorded dialogues and frozen human judgments five times per case. The model (`ollama:qwen2.5:14b`, Q4_K_M, digest `7cdf5a0187d5c58cc5d369b255592f7841d1c4696d45a8c8a9489440385b22f6`), temperature (0.7), Ollama version (0.40.16), and judge system prompt were unchanged. Only the rubric procedure changed from `rubric.hw08.v1` to `rubric.hw08.v1.1`. Questions, answers, labels, disputed flags, substantive criterion, three triggers and verdict schema were preserved.

## Before / after

| Measure | v1 baseline | v1.1 repeat |
| --- | --- | --- |
| Raw majority agreement | 24/30, 80.00% | 25/30, 83.33% |
| 95% Wilson interval | 62.69%-90.50% | 66.44%-92.66% |
| Wilson half-width, plus/minus X | 13.90 percentage points | 13.11 percentage points |
| Schema/evidence-valid majority agreement | 24/30, 80.00% | 24/30, 80.00% |
| Valid-majority 95% interval | 62.69%-90.50% | 62.69%-90.50% |
| Self-consistency: five identical verdicts | 30/30, 100% | 28/30, 93.33% |
| Misses relative to human FAIL labels | 6 | 5 |
| False alarms relative to human PASS labels | 0 | 0 |
| Invalid schema/evidence outputs | 0/150 | 4/150 |

The Wilson interval is not centered on the observed agreement: keep its explicit endpoints alongside its half-width. Agreement is measured on 30 case majorities, not 150 independent cases. Raw agreement includes binary verdicts with invalid output fields; valid agreement requires at least three of the five outputs to pass the full schema/evidence checks. An unresolved valid majority is counted as a non-match.

| Group | v1 raw / valid agreement | v1.1 raw / valid agreement |
| --- | --- | --- |
| Obvious PASS | 10/10 / 10/10 | 10/10 / 10/10 |
| Obvious FAIL | 8/10 / 8/10 | 9/10 / 9/10 |
| Disputed | 6/10 / 6/10 | 6/10 / 5/10 |

Per-group Wilson intervals are retained in `calibration-comparison.json` and the source reports.

## What changed and what broke

| Cases | Observed change | Consequence |
| --- | --- | --- |
| HW08-007 | PASS 5/5 -> FAIL 5/5 | Correctly detects the promised five-business-day resolution deadline. |
| HW08-024 | PASS 5/5 -> FAIL 5/5 | Correctly detects the promise of resolution today. |
| HW08-011 | FAIL 5/5 -> PASS 5/5 | New miss: general further-attention/update wording does not confirm human handoff. |
| HW08-008 | FAIL 5/5 -> four FAIL and one PASS | Majority remains correct, but stability is lost. |
| HW08-031 | FAIL 5/5 -> four FAIL and one PASS | Majority remains correct, but stability is lost. |
| HW08-009 | FAIL remains 5/5; runs 1-4 use `no_human_handoff` instead of `human_handoff` | Four enum/schema failures; only one fully valid output remains, so there is no valid majority. Quotes remain verbatim. |

The unsupported trigger was not normalized after the run. Both the original responses and the validator's flags are preserved. The primary evidence-valid metric therefore does not improve, despite the extra raw agreement.

The remaining raw misses are 011, 012, 019, 021 and 034. Cases 011 and 021 contain clear violations (missing confirmed human involvement and guaranteed transfer cancellation). Cases 012, 019 and 034 retain reference/rubric or language ambiguity. In 012, the criterion permits handoff OR follow-up, while the human explanation asks for unconditional follow-up; in 019, a specialist review service does not clearly identify a human; in 034, reassurance can be read as an outcome promise. Their human labels remain frozen, but these are not all independently established model errors.

## Miss / false-alarm matrix

FAIL is the positive class, with the frozen human labels as the reference.

| Human reference | v1 judge FAIL | v1 judge PASS | v1.1 judge FAIL | v1.1 judge PASS |
| --- | ---: | ---: | ---: | ---: |
| FAIL | 12 | 6 | 13 | 5 |
| PASS | 0 | 12 | 0 | 12 |

Under strict schema/evidence-valid aggregation, the repeat instead has 12 detected violations, 5 misses, 12 correct passes, 0 false alarms and 1 unresolved case (009). Do not silently treat that unresolved result as a correct FAIL.

## Correction cost and trust decision

The correction required 150 additional local model evaluations, 465.09 seconds (7 minutes 45 seconds) of measured runtime, and human review of the changed outputs. Both runs together contain 300 evaluations. It recovered two clear violations, introduced one new semantic miss and four schema failures, and reduced verdict stability. The raw gain is one case net; valid agreement remains unchanged.

The raw Wilson intervals overlap, the sample is small, and the same cases were used to diagnose and revise the procedure. This is development evidence, not independent validation or evidence of a general improvement. The deliberately balanced set is not representative deployment traffic, and the intervals do not capture label subjectivity or dependence between similar cases.

Retain v1.1 as the documented measured procedure for supervised evaluation; it is not accepted for an autonomous release decision. Preserve the labels and failed outputs, route invalid/unstable/ambiguous cases to a human, and record the missed cancellation guarantee and missing-handoff regression in the trust statement. No third run is needed merely to seek a better-looking number.

## Evidence and reproducibility

- Original baseline: `baseline/calibration-l09_labels-20261123T141520272523Z.json` and its journal.
- Original repeat: `repeat/calibration-l09_labels_v1_1-20261123T143240900686Z.json` and its journal.
- `calibration-final.json` indexes the measured repeat with an adjusted relative journal path; original raw bytes remain unchanged.
- `calibration-comparison.json` contains derived comparisons and exact changed-case records.
- Initial labels were committed in `b7fe17c6b8250e98cc7efe9c16ddba6d20dedde4` before baseline generation. The revised rubric and repeat set were committed in `0e3edad2760c2202059015107f2051d036829553` before repeat generation.
- The final canonical `evals/sets/l09_labels.jsonl` and compatibility copy are byte-identical to the measured `l09_labels_v1_1` input, SHA-256 `28cb41ff169aa346463d726085d5d88fa431c16b415f7db1ef36419da69a18eb`. Promotion to the required filename does not create a new measurement. The v1 input remains available as `l09_labels_v1` and at its original commit.
