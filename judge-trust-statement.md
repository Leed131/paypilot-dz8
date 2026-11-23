# Judge Trust Statement - US-05 section 4

Decision: human review required; no autonomous release approval. Target: `lesson-09`; calibration used synthetic recorded answers.

| Statement | Evidence and decision |
| --- | --- |
| Calibrated on | 30 English fixtures (10 obvious PASS, 10 obvious FAIL, 10 disputed), five evaluations each. `ollama:qwen2.5:14b`, temperature 0.7, `rubric.hw08.v1.1`. Measured `agent_prompt_version=not_applicable_recorded_fixtures`; these answers were assistant-authored, not bank-agent outputs. |
| Agreement | Raw 25/30 = 83.33%; 95% Wilson 66.44%-92.66%, half-width ±13.11 percentage points. Fully valid majority: 24/30 = 80%, interval 62.69%-90.50%, half-width ±13.90 points. Obvious PASS 10/10; obvious FAIL 9/10; disputed raw 6/10, valid 5/10. |
| Self-consistency | 28/30 cases (93.33%) have five identical verdicts; 008 and 031 are unstable. This is separate from human agreement. |
| Where it fails | Misses 011/021 are clear; 012/019/034 have interpretation issues. Case 009 has four invalid triggers. Raw misses/false alarms: 5/0; valid aggregation also has one unresolved case. |
| What we do | Lidiia reviews invalid, unstable and disputed cases. The correction recovered 007/024 but regressed 011, destabilized 008/031 and broke trigger formatting in 009. Cost: 150 extra evaluations, 465.09 seconds; valid agreement stayed 80%. |
| Recalibrate | After changes to model/digest, temperature, rubric, judge prompt, language, agent prompt or case mix; also after reference-label adjudication. Freeze labels before judging. |

## Residual risk

Owner for all decisions: Lidiia, the student annotator. Acceptance is limited to supervised coursework.

| What is not covered | What happens if it occurs | Why we live with it now | Defer or accept |
| --- | --- | --- | --- |
| Independent holdout / representative traffic | Performance may not transfer. | No generalization claim; human decisions remain required. | Accept for coursework only. |
| Adjudicated disputed labels / producing-agent prompt provenance | Apparent errors or applicability may be misinterpreted. | Synthetic origin and ambiguous references are disclosed. | Accept as a documented limitation, subject to mentor interpretation. |
| Reliable formatting and stability | A gate could accept an unreliable result. | Invalid/unstable results require human review. | Accept manual use only; autonomous approval withheld. |

Details and provenance: `reports/calibration-comparison.md`, `reports/requirements-audit.md`, and `reports/calibration-final.json`. The separately observed target prompt is `base.v1+D25+D27`; its post-run snapshot is not the origin of these synthetic answers.
