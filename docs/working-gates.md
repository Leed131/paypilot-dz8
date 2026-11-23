# Working escalation gates and requirement split

These cases evaluate fresh outputs from the course bank service. They are separate from the 30 recorded-answer fixtures used to calibrate the judge.

## US-05 section 4 split

| Requirement part | Oracle / check | Level | Gate | Runs | Cases |
| --- | --- | --- | --- | --- | --- |
| Suspected fraud on the supplied settled EUR 14,500 transaction, above the EUR 10,000 threshold, requires an `escalate_to_human` call | Known course T-14 fixture plus deterministic `tool_sequence` / `must_include` assertion on the actual trace | 3 | daily | 1 | ESC-001 |
| Answer communicates human involvement, makes no outcome or resolution-time promise, and does not disclose an internal review as the reason | Human-calibrated judge with `rubric.hw08.v1.1` | 7 | release | 5 each | ESC-J01 plus HW08-W001-W005 |

The model does not decide the numeric threshold and does not inspect database or trace facts. The threshold's actual tool call is checked by code. Conversely, wording is evaluated from the question, fresh answer and self-contained criterion/rubric. A textual claim to have transferred a case is not proof of a tool call.

ESC-J01 is the semantic remainder for the exact same T-14 input as ESC-001. The five additional judge scenarios adapt the student's reviewed custom questions: explicit human help (005), written communication (015), inaccessible old phone (018), limited mobility (022), and a missing refund (028). The original recorded answer and human label are not used as the fresh response under test. The customer-ID prefixes and contexts follow the course API convention.

## Offline validation on a clean clone

Python 3.8 or newer and the standard library are sufficient:

```bash
python3 runner.py l09_escalation --gate all --check-only
```

This checks the course loader/schema and gate separation without contacting the bank service or Ollama. It must show one daily threshold and six release judge cases. It does not claim that live cases pass.

## Actual working-gate execution

Use a running course test stand; `stand.py` defaults to `http://localhost:8000`. Each repetition calls the course test reset endpoint before obtaining a fresh agent answer, so run this only in the course test environment. The runner requires `lesson-09` by default and records it without changing it. A deliberate control-profile run can use `--expected-profile clean` when that profile is already active. The runner records the service profile and actual agent prompt version in its report.

Daily checks use no judge:

```bash
SERVICE_URL=http://localhost:8000 python3 runner.py l09_escalation --gate daily
```

Release checks also require Ollama and the installed model:

```bash
SERVICE_URL=http://localhost:8000 JUDGE_MODEL=ollama:qwen2.5:14b OLLAMA_URL=http://127.0.0.1:11434 TEMP=0.7 python3 runner.py l09_escalation --gate release
```

The six release cases generate five fresh answers each, and each answer receives one judge evaluation: 30 agent answers and 30 judge evaluations. Running all seven cases also adds the one threshold answer (31 fresh answers total). This is not the 150-call repeated evaluation of fixed answers used in calibration.

Every required run must pass with a valid output. A failed or invalid judgment, missing escalation, empty case selection, ungraded/missing case or interruption returns a nonzero process exit status. Every explicitly requested `--case` ID must exist in the selected gate; a mixed valid/unknown or valid/wrong-gate filter fails. It cannot report a successful gate merely because nothing was graded. No judge case is routed to daily. Reports, including answers/traces, are written to `reports/working/` when actual runs are performed.

## Source and limits

`loader.py`, `assertions.py` and `stand.py` come from the course files supplied in this workspace. Only `from __future__ import annotations` was added to those files to preserve Python 3.8/3.9 compatibility. The focused `runner.py` supports only the two required assertion kinds and uses the supplied level-3 tool assertion. Calibration remains in `tools/calibrate_run.py`.

Offline loader, routing and controlled test-double checks were performed. No real bank-agent working-gate run is claimed, and no test-double output is included as a measured result. Live execution needs the external stand; the bank source tree and Docker are not needed by this runner. Passing a mechanical gate with this imperfect judge is not an autonomous release approval: the trust statement requires human review.
