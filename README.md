# HW08 - Judge calibration for PayPilot escalation

**Revision required after mentor review.** The completed 30-case experiment used assistant-authored answers. Its 300 real judge evaluations are preserved as historical learning evidence; they do not establish judge accuracy on PayPilot answers. Final submission remains pending calibration on actual agent answers or the authorized course kit pool.

The class-based correction is in [judge-trust-statement.md](judge-trust-statement.md), under **What we do**, and [manual-review.hw08.v1.json](policies/manual-review.hw08.v1.json). Generic progress/update responses without confirmed human involvement require human review even with PASS five times. This is a manual policy, not a measured accuracy improvement.

## Required replacement

45 actual course-agent answers have already been collected. Original questions, answers and provenance are in [annotations/live-source/candidates.jsonl](annotations/live-source/candidates.jsonl), alongside the uploaded manifest and journal. Producing prompt: `base.v1+D25+D27`; profile: `lesson-09`; observed model: `anthropic/claude-haiku-5.5`. Raw `sources/` traces were not attached and have not been independently re-inspected here. Keep the original local collection directory.

Human annotation is in progress; no judge calls have been made for this pool. The annotation ledger records finalized decisions, current progress and the next pending review. Follow [docs/live-replacement-plan.md](docs/live-replacement-plan.md) and record each explicit human decision in [annotations/live-human-review.json](annotations/live-human-review.json).

1. Finish human annotation under the three-condition criterion.
2. Select the first ten finalized annotations per group in candidate-ID order: obvious PASS, obvious FAIL and genuinely disputed. If a group is short, obtain more actual-agent or authorized-kit answers. Do not force labels or dispute flags to fill quotas.
3. Commit exact selected responses, labels, rubric and source provenance before judging. Then replace canonical inputs and configure correct runner rubric/source metadata.
4. Evaluate each selected answer five times for baseline and a versioned correction on the same cases. Recompute all metrics and the final trust statement from these new reports.

## Historical experiment

The current `evals/sets/l09_labels.jsonl`, compatibility copy `sets/l09_labels.jsonl`, and version aliases are **still the synthetic legacy set**, not the required replacement. Their exact answers, labels, disputed flags and hashes are preserved.

| Historical measure | v1 | v1.1 |
| --- | --- | --- |
| Raw majority agreement | 24/30, 80.00% | 25/30, 83.33% |
| Schema/evidence-valid agreement | 24/30, 80.00% | 24/30, 80.00% |
| Five identical verdicts | 30/30 | 28/30 |
| Invalid outputs | 0/150 | 4/150 |

Full intervals, misses, costs and source reports: [reports/calibration-comparison.md](reports/calibration-comparison.md). `reports/calibration-final.json` is a historical repeat-report index, not the corrected PayPilot calibration. Previous narrative/status files are archived under `reports/history/pre-mentor-correction/`.

`tools/calibrate_run.py l09_labels` still selects the legacy set. It refuses to proceed unless `--allow-legacy-fixtures` is explicitly supplied for historical reproduction; this flag does not satisfy the mentor correction. No new replacement run should start until labels and correct runner provenance are frozen. Never attach the bank prompt version retroactively to synthetic answers.

## Working gates

`sets/l09_escalation.jsonl` contains one daily tool-sequence case and six release judge cases, each release case configured for five runs. Offline checks and fresh-answer gate execution are separate from recorded-answer calibration. Live working-gate execution is unclaimed. See [docs/working-gates.md](docs/working-gates.md).

Current status: [validation.json](validation.json). Remaining checks: [reports/requirements-audit.md](reports/requirements-audit.md).
