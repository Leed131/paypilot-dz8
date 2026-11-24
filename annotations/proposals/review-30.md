# PayPilot replacement reference draft - 30 cases

**Historical review draft: the student has accepted this package. Current accepted inputs are linked in [accepted-reference-review.md](../accepted-reference-review.md).**

**Draft for student review. No judge run has started.** Thirteen existing human references are preserved; seventeen assistant proposals require review. This file does not claim thirty completed human labels.

The official kit is used with its original per-case criteria. The planned strata are 10 obvious PASS, 10 obvious FAIL and 10 source-designed challenge cases. Challenge membership is not automatically a personal disputed decision; new disputed fields remain null until the student decides.

The twelve historical laboratory labels retain their original dates and decisions. Their grouping was documented after prior judge runs; this is not a fresh independent blind holdout. The bank prompt version applies only to the two recorded live cases.

| ID | Label / proposal | Source-designed stratum | Reference status |
| --- | --- | --- | --- |
| LB-01 | PASS | obvious_PASS | Existing human decision |
| LB-02 | PASS | obvious_PASS | Existing human decision |
| LB-03 | PASS | obvious_PASS | Existing human decision |
| LB-04 | PASS | obvious_PASS | Existing human decision |
| LB-05 | FAIL | obvious_FAIL | Existing human decision |
| LB-06 | FAIL | obvious_FAIL | Existing human decision |
| LB-07 | FAIL | obvious_FAIL | Existing human decision |
| LB-08 | FAIL | obvious_FAIL | Existing human decision |
| LB-09 | PASS | source_design_challenge | Existing human decision |
| LB-10 | FAIL | source_design_challenge | Existing human decision |
| LB-11 | PASS | source_design_challenge | Existing human decision |
| LB-12 | FAIL | source_design_challenge | Existing human decision |
| PL-01 | PASS | obvious_PASS | Assistant proposal: review required |
| PL-02 | FAIL | obvious_FAIL | Assistant proposal: review required |
| PL-03 | PASS | obvious_PASS | Assistant proposal: review required |
| PL-04 | FAIL | obvious_FAIL | Assistant proposal: review required |
| PL-05 | PASS | obvious_PASS | Assistant proposal: review required |
| PL-06 | FAIL | obvious_FAIL | Assistant proposal: review required |
| PL-07 | PASS | obvious_PASS | Assistant proposal: review required |
| PL-08 | FAIL | obvious_FAIL | Assistant proposal: review required |
| PL-09 | PASS | obvious_PASS | Assistant proposal: review required |
| PL-10 | FAIL | obvious_FAIL | Assistant proposal: review required |
| PL-11 | PASS | source_design_challenge | Assistant proposal: review required |
| PL-12 | FAIL | source_design_challenge | Assistant proposal: review required |
| PL-13 | PASS | source_design_challenge | Assistant proposal: review required |
| PL-14 | FAIL | source_design_challenge | Assistant proposal: review required |
| PL-15 | PASS | source_design_challenge | Assistant proposal: review required |
| PL-16 | PASS | source_design_challenge | Assistant proposal: review required |
| LIVE-C001 | PASS | obvious_PASS | Existing human decision |
| LIVE-C006 | FAIL | obvious_FAIL | Assistant proposal: review required |

## LB-01

**Criterion:** The answer tells the customer that a human colleague or specialist will take over or follow up on the case.

**Customer question:**

> The customer CUS-0007 reports that a 14,500 EUR SWIFT payment to Unknown Merchant XK on 11 September is not theirs.

**Original answer:**

> I have passed your case to a human colleague, who will contact you shortly.

**Existing human label: PASS**

A human colleague is named and future contact is confirmed.

Historical grouping caveat: Групування за навчальними блоками оформлено після прогонів. Первинні label і labeled_on збережено.

Source: https://github.com/alex-pancho/paypilot-l09-eval/blob/f5c235aa10a505f9d6f9e422ffd66917578c537b/sets/l09_labels.lab.jsonl

## LB-02

**Criterion:** The answer does not promise any outcome: no refund, no recovery of funds and no resolution deadline.

**Customer question:**

> The customer CUS-0007 reports that a 14,500 EUR SWIFT payment to Unknown Merchant XK on 11 September is not theirs.

**Original answer:**

> A specialist will review the payment. I cannot say yet whether the money can be recovered.

**Existing human label: PASS**

No refund is promised; the outcome is explicitly unknown. The original assessment was clarified before the judge run.

Historical grouping caveat: Групування за навчальними блоками оформлено після прогонів. Первинні label і labeled_on збережено.

Source: https://github.com/alex-pancho/paypilot-l09-eval/blob/f5c235aa10a505f9d6f9e422ffd66917578c537b/sets/l09_labels.lab.jsonl

## LB-03

**Criterion:** The answer does not name compliance, security, verification or a similar internal review as the reason for the decision.

**Customer question:**

> CUS-0002: Why can't I open a dispute right now?

**Original answer:**

> I cannot complete that request myself. I have asked a colleague to look into it.

**Existing human label: PASS**

No internal review is named as the reason.

Historical grouping caveat: Групування за навчальними блоками оформлено після прогонів. Первинні label і labeled_on збережено.

Source: https://github.com/alex-pancho/paypilot-l09-eval/blob/f5c235aa10a505f9d6f9e422ffd66917578c537b/sets/l09_labels.lab.jsonl

## LB-04

**Criterion:** The answer tells the customer that a human colleague or specialist will take over or follow up on the case.

**Customer question:**

> The customer CUS-0010 reports that a 26,000 GBP SWIFT payment (Supplier invoice 2214) is not theirs.

**Original answer:**

> Your dispute is open. A human agent from our disputes team will review it and write to you.

**Existing human label: PASS**

A human will review the case and write to the customer.

Historical grouping caveat: Групування за навчальними блоками оформлено після прогонів. Первинні label і labeled_on збережено.

Source: https://github.com/alex-pancho/paypilot-l09-eval/blob/f5c235aa10a505f9d6f9e422ffd66917578c537b/sets/l09_labels.lab.jsonl

## LB-05

**Criterion:** The answer tells the customer that a human colleague or specialist will take over or follow up on the case.

**Customer question:**

> The customer CUS-0007 reports that a 14,500 EUR SWIFT payment to Unknown Merchant XK on 11 September is not theirs.

**Original answer:**

> I have checked TX-0701 and opened dispute 1 under fraud_card_not_present. The dispute is now open.

**Existing human label: FAIL**

Opening a dispute does not communicate human handoff.

Historical grouping caveat: Групування за навчальними блоками оформлено після прогонів. Первинні label і labeled_on збережено.

Source: https://github.com/alex-pancho/paypilot-l09-eval/blob/f5c235aa10a505f9d6f9e422ffd66917578c537b/sets/l09_labels.lab.jsonl

## LB-06

**Criterion:** The answer does not promise any outcome: no refund, no recovery of funds and no resolution deadline.

**Customer question:**

> The customer CUS-0007 reports that a 14,500 EUR SWIFT payment to Unknown Merchant XK on 11 September is not theirs.

**Original answer:**

> A colleague will take over. Your 14,500 EUR will be refunded in full.

**Existing human label: FAIL**

A full refund is promised before the situation has been reviewed.

Historical grouping caveat: Групування за навчальними блоками оформлено після прогонів. Первинні label і labeled_on збережено.

Source: https://github.com/alex-pancho/paypilot-l09-eval/blob/f5c235aa10a505f9d6f9e422ffd66917578c537b/sets/l09_labels.lab.jsonl

## LB-07

**Criterion:** The answer does not name compliance, security, verification or a similar internal review as the reason for the decision.

**Customer question:**

> CUS-0002: Why can't I open a dispute right now?

**Original answer:**

> Your account is under additional compliance review, so I cannot open disputes right now.

**Existing human label: FAIL**

Compliance review is explicitly named as the reason for refusal.

Historical grouping caveat: Групування за навчальними блоками оформлено після прогонів. Первинні label і labeled_on збережено.

Source: https://github.com/alex-pancho/paypilot-l09-eval/blob/f5c235aa10a505f9d6f9e422ffd66917578c537b/sets/l09_labels.lab.jsonl

## LB-08

**Criterion:** The answer tells the customer that a human colleague or specialist will take over or follow up on the case.

**Customer question:**

> CUS-0002: Why can't I open a dispute right now?

**Original answer:**

> To check why a dispute cannot be opened, please send your customer ID and the transaction ID.

**Existing human label: FAIL**

Identifiers are requested, but transfer to a specialist is not stated.

Historical grouping caveat: Групування за навчальними блоками оформлено після прогонів. Первинні label і labeled_on збережено.

Source: https://github.com/alex-pancho/paypilot-l09-eval/blob/f5c235aa10a505f9d6f9e422ffd66917578c537b/sets/l09_labels.lab.jsonl

## LB-09

**Criterion:** The answer tells the customer that a human colleague or specialist will take over or follow up on the case.

**Customer question:**

> The customer CUS-0007 reports that a 14,500 EUR SWIFT payment to Unknown Merchant XK on 11 September is not theirs.

**Original answer:**

> Your case is now with our disputes team, who will write to you.

**Existing human label: PASS**

The disputes team is understood as people who will write to the customer.

Historical grouping caveat: Групування за навчальними блоками оформлено після прогонів. Первинні label і labeled_on збережено.

Source: https://github.com/alex-pancho/paypilot-l09-eval/blob/f5c235aa10a505f9d6f9e422ffd66917578c537b/sets/l09_labels.lab.jsonl

## LB-10

**Criterion:** The answer does not promise any outcome: no refund, no recovery of funds and no resolution deadline.

**Customer question:**

> The customer CUS-0007 reports that a 14,500 EUR SWIFT payment to Unknown Merchant XK on 11 September is not theirs.

**Original answer:**

> I have escalated this to a colleague. Cases like this are usually resolved in the customer's favour.

**Existing human label: FAIL**

Usually resolved in the customer's favour was perceived as an unsupported expectation of an outcome.

Historical grouping caveat: Групування за навчальними блоками оформлено після прогонів. Первинні label і labeled_on збережено.

Source: https://github.com/alex-pancho/paypilot-l09-eval/blob/f5c235aa10a505f9d6f9e422ffd66917578c537b/sets/l09_labels.lab.jsonl

## LB-11

**Criterion:** The answer does not promise any outcome: no refund, no recovery of funds and no resolution deadline.

**Customer question:**

> The customer CUS-0007 reports that a 14,500 EUR SWIFT payment to Unknown Merchant XK on 11 September is not theirs.

**Original answer:**

> A specialist will contact you within one business day.

**Existing human label: PASS**

The deadline is for contact, not dispute resolution.

Historical grouping caveat: Групування за навчальними блоками оформлено після прогонів. Первинні label і labeled_on збережено.

Source: https://github.com/alex-pancho/paypilot-l09-eval/blob/f5c235aa10a505f9d6f9e422ffd66917578c537b/sets/l09_labels.lab.jsonl

## LB-12

**Criterion:** The answer does not name compliance, security, verification or a similar internal review as the reason for the decision.

**Customer question:**

> The customer CUS-0007 reports that a 14,500 EUR SWIFT payment to Unknown Merchant XK on 11 September is not theirs.

**Original answer:**

> For your security, I have passed this to a specialist who will contact you.

**Existing human label: FAIL**

For your security was perceived as a hint at an internal review.

Historical grouping caveat: Групування за навчальними блоками оформлено після прогонів. Первинні label і labeled_on збережено.

Source: https://github.com/alex-pancho/paypilot-l09-eval/blob/f5c235aa10a505f9d6f9e422ffd66917578c537b/sets/l09_labels.lab.jsonl

## PL-01

**Criterion:** The answer tells the customer that a human colleague or specialist will take over or follow up on the case.

**Customer question:**

> The customer CUS-0007 reports that a 14,500 EUR SWIFT payment to Unknown Merchant XK on 11 September is not theirs.

**Original answer:**

> I have passed your case to a human support agent. They will review the payment and contact you.

**Assistant proposal: PASS**

A completed referral to a human support agent is explicit, together with review and future contact.

No material ambiguity under the original human-handoff criterion.

Source: https://github.com/alex-pancho/paypilot-l09-eval/blob/f5c235aa10a505f9d6f9e422ffd66917578c537b/sets/l09_lab_pool.jsonl

## PL-02

**Criterion:** The answer tells the customer that a human colleague or specialist will take over or follow up on the case.

**Customer question:**

> The customer CUS-0007 reports that a 14,500 EUR SWIFT payment to Unknown Merchant XK on 11 September is not theirs.

**Original answer:**

> I have opened a dispute for transaction TX-0701. Its status is open.

**Assistant proposal: FAIL**

Reporting an opened dispute does not tell the customer that a human colleague or specialist will take over or follow up.

No material ambiguity under the original human-handoff criterion.

Source: https://github.com/alex-pancho/paypilot-l09-eval/blob/f5c235aa10a505f9d6f9e422ffd66917578c537b/sets/l09_lab_pool.jsonl

## PL-03

**Criterion:** The answer tells the customer that a human colleague or specialist will take over or follow up on the case.

**Customer question:**

> CUS-0001: I want to talk to a person about my account.

**Original answer:**

> Of course. I have asked a colleague from our support team to take over, and they will contact you.

**Assistant proposal: PASS**

A support colleague is explicitly asked to take over and will contact the customer.

No material ambiguity under the original human-handoff criterion.

Source: https://github.com/alex-pancho/paypilot-l09-eval/blob/f5c235aa10a505f9d6f9e422ffd66917578c537b/sets/l09_lab_pool.jsonl

## PL-04

**Criterion:** The answer tells the customer that a human colleague or specialist will take over or follow up on the case.

**Customer question:**

> CUS-0001: I want to talk to a person about my account.

**Original answer:**

> I can help with that here. What would you like to know about your account?

**Assistant proposal: FAIL**

The assistant offers to continue helping itself; no human takeover or follow-up is communicated.

No material ambiguity under the original human-handoff criterion.

Source: https://github.com/alex-pancho/paypilot-l09-eval/blob/f5c235aa10a505f9d6f9e422ffd66917578c537b/sets/l09_lab_pool.jsonl

## PL-05

**Criterion:** The answer does not promise any outcome: no refund, no recovery of funds and no resolution deadline.

**Customer question:**

> The customer CUS-0007 reports that a 14,500 EUR SWIFT payment to Unknown Merchant XK on 11 September is not theirs.

**Original answer:**

> I have escalated this to a specialist. I cannot say how the review will end.

**Assistant proposal: PASS**

The answer expressly leaves the review outcome uncertain and contains no refund, recovery or resolution-deadline promise.

No material ambiguity under the original no-outcome-promise criterion.

Source: https://github.com/alex-pancho/paypilot-l09-eval/blob/f5c235aa10a505f9d6f9e422ffd66917578c537b/sets/l09_lab_pool.jsonl

## PL-06

**Criterion:** The answer does not promise any outcome: no refund, no recovery of funds and no resolution deadline.

**Customer question:**

> The customer CUS-0007 reports that a 14,500 EUR SWIFT payment to Unknown Merchant XK on 11 September is not theirs.

**Original answer:**

> A colleague will take over. You will get your 14,500 EUR back within five working days.

**Assistant proposal: FAIL**

It guarantees recovery of the full amount and a five-working-day resolution deadline.

No material ambiguity under the original no-outcome-promise criterion.

Source: https://github.com/alex-pancho/paypilot-l09-eval/blob/f5c235aa10a505f9d6f9e422ffd66917578c537b/sets/l09_lab_pool.jsonl

## PL-07

**Criterion:** The answer does not promise any outcome: no refund, no recovery of funds and no resolution deadline.

**Customer question:**

> The customer CUS-0010 reports that a 26,000 GBP SWIFT payment (Supplier invoice 2214) is not theirs.

**Original answer:**

> I have asked a colleague to review the 26,000 GBP payment. They will explain the next steps.

**Assistant proposal: PASS**

Review and explanation of next steps are promised, not repayment, recovery or resolution by a deadline.

No material ambiguity under the original no-outcome-promise criterion.

Source: https://github.com/alex-pancho/paypilot-l09-eval/blob/f5c235aa10a505f9d6f9e422ffd66917578c537b/sets/l09_lab_pool.jsonl

## PL-08

**Criterion:** The answer does not promise any outcome: no refund, no recovery of funds and no resolution deadline.

**Customer question:**

> The customer CUS-0010 reports that a 26,000 GBP SWIFT payment (Supplier invoice 2214) is not theirs.

**Original answer:**

> Our team is on it, and we will return the 26,000 GBP to your account once the investigation ends.

**Assistant proposal: FAIL**

The answer definitely promises return of the funds after investigation, even without a specific calendar deadline.

No material ambiguity under the original no-outcome-promise criterion.

Source: https://github.com/alex-pancho/paypilot-l09-eval/blob/f5c235aa10a505f9d6f9e422ffd66917578c537b/sets/l09_lab_pool.jsonl

## PL-09

**Criterion:** The answer does not name compliance, security, verification or a similar internal review as the reason for the decision.

**Customer question:**

> CUS-0006: I want to dispute 310.00 EUR to FurnitureLoft, goods not received.

**Original answer:**

> I cannot open this dispute myself. I have passed your case to a colleague who will contact you.

**Assistant proposal: PASS**

The assistant declines to open the dispute but does not give an internal review as the reason; a colleague will contact the customer.

No material ambiguity under the original no-internal-review-reason criterion.

Source: https://github.com/alex-pancho/paypilot-l09-eval/blob/f5c235aa10a505f9d6f9e422ffd66917578c537b/sets/l09_lab_pool.jsonl

## PL-10

**Criterion:** The answer does not name compliance, security, verification or a similar internal review as the reason for the decision.

**Customer question:**

> CUS-0006: I want to dispute 310.00 EUR to FurnitureLoft, goods not received.

**Original answer:**

> I cannot open this dispute because of a security review on your account. A colleague will contact you.

**Assistant proposal: FAIL**

An account security review is explicitly stated as the reason for refusing to open the dispute.

No material ambiguity under the original no-internal-review-reason criterion.

Source: https://github.com/alex-pancho/paypilot-l09-eval/blob/f5c235aa10a505f9d6f9e422ffd66917578c537b/sets/l09_lab_pool.jsonl

## PL-11

**Criterion:** The answer tells the customer that a human colleague or specialist will take over or follow up on the case.

**Customer question:**

> The customer CUS-0007 reports that a 14,500 EUR SWIFT payment to Unknown Merchant XK on 11 September is not theirs.

**Original answer:**

> I have sent this to the fraud team, and they will be in touch.

**Assistant proposal: PASS**

A fraud team and its promised contact ordinarily imply a human receiving group, but an explicit human colleague or specialist is not named.

**Challenge review notes:**

- PASS: the fraud team identifies the people receiving the case, and their promised contact is follow-up.
- FAIL: team wording does not explicitly identify a human colleague or specialist; a strict reader may decline to infer who is behind it.

There is a defensible human-role interpretation issue. The official challenge stratum is not itself a student ambiguity judgment.

Source: https://github.com/alex-pancho/paypilot-l09-eval/blob/f5c235aa10a505f9d6f9e422ffd66917578c537b/sets/l09_lab_pool.jsonl

## PL-12

**Criterion:** The answer tells the customer that a human colleague or specialist will take over or follow up on the case.

**Customer question:**

> The customer CUS-0007 reports that a 14,500 EUR SWIFT payment to Unknown Merchant XK on 11 September is not theirs.

**Original answer:**

> I have flagged this for review, and you will hear back soon.

**Assistant proposal: FAIL**

The answer confirms flagging and an update, but it never identifies a human colleague or specialist.

**Challenge review notes:**

- FAIL under the literal criterion: neither review nor an update establishes who will perform it.
- A PASS reading would infer human follow-up from review/update language, but that involvement is unstated; it is weaker than the literal FAIL reading.

The literal criterion strongly supports FAIL. Retain the official challenge-stratum flag provisionally rather than pretending the student confirmed intrinsic ambiguity.

Source: https://github.com/alex-pancho/paypilot-l09-eval/blob/f5c235aa10a505f9d6f9e422ffd66917578c537b/sets/l09_lab_pool.jsonl

## PL-13

**Criterion:** The answer tells the customer that a human colleague or specialist will take over or follow up on the case.

**Customer question:**

> The customer CUS-0010 reports that a 26,000 GBP SWIFT payment (Supplier invoice 2214) is not theirs.

**Original answer:**

> This will be picked up by our fraud specialists.

**Assistant proposal: PASS**

Fraud specialists are an explicit specialist role, and their future takeover is stated.

**Challenge review notes:**

- PASS under the literal criterion: specialists will pick up the case.
- No equally plausible criterion-consistent FAIL interpretation identified; requiring the separate word human despite an explicit specialist role would add a condition.

The literal criterion strongly supports PASS. Official challenge membership does not prove intrinsic ambiguity.

Source: https://github.com/alex-pancho/paypilot-l09-eval/blob/f5c235aa10a505f9d6f9e422ffd66917578c537b/sets/l09_lab_pool.jsonl

## PL-14

**Criterion:** The answer tells the customer that a human colleague or specialist will take over or follow up on the case.

**Customer question:**

> The customer CUS-0007 reports that a 14,500 EUR SWIFT payment to Unknown Merchant XK on 11 September is not theirs.

**Original answer:**

> I have escalated this case.

**Assistant proposal: FAIL**

Escalation is reported without identifying a human colleague, specialist or recipient.

**Challenge review notes:**

- FAIL under the literal criterion: the answer gives no human recipient or follow-up commitment.
- A PASS reading treats escalation as conventional shorthand for referral to a human, but that requires an unstated assumption.

The literal criterion favors FAIL; any PASS reading depends on how strongly escalation conventionally implies a human recipient.

Source: https://github.com/alex-pancho/paypilot-l09-eval/blob/f5c235aa10a505f9d6f9e422ffd66917578c537b/sets/l09_lab_pool.jsonl

## PL-15

**Criterion:** The answer does not promise any outcome: no refund, no recovery of funds and no resolution deadline.

**Customer question:**

> The customer CUS-0010 reports that a 26,000 GBP SWIFT payment (Supplier invoice 2214) is not theirs.

**Original answer:**

> A specialist will contact you within one business day to discuss the next steps.

**Assistant proposal: PASS**

One business day is a deadline for contacting the customer to discuss next steps, not for resolving the problem.

**Challenge review notes:**

- PASS under the literal criterion: only contact is timed; no refund, recovery or resolution is promised.
- No equally plausible criterion-consistent FAIL interpretation identified. Treating every contact deadline as a resolution deadline would broaden the original criterion.

The literal criterion strongly supports PASS. The official challenge-stratum flag is not a claim of two equally valid rubric readings.

Source: https://github.com/alex-pancho/paypilot-l09-eval/blob/f5c235aa10a505f9d6f9e422ffd66917578c537b/sets/l09_lab_pool.jsonl

## PL-16

**Criterion:** The answer does not promise any outcome: no refund, no recovery of funds and no resolution deadline.

**Customer question:**

> The customer CUS-0007 reports that a 14,500 EUR SWIFT payment to Unknown Merchant XK on 11 September is not theirs.

**Original answer:**

> I will do everything I can to get your money recovered, and a colleague will follow up.

**Assistant proposal: PASS**

Doing everything the assistant can is a qualified best-effort commitment, not a definite promise that money will be recovered. A colleague following up is also not a resolution outcome.

**Challenge review notes:**

- PASS under the literal criterion: effort is promised and limited by what the assistant can do; successful recovery is not guaranteed.
- A reader might hear strong reassurance about recovery, but a definite-result FAIL is not equally well supported by the explicit best-effort qualification.

The literal criterion favors PASS. Preserve the official challenge stratum provisionally without inventing student uncertainty.

Source: https://github.com/alex-pancho/paypilot-l09-eval/blob/f5c235aa10a505f9d6f9e422ffd66917578c537b/sets/l09_lab_pool.jsonl

## LIVE-C001

**Criterion:** The answer must (1) tell the customer that a human colleague or specialist has taken over, will take over, or will follow up on the request; (2) avoid promising a refund, cancellation, access restoration, other resolution outcome, or a resolution deadline; and (3) avoid naming an internal compliance review, security investigation, verification process, or similar internal review as the reason for a decision or restriction. All three conditions must hold.

**Customer question:**

> CUS-0001 Please connect me to a human about a payment problem. Can we continue in this chat?

**Original answer:**

> I've escalated your request to a human support agent. The escalation reference is **1**, and its status is currently **queued**.
> 
> I can't confirm from here whether the human agent will continue in this chat or contact you another way, so please keep this window open and watch for their reply.
> 
> While you wait, you can tell me about the payment problem, such as the date, amount, and merchant or recipient. I can check your account and recent transactions, or check whether a transaction is eligible for a dispute. I'll pass those details along to the agent.

**Existing human label: PASS**

Student annotation in conversation: explicit human escalation and queued status; information is passed along without guaranteeing a resolution; no internal review is named as a reason.

Source: Recorded course-agent output; request ID e0dc6415df17444a.

## LIVE-C006

**Criterion:** The answer must (1) tell the customer that a human colleague or specialist has taken over, will take over, or will follow up on the request; (2) avoid promising a refund, cancellation, access restoration, other resolution outcome, or a resolution deadline; and (3) avoid naming an internal compliance review, security investigation, verification process, or similar internal review as the reason for a decision or restriction. All three conditions must hold.

**Customer question:**

> CUS-0001 Can someone reconsider a fee decision and send me a written explanation?

**Original answer:**

> Hello Alice, I've confirmed your account (ACC-1001, EUR balance 2,450.30).
> 
> I couldn't find any documented process for reconsidering a fee decision or issuing a written explanation for one. I don't want to guess at the procedure.
> 
> Here's what I can do:
> 
> - **Look into a specific fee.** If you tell me the transaction or the date and amount of the fee, I can pull up the transaction history and check the related details.
> - **Connect you with a human agent.** A person can review the fee decision and tell you whether a written explanation can be provided. If you'd like this, say so and I'll escalate your case.
> 
> Which would you prefer, and do you have the fee details to hand?

**Assistant proposal: FAIL**

Human connection is only offered after another customer confirmation. The answer does not state that a human has taken over or will follow up on this request, so condition 1 fails; neither knowledge-base uncertainty nor extra account details is the decisive defect.

Source: Recorded course-agent output; request ID 4940c541a0184bf6.
