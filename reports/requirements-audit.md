# HW08 - Required corrections after mentor review

Review date: 2026-11-24. Repository: `Leed131/paypilot-dz8`, branch `main`.

Karina's feedback resolves the source interpretation: calibration must use actual agent answers or the authorized kit pool. Assistant-authored answers do not support a PayPilot calibration claim. The previous decision to treat live collection as optional was incorrect and is withdrawn. The former audit is preserved in `history/pre-mentor-correction/`.

| Required correction | Evidence | Status |
| --- | --- | --- |
| Calibrate on actual-agent or authorized-kit answers | 45 course-agent answers, unchanged uploaded manifest and journal in `annotations/live-source/`; prompt `base.v1+D25+D27`, profile `lesson-09`, observed model `anthropic/claude-haiku-5.5`. | Source available; human annotation and new calibration pending. |
| Add answer-class rule in What we do | `manual-review.hw08.v1` requires human review for unconfirmed human handoff regardless of verdict, unanimous votes or valid schema. The primary statement includes the rule. | Documented manual policy; operational effect unmeasured. |

## Current replacement package

The official kit guide explicitly recommends combining the twelve already-labelled lab cases with the unlabelled pool and adding two obvious cases. The prepared draft selects LB-01 through LB-12, PL-01 through PL-16, LIVE-C001 and LIVE-C006. The kit files byte-match official Git blobs at commit `f5c235aa10a505f9d6f9e422ffd66917578c537b`.

- Thirteen existing human decisions are preserved: twelve exact laboratory cases under their unchanged original criteria, plus LIVE-C001.
- Seventeen proposed annotations are explicitly assistant-authored and await student review. No new human label or disputed flag is inferred.
- Designed benchmark strata are 10 obvious PASS, 10 obvious FAIL and 10 source-designed challenge cases. Challenge membership is separate from student uncertainty; six new challenge flags remain provisional. Preserve the historical note that the four laboratory disputed flags were documented after earlier judge runs.
- Use each kit case's original criterion. Do not substitute the common all-three-condition rubric; align the runner and rubric family before judging. The two live cases keep the combined criterion.
- Record official kit source/commit and unspecified kit producing prompts honestly. The observed bank prompt `base.v1+D25+D27` applies only to the two live answers. Raw live traces were not attached; no independent raw-trace verification is claimed.
- Verify groups after review, then freeze exact selected sources, references and evaluator in Git before any new judge call. The existing canonical files remain legacy synthetic data; the draft is not executable through the current set registry.
- Run five evaluations per case for baseline and a versioned correction on the same cases. Record model/digest, temperature, per-case source provenance, evaluator hashes, commits and raw outputs.
- Recompute raw and schema/evidence-valid reference agreement, Wilson intervals/half-widths, self-consistency, group metrics, misses/false alarms and cost. Keep stability separate from correctness; do not normalize invalid triggers afterward.
- Replace final report links and trust metrics only after new measurements. Old synthetic scores are not reused.

Files: `annotations/proposals/review-30.md`, `review-17.uk.md`, `kit-replacement-30.draft.jsonl` and `kit-replacement-manifest.json`. Original kit sources and earlier lab decisions are preserved under `annotations/kit-source/`.

## Response-class check

Legacy HW08-011: “Your case has been flagged for further attention. You should receive an update soon, but I cannot confirm the outcome.” No explicit human role is positively committed to handoff/follow-up. It requires manual review even though v1.1 returned PASS 5/5.

LIVE-C001 explicitly reports escalation to a human support agent before reporting queued status. Queue wording alone therefore does not trigger the generic-routing rule. This routing assessment does not assign its final human verdict or waive either remaining criterion.

The separate policy does not change the judge's fixed `trigger` enum, rubric, historical verdicts or scores. Review records use `review_policy_version`, `manual_review_reasons` and an explicit human resolution; unresolved cases have no automatic acceptance. The policy is a mandatory manual procedure, not an implemented automated classifier.

## Preserved evidence and readiness

Original reports and all 300 historical outputs remain unchanged. Their freeze timeline and audits are linked through `calibration-comparison.md` and the archived prior audit. Existing offline checks remain historical technical evidence, not completion of the required actual-agent calibration. Live working-gate execution is also unclaimed.

**Not ready for final resubmission.** Next required human action: review the seventeen assistant proposals as a batch. Evaluator alignment and actual calibration are also pending. No further mentor clarification is needed to act on these two corrections.
