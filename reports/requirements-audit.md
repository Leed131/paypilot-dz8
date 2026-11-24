# HW08 - Required corrections after mentor review

Review date: 2026-11-24. Repository: `Leed131/paypilot-dz8`, branch `main`.

Karina's feedback resolves the source interpretation: calibration must use actual agent answers or the authorized kit pool. Assistant-authored answers do not support a PayPilot calibration claim. The previous decision to treat live collection as optional was incorrect and is withdrawn. The former audit is preserved in `history/pre-mentor-correction/`.

| Required correction | Evidence | Status |
| --- | --- | --- |
| Calibrate on actual-agent or authorized-kit answers | 45 course-agent answers, unchanged uploaded manifest and journal in `annotations/live-source/`; prompt `base.v1+D25+D27`, profile `lesson-09`, observed model `anthropic/claude-haiku-5.5`. | Source available; human annotation and new calibration pending. |
| Add answer-class rule in What we do | `manual-review.hw08.v1` requires human review for unconfirmed human handoff regardless of verdict, unanimous votes or valid schema. The primary statement includes the rule. | Documented manual policy; operational effect unmeasured. |

## Replacement acceptance checks

- Preserve exact source questions/answers and provenance. Original raw `sources/` traces were not attached; this review verifies attached-file consistency, not independent raw-trace authenticity.
- Obtain explicit human PASS/FAIL labels and criterion-based explanations before showing any new judge verdict. Both the final label and disputed flag must be explicit human decisions; neither may be inferred from an incomplete criterion discussion. Current progress is recorded in `annotations/live-human-review.json`.
- Select exactly 10 obvious PASS, 10 obvious FAIL and 10 genuinely disputed cases. Disputed reasons must identify plausible competing interpretations of the criterion, rather than only unfamiliarity, verbosity or unrelated concerns. Obtain more actual/kit answers if needed; do not force flags to fill quotas.
- Apply the predeclared rule: first ten finalized annotations per group, sorted by candidate ID. Preserve all annotations and exclusions.
- Freeze selected responses, labels, rubric and provenance in Git before the first judge call. Current canonical label files remain legacy synthetic data. The runner must receive correct actual-source metadata before new measurement.
- Run five evaluations per case for baseline and a versioned correction on the same cases. Record model/digest, temperature, producing-agent prompt, judge system/rubric hashes, Git commits and raw outputs.
- Recompute raw and schema/evidence-valid human agreement, Wilson intervals/half-widths, self-consistency, group metrics, misses/false alarms and correction cost. Keep stability separate from correctness. Do not normalize invalid triggers after the run.
- Replace final report links and trust metrics only after actual new measurements. Record additional manual workload without claiming unmeasured improvement.

## Response-class check

Legacy HW08-011: “Your case has been flagged for further attention. You should receive an update soon, but I cannot confirm the outcome.” No explicit human role is positively committed to handoff/follow-up. It requires manual review even though v1.1 returned PASS 5/5.

LIVE-C001 explicitly reports escalation to a human support agent before reporting queued status. Queue wording alone therefore does not trigger the generic-routing rule. This routing assessment does not assign its final human verdict or waive either remaining criterion.

The separate policy does not change the judge's fixed `trigger` enum, rubric, historical verdicts or scores. Review records use `review_policy_version`, `manual_review_reasons` and an explicit human resolution; unresolved cases have no automatic acceptance. The policy is a mandatory manual procedure, not an implemented automated classifier.

## Preserved evidence and readiness

Original reports and all 300 historical outputs remain unchanged. Their freeze timeline and audits are linked through `calibration-comparison.md` and the archived prior audit. Existing offline checks remain historical technical evidence, not completion of the required actual-agent calibration. Live working-gate execution is also unclaimed.

**Not ready for final resubmission.** Next required human action: finish replacement annotations. No further mentor clarification is needed to act on these two corrections.
