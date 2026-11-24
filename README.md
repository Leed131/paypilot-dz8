# HW08 - Judge calibration for PayPilot escalation

**Revision required after mentor review.** The completed 30-case experiment used assistant-authored answers. Its 300 real judge evaluations are preserved as historical learning evidence; they do not establish judge accuracy on PayPilot answers. Final submission remains pending calibration on actual agent answers or the authorized course kit pool.

The class-based correction is in [judge-trust-statement.md](judge-trust-statement.md), under **What we do**, and [manual-review.hw08.v1.json](policies/manual-review.hw08.v1.json). Generic progress/update responses without confirmed human involvement require human review even with PASS five times. This is a manual policy, not a measured accuracy improvement.

## Required replacement - batch review draft

A [30-case replacement draft](annotations/proposals/review-30.md) is ready: 28 unchanged authorized-kit cases and two recorded course-agent answers. It reuses twelve saved laboratory decisions and LIVE-C001, and proposes seventeen additional annotations for student review. The [Ukrainian review file](annotations/proposals/review-17.uk.md) contains only those seventeen pending decisions; no retyping or individual-question workflow is required.

This follows the official kit guide at commit `f5c235aa10a505f9d6f9e422ffd66917578c537b`: reuse the laboratory cases and pool, select challenge cases, and add one obvious positive and one obvious negative. The planned benchmark strata are 10 obvious PASS, 10 obvious FAIL and 10 source-designed challenge cases. New student disputed flags remain unassigned; intended challenge membership does not establish the student's uncertainty.

**Criterion scope:** each kit case retains its original single-condition criterion. The two live cases retain the combined three-condition criterion. This is a deliberate casewise calibration scope. The current common-rubric runner must be aligned before judging; do not run the new draft through the old all-three-condition check.

**Provenance:** kit source files byte-match the official repository and retain its original criteria. Its producing-agent prompt versions were not supplied. `base.v1+D25+D27` and observed model `anthropic/claude-haiku-5.5` apply only to the two live answers. The twelve old laboratory labels retain their dates and decisions; their grouping was documented after earlier laboratory judge runs. This is not a fresh independent blind holdout.

1. Review/adopt or correct the seventeen assistant proposals, including six provisional challenge flags. Thirteen existing human references remain unchanged.
2. Verify final groups after review. The draft's designed 10/10/10 is provisional; do not force uncertainty flags if the student disagrees.
3. Align the evaluator with each supplied case criterion, then freeze the exact selected responses, references, rubric and source provenance in Git.
4. Run five evaluations per case for baseline and a versioned correction on the same cases. Compute new reports and the final trust statement; old synthetic scores do not transfer.

Manifest and exact draft: [annotations/proposals/kit-replacement-manifest.json](annotations/proposals/kit-replacement-manifest.json) and [kit-replacement-30.draft.jsonl](annotations/proposals/kit-replacement-30.draft.jsonl). The draft is not installed as the canonical label file and cannot be run by its current set registry.

All 45 earlier live responses remain unchanged in `annotations/live-source/`. Their full annotation route is an alternative if needed; it is not necessary to repeat that whole pool while reviewing this kit-based draft. Raw `sources/` traces were not attached and have not been independently re-inspected here; keep the original local collection directory.

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
