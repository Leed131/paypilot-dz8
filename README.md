# HW08 - Final human annotation set

This package contains 30 selected homework cases: 10 obvious PASS, 10 obvious FAIL and 10 disputed. It is the annotation stage, not the completed homework submission. No new judge report or Judge Trust Statement is claimed.

## Files

- `evals/sets/l09_labels.jsonl`: canonical 30-case homework file.
- `sets/l09_labels.jsonl`: identical compatibility copy for the provided `tools/calibrate_run.py`, which hardcodes the `sets` directory.
- `HW08-annotations.md`: readable English questions, bot answers, explanations and a complete selection table.
- `annotations/all_recovered_32.jsonl`: all 32 complete human-labelled dialogues, including reserves.
- `annotations/reserve.jsonl`: HW08-004 and HW08-028, still obvious PASS, excluded only to obtain the requested exact group sizes. Both are standard handoff/no-refund examples; the more varied other PASS examples remain. Selection was made without running a judge on this set.
- `annotations/incomplete-records.json`: partial evidence for HW08-001/002, excluded from calibration rather than inventing missing dialogues.
- `rubrics/escalation.rubric.hw08.v1.json` and `rubrics/CHANGELOG.md`: common English criterion, three triggers and verdict format.
- `validation.json`: checks performed, hash, and limitations.

## Annotation history and provenance

The cases were authored by the assistant during the course discussion and labelled by the user with assistant translation and rubric clarification. They are new discussion fixtures, not relabelled LB laboratory records. Explanations are English translations or faithful summaries, not verbatim original English user statements.

Accepted replacements for HW08-014 and HW08-015 are used; the discarded, unlabelled versions are not extra cases. Human corrections of 006, 007, 009, 013, 019, 027 and 033 are retained in per-case history. In particular, the user explicitly approved HW08-013 PASS -> FAIL on 2026-11-23. No label is changed to agree with a model.

`labeled_on: 2026-11-23` records finalization of this assembled set. It is not a backdated claim about when each original answer was labelled. `original_labeled_on` is null because precise original dates are not established. The exact packaged rubric wording was written at final assembly, not preregistered before every original annotation. The three substantive conditions were discussed during human labelling. Commit this assembled version before the first judge run on the selected set; verify chronology in the real repository rather than claiming it from these files alone.

Disputed flags preserve human uncertainty; they are not proof that a trained second annotator would disagree. Some original explanations concern extra information or missing timing, which are not independent failures under this rubric. That distinction is disclosed in the annotations. Cases 025/030 (obvious PASS) and 034 (disputed FAIL) preserve the human's different readings of qualified assistance and general reassurance; these judgments are not silently made uniform.

## Validation performed

The unmodified supplied course `loader.load` accepts all 30 selected cases. JSONL parsing, unique IDs and dialogues, required metadata, conditional explanations, English text, exact group counts and identical file copies pass. No judge or live agent was called. Existing 12-case lab calibration reports do not measure this dataset.

## Next steps in the course repository

Review and copy the files into the homework repository. Keep the canonical and compatibility copies identical if using the original calibration script. Inspect the diff, then commit these human annotations and rubric before calibration. Do not publish `.env` or keys.

Next, run the course calibration script for five evaluations per case. The existing script reads `sets/l09_labels.jsonl`; adding only the canonical `evals/sets` file will not redirect it. Confirm the report includes the actual model, temperature, rubric version and set hash; the provided older calibration script does not automatically write all required rubric metadata. Calculate agreement with a 95% Wilson interval and plus/minus width, self-consistency separately, group agreement, disagreement analysis and the miss/false-alarm matrix. Apply a documented correction, remeasure, and update the Judge Trust Statement. The working threshold/judge set and the public-repository submission remain separate homework requirements.
