# Judge Trust Statement - US-05 section 4

Status: **revision in progress; actual-agent calibration pending**. Autonomous release approval is withheld. The previous synthetic study is historical evidence, not a PayPilot performance estimate.

| Statement | Evidence and decision |
| --- | --- |
| Calibrated on | Replacement pool: 45 recorded course-agent answers, profile `lesson-09`, prompt `base.v1+D25+D27`, observed model `anthropic/claude-haiku-5.5`. Human annotation is in progress; no judge evaluations yet. Select 30 with 10 obvious PASS, 10 obvious FAIL and 10 genuinely disputed cases; freeze before judging. |
| Agreement | Pending actual-agent measurement. Historical synthetic scores cannot be transferred. Report case-majority agreement, schema/evidence-valid agreement and 95% Wilson intervals separately. |
| Self-consistency | Pending. Report five identical verdicts separately from human agreement: a stable answer can be wrong. |
| Where it fails | Historical HW08-011 received five false PASS verdicts: generic further-attention/update wording did not confirm human involvement. This motivates a response-class review rule whose operational effect is unmeasured. |
| What we do | Lidiia must review **unconfirmed human handoff**: status, queue, routing or update wording without positive confirmation of transfer to an explicit human role, or that such a role takes over or follows up; also conditional offers or refusals. Apply even with valid output and PASS 5/5. No automatic acceptance until review. Invalid, unstable and disputed cases also require review. Cost: additional human work. |
| Recalibrate | Freeze actual-agent labels before five evaluations per case; measure baseline and versioned correction on the same cases. Recalibrate after model, prompt, rubric, language, case-mix or adjudicated-reference changes. |

## Residual risk

Owner: Lidiia, the student annotator. This draft does not certify completion.

| What is not covered | What happens if it occurs | Why we live with it now | Defer or accept |
| --- | --- | --- | --- |
| Completed actual-agent calibration | Synthetic accuracy could be misattributed to PayPilot. | Withhold the final performance claim until labels and measurements exist. | Defer final submission. |
| Independent holdout and representative traffic | Results may not generalize. | A curated coursework set supports limited, supervised conclusions. | Accept this scope limitation; no deployment claim. |
| Automated response-class detection | A stable false PASS can evade dispersion checks. | The class check is mandatory and manual, independent of votes. An explicitly human-assigned queue alone does not trigger the generic-queue rule. | Accept manual use only; no autonomous approval. |

Policy: [manual-review.hw08.v1.json](policies/manual-review.hw08.v1.json). Progress: [live-human-review.json](annotations/live-human-review.json). Previous statement: [archived statement](reports/history/pre-mentor-correction/judge-trust-statement.md). Historical metrics: [calibration-comparison.md](reports/calibration-comparison.md).
