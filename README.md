# HW08 - Judge Trust Statement for escalation

The public homework repository contains 30 English human-labelled fixtures, a versioned rubric, two completed calibration runs and the measured cost of a correction. The judge-use decision is **human-supervised use only; autonomous release gating is not accepted**. A strict submission audit is recorded in [reports/requirements-audit.md](reports/requirements-audit.md): agent-prompt provenance and the meaning of disputed labels remain documented interpretation issues, not unconditional compliance claims.

**Strict replacement stage in progress:** [live-answer collection plan](docs/live-replacement-plan.md). The 45 unlabelled questions and collector are ready; the future replacement answers, human labels and measurements are not yet collected. The existing files below document the first synthetic experiment.

Start with [judge-trust-statement.md](judge-trust-statement.md). The complete before/after analysis is [reports/calibration-comparison.md](reports/calibration-comparison.md).

## Measured results

| Measure | Baseline v1 | Final measured v1.1 |
| --- | --- | --- |
| Majority agreement | 24/30, 80.00% | 25/30, 83.33% |
| 95% Wilson interval | 62.69%-90.50% | 66.44%-92.66% |
| Wilson half-width | 13.90 percentage points | 13.11 percentage points |
| Schema/evidence-valid majority agreement | 24/30, 80.00% | 24/30, 80.00% |
| Self-consistency, five identical verdicts | 30/30 | 28/30 |
| Misses / false alarms against human labels | 6 / 0 | 5 / 0 |
| Invalid outputs | 0/150 | 4/150 |

The correction recovered 007/024, introduced a new miss in 011, made 008/031 unstable and produced four invalid trigger values in 009. The quotes in those four outputs are verbatim; the defect is an unsupported enum. Only one output for 009 is fully valid, so it has no valid majority. No post-hoc trigger normalization was applied. Same-set development, small curated samples and subjective disputed labels limit the conclusion.

## Required submission files

- `judge-trust-statement.md`: six statement rows, the measured correction cost and residual-risk decisions.
- `evals/sets/l09_labels.jsonl`: final canonical 30-case set, exactly 10 obvious PASS, 10 obvious FAIL and 10 disputed.
- `sets/l09_labels.jsonl`: byte-identical compatibility copy for native course-style tools.
- `sets/l09_escalation.jsonl`: threshold check, its paired semantic remainder, and five additional fresh-answer judge scenarios.
- `rubrics/escalation.rubric.hw08.v1.1.json` and `rubrics/CHANGELOG.md`: final version and history.
- `reports/calibration-final.json`: measured final report index with a working relative journal pointer; no measured values were changed.
- `reports/calibration-comparison.json`: derived comparison and changed-case records.

The original uploaded reports and all 300 evaluation records are preserved byte-for-byte under `reports/baseline/` and `reports/repeat/`. The archived directories avoid conflicts with users' untracked local run outputs when updating this repository.

## Human annotation provenance

Dialogues were authored by the assistant during the course discussion and labelled by the student with translation and criterion clarification. Explanations are English translations or faithful summaries of that discussion. Human labels were not changed to agree with the judge.

Initial labels and rubric were committed in `b7fe17c6b8250e98cc7efe9c16ddba6d20dedde4` before baseline generation. The revised procedure and exact v1.1 measurement inputs were committed in `0e3edad2760c2202059015107f2051d036829553` before the repeat. Reports record exact Git-verified input paths and hashes. `labeled_on: 2026-11-23` is the assembled-set finalization date; original individual annotation dates were not recovered and are not invented.

The user-approved HW08-013 correction (PASS to FAIL), earlier accepted revisions, and replacement versions of 014/015 are retained in annotation history. `annotations/all_recovered_32.jsonl` is the historical recovered collection; `annotations/reserve.jsonl` preserves 004/028 as obvious PASS. Incomplete 001/002 are documented but excluded from calibration. Laboratory LB cases are not substituted for the new fixtures.

Disputed flags retain the student's uncertainty. In particular, 012 has a reference/rubric-alignment issue about unconditional follow-up, 019 has ambiguous specialist-service wording, and 034 has reassurance-versus-promise ambiguity. Preserve those limitations rather than silently adjudicating after seeing model outputs.

## Dataset names and immutable measurements

| Current set name | Rubric | Purpose |
| --- | --- | --- |
| `l09_labels` | `rubric.hw08.v1.1` | Required final canonical filename |
| `l09_labels_v1_1` | `rubric.hw08.v1.1` | Exact input name used in the completed repeat |
| `l09_labels_v1` | `rubric.hw08.v1` | Archived original baseline input |

Final `l09_labels` is byte-identical to measured `l09_labels_v1_1`, SHA-256 `28cb41ff169aa346463d726085d5d88fa431c16b415f7db1ef36419da69a18eb`. Promotion to the canonical filename changes neither the evaluated bytes nor the existing reports. The baseline report originally used the name `l09_labels` at its recorded historical commit; its input bytes are now also archived as `l09_labels_v1`.

Both versions have identical questions, answers, human labels and disputed flags (fixture-label SHA-256 `e4a99504bc86164a5fb6b8f13eb756c4cffa7d2e167de5e7063d9270580ee374`). The exact packaged initial rubric was written down on assembly, not preregistered before every original annotation; the three substantive conditions were discussed while labelling.

## Reproduce calibration

Requirements: Git, Python 3.8 or newer, running Ollama and an installed `qwen2.5:14b` model. Only the standard library is required. The bank service and Docker are not needed to evaluate recorded answers. Human labels and annotation notes never enter the judge prompt.

Readiness check only (no generation):

```bash
JUDGE_MODEL=ollama:qwen2.5:14b OLLAMA_URL=http://127.0.0.1:11434 TEMP=0.7 python3 tools/calibrate_run.py l09_labels --check-only
```

Intentional new measurement (150 evaluations):

```bash
JUDGE_MODEL=ollama:qwen2.5:14b OLLAMA_URL=http://127.0.0.1:11434 RUNS=5 TEMP=0.7 python3 tools/calibrate_run.py l09_labels
```

Use `l09_labels_v1` only when intentionally reproducing the baseline. Keep prior reports. The script checks exact committed inputs, records the model digest and rubric/system hashes, journals every output, and preserves partial runs. Exit 2 means generation completed with schema/evidence errors; the measured v1.1 run has that status, not a transport failure. Exit 1 means a preflight/run failure. No third run is required to complete the documented two-run experiment.

`agent_prompt_version` is `not_applicable_recorded_fixtures`: these fixtures are not fresh outputs from a versioned bank-agent prompt. When switching to real agent outputs, record the actual prompt version and recalibrate. Native Python does not load `.env`; secrets must not be committed.

## Working gates and scope

The working set checks fresh bank-agent answers, separately from the recorded-answer calibration. Its threshold check belongs to `daily`, runs once and checks the required tool sequence. Its paired semantic case and five additional judge scenarios belong to `release`, run five times and use the final rubric. Offline validation can verify file structure and routing; actual execution needs the course bank service and local Ollama. A working gate result is not one of the recorded-answer calibration measurements.

See `docs/working-gates.md` for exact commands, source provenance, execution rules and limits. Live working-gate results are not claimed by this submission; check this separately before any actual release decision.
