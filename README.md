# HW08 - PayPilot judge trust calibration

**Ready for mentor review within the declared supervised coursework scope.** Both requested corrections are complete: calibration now uses authorized-kit/recorded-agent answers, and the trust statement contains a response-class human-review rule that applies even at PASS 5/5. All 300 current-study outputs are preserved and audited.

Start with [judge-trust-statement.md](judge-trust-statement.md). Detailed results: [calibration-comparison.md](reports/calibration-comparison.md).

## Measured result and decision

| Measure | Preferred v1 | Measured v1.1 correction |
| --- | --- | --- |
| Raw / schema-evidence-valid agreement | 22/30, 73.33% | 19/30, 63.33% |
| Agreement 95% Wilson | 55.55%-85.82%; half-width 15.13 points | 45.51%-78.13%; half-width 16.31 points |
| Five identical verdicts | 26/30, 86.67% | 27/30, 90.00% |
| Stable reference disagreements | 5 | 9 |
| Invalid outputs | 3/150, non-verbatim quotes | 3/150, evidence_turn=2 |
| Raw misses / false alarms | 4 / 4 | 3 / 8 |
| Recorded live combined cases | 0/2 matches | 0/2 matches |

The correction recovered three reference matches and regressed six. Its cost was 150 additional evaluations and 551.33 seconds. All 300 evaluations together took 1233.38 seconds. More stable verdicts did not imply better agreement. The intervals overlap and the cases were used for development; no significance, independent validation or representative-traffic claim is made.

Retain `rubric.hw08.kit.v1` as a supervised aid and reject v1.1 as the default. Neither version is approved for autonomous release. The class rule requires human review for unconfirmed human handoff, independently of verdict unanimity; schema-invalid, unstable and challenge cases also require review. It is a manual policy, not an automated classifier or a measured post-review accuracy gain.

## Accepted sources and references

The final set contains 28 unchanged authorized-kit cases under their original per-case criteria plus two recorded PayPilot answers under the combined criterion. It has exactly 10 obvious PASS, 10 obvious FAIL and 10 accepted source-designed challenge cases; reference verdict totals are 16 PASS and 14 FAIL.

Thirteen prior human decisions and dates are preserved; seventeen assistant proposals were adopted by the student as a batch before this study. This is not independent case-by-case annotation for those seventeen cases. Historical laboratory grouping was documented after earlier judge runs. The official guide explicitly permits reuse of those lab cases. New-study labels/procedure were committed before their respective model runs; see the freeze timeline in the comparison.

Kit files byte-match `alex-pancho/paypilot-l09-eval` commit `f5c235aa10a505f9d6f9e422ffd66917578c537b`. Kit producing prompts were not supplied. Profile `lesson-09`, prompt `base.v1+D25+D27` and producing model `anthropic/claude-haiku-5.5` apply only to the two recorded live answers. Original raw live trace files were not attached and are not independently re-inspected here.

The pooled percentage is a kit/live reference benchmark, not a validated estimate for fresh combined bank gates. Both live cases disagree in both versions. Original reference ambiguities, including LB-10/LB-12, are retained rather than relabelled after seeing judge results.

## Final files

- `judge-trust-statement.md`: six statement rows and residual-risk decisions.
- `evals/sets/l09_labels.jsonl` and `sets/l09_labels.jsonl`: byte-identical preferred v1 inputs, also available as `l09_labels_kit_v1`.
- `rubrics/escalation.rubric.hw08.kit.v1.json` and `rubrics/CHANGELOG.md`: preferred procedure and version history. The measured v1.1 packet and aliases remain preserved.
- `sets/l09_escalation.jsonl`: one daily level-3 threshold check, its paired semantic remainder and five additional release judge cases; all six judge cases run five times and use the preferred combined rendering.
- `reports/calibration-final.json`: selected measured v1 report index with a working journal pointer. The original source report is unchanged.
- `reports/calibration-comparison.md` and `.json`: conditions, Wilson intervals, source/group results, matrices, common error classes, regressions and correction cost.
- `reports/kit-baseline/` and `reports/kit-repeat/`: original report/journal pairs, byte-for-byte; their full audits are adjacent.
- `annotations/reference-adoption-2026-11-24.json`, versioned accepted-reference manifests and `annotations/final-procedure-selection.json`: acceptance, freeze and selection provenance.

Canonical promotion after comparison creates no new measurement: it restores the exact v1 bytes already frozen in `34d2fc695f4623025eb6d7b9a7a0f71699d35e43` and evaluated by the baseline. The rejected correction remains frozen at `f4969a3576c727f9df96a34ad33ffa484f0097b3`.

## Reproducibility and offline checks

Requirements: Git, Python 3.8+ and the standard library. Actual recorded-answer calibration additionally needs local Ollama and installed `qwen2.5:14b`. The frozen run used temperature 0.7, Q4_K_M digest `7cdf5a0187d5c58cc5d369b255592f7841d1c4696d45a8c8a9489440385b22f6`, Ollama 0.40.16, and `course-judge-system.hw08.v1`. Labels and annotation notes never enter the model prompt.

Working-set offline check (no bank/model calls):

```bash
python3 runner.py l09_escalation --gate all --check-only
```

Local model readiness only (no generation):

```bash
JUDGE_MODEL=ollama:qwen2.5:14b OLLAMA_URL=http://127.0.0.1:11434 TEMP=0.7 python3 tools/calibrate_run.py l09_labels --check-only
```

For intentional reproduction, use `l09_labels_kit_v1` or `l09_labels_kit_v1_1` without `--check-only`, with `RUNS=5`. Both measured runs are already complete. Keep previous reports. The script verifies exact committed inputs/adoption evidence, records per-case prompt provenance, journals raw outputs and preserves invalid/partial results. Exit 2 means generation completed with schema/evidence errors; exit 1 is a preflight/run failure. Working-gate execution instead fails nonzero for any missing, failed or ungraded required case. See [docs/working-gates.md](docs/working-gates.md); live execution is not claimed.

## Historical learning evidence

Earlier assistant-authored answers, their human labels and 300 synthetic-study outputs remain separate. Legacy aliases `l09_labels_v1` and `l09_labels_v1_1` require `--allow-legacy-fixtures` for intentional reproduction. Their original reports remain under `reports/baseline/` and `reports/repeat/`; old derived indexes are archived under `reports/history/legacy-synthetic-indexes/`. They are not pooled with the final actual-source study. The `annotations/proposals/` folder preserves the pre-acceptance review draft, not the current reference state.

Final checklist: [reports/requirements-audit.md](reports/requirements-audit.md). Machine-readable status: [validation.json](validation.json).
