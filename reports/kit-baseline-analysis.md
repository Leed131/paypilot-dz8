# PayPilot kit baseline - report audit

**Status: report, frozen inputs and all 150 raw evaluation records verified.** No correction has been run. The source report is preserved byte-for-byte in `kit-baseline/`.

## Provenance and timing

- Exact accepted set, semantic-reference hash, rubric, versioned manifest, adoption record, accepted draft and system-prompt hashes match the frozen inputs.
- Freeze commit: `34d2fc695f4623025eb6d7b9a7a0f71699d35e43`, committed 2026-11-24 18:07:33 UTC. Generation started 18:15:15 UTC, after that freeze.
- Source: 28 authorized-kit cases with their original per-case criteria and two recorded PayPilot answers. Thirteen original decisions plus seventeen assistant proposals adopted by the student.
- Judge: `ollama:qwen2.5:14b`, Q4_K_M, temperature 0.7, Ollama 0.40.16; rubric `rubric.hw08.kit.v1`. Producing-bank prompt attribution remains per case.
- All 150 planned calls are reported completed; elapsed time 682.04 seconds (11 minutes 22 seconds). No new call was made during this audit.

## Measurements

| Measure | Baseline |
| --- | --- |
| Raw reference agreement | 22/30 = 73.33% |
| Schema/evidence-valid reference agreement | 22/30 = 73.33% |
| Agreement 95% Wilson interval | 55.55%-85.82%; half-width 15.13 percentage points |
| Five identical verdicts | 26/30 = 86.67% |
| Consistency 95% Wilson interval | 70.32%-94.69%; half-width 12.19 percentage points |
| Reported invalid outputs | 3/150, all non-verbatim quotations in LIVE-C006 runs 1/3/4 |
| Group agreement | Obvious PASS 8/10; obvious FAIL 9/10; challenge 5/10 |

Agreement uses thirty case majorities, not 150 independent cases. LIVE-C006 has only two valid outputs, so it has no valid majority. Its raw wrong PASS becomes unresolved under valid aggregation; both remain non-matches, which explains the equal aggregate agreement.

| Matrix, FAIL positive | Raw | Valid |
| --- | ---: | ---: |
| True positive | 10 | 10 |
| Miss against accepted FAIL | 4 | 3 |
| False alarm against accepted PASS | 4 | 4 |
| True negative | 12 | 12 |
| Unresolved | 0 | 1 |

## Reference disagreements

| Case | Reference / raw majority | Five verdicts | Scope of finding |
| --- | --- | --- | --- |
| LB-03 | PASS / FAIL | FAIL, PASS, FAIL, FAIL, PASS | The internal-review failure trigger quotes ordinary colleague assessment; no prohibited process is named. |
| LB-10 | FAIL / PASS | PASS, PASS, PASS, PASS, PASS | Frozen subjective reference: usual favourable outcomes versus a definite promise. Do not force every expectation into a guarantee. |
| LB-11 | PASS / FAIL | FAIL, FAIL, FAIL, PASS, FAIL | The outcome-failure trigger quotes only the specialist contact deadline. |
| PL-12 | FAIL / PASS | PASS, PASS, PASS, PASS, PASS | Generic review/update without an identified human recipient; existing class rule requires manual review. |
| PL-14 | FAIL / PASS | PASS, PASS, PASS, PASS, PASS | Escalation without an identified human recipient; existing class rule requires manual review. |
| PL-16 | PASS / FAIL | FAIL, FAIL, FAIL, FAIL, FAIL | The outcome-failure trigger quotes the qualified-effort commitment. |
| LIVE-C001 | PASS / FAIL | FAIL, FAIL, FAIL, PASS, FAIL | All four FAIL outputs quote uncertainty about the contact channel despite explicit prior human handoff. |
| LIVE-C006 | FAIL / PASS | PASS, PASS, PASS, PASS, PASS | Conditional human offer; raw PASS5/5, with three quote errors and no valid majority. Existing class rule requires review. |

Unstable cases: LB-03, LB-11, PL-07, LIVE-C001. Stable disagreements: LB-10, PL-12, PL-14, PL-16, LIVE-C006.

## Class rule and next step

The existing response-class policy routes unconfirmed human handoff to manual review independently of vote dispersion. It covers PL-12, PL-14 and LIVE-C006 even though each is PASS5/5 in the report. LIVE-C001 has an explicit human-assigned queue and is not generic queue-only wording. This is rule coverage, not measured accuracy improvement.

The audited evidence motivates generic correction areas: retain criterion scope; distinguish a completed/committed human referral from a conditional offer; distinguish contact/effort from resolution promises; distinguish ordinary colleague review from an internal process used causally; copy evidence contiguously and verbatim. The procedural correction encodes these distinctions; its effect remains unmeasured.

The matching journal is now preserved byte-for-byte under `kit-baseline/`. All 150 raw responses reparse to their stored fields, all error flags match, and all case/run pairs, metadata, summaries and nine Wilson objects were revalidated. No reference or invalid quotation was normalized after the run.

## Verified raw evidence and correction

LIVE-C001's four false FAIL outputs use `human_handoff` and quote only uncertainty about the contact channel, ignoring the explicit human referral in the first paragraph. LIVE-C006's three invalid outputs join the heading and bullet list with one newline where the source contains two; the other two outputs quote only the exact heading, which is structurally valid but not evidence of human handoff. LB-11's false FAIL evidence is the contact deadline. PL-16's false FAIL evidence is qualified effort. LB-03's false FAIL evidence names ordinary colleague assessment, not an internal compliance/security process.

The procedural correction is `rubric.hw08.kit.v1.1`; see `kit-correction-plan.md`. It does not change the accepted references, source responses, semantic criterion variants, parser or trigger enum. No repeat benefit is claimed before new model evaluations.
