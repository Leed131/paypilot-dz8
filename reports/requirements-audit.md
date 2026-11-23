# Strict pre-submission audit - HW08

This audit checks the attached assignment against the actual repository, not against earlier assurances of readiness. The independent public repository is `Leed131/paypilot-dz8`; the submission branch is `main`.

**Decision:** structural, runtime and measured-calibration checks pass after the fixes below. Two substantive interpretation issues remain documented. They must not be represented as unconditional compliance or concealed by invented provenance or changed human labels.

## Mandatory requirements and evidence

| Requirement | Evidence / check | Status |
| --- | --- | --- |
| `judge-trust-statement.md`: six required statement rows and residual risk | Six-row decision note, concise risk table, reason and owner for each acceptance | Pass |
| At least 30 labelled cases, with 10 obvious PASS, 10 obvious FAIL, 10 disputed | Final canonical `evals/sets/l09_labels.jsonl`; exact 10/10/10 validated | Pass for explicit counts; disputed quality qualified below |
| Required case fields | All 30 contain question, recorded answer, criterion, rubric, PASS/FAIL, Boolean disputed, labelled date, rubric version, oracle/assertion, runs/gate and added_in; appropriate explanation field present | Pass |
| Blind labels committed before judge runs | Actual Git timeline below; no human label was changed after viewing judge verdicts | Pass for before-run freeze; annotation dates are coarsely recorded |
| Self-contained criterion, no hidden database or trace truth | The fixed-answer judge receives question, answer and rubric only; no trace, database, human label or annotation note enters the prompt | Pass |
| Split US-05 section 4 into threshold and semantic remainder | ESC-001 checks actual tool use; paired ESC-J01 uses exactly the same question and context to check answer wording | Pass after audit fix |
| Add at least five further judge cases | HW08-W001-W005 remain in addition to ESC-001 and ESC-J01: seven working cases, six judges | Pass after audit fix |
| Threshold is level 3, `daily`, `runs: 1` | `tool_sequence`, `must_include: [escalate_to_human]`; supplied T-14 fixture | Pass |
| Judge cases are `release`, `runs: 5`, never daily | All six working judge cases; calibration fixtures also carry release/runs 5 | Pass |
| Three observable rubric triggers | Human handoff, no outcome promise/resolution deadline, no internal-review reason; no subjective adequacy requirement or trace arithmetic | Pass |
| Verdict fields | `verdict`, `trigger`, `evidence_turn`, `quote`; validator flags unsupported enum values and non-verbatim evidence | Pass |
| Versioned rubric and changelog; each change measured | v1 and v1.1 preserved; both committed before their measurements; criterion and labels unchanged | Pass |
| Five evaluations per fixed answer via `tools/calibrate_run.py` | Two original journals, 150 unique id/run records each; no live agent answer substituted for `answer_under_test` | Pass |
| Wilson 95% interval and plus/minus X | Both source reports, comparison and statement; calculations independently reproduced | Pass |
| Agreement separate from self-consistency | Final raw agreement 25/30, valid agreement 24/30, self-consistency 28/30, clearly separated | Pass |
| Obvious/disputed agreement separately | Both reports contain all group counts and intervals; statement gives group agreements | Pass |
| Common-feature table and miss/false-alarm matrix | `baseline-analysis.md` and `calibration-comparison.md`; six raw mismatches are not all treated as independently proven errors | Pass |
| Correction remeasured on the same set, with its price and regressions | Same 30 dialogues and human labels; two recovered misses, new 011 miss, two unstable cases, four enum failures; 150 extra evaluations / 465.09 seconds | Pass |
| Judge model, rubric version, temperature match the report | `ollama:qwen2.5:14b`, v1.1, 0.7; hashes and model digest verified | Pass |
| Actual producing-agent prompt version | Measured reports honestly say `not_applicable_recorded_fixtures` because answers were authored as fixtures. The current bank target prompt is separately observed as `base.v1+D25+D27` after calibration | **Documented exception / mentor interpretation** |
| Residual risk follows L03/course template | Three rows use the supplied four-column format. Acceptance reasons and owner are stated; none is an undated deferral | Pass |
| Same `loader.py` as previous sets | Supplied course loader retained; only postponed annotations added for Python 3.8/3.9 compatibility. It loads both calibration and working sets | Pass |
| Clean-clone runnable code and gate failure exit | Standard-library runtime included; offline commands pass; absent/wrong-gate requested IDs, invalid outputs and ungraded/missing runs fail rather than silently pass | Pass for tested code; real bank gate not claimed |
| `reports/calibration-*.json` exists | `calibration-final.json` and `calibration-comparison.json`; unchanged originals and journals retained in subdirectories | Pass |
| Public separate GitHub repository, files in `main` | Repository metadata and branch checked through GitHub | Pass |
| No `.env` or committed keys | Tracked paths and supplied content checked; `.gitignore` excludes environment files | Pass for audited tree |
| Submit repository URL on the course platform | No submission has been sent during this audit | User action remains |

The assignment does not set a minimum judge accuracy, require successful optimization, or explicitly require executing the fresh-answer working set before submission. Low agreement, a documented regression, or an unaccepted autonomous-release decision are not themselves missing homework steps. Optional experiments with another model, a second annotator or mixed defects are not mandatory.

## Fixes made during this audit

1. Added ESC-J01, the semantic remainder paired with the T-14 threshold, while retaining all five additional custom judge cases. This follows the strictest reading of stage 1 rather than relying only on the later five-case minimum.
2. Fixed selective execution: a request containing a valid ID plus an unknown ID, or an ID outside the selected gate, now fails. No requested case may be silently dropped.
3. Added an explicit expected-profile preflight. The live runner defaults to requiring `lesson-09`, records the actual prompt/profile, and never silently changes the stand configuration. Offline validation does not pretend to verify a live profile.
4. Shortened the six-row trust statement, named US-05 section 4 and the target profile, and left full numbers/hashes/case details in the reports.
5. Added an exact Git timeline and separated producing-fixture provenance from the current bank target context. No input label date, raw report, response enum or measured score was rewritten.

## Verified freeze timeline (UTC)

| Event | Time | Evidence |
| --- | --- | --- |
| Human labels and initial rubric committed | 2026-11-23 13:26:30 | `b7fe17c6b8250e98cc7efe9c16ddba6d20dedde4` |
| Runtime used by baseline committed | 2026-11-23 14:13:55 | `9250a38fd98d5660d7eb59ba93812d0624627bd0` |
| Baseline generation began | 2026-11-23 14:15:20 | Original report started_at; 150-record journal |
| v1.1 rubric and same-label repeat input committed | 2026-11-23 14:31:29 | `0e3edad2760c2202059015107f2051d036829553` |
| Repeat generation began | 2026-11-23 14:32:40 | Original repeat report started_at; 150-record journal |
| Exact measured v1.1 bytes promoted to required canonical filename | 2026-11-23 14:57:57 | `1ed8e911953d5a2bd79bca0643d9f3d2bd7732b1` |

`labeled_on` is date-only and records assembled-set finalization, not recovered individual annotation timestamps. Precise Git metadata establishes the before-run ordering. The later canonical promotion retains the measured v1.1 bytes; its original pre-run alias and hash remain in the report. The `l09_labels_v1` alias preserves the original baseline bytes and historical commit.

## Remaining interpretation issue 1: agent prompt provenance

The assignment permits own cases, and our answers are explicitly synthetic fixtures authored during the discussion. They were not produced by the running PayPilot agent. Consequently, an actual producing-bank-agent prompt version cannot truthfully be added to those historical measurements. The reports' `agent_prompt_version=not_applicable_recorded_fixtures` and the trust statement match.

Read-only observation of the current stand confirms target profile `lesson-09`, active defects D18/D25/D27 and target prompt `base.v1+D25+D27`. `target-stand-context.json` timestamps that observation **after** both runs. It improves working-set context and is not retroactive producing-agent provenance.

This is a defensible explanation for synthetic cases, but requirement 7 literally asks for an agent prompt version. Acceptance of this exception cannot be certified by code. Do not replace N/A with the target version and imply that it generated the measured answers. If the mentor requires actual agent-produced answers, that requires new captured answers under a known prompt, human labels before judging, and new measurements.

## Remaining interpretation issue 2: meaning of disputed

The dataset contains ten explicit human disputed flags with explanations. Some explanations record learner uncertainty or concerns outside the criterion, rather than two plausible verdicts under the fixed rubric. Examples are 003 (timing/anxiety despite explicit internal-review disclosure), 020 (promise of a decision explanation rather than a resolution), 021 (explicit cancellation guarantee) and 033 (extra information).

These original human decisions were retained; no flags were changed after observing model results merely to obtain 10/10/10. If the course means each disputed case must be intrinsically ambiguous to two rubric-following readers, this is a qualitative dataset risk. It cannot be fixed by making the explanation sound more sophisticated or relabelling cases post hoc. New genuinely ambiguous examples would need human blind labels and a new measurement set. If disputed means the annotator's recorded uncertainty, the present records satisfy that interpretation.

## Suggested clarification before claiming unconditional readiness

1. For own synthetic answer fixtures, may `agent_prompt_version` be documented as inapplicable, with the live target prompt version recorded separately, or must all measured answers originate from a versioned bank agent?
2. Does disputed mean the annotator's recorded uncertainty, or must each such case admit competing verdicts under the fixed rubric?

These are concrete questions about the supplied wording. They are not a claim that another optimization run, a second model or a second annotator is mandatory. The complete measured work and original evidence remain available for review.
