# Final HW08 readiness audit

Scope: the two mentor corrections and the supplied assignment, with supervised judge use only. Both actual-source runs and all 300 raw outputs are audited; no third tuning run or reference relabelling is needed.

## Mentor corrections

| Requested correction | Final evidence | Status |
| --- | --- | --- |
| Calibrate on actual-agent or authorized-kit answers | 28 official-kit cases with unchanged original criteria plus two recorded PayPilot answers; two 150-evaluation report/journal pairs and full raw-output audits. Earlier assistant-authored answers are excluded from this score. | Complete for the declared kit/live benchmark scope. |
| Add an answer-class rule in What we do | Unconfirmed human handoff requires human review even at valid PASS 5/5; generic progress/escalation and conditional offers are covered. Explicitly human-assigned queues are treated separately. The rule explains the historical HW08-011 problem and actual PL-12/PL-14/LIVE-C006 evidence. | Complete as a mandatory manual policy; no automated-policy performance claim. |

## Assignment checklist

| Requirement | Verified evidence | Result |
| --- | --- | --- |
| US-05 section 4 split | ESC-001 is level 3 / daily / 1 tool check; ESC-J01 is its paired semantic remainder, plus five additional release judge cases. No numeric threshold is delegated to the judge. | Pass |
| Observable rubric | Three trigger IDs; verdict/trigger/evidence_turn/quote; versioned packets and changelog. The preferred combined rendering is used by all six release cases. | Pass |
| Labelled set | Thirty unique question/answer pairs and IDs, 10 obvious PASS, 10 obvious FAIL, 10 accepted source-designed challenge flags; label/disputed/labeled_on/rubric_version and explanations present. | Pass with reference-provenance caveat below |
| Before-run freeze | Baseline labels/evaluator committed `34d2fc6` at 18:07:33 UTC before 18:15:15 UTC generation; correction inputs committed `f4969a3` at 18:57:35 UTC before 18:58:31 UTC generation. | Pass |
| Five evaluations per case | Exact 30×5 coverage/order in each journal; all 300 outputs reparse, fields/flags/model metadata and report summaries match. | Pass |
| Statistics and error classes | Raw/valid agreement, 95% Wilson endpoints/±half-widths, self-consistency separately, group intervals, miss/false-alarm matrices and common response-class table. | Pass |
| Measured correction and cost | Same semantic reference hash; same model/digest/temperature/system; three recovered matches, six regressions; additional 150 calls / 551.33 seconds. More stability accompanies worse agreement. | Pass; correction rejected |
| Trust document | Six main rows within the approximate 200–250-word target, model/rubric/temperature/producing-prompt scope, mandatory class rule and L03 residual-risk table with owner/decision. | Pass |
| Chain-ready files/runtime | Supplied loader accepts canonical set; daily 1 and release 6×5; offline runner checks pass; unknown/mixed/empty/failed/invalid/ungraded selections fail closed. No credentials included. | Pass offline; live gate not claimed |
| Languages | Final narrative/artifacts use English or Ukrainian; original raw evidence is preserved. | Pass |

The primary assignment (`Markdown pegado(6).md`, stages1–5 and lines242–259) specifies these configurations, repeated measurement, regression/cost reporting and runnable failure behavior. It does not set a minimum judge accuracy, require that optimization succeed, or explicitly require fresh-answer gate execution before submission. The mentor requested two specific changes; both are now addressed without fabricating a successful correction.

## Reference and applicability caveats

The official kit guide permits reuse of the twelve laboratory cases. Their original labels/dates are preserved; challenge grouping was documented after earlier laboratory judge runs. Seventeen additional proposals were adopted by the student as a batch before this study. This is not thirty new independent blind case assessments or an independent holdout. Source-designed challenge flags are not newly inferred personal uncertainty.

Kit producing prompt versions are unspecified; `base.v1+D25+D27` applies only to the two live answers. Both live combined cases disagree in both versions (0/2). The pooled score therefore does not validate fresh combined-gate performance. Raw live trace originals were not attached; source-record consistency is verified without claiming their independent reinspection.

LB-10 and LB-12 retain subjective reference interpretations. Reference matches/regressions are not automatically proven semantic improvements/errors. No label or quote was normalized after the run. The current canonical dataset restores exact measured v1 bytes after comparison; it is not a new trial or retroactive freeze claim.

## Final decision

Retain `rubric.hw08.kit.v1` only as a supervised aid; reject v1.1 as default and withhold autonomous release approval. Live working-gate execution remains a disclosed future-release check, not a claimed passed result. All original raw reports/journals, failed outputs and historical synthetic evidence remain available.

Evidence: [comparison](calibration-comparison.md), [selected report index](calibration-final.json), [baseline audit](kit-baseline-audit.json), [repeat audit](kit-repeat-audit.json), and [trust statement](../judge-trust-statement.md).
