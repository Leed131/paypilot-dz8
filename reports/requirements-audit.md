# HW08 - Required corrections after mentor review

Review date: 2026-11-24. Repository: `Leed131/paypilot-dz8`, branch `main`.

Karina's feedback resolves the source interpretation: calibration must use actual agent answers or the authorized kit pool. Assistant-authored answers do not support a PayPilot calibration claim. The previous decision to treat live collection as optional was incorrect and is withdrawn. The former audit is preserved in `history/pre-mentor-correction/`.

| Required correction | Evidence | Status |
| --- | --- | --- |
| Calibrate on actual-agent or authorized-kit answers | Accepted set: 28 official-kit cases with original criteria plus two recorded agent answers; sources and acceptance evidence preserved. | Baseline and all raw records verified; procedural correction prepared, repeat pending. |
| Add answer-class rule in What we do | `manual-review.hw08.v1` requires human review for unconfirmed human handoff regardless of verdict, unanimous votes or valid schema. The primary statement includes the rule. | Documented manual policy; operational effect unmeasured. |

## Accepted replacement package

The official kit guide permits reuse of twelve labelled lab cases, the unlabelled pool and two additional obvious cases. The accepted set contains LB-01..12, PL-01..16, LIVE-C001 and LIVE-C006. The source kit files byte-match official Git blobs at commit `f5c235aa10a505f9d6f9e422ffd66917578c537b`.

The student explicitly accepted the seventeen assistant proposals as a batch and requested another audit. All seventeen verdicts are consistent with their stated criteria; no corrections were required. Thirteen prior human decisions and their dates remain unchanged. The new references record assistance and batch adoption rather than claiming thirty independent human case assessments.

- Exactly 30 unique question/answer pairs; 10 obvious PASS, 10 obvious FAIL and 10 accepted source-designed challenge cases. Reference totals: 16 PASS and 14 FAIL.
- All 28 kit semantic criteria are unchanged; the two live cases retain the combined criterion. `rubric.hw08.kit.v1` supplies a common evidence/output protocol without adding unstated semantic conditions.
- Challenge membership is separate from personal uncertainty. Prior laboratory grouping was documented after earlier judge runs; no new independent blind-holdout claim is made.
- Kit producing prompts remain unspecified. The recorded prompt `base.v1+D25+D27` applies only to the two live cases. Original raw live traces were not attached; this audit verifies available records and source consistency.
- The exact canonical and baseline-alias bytes, rubric and acceptance evidence must be committed before generation. Runtime checks enforce this and preserve source-specific prompt metadata.
- Actual baseline: five evaluations per case; then inspect errors, version a correction and remeasure the same accepted sources, semantic criteria and references. Record all raw outputs, schema/evidence flags and exact runtime hashes.
- Recompute raw/valid reference agreement, Wilson intervals/half-widths for both agreement and self-consistency, group metrics, confusion matrices and correction cost. Old synthetic scores remain historical and are not transferred.

Accepted files: `evals/sets/l09_labels.jsonl`, `evals/sets/l09_labels_kit_v1.jsonl`, their compatibility copies, `annotations/accepted-reference-manifest.json`, and `annotations/reference-adoption-2026-11-24.json`. The original proposal files remain unchanged as review evidence.

## Response-class check

Legacy HW08-011: “Your case has been flagged for further attention. You should receive an update soon, but I cannot confirm the outcome.” No explicit human role is positively committed to handoff/follow-up. It requires manual review even though v1.1 returned PASS 5/5.

LIVE-C001 explicitly reports escalation to a human support agent before reporting queued status. Queue wording alone therefore does not trigger the generic-routing rule. This routing assessment does not assign its final human verdict or waive either remaining criterion.

The separate policy does not change the judge's fixed `trigger` enum, rubric, historical verdicts or scores. Review records use `review_policy_version`, `manual_review_reasons` and an explicit human resolution; unresolved cases have no automatic acceptance. The policy is a mandatory manual procedure, not an implemented automated classifier.

## Preserved evidence and readiness

Original reports and all 300 historical outputs remain unchanged. Their freeze timeline and audits are linked through `calibration-comparison.md` and the archived prior audit. Existing offline checks remain historical technical evidence, not completion of the required actual-agent calibration. Live working-gate execution is also unclaimed.

**Baseline fully verified; final resubmission still pending the measured correction.** All 150 raw outputs, flags and metrics match. `rubric.hw08.kit.v1.1` and the same-reference repeat inputs are prepared. Next step: execute the committed repeat, compare benefits/regressions and update final trust metrics. No reference change or further approval is required. No further mentor clarification is needed to act on these two corrections.

Baseline report audit: `kit-baseline-audit.json`; summary and case patterns: `kit-baseline-analysis.md`. The report records 150 completed calls, 22/30 raw and valid agreement, 26/30 stable cases and three non-verbatim quote errors. All raw outputs have been revalidated against the matching journal.
