# Judge Trust Statement - US-05 section 4

Status: **baseline and all raw records audited; procedural repeat pending**. Autonomous release approval remains withheld. Historical synthetic scores are not PayPilot performance estimates.

| Statement | Evidence and decision |
| --- | --- |
| Calibrated on | Accepted set: 28 authorized-kit cases with unchanged per-case criteria plus two recorded PayPilot answers; groups 10 obvious PASS, 10 obvious FAIL, 10 source-designed challenge cases. Thirteen prior references are preserved; seventeen assistant proposals were adopted by the student as a batch. Baseline `rubric.hw08.kit.v1` evaluates each supplied criterion; procedural v1.1 is frozen for the same-reference repeat. |
| Agreement | Raw and valid agreement are 22/30 = 73.33%; 95% Wilson 55.55%-85.82%, half-width 15.13 points. LIVE-C006 has no valid majority; equal totals do not mean identical failure composition. All 150 raw records and flags have now been revalidated. |
| Self-consistency | 26/30 = 86.67% have five identical verdicts; 95% Wilson 70.32%-94.69%, half-width 12.19 points. Stable disagreements still occur, including PL-12, PL-14 and LIVE-C006. |
| Where it fails | Historical HW08-011 was missed at PASS 5/5: further-attention/update wording did not confirm human involvement. The baseline has eight reference disagreements and three exact-quote errors caused by omitted newlines. Subjective LB-10/LB-12 references require interpretation; discrepancies are not automatically proven judge errors. |
| What we do | Lidiia reviews **unconfirmed human handoff** whenever handoff is required: generic status, queue, routing or updates without positive transfer to an explicit human role or committed takeover/follow-up; also conditional offers/refusals. Apply even with valid PASS 5/5. No automatic acceptance until review. Invalid, unstable and disputed cases also require review. Cost: additional human work. |
| Recalibrate | Commit exact references and evaluator before five evaluations per case. After baseline analysis, version a correction and remeasure unchanged references. Recalibrate after model, prompt, semantic criterion, language, case mix or reference adjudication changes. |

## Residual risk

Owner: Lidiia, student reviewer. Acceptance is limited to supervised coursework. Kit producing prompts are unspecified; `base.v1+D25+D27` applies only to the two recorded live answers.

| What is not covered | What happens if it occurs | Why we live with it now | Defer or accept |
| --- | --- | --- | --- |
| Completed replacement calibration | The full evidence or a correction benefit could be overstated. | The full baseline is audited; the frozen correction still requires actual measurement. | Defer final submission. |
| Independent holdout and representative combined-gate traffic | Pooled component scores may not generalize. | Reused lab cases and source-designed challenge flags are disclosed; only two cases use the combined criterion. | Accept limited coursework scope; no autonomous-gate claim. |
| Automated response-class detection | A stable false PASS can evade dispersion checks. | The class check is manual and independent of votes; an explicitly human-assigned queue is not generic queue-only wording. | Accept manual use only. |

References: [accepted set review](annotations/accepted-reference-review.md), [input manifest](annotations/accepted-reference-manifest.json), [manual policy](policies/manual-review.hw08.v1.json), and [requirements audit](reports/requirements-audit.md).

Actual baseline: [analysis](reports/kit-baseline-analysis.md), [report audit](reports/kit-baseline-audit.json). The immutable input manifest remains the pre-run snapshot.

Prepared correction: [kit-correction-plan.md](reports/kit-correction-plan.md). Its extra 150 evaluations and elapsed cost remain to be measured.
