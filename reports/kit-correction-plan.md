# Procedural correction for kit v1.1 - frozen before repeat

This proposal changes the evaluation procedure, not source answers, semantic criteria, labels, flags, trigger enum, system prompt or validator. No model was run to assess the proposal.

Observed raw evidence supports these targets:

- LB-03: the same ordinary-colleague-review quote accompanies both PASS and FAIL. The failure trigger is the internal-review condition, but the quote names no prohibited internal process.
- LB-11: the failure evidence is a deadline for specialist contact. PL-15 passes under a comparable contact-only condition, so the issue is not uniform across contact-time answers.
- PL-16: the model repeatedly treats qualified effort as an outcome promise. Preserve the distinction between bounded effort and a definite recovery commitment.
- LIVE-C001: all four FAIL outputs quote uncertainty about the communication channel, despite the explicit human transfer earlier in the answer.
- PL-12 and PL-14: PASS 5/5 on generic review/escalation without an identified human recipient. LIVE-C006: PASS 5/5 on a conditional offer.
- LIVE-C006 runs 1/3/4: quotations omit the blank line before the bullet list. The words are otherwise present, but the extracted span is not a contiguous verbatim substring. Preserve the errors; do not normalize them afterward.

LB-10 remains a reference-interpretation caveat. The frozen human FAIL is broader than a literal definite-promise reading of a usual expectation. Do not rewrite the criterion to force that label. LB-12's broad security-preface reading also remains a reference caveat. Team wording in LB-09/PL-11 is ambiguous; the correction should not silently require the literal word human.

## Five checks and risks before/after the repeat

1. **Semantic freeze:** exact criterion variants, source texts, labels and challenge flags must match v1; only the procedural template/version changes. Verify the shared semantic fixture/reference hash, not the full byte hash that necessarily includes the new rubric version.
2. **No fitting by ID:** rendered instructions must contain no case IDs, reference labels, answer examples or copied source responses. Only the supplied criterion is substituted into the template. This proposal's one placeholder and absence of complete source-answer strings were checked offline.
3. **Handoff behavior to measure:** generic/conditional handoffs should be distinguished from explicit human transfer plus queue/channel uncertainty. Do not add immediate availability, a guaranteed channel or unconditional contact as new requirements. More restrictive wording could regress team/specialist examples; measure rather than presume improvement.
4. **Other criterion behavior to measure:** contact deadlines and qualified effort should not be promoted to resolution promises; ordinary colleague assessment should not be promoted to a prohibited internal reason. Excessively permissive qualification rules could miss actual guarantees; retain whole-answer checking. Do not use LB-10 disagreement as a reason to tune every optimistic expectation into FAIL.
5. **Evidence and comparison:** keep the existing parser and exact-substring test unchanged. The prompt encourages short contiguous quotations instead of whitespace reconstruction. Repeat all 30 cases five times with the same model/digest and temperature, report raw and evidence-valid agreement, self-consistency intervals, regressions, invalid outputs and measured time/cost. No accuracy gain or schema improvement is established until that repeat.

## Frozen repeat protocol

The shared semantic fixture/reference SHA-256 is `15ab35384ac454af9366785c4b442533b216746842372db7d084b7ad9a871eb8`. The baseline alias and its versioned manifest remain unchanged; the repeat alias is `l09_labels_kit_v1_1`. The canonical file points to the same repeat bytes. Reference adoption timestamps and all original lab dates are retained.

Run all 30 cases five times with `ollama:qwen2.5:14b`, temperature 0.7. Confirm the installed digest matches baseline `7cdf5a0187d5c58cc5d369b255592f7841d1c4696d45a8c8a9489440385b22f6` before interpreting the change as a controlled comparison. The runtime records actual metadata. This is one bundled procedural revision; component effects cannot be isolated.

Cost to measure: 150 additional local evaluations, elapsed time and extra instruction tokens. Longer instructions may increase latency; stricter handoff reading may regress team/specialist language, while qualified-outcome/internal-review clarification may disagree with subjective accepted references. Same-set development is disclosed; it is not independent validation.

The existing manual response-class policy independently routes generic or conditional handoff replies to human review even at PASS5/5. This addresses stable actual-source misses as well as the historical HW08-011 pattern. No measured operational policy gain is claimed.
