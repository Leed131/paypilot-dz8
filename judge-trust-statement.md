# Judge Trust Statement - US-05 section 4

Decision: retain v1 as a supervised aid; no autonomous release approval.

| Statement | Evidence and decision |
| --- | --- |
| Calibrated on | 30 English cases: 28 authorized-kit responses, two recorded PayPilot answers; 13 prior human decisions and 17 student-adopted assistant proposals. `ollama:qwen2.5:14b`, temperature 0.7. Preferred `rubric.hw08.kit.v1`; compared `rubric.hw08.kit.v1.1`. Live producing prompt: `base.v1+D25+D27`; kit prompts unspecified. |
| Agreement | Raw/valid v1: 22/30, 73.33%; 95% Wilson 55.55%-85.82%, half-width ±15.13 points. v1.1: 19/30, 63.33%; 45.51%-78.13%, ±16.31 points. Both recorded live cases disagree in both versions. |
| Self-consistency | v1: 26/30, 86.67%; Wilson 70.32%-94.69%. v1.1: 27/30, 90%; 74.38%-96.54%. Stable reference disagreements increase from five to nine; stability is separate from correctness. |
| Where it fails | Generic/conditional handoff is missed; contact, uncertainty and qualified effort produce false alarms. v1.1 recovers three reference matches and loses six. Invalid outputs remain three per run: quote errors become turn errors. LB-10/LB-12 retain reference caveats. |
| What we do | Lidiia must review unconfirmed human handoff: generic routing/status/updates without positive human-role assignment or committed takeover/follow-up, plus conditional offers/refusals. Apply even at valid PASS 5/5. An explicitly human-assigned queue is insufficient grounds to reject handoff. Invalid, unstable and disputed cases also require review. |
| Recalibrate | Freeze references before generation; repeat after model, rubric, prompt, language, case-mix or reference changes. Reject v1.1 as default. Its measured cost: 150 additional evaluations and 551.33 seconds; manual-review workload is additional. |

## Residual risk

Owner: Lidiia, student reviewer. Scope: supervised coursework. Challenge flags identify accepted kit-design strata; old lab exposure and batch adoption are disclosed. This is not an independent blind holdout.

| What is not covered | What happens if it occurs | Why we live with it now | Defer or accept |
| --- | --- | --- | --- |
| Independent adjudication and representative live traffic | Reference ambiguity or domain shift can distort the pooled estimate. | The kit is authorized, assistance is disclosed and both live cases' 0/2 agreement is explicit. | Accept limited study scope; defer deployment claims. |
| Reliable autonomous semantic/evidence checking | A unanimous or well-formed wrong verdict could pass. | The response-class check is mandatory and manual, independent of dispersion; humans retain release authority. Its operational effect is unmeasured. | Accept advisory use only; defer autonomous approval. |
| Fresh working-gate execution | Configuration can pass offline checks yet fail on the stand. | Required gate configuration and failure paths are tested; no live gate pass is claimed. | Defer live verification until an actual release decision. |

Wilson ± values are interval half-widths; explicit endpoints are authoritative. The pooled component result does not validate the combined gate. Original references and both runs remain unchanged; canonical promotion restores exact measured v1 bytes and creates no new observation.

Evidence: [comparison](reports/calibration-comparison.md), [selected report index](reports/calibration-final.json), [baseline audit](reports/kit-baseline-audit.json), [repeat audit](reports/kit-repeat-audit.json), [manual class policy](policies/manual-review.hw08.v1.json), and [requirements audit](reports/requirements-audit.md).
