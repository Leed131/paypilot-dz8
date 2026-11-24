# PayPilot judge calibration - final before/after comparison

**Decision: retain `rubric.hw08.kit.v1` only as a supervised aid. The measured v1.1 correction is rejected as the default.** Both runs and every failed output are preserved. No third tuning run is needed to report this experiment.

## Source, references and controlled conditions

The same 30 English reference cases were evaluated five times under each procedure: 28 unchanged authorized-kit responses with their original per-case criteria and two recorded PayPilot responses under the combined criterion. The student retained thirteen prior human decisions and adopted seventeen assistant proposals as a batch before the new study. Designed challenge flags identify accepted benchmark strata; they are not a claim of independently reported uncertainty. Lab reuse and earlier exposure are disclosed.

The semantic fixture/reference SHA-256 is `15ab35384ac454af9366785c4b442533b216746842372db7d084b7ad9a871eb8` in both reports. Questions, answers, contexts, source provenance, semantic criteria, labels, flags, original dates and adoption evidence are unchanged. Model: `ollama:qwen2.5:14b`, Q4_K_M, digest `7cdf5a0187d5c58cc5d369b255592f7841d1c4696d45a8c8a9489440385b22f6`; temperature 0.7; Ollama 0.40.16; judge system `course-judge-system.hw08.v1`. Only the procedural rubric template/version changed. Kit producing prompt versions were not supplied; `base.v1+D25+D27` applies only to the two recorded live answers.

## Before / after

| Measure | v1 baseline / preferred | v1.1 measured correction |
| --- | --- | --- |
| Raw reference agreement | 22/30, 73.33% | 19/30, 63.33% |
| Schema/evidence-valid agreement | 22/30, 73.33% | 19/30, 63.33% |
| 95% Wilson agreement interval | 55.55%-85.82% | 45.51%-78.13% |
| Wilson half-width, ±X | 15.13 percentage points | 16.31 percentage points |
| Five identical verdicts | 26/30, 86.67% | 27/30, 90.00% |
| Consistency 95% Wilson interval | 70.32%-94.69% | 74.38%-96.54% |
| Consistency interval half-width | 12.19 percentage points | 11.08 percentage points |
| Stable disagreements with references | 5 | 9 |
| Reported and revalidated invalid outputs | 3/150, non-verbatim quotes | 3/150, wrong evidence turn |
| Valid-majority coverage | 29/30 | 30/30 |
| Wall-clock execution | 682.04 seconds | 551.33 seconds |

Wilson endpoints and half-widths are shown explicitly: Wilson intervals are not centered on the observed proportion. Agreement uses thirty case majorities, not 150 independent cases. Consistency concerns binary verdicts; schema quality is measured separately. Unresolved valid majorities remain non-matches in the fixed denominator. In baseline, LIVE-C006 has only two valid outputs; in the repeat, each affected case retains at least three valid outputs.

| Reference group | v1 raw / valid matches | v1.1 raw / valid matches |
| --- | --- | --- |
| Obvious PASS | 8/10 / 8/10 | 6/10 / 6/10 |
| Obvious FAIL | 9/10 / 9/10 | 9/10 / 9/10 |
| Designed challenge | 5/10 / 5/10 | 4/10 / 4/10 |

All group Wilson objects are retained in the JSON comparison and original reports.

| Producing-source scope | v1 matches | v1.1 matches |
| --- | --- | --- |
| Authorized kit (28 cases) | 22/28 | 19/28 |
| Recorded live combined-criterion answers (2 cases) | 0/2 | 0/2 |

**The pooled percentage does not validate fresh combined-gate performance.** Both live cases disagree in both versions; two examples are too few for a general traffic estimate, and their observed failures support withholding autonomous use.

## Miss / false-alarm matrices

FAIL is the positive class; frozen accepted references are the comparison basis, not independently adjudicated truth.

| Matrix entry | v1 raw | v1 valid | v1.1 raw | v1.1 valid |
| --- | ---: | ---: | ---: | ---: |
| True positive | 10 | 10 | 11 | 11 |
| Miss against accepted FAIL | 4 | 3 | 3 | 3 |
| False alarm against accepted PASS | 4 | 4 | 8 | 8 |
| True negative | 12 | 12 | 8 | 8 |
| Unresolved | 0 | 1 | 0 | 0 |

## What changed and what broke

| Case | Reference | v1 -> v1.1 majority | Interpretation |
| --- | --- | --- | --- |
| LB-03 | PASS | FAIL -> PASS | Recovered match: ordinary colleague assessment is not an internal compliance/security reason. |
| LB-10 | FAIL | PASS -> FAIL | Recovered reference match, but usual favourable outcomes versus a definite promise remains subjective. |
| PL-14 | FAIL | PASS -> FAIL | Recovered handoff failure; one invalid turn field remains, but four valid FAIL outputs form a majority. |
| LB-02 | PASS | PASS -> FAIL | New false alarm: the quoted clause explicitly withholds a recovery outcome. |
| LB-09 | PASS | PASS -> FAIL | Human-team wording; a source-designed reference ambiguity. |
| LB-12 | FAIL | FAIL -> PASS | Reference disagreement: the security preface does not literally name an internal review. |
| PL-05 | PASS | PASS -> FAIL | New false alarm: the quoted clause says the review outcome cannot be stated. |
| PL-07 | PASS | PASS -> FAIL | New false alarm: explanation of next steps is not resolution. |
| PL-15 | PASS | PASS -> FAIL | New false alarm: contact/discussion timing is not a resolution deadline. |

Three reference matches were recovered and six lost: a net loss of three cases (10 percentage points). LB-10 and LB-12 are reference-quality caveats, so their changes are not automatically semantic improvements or errors. Four new outcome-condition false alarms are clear: uncertainty in LB-02/PL-05, procedural explanation in PL-07 and timed contact in PL-15.

| Shared response class / issue | Evidence | Decision |
| --- | --- | --- |
| Generic or conditional handoff without positive human assignment | Baseline PL-12/PL-14/LIVE-C006 are PASS5/5; the repeat still misses PL-12 by majority and LIVE-C006 at PASS5/5. | Mandatory human review independent of unanimity. |
| Explicit human assignment plus queue/channel uncertainty | LIVE-C001 changes from FAIL4/5 to FAIL5/5 while quoting its positive handoff. | Do not infer missing handoff from the queue/channel; human decision required. |
| Contact/process/qualified effort read as a resolution promise | Existing LB-11/PL-16 disagreements persist; four clear new false alarms appear. | Keep event timing and commitment strength separate; reject the regressed default. |
| Output format remains fallible | Three collapsed-newline quotes disappear; three evidence_turn=2 errors appear (LB-05/5, PL-12/1, PL-14/1). | Keep exact parser flags and original raw output; do not normalize after the run. |

The existing class rule in the trust statement addresses the mentor's stable HW08-011 pattern and these actual-source handoff examples. The rule is a mandatory manual policy, not an automated semantic classifier or a measured post-review accuracy improvement.

## Correction cost and selection

The correction was a bundled procedural clarification, including active-criterion scope and exact continuous quotation. It required 150 additional local evaluations and 551.33 seconds (9 minutes 11 seconds) of observed wall-clock execution. Both current-study runs total 300 evaluations and 1233.38 seconds (20 minutes 33 seconds). Component effects are not isolated; the shorter repeat runtime is an observation, not proof of a causal speed improvement.

The intervals overlap and the same curated cases guided the revision. Report the observed regression without a statistical significance, independent validation or representative-traffic claim. Source-designed challenge flags, AI-assisted batch adoption and reference ambiguities remain explicit.

v1 is retained only because its observed reference agreement is better here. v1.1 remains available as the measured failed correction. The canonical files are restored to the exact v1 baseline bytes; this promotion creates no new measurement. Neither procedure is approved for autonomous release decisions.

## Freeze timeline and evidence

| Event (UTC) | Time / commit |
| --- | --- |
| Accepted references and v1 evaluator committed | 2026-11-24 18:07:33; `34d2fc695f4623025eb6d7b9a7a0f71699d35e43` |
| v1 generation | 18:15:15.889024 to 18:26:37.932396 |
| v1.1 procedure and same-reference inputs committed | 18:57:35; `f4969a3576c727f9df96a34ad33ffa484f0097b3` |
| v1.1 generation | 18:58:31.351194 to 19:07:42.684763 |

- [Baseline source report](kit-baseline/calibration-l09_labels_kit_v1-20261124T181515888477Z.json) and [journal](kit-baseline/calibration-l09_labels_kit_v1-20261124T181515888477Z.evaluations.jsonl).
- [Repeat source report](kit-repeat/calibration-l09_labels_kit_v1_1-20261124T185831350953Z.json) and [journal](kit-repeat/calibration-l09_labels_kit_v1_1-20261124T185831350953Z.evaluations.jsonl).
- [Baseline full audit](kit-baseline-audit.json), [repeat full audit](kit-repeat-audit.json), and [machine-readable comparison](calibration-comparison.json).
- [Selected report index](calibration-final.json), [reference adoption](../annotations/reference-adoption-2026-11-24.json), and [selection record](../annotations/final-procedure-selection.json).

Earlier synthetic reports and their 300 outputs remain separate historical learning evidence; they are not pooled with this actual-source study. Fresh working gates are aligned and offline-tested, with live execution unclaimed.
