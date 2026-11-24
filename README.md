# HW08 - PayPilot judge calibration

**Baseline fully audited; corrected same-reference repeat ready.** The student accepted the review package and requested a further audit. All 30 source question/answer pairs and original semantic criteria passed review; no verdict corrections were needed.

## Audited baseline and prepared correction

The baseline completed 150 evaluations. Agreement is 22/30 (73.33%; Wilson 55.55%-85.82%); consistency is 26/30 (86.67%; Wilson 70.32%-94.69%). All raw responses, stored fields, flags, case/run identities, metadata and aggregate statistics have now been independently checked against the matching journal. The three invalid quotations in LIVE-C006 omit one source newline; they remain invalid and preserved.

The baseline source report and journal are stored byte-for-byte in `reports/kit-baseline/`. See [kit-baseline-analysis.md](reports/kit-baseline-analysis.md), [kit-baseline-audit.json](reports/kit-baseline-audit.json), and [kit-correction-plan.md](reports/kit-correction-plan.md).

`rubric.hw08.kit.v1.1` is a procedural correction: retain active-criterion scope, distinguish actual human referral from conditional offers and queue/channel uncertainty, distinguish contact/effort from guaranteed outcomes, distinguish ordinary colleague review from an internal-review reason, and copy a short exact continuous quote. Source questions/answers, semantic criteria, accepted references, dates, trigger schema, judge system and validators are unchanged. No improvement is claimed before measuring the repeat.

Canonical `l09_labels` now matches the repeat alias `l09_labels_kit_v1_1`. The original `l09_labels_kit_v1` files and versioned input manifest remain unchanged. Both share semantic fixture/reference SHA-256 `15ab35384ac454af9366785c4b442533b216746842372db7d084b7ad9a871eb8`; procedural and full-set hashes differ as intended.

## Run the same-reference repeat

On the local Mac, using the same Ollama installation and model as baseline:

```bash
bash <<'SH'
set -e
cd "$HOME/Downloads/paypilot-dz8"
git pull --ff-only
JUDGE_MODEL=ollama:qwen2.5:14b OLLAMA_URL=http://127.0.0.1:11434 RUNS=5 TEMP=0.7 python3 tools/calibrate_run.py l09_labels_kit_v1_1
SH
```

This measures 150 additional evaluations after the new inputs and procedure are committed. Wait for `Report:` and preserve the new `.json` plus `.evaluations.jsonl` pair. The installed digest must match baseline before attributing changes to the procedural correction; runtime metadata records it. Compare raw and valid agreement, Wilson intervals, stability, schema errors, recovered cases, regressions and elapsed cost. Do not repeat merely to seek a better-looking number.

## Accepted reference set

- 28 unchanged cases from the mentor-authorized official kit, evaluated under their original per-case criteria.
- Two recorded PayPilot answers: LIVE-C001 and LIVE-C006, evaluated under the combined criterion.
- 13 prior human references preserved with their original dates; 17 assistant proposals adopted by the student as a batch. This is not independent case-by-case human annotation for those seventeen cases.
- Exactly 10 obvious PASS, 10 obvious FAIL and 10 accepted source-designed challenge examples; reference verdict totals are 16 PASS and 14 FAIL.

Start with [accepted-reference-review.md](annotations/accepted-reference-review.md) and [accepted-reference-manifest.json](annotations/accepted-reference-manifest.json). The [acceptance record](annotations/reference-adoption-2026-11-24.json) links the exact reviewed draft. The original proposal files remain historical review evidence.

Challenge flags describe accepted benchmark strata. They do not assert newly reported personal uncertainty. Laboratory grouping was documented after prior laboratory judge runs; this is not a fresh independent blind holdout. The official kit guide recommends reusing those lab cases and adding pool cases and two obvious examples.

Canonical and compatibility files are `evals/sets/l09_labels.jsonl` and `sets/l09_labels.jsonl`. The immutable baseline aliases `evals/sets/l09_labels_kit_v1.jsonl` and `sets/l09_labels_kit_v1.jsonl` retain baseline bytes. The two repeat aliases `l09_labels_kit_v1_1` match the canonical files. Baseline uses `rubric.hw08.kit.v1`; the repeat uses `rubric.hw08.kit.v1.1`. Each case is checked only against its supplied semantic criterion, with the shared verdict/evidence protocol. Labels, flags and annotation notes never enter the judge prompt.

## Intentional baseline reproduction on the local Mac

Requirements: Git, Python 3.8+, running Ollama and installed `qwen2.5:14b`. Only the Python standard library is needed. The bank service is not needed to evaluate the recorded answers.

```bash
cd "$HOME/Downloads/paypilot-dz8"
git pull --ff-only
JUDGE_MODEL=ollama:qwen2.5:14b OLLAMA_URL=http://127.0.0.1:11434 RUNS=5 TEMP=0.7 python3 tools/calibrate_run.py l09_labels_kit_v1
```

The recorded baseline is already complete. Use this command only for intentional reproduction; it is not the next required action. It requests 150 evaluations: five per case. It verifies committed label, rubric and acceptance inputs before any generation. It records source prompt provenance per case; a global environment setting cannot turn unknown kit prompts into the recorded live bank prompt. Keep the terminal open until `Report:` appears. Exit 2 indicates completed generation with invalid schema/evidence records; retain those outputs. Exit 1 indicates a preflight or run failure; partial evidence is preserved.

For a metadata-only model readiness check, add `--check-only`. It does not generate. After the actual baseline, inspect discrepancies, version a correction, remeasure the same cases and references, and update the trust statement with the new results. Report 95% Wilson intervals for both reference agreement and self-consistency. Baseline reference agreement is now recorded; no correction benefit is claimed before a measured repeat.

## Source provenance and scope

Kit files in `annotations/kit-source/` byte-match official Git blobs at commit `f5c235aa10a505f9d6f9e422ffd66917578c537b` of `alex-pancho/paypilot-l09-eval`. Kit producing prompts were not supplied. Prompt `base.v1+D25+D27`, profile `lesson-09` and observed agent `anthropic/claude-haiku-5.5` apply only to the two recorded live answers. Raw live trace files were not attached and are not independently re-inspected here.

The pool covers component criteria case by case and two combined-criterion answers. Its pooled score must not be represented as a validated autonomous combined working gate. Human review remains required. The response-class rule in [judge-trust-statement.md](judge-trust-statement.md) applies even when all five verdicts agree.

## Historical synthetic experiment

All original synthetic responses, human labels and 300 model outputs remain preserved. `l09_labels_v1` and `l09_labels_v1_1` reproduce the old inputs; they require `--allow-legacy-fixtures` for intentional historical use. Their scores are not PayPilot replacement results. [calibration-comparison.md](reports/calibration-comparison.md) and `reports/calibration-final.json` are explicitly legacy indexes; the latter name does not identify the corrected final measurement.

Working-gate files remain separate from recorded-answer calibration; live working-gate execution is unclaimed. See [working-gates.md](docs/working-gates.md). Current status: [validation.json](validation.json).
