# Optional live-answer extension (paused)

The completed 30-case own-fixture experiment, human labels and all 300 judge evaluations form the submission. The assignment permits own cases and does not explicitly require unmodified live answers. This separate optional extension collected 45 real agent answers with producing-prompt provenance; no judge was run and no final human labels were assigned. Annotation is paused, and these candidates are not included in the submitted dataset or its reported scores. The partial LIVE-C001 criterion discussion is preserved without inferring its final label. If this extension is resumed, the workflow below applies.

## Collection

`sets/l09_candidate_questions.jsonl` contains 45 distinct English customer questions, with course customer IDs and no prewritten answers, labels or intended groups. Questions vary human requests, appeals, accessibility, contact versus resolution, pending cancellation and suspected fraud. The group distribution is unknown until the real answers are assessed.

The collector requires the running course test service at `http://localhost:8000`, profile `lesson-09`, and exactly D18/D25/D27. It verifies the actual prompt text/version before and after every request, checks trace prompt-version evidence when exposed, starts fresh sessions and preserves exact responses. It resets course fixture state before each question; existing homework files and the stand profile are not changed. No judge module is imported or called.

Run from the updated repository:

```bash
python3 tools/collect_live_candidates.py --check-only
SERVICE_URL=http://localhost:8000 python3 tools/collect_live_candidates.py --preflight-only
SERVICE_URL=http://localhost:8000 python3 tools/collect_live_candidates.py
```

The first command is offline; the second reads configuration only; the third requests 45 real agent answers. The existing running service supplies its configured agent backend. The number of underlying agent LLM/tool calls may differ from the number of chat requests.

Each run creates a new directory under `data/live-candidates/<timestamp>/`:

- `candidates.jsonl`: exact recorded questions/answers plus producing-version provenance; no labels.
- `collection-manifest.json`: configuration, counts, timestamps and completion/failure status.
- `review.md`: readable questions and recorded answers, without suggested assessments.
- `sources/`: original responses, traces and full configuration snapshots for local provenance.
- `collection-journal.jsonl`: durable per-candidate collection status.

Raw collection directories are ignored by Git and are not published automatically. Preserve them locally. Attach `candidates.jsonl` and `collection-manifest.json` for the annotation stage. Errors or provenance mismatches stop collection and leave partial results explicitly marked; do not replace a failed answer with a fabricated response.

## Human annotation before judging

1. Apply the same frozen three-condition escalation criterion. The student supplies PASS/FAIL and a reason before any judge verdicts are shown for these new answers.
2. For a disputed case, record the particular wording and two plausible interpretations under the criterion that could lead to different verdicts. Lack of rubric familiarity, extra verbosity or a contact time not required by the criterion is not by itself evidence of intrinsic ambiguity. Clarify those issues before deciding the disputed flag.
3. Choose 10 obvious PASS, 10 obvious FAIL and 10 genuinely disputed examples after assessment, with readable explanations. If a group lacks enough real examples, collect additional candidates; the initial 45-question pool does not guarantee a balanced final set.
4. Preserve all original collected responses and exclude candidates transparently. Record actual annotation dates and the producing prompt version of each selected answer. Keep trace/configuration evidence outside the judge input; its criterion must remain self-contained.
5. Commit the new labelled dataset and its rubric before the first judge run on these new answers. Then perform the required baseline/correction measurements on the same selected cases, and rewrite the final trust statement from those actual results.

The original synthetic measurements are not measurements of this future live-answer dataset. Existing scores must not be reused under a new set name or input hash. The current producing prompt cannot be retroactively attributed to older synthetic answers.
