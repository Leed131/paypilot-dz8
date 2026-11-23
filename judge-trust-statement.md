# Judge Trust Statement - HW08 escalation

Decision: use only with human review; autonomous release gating is not accepted.

| Statement | Measured evidence and decision |
| --- | --- |
| Calibrated on | 30 English recorded fixtures: 10 obvious PASS, 10 obvious FAIL, 10 disputed; five evaluations each. Final canonical set is identical to measured `l09_labels_v1_1`. Judge: `ollama:qwen2.5:14b` (Q4_K_M); temperature 0.7; Ollama 0.40.16; `rubric.hw08.v1.1`; system prompt `course-judge-system.hw08.v1`. Agent prompt version: `not_applicable_recorded_fixtures` (assistant-authored fixtures, not live bank-agent outputs). |
| Agreement | Raw: 25/30 = 83.33%, 95% Wilson interval 66.44%-92.66%, half-width plus/minus 13.11 percentage points. Requiring schema/evidence-valid majority: 24/30 = 80.00%, interval 62.69%-90.50%, half-width 13.90 points. Obvious PASS: 10/10; obvious FAIL: 9/10; disputed: raw 6/10, valid 5/10. |
| Self-consistency | 28/30 cases have the same verdict in all five runs (93.33%). Cases 008 and 031 each split four FAIL to one PASS. Stability is separate from human agreement. |
| Where it fails | Clear remaining misses: 011 does not confirm human handoff; 021 guarantees cancellation. Raw misses also include ambiguous 012/019/034. Case 009 has four invalid trigger enums and no fully valid majority. Against human labels, raw misses/false alarms = 5/0; strict aggregation also has one unresolved case. |
| What we do | Human review of invalid, unstable, ambiguous and outcome-promise/handoff cases. Whole-answer checking recovered 007/024, but introduced a new miss in 011, lost stability in 008/031 and broke trigger formatting in 009. Cost: 150 additional evaluations and 465.09 seconds; valid agreement stayed 80%. Record v1.1 as a supervised aid, not a successful autonomous gate. Owner: student annotator/reviewer. |
| Recalibrate | Before relying on changed model/digest, temperature, backend, rubric, system prompt, language or case distribution; also after introducing a real agent prompt or adjudicating reference-label ambiguities. Keep labels committed before judging and preserve each prior run. |

## Residual risk

The rows below use the course template's residual-risk columns. Decisions apply to this supervised coursework scope, not a production launch approval.

| What is not covered | What happens if it occurs | Why we live with it now | Defer or accept |
| --- | --- | --- | --- |
| Independent holdout and representative deployment traffic | Agreement may not transfer to new cases; 30 curated cases can overstate confidence. | This is explicitly same-set calibration with no independent-validation claim. | Accept for supervised coursework only; reason: every disputed/high-risk decision remains with a human. Owner: student reviewer. |
| Independently adjudicated labels for 012/019/034 | A reference/rubric mismatch can be mistaken for model error or obscure one. | Preserve original labels for a fair comparison and disclose their ambiguity instead of tuning them after seeing judge results. | Accept this measurement limitation; reason: no autonomous decision is authorized from these labels. Owner: student annotator. |
| Reliable structured output and stable future evaluations | Wrong enums or variable verdicts can produce unreliable gate outcomes. | The observed errors are retained, flagged and excluded from valid-majority successes; invalid/unstable cases require human review. | Accept only the manual-review workflow; reason: automatic release acceptance is withheld. Owner: student reviewer. |

## Evidence

`reports/calibration-final.json` indexes the unchanged measured repeat. Full comparison, group intervals, matrices and the correction's cost are in `reports/calibration-comparison.md` and `.json`; all 300 raw evaluations are preserved under `reports/baseline/` and `reports/repeat/`. Model digest: `7cdf5a0187d5c58cc5d369b255592f7841d1c4696d45a8c8a9489440385b22f6`. System prompt SHA-256: `ff1786fc7ade078d24b1f26c8f994d88af7b5646c418a1aa0d97f4408f290b49`.
