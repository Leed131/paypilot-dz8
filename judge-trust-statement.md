# Judge Trust Statement - US-05 section 4

Status: **accepted replacement references; new calibration pending**. Autonomous release approval remains withheld. Historical synthetic scores are not PayPilot performance estimates.

| Statement | Evidence and decision |
| --- | --- |
| Calibrated on | Accepted set: 28 authorized-kit cases with unchanged per-case criteria plus two recorded PayPilot answers; groups 10 obvious PASS, 10 obvious FAIL, 10 source-designed challenge cases. Thirteen prior references are preserved; seventeen assistant proposals were adopted by the student as a batch. `rubric.hw08.kit.v1` evaluates only each supplied criterion. |
| Agreement | New measurement pending. Report case-majority and schema/evidence-valid agreement separately, with 95% Wilson intervals and half-widths. Legacy synthetic scores do not transfer. |
| Self-consistency | Pending: report five identical verdicts with a 95% Wilson interval, separately from agreement with accepted references. A stable answer can still be wrong. |
| Where it fails | Historical HW08-011 was missed at PASS 5/5: further-attention/update wording did not confirm human involvement. New kit disagreements, including subjective LB-10/LB-12 references, require interpretation rather than automatic attribution of judge error. |
| What we do | Lidiia reviews **unconfirmed human handoff** whenever handoff is required: generic status, queue, routing or updates without positive transfer to an explicit human role or committed takeover/follow-up; also conditional offers/refusals. Apply even with valid PASS 5/5. No automatic acceptance until review. Invalid, unstable and disputed cases also require review. Cost: additional human work. |
| Recalibrate | Commit exact references and evaluator before five evaluations per case. After baseline analysis, version a correction and remeasure unchanged references. Recalibrate after model, prompt, semantic criterion, language, case mix or reference adjudication changes. |

## Residual risk

Owner: Lidiia, student reviewer. Acceptance is limited to supervised coursework. Kit producing prompts are unspecified; `base.v1+D25+D27` applies only to the two recorded live answers.

| What is not covered | What happens if it occurs | Why we live with it now | Defer or accept |
| --- | --- | --- | --- |
| Completed replacement calibration | An unsupported accuracy claim could be made. | Final metrics and readiness are withheld until new actual runs. | Defer final submission. |
| Independent holdout and representative combined-gate traffic | Pooled component scores may not generalize. | Reused lab cases and source-designed challenge flags are disclosed; only two cases use the combined criterion. | Accept limited coursework scope; no autonomous-gate claim. |
| Automated response-class detection | A stable false PASS can evade dispersion checks. | The class check is manual and independent of votes; an explicitly human-assigned queue is not generic queue-only wording. | Accept manual use only. |

References: [accepted set review](annotations/accepted-reference-review.md), [input manifest](annotations/accepted-reference-manifest.json), [manual policy](policies/manual-review.hw08.v1.json), and [requirements audit](reports/requirements-audit.md).
