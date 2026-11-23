# HW08 - Final human annotation set

This repository contains 30 selected homework cases: 10 obvious PASS, 10 obvious FAIL and 10 disputed. The human labels and rubric were committed before calibration in `b7fe17c6b8250e98cc7efe9c16ddba6d20dedde4`. The v1 baseline is complete: 24/30 agreement (80%), 95% Wilson interval 62.69%-90.50%, and self-consistency 30/30. A procedural v1.1 repeat is pending; the final Judge Trust Statement will be completed after comparison.

## Files

- `evals/sets/l09_labels.jsonl`: canonical 30-case homework file.
- `sets/l09_labels.jsonl`: identical compatibility copy for the provided `tools/calibrate_run.py`, which hardcodes the `sets` directory.
- `HW08-annotations.md`: readable English questions, bot answers, explanations and a complete selection table.
- `annotations/all_recovered_32.jsonl`: all 32 complete human-labelled dialogues, including reserves.
- `annotations/reserve.jsonl`: HW08-004 and HW08-028, still obvious PASS, excluded only to obtain the requested exact group sizes. Both are standard handoff/no-refund examples; the more varied other PASS examples remain. Selection was made without running a judge on this set.
- `annotations/incomplete-records.json`: partial evidence for HW08-001/002, excluded from calibration rather than inventing missing dialogues.
- `rubrics/escalation.rubric.hw08.v1.json` and `rubrics/CHANGELOG.md`: common English criterion, three triggers and verdict format.
- `validation.json`: annotation-package checks performed, hash, and limitations.
- `reports/baseline/calibration-l09_labels-20261123T141520272523Z.json` and its `.evaluations.jsonl`: original completed baseline and all 150 raw evaluations.
- `reports/baseline-analysis.md` and `reports/baseline-audit.json`: verified metrics, six discrepancies, interpretation limits and correction plan.
- `evals/sets/l09_labels_v1_1.jsonl` and its identical `sets/` copy: same 30 dialogues and human labels, with procedural rubric version `rubric.hw08.v1.1`.
- `rubrics/escalation.rubric.hw08.v1.1.json`: revised procedure; baseline criterion and rubric are preserved.

## Annotation history and provenance

The cases were authored by the assistant during the course discussion and labelled by the user with assistant translation and rubric clarification. They are new discussion fixtures, not relabelled LB laboratory records. Explanations are English translations or faithful summaries, not verbatim original English user statements.

Accepted replacements for HW08-014 and HW08-015 are used; the discarded, unlabelled versions are not extra cases. Human corrections of 006, 007, 009, 013, 019, 027 and 033 are retained in per-case history. In particular, the user explicitly approved HW08-013 PASS -> FAIL on 2026-11-23. No label is changed to agree with a model.

`labeled_on: 2026-11-23` records finalization of this assembled set. It is not a backdated claim about when each original answer was labelled. `original_labeled_on` is null because precise original dates are not established. The exact packaged rubric wording was written at final assembly, not preregistered before every original annotation. The three substantive conditions were discussed during human labelling. Commit this assembled version before the first judge run on the selected set; verify chronology in the real repository rather than claiming it from these files alone.

Disputed flags preserve human uncertainty; they are not proof that a trained second annotator would disagree. Some original explanations concern extra information or missing timing, which are not independent failures under this rubric. That distinction is disclosed in the annotations. Cases 025/030 (obvious PASS) and 034 (disputed FAIL) preserve the human's different readings of qualified assistance and general reassurance; these judgments are not silently made uniform.

## Validation performed

The unmodified supplied course `loader.load` accepts all 30 selected cases. JSONL parsing, unique IDs and dialogues, required metadata, conditional explanations, English text, exact group counts and identical file copies pass. No judge or live agent was called during annotation-package validation. The subsequent completed v1 baseline is preserved under `reports/`; existing 12-case lab reports are not measurements of this new dataset.

## Run calibration on the computer with Ollama

Requirements: Git, Python 3.8 or newer, running Ollama, and the installed `qwen2.5:14b` model. Only the Python standard library is used. These cases contain recorded answers; the bank service and Docker are not needed for this calibration.

From this repository directory, check readiness without generating any judgments:

```bash
JUDGE_MODEL=ollama:qwen2.5:14b OLLAMA_URL=http://127.0.0.1:11434 TEMP=0.7 python3 tools/calibrate_run.py l09_labels_v1_1 --check-only
```

Then run the v1.1 repeat: five evaluations per case (150 additional model evaluations):

```bash
JUDGE_MODEL=ollama:qwen2.5:14b OLLAMA_URL=http://127.0.0.1:11434 RUNS=5 TEMP=0.7 python3 tools/calibrate_run.py l09_labels_v1_1
```

The command runs sequentially and prints progress. It uses the frozen question, answer and rubric; human labels and annotation notes are not sent to the judge. Keep the terminal open until the run finishes. Stop with Ctrl+C if necessary; preserve the partial evaluation journal and do not represent it as a complete calibration.

The runner verifies that both label copies match and are committed in Git, checks the selected model in Ollama, and records real measurement metadata. It writes a per-evaluation journal and a calibration report under `reports/`. A failed or interrupted run remains explicitly incomplete. Review verdict schema and evidence validity alongside raw agreement; invalid evidence must remain visible rather than being silently counted as a trustworthy success.

The report records `agent_prompt_version` as `not_applicable_recorded_fixtures` by default because these are assistant-authored dialogue fixtures, not fresh outputs from a versioned bank-agent prompt. If evaluating an actual versioned agent dataset instead, supply its real `AGENT_PROMPT_VERSION`; do not invent one for these fixtures. `.env` is not loaded by native Python and must not be committed.

## Baseline interpretation

All six disagreements are false PASS relative to the frozen human labels. Three (007, 021, 024) contain clear outcome or resolution-deadline violations. Three (012, 019, 034) involve ambiguous human-referral wording, reassurance, or reference/rubric alignment. Preserve their human labels and disclose these limitations; do not treat all six as independently proven model errors. Agreement on obvious PASS is 10/10, obvious FAIL 8/10, and disputed 6/10. There are six misses and zero false alarms against the frozen human reference.

The v1.1 procedure requires checking the whole answer and all three conditions before PASS. It does not add case-specific examples or an unconditional-follow-up requirement to fit disputed labels. Questions, answers, human labels, disputed flags, criterion, output schema, model configuration and system prompt remain unchanged. Compare all cases, including newly introduced errors. Same-set improvement is development evidence, not independent validation.

Use `l09_labels` instead of `l09_labels_v1_1` only when intentionally reproducing the original baseline. Neither baseline data nor its report is overwritten by the repeat.

## After the v1.1 repeat

Inspect the report's actual model, temperature, rubric version, set hash and annotation commit. Review overall and group agreement with 95% Wilson intervals and plus/minus widths, self-consistency separately, disagreements and the miss/false-alarm matrix. Apply a documented correction, remeasure on the same set, and complete the Judge Trust Statement with residual risk. The working threshold/judge set and the public-repository submission remain separate homework requirements.
