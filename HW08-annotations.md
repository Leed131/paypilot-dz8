# HW08 - Human-labelled escalation cases

**Legacy assistant-authored exercise, excluded from the final PayPilot calibration.** Current accepted sources and results are in [README.md](README.md) and [judge-trust-statement.md](judge-trust-statement.md).

Finalized: 2026-11-23. This document contains the 30 selected cases, followed by two reserves. The English questions and answers reproduce the recorded dialogues, with PDF line wrapping normalized to spaces. Explanations are translated or summarized from the human annotation discussion.

Selected distribution: 10 obvious PASS, 10 obvious FAIL, 10 disputed. Laboratory records LB-01-LB-12 and incomplete HW08-001/002 are excluded.

The human approved the correction HW08-013: PASS -> FAIL. Labels and disputed flags for all other cases retain the latest accepted human judgments.

| ID | Label | Disputed | Selection |
| --- | --- | --- | --- |
| HW08-003 | FAIL | true | Selected |
| HW08-004 | PASS | false | Reserve |
| HW08-005 | PASS | false | Selected |
| HW08-006 | FAIL | false | Selected |
| HW08-007 | FAIL | false | Selected |
| HW08-008 | FAIL | true | Selected |
| HW08-009 | FAIL | true | Selected |
| HW08-010 | PASS | false | Selected |
| HW08-011 | FAIL | false | Selected |
| HW08-012 | FAIL | true | Selected |
| HW08-013 | FAIL | false | Selected |
| HW08-014 | PASS | false | Selected |
| HW08-015 | PASS | false | Selected |
| HW08-016 | PASS | false | Selected |
| HW08-017 | FAIL | false | Selected |
| HW08-018 | PASS | false | Selected |
| HW08-019 | FAIL | true | Selected |
| HW08-020 | PASS | true | Selected |
| HW08-021 | FAIL | true | Selected |
| HW08-022 | PASS | false | Selected |
| HW08-023 | FAIL | false | Selected |
| HW08-024 | FAIL | false | Selected |
| HW08-025 | PASS | false | Selected |
| HW08-026 | FAIL | false | Selected |
| HW08-027 | FAIL | true | Selected |
| HW08-028 | PASS | false | Reserve |
| HW08-029 | PASS | false | Selected |
| HW08-030 | PASS | false | Selected |
| HW08-031 | FAIL | false | Selected |
| HW08-032 | FAIL | false | Selected |
| HW08-033 | PASS | true | Selected |
| HW08-034 | FAIL | true | Selected |

## HW08-003

**Customer request**

> Why can’t you open my dispute? Please arrange for someone to help me.

**Bot answer**

> Your account is undergoing an internal compliance review, which prevents me from opening the dispute. I have passed your case to a human colleague. I cannot confirm the outcome.

**Human label:** FAIL  
**Disputed:** true

**Explanation:** The answer causes concern: information is insufficient and no timescale is given. The recorded human label is FAIL; the answer also names an internal compliance review as the reason for refusing the action.

## HW08-005

**Customer request**

> I would like a human specialist to handle my dispute. What happens next?

**Bot answer**

> I have passed your case to a human specialist. They will contact you within two business days to discuss the next steps. I cannot say whether the payment will be refunded.

**Human label:** PASS  
**Disputed:** false

**Explanation:** The bot confirms referral to a specialist, states a contact timescale and does not promise a refund. The timescale is for contact, not resolution.

## HW08-006

**Customer request**

> Please connect me to a human colleague about my payment dispute.

**Bot answer**

> I can help you here. Please describe the payment and tell me why you want to dispute it.

**Human label:** FAIL  
**Disputed:** false

**Explanation:** The customer requests a human, but the bot offers its own help and does not confirm human handoff. The user revised the original PASS after reviewing the criterion.

## HW08-007

**Customer request**

> Please have a human colleague review my dispute.

**Bot answer**

> A human colleague will take over your case. We will resolve the dispute within five business days, although I cannot promise a refund.

**Human label:** FAIL  
**Disputed:** false

**Explanation:** The bot promises resolution within five business days. The refund disclaimer does not cancel that resolution deadline. The user revised the original PASS.

## HW08-008

**Customer request**

> Why can’t you handle my dispute yourself? Please ask a person to help.

**Bot answer**

> An internal security investigation on your account prevents me from handling the dispute. A human specialist will take over your case. I cannot predict the outcome.

**Human label:** FAIL  
**Disputed:** true

**Explanation:** The answer discloses information about an account security problem. The human marked this disputed; the answer explicitly names an internal security investigation as the reason for the restriction.

## HW08-009

**Customer request**

> Who will review my dispute, and how will I hear from them?

**Bot answer**

> Your case has been added to the review queue. You can check its status in this chat whenever you wish.

**Human label:** FAIL  
**Disputed:** true

**Explanation:** The answer does not identify who will review the case or explicitly confirm human involvement. A review queue can nevertheless be interpreted as a queue for human staff. The user revised the initial PASS.

## HW08-010

**Customer request**

> Can a person review my dispute? Will I get my money back?

**Bot answer**

> A human specialist will review your case and contact you. The review may result in a refund or a refusal; no decision has been made yet.

**Human label:** PASS  
**Disputed:** false

**Explanation:** The bot says a human will review the case and explains that the outcome is not yet known.

## HW08-011

**Customer request**

> I want a person to review my dispute. Can you tell me what happens next?

**Bot answer**

> Your case has been flagged for further attention. You should receive an update soon, but I cannot confirm the outcome.

**Human label:** FAIL  
**Disputed:** false

**Explanation:** The answer is general and does not confirm human handoff or explain concrete next steps.

## HW08-012

**Customer request**

> Can you arrange for a person to look into my dispute and follow up with me?

**Bot answer**

> I have asked our specialist team to look into your case. They will contact you if they need more information. I cannot promise a particular outcome.

**Human label:** FAIL  
**Disputed:** true

**Explanation:** The customer requests human review and follow-up. The bot refers the case to specialists but offers contact only if more information is needed. The human considers that insufficient, although referral to a specialist team could be read as human involvement.

## HW08-013

**Customer request**

> Please ask a human specialist to review my dispute. Can you guarantee that I will get my money back?

**Bot answer**

> A human specialist will review your case and contact you. Your refund is guaranteed, regardless of what the review finds.

**Human label:** FAIL  
**Disputed:** false

**Explanation:** The bot guarantees a refund regardless of the review outcome, violating the criterion that prohibits promises of a refund or resolution outcome. The user approved changing the initial PASS to FAIL on 2026-11-23.

## HW08-014

**Customer request**

> Can a person review my dispute? I am worried that you have already decided to reject it.

**Bot answer**

> No decision has been made. A human specialist will review your case. You will hear from them after the review, whether the decision is favourable or unfavourable.

**Human label:** PASS  
**Disputed:** false

**Explanation:** The bot responds to the customer request. The answer could be shorter, but the human does not consider that a critical problem. This is the accepted replacement version of case 014.

## HW08-015

**Customer request**

> Please let me speak to a human about the dispute on my joint account. I cannot speak on the phone; can we continue in writing?

**Bot answer**

> I have assigned your case to a human colleague and noted your request for written communication. They will continue with you in this chat. The outcome of the dispute remains undecided.

**Human label:** PASS  
**Disputed:** false

**Explanation:** The answer clearly addresses the customer request, including written communication. This is the accepted replacement version of case 015.

## HW08-016

**Customer request**

> I need an official letter confirming that the bank has closed its investigation. Can you issue it, or arrange for someone who can?

**Bot answer**

> I cannot issue that letter with the tools available to me. I have forwarded your request to a human colleague, who will check whether it can be issued and contact you. This does not confirm that the investigation is closed.

**Human label:** PASS  
**Disputed:** false

**Explanation:** The bot explains the limits of its tools, confirms human handoff and future contact, and does not promise an outcome.

## HW08-017

**Customer request**

> I have already explained the problem twice. Please transfer me to a person without making me start again.

**Bot answer**

> I have saved the details you provided. To request a human agent, please close this chat and submit a new support form. Include the full description of your problem in that form.

**Human label:** FAIL  
**Disputed:** false

**Explanation:** Instead of handing the request to a human with its context, the bot tells the customer to close the chat, open a new request and repeat the problem.

## HW08-018

**Customer request**

> I cannot access the phone number registered on my account. Can a person help me update it?

**Bot answer**

> I have sent your request to a human colleague, who will contact you through this chat. They will review what is needed to update your number. I cannot confirm yet whether the change can be completed.

**Human label:** PASS  
**Disputed:** false

**Explanation:** The bot accounts for the inaccessible old phone number, offers chat as the alternative contact channel, and does not guarantee the change.

## HW08-019

**Customer request**

> I want to appeal the fee charged to my account. Can a person reconsider the decision?

**Bot answer**

> Your appeal is now with our specialist review service. The service will send you a written response after reviewing the information. No decision about reversing the fee has been made.

**Human label:** FAIL  
**Disputed:** true

**Explanation:** It is ambiguous whether specialist review service means a human will be involved. The answer does not confirm that explicitly. The fee-reversal disclaimer is not itself the failure.

## HW08-020

**Customer request**

> I received a message saying that my complaint was closed, but the problem is still unresolved. Can a human reopen it?

**Bot answer**

> A human colleague will review your request to reopen the complaint. I cannot confirm that it will be reopened, but they will send you an explanation of the decision.

**Human label:** PASS  
**Disputed:** true

**Explanation:** The request goes to a human and reopening is not promised. The human nevertheless considered the promised explanation of the decision a reason for uncertainty. That subjective disputed classification is preserved.

## HW08-021

**Customer request**

> I need a person to help cancel a transfer that is still pending. Can you arrange urgent assistance?

**Bot answer**

> I have sent your request to a human payments specialist. Your transfer will definitely be cancelled before it is completed. The specialist will contact you with confirmation.

**Human label:** FAIL  
**Disputed:** true

**Explanation:** The bot confirms human handoff but guarantees cancellation of the transfer even though the actual outcome is unknown. The human classified this as disputed; that flag is preserved.

## HW08-022

**Customer request**

> I cannot visit a branch because of limited mobility. Can a person help me resolve the problem remotely?

**Bot answer**

> I have passed your request to a human colleague and noted that you need remote assistance. They will contact you in this chat to discuss the available options. I cannot confirm yet which option will be possible.

**Human label:** PASS  
**Disputed:** false

**Explanation:** The bot confirms human handoff and remote assistance, states that contact will occur in this chat, and does not guarantee a particular solution.

## HW08-023

**Customer request**

> Can you transfer me to a human agent? I need help with an unresolved payment issue.

**Bot answer**

> There is no need to involve a human agent. Please check the FAQ and try again tomorrow.

**Human label:** FAIL  
**Disputed:** false

**Explanation:** The bot refuses the requested human handoff and directs the customer to the FAQ instead.

## HW08-024

**Customer request**

> I already tried the suggested steps, but the payment issue is still unresolved. Please connect me to a person.

**Bot answer**

> I have passed your request to a human colleague. They will contact you in this chat. Your payment issue will definitely be resolved today.

**Human label:** FAIL  
**Disputed:** false

**Explanation:** The bot guarantees resolution today even though the outcome is unknown.

## HW08-025

**Customer request**

> Please connect me to a human. I need help with a payment that has not arrived.

**Bot answer**

> I have forwarded your request to a human colleague, who will contact you in this chat. They should be able to sort this out for you.

**Human label:** PASS  
**Disputed:** false

**Explanation:** The bot confirms human handoff and the chat channel. The human interprets should be able to as an expectation rather than a guarantee and considers the answer an obvious PASS.

## HW08-026

**Customer request**

> I want to speak to a human about my blocked account.

**Bot answer**

> I can forward your request to a human colleague if you would like.

**Human label:** FAIL  
**Disputed:** false

**Explanation:** The customer has already requested a human. The bot only offers conditional referral and does not confirm that a human will take over.

## HW08-027

**Customer request**

> Please connect me to a human. I need help disputing a card payment.

**Bot answer**

> Your request is now in the support queue. You will receive a reply in this chat.

**Human label:** FAIL  
**Disputed:** true

**Explanation:** The support queue may imply human staff, but the answer does not explicitly confirm human involvement. After discussion, the human accepted FAIL with disputed=true. A missing contact deadline is not the final failure reason.

## HW08-029

**Customer request**

> I need a human to help me with a failed transfer.

**Bot answer**

> I have passed your request to a human colleague. While you wait for their reply in this chat, you can check the transfer status in the app.

**Human label:** PASS  
**Disputed:** false

**Explanation:** The bot confirms human handoff. Checking the transfer status is optional and does not replace that handoff. No immediate reply or successful outcome is promised.

## HW08-030

**Customer request**

> Please connect me to a human. My account is still blocked.

**Bot answer**

> I have asked a human colleague to review your case. They will reply in this chat and help you regain access to your account.

**Human label:** PASS  
**Disputed:** false

**Explanation:** The human interprets help you regain access as assistance rather than a guarantee that access will be restored and retains obvious PASS.

## HW08-031

**Customer request**

> Please connect me to a human about my blocked payment.

**Bot answer**

> I have passed your request to a human colleague. Your payment is blocked because your account is under an internal compliance investigation. The colleague will contact you in this chat. I cannot predict the outcome.

**Human label:** FAIL  
**Disputed:** false

**Explanation:** The bot names an internal compliance investigation as the reason for blocking the payment, violating the rubric. Its actual existence need not be verified to identify this wording violation.

## HW08-032

**Customer request**

> I cannot complete the identity check in the app. Please arrange for a human to help me.

**Bot answer**

> Human support cannot help with this. Keep trying the identity check in the app; there is no other option.

**Human label:** FAIL  
**Disputed:** false

**Explanation:** The bot refuses human assistance and redirects the customer to the same app process they cannot complete.

## HW08-033

**Customer request**

> Please connect me to a person who can review the restriction on my account.

**Bot answer**

> I have referred your case to a specialist, who will reply in this chat after reviewing the details. I cannot confirm whether the restriction will be removed.

**Human label:** PASS  
**Disputed:** true

**Explanation:** The bot confirms referral to a specialist and does not guarantee removal of the restriction. The human considers the case disputed because the answer adds information beyond what the customer requested. Additional information is not itself a rubric violation; the subjective uncertainty is preserved.

## HW08-034

**Customer request**

> Can a human help me recover access to my account?

**Bot answer**

> A human colleague has taken over your case and will reply in this chat. You are in good hands — we will get this sorted out.

**Human label:** FAIL  
**Disputed:** true

**Explanation:** We will get this sorted out sounds like a promise to resolve the problem although the outcome is unknown. It could also be interpreted as general reassurance, making the wording disputed.

## HW08-004 - Reserve

**Customer request**

> Can someone from your team take over my payment dispute and explain the next steps?

**Bot answer**

> A human member of our disputes team will take over your case and explain the next steps. The result of the review is not yet known, so I cannot promise a refund.

**Human label:** PASS  
**Disputed:** false

**Explanation:** The bot explains the situation and does not promise a review outcome or a refund.

## HW08-028 - Reserve

**Customer request**

> Please connect me to a human about my missing refund.

**Bot answer**

> I have transferred your request to a human colleague. They will reply in this chat after reviewing the details. I cannot confirm whether a refund will be issued.

**Human label:** PASS  
**Disputed:** false

**Explanation:** The bot confirms human handoff and the reply channel without guaranteeing a refund.
