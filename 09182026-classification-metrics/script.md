# Accuracy vs Precision vs Recall vs F1 Score, Oversimplified — Narration script

Voice: Kokoro `am_onyx` (local, free). Verbatim from `narration_text` in [`beat_sheet.json`](beat_sheet.json).

## B00 · ASK (20.3s)

Sawubona. This is Liam, in for Sanjiv. A classifier can look excellent by one metric and careless by another. Accuracy counts every correct decision. Precision asks whether positive alerts deserve trust. Recall asks how many real positives it catches. F1 combines precision and recall. Let us use one confusion matrix to learn what each score reveals—and what each can hide.

## B01 · EXECUTIVE SUMMARY (20.8s)

Here is the whole idea. Accuracy asks how often the classifier is right overall. Precision asks whether positive alerts are trustworthy. Recall asks how many real positives were caught. F1 rewards precision and recall together. None is automatically best: class balance, the positive class, the decision threshold, and the real cost of each mistake decide which number deserves attention.

## B02 · FRAMEWORK (22.5s)

Name the four cells first. True positives and true negatives are correct decisions; false positives are false alarms; false negatives are misses. Accuracy divides both correct cells by every case. Precision divides true positives by all predicted positives. Recall divides true positives by all actual positives. F1 takes the harmonic mean of precision and recall. Different denominators ask different questions.

## B03 · WORKED EXAMPLE (21.5s)

Suppose one hundred patients are tested. Ten truly have the condition. The model catches six, misses four, and raises two false alarms, leaving eighty-eight true negatives. Accuracy is ninety-four percent. Precision is six divided by eight, or seventy-five percent. Recall is six divided by ten, or sixty percent. F1 is about sixty-six point seven percent. Same predictions, four different summaries.

## B04 · THRESHOLD TRADEOFF (21.6s)

Now move the decision threshold. Lowering it labels more cases positive, so recall can rise or stay level because fewer actual positives are missed. Precision often falls as extra false alarms enter, but it is not guaranteed to move monotonically. Raising the threshold reverses the pressure. A precision-recall curve shows these operating points; the threshold chooses which mistake the system tolerates.

## B05 · ACCURACY TRAP (20.6s)

Now notice the trap. Ninety-four percent accuracy sounds excellent, yet the model misses four of ten sick patients: recall is only sixty percent. The eighty-eight easy true negatives dominate the overall score. Accuracy is useful when classes and error costs are reasonably balanced. With a rare positive class, always compare it with the confusion matrix, precision, recall, and the operating threshold.

## B06 · FALSIFIABILITY (22.6s)

F1 fixes one accuracy problem by ignoring true negatives and punishing imbalance between precision and recall. But that creates limits of its own. F1 weights precision and recall equally, so it is wrong when misses cost far more than false alarms. It also omits true negatives entirely. Undefined denominators and micro, macro, or per-class averaging choices add hidden policy. One score never removes judgment.

## B07 · VERDICT (20.6s)

The verdict: use accuracy for an overall score when classes and error costs are reasonably balanced. Use precision when false alarms are expensive. Use recall when misses are expensive. Use F1 when one balance score is needed and equal weight is defensible. Always report the positive class, threshold, support, and confusion matrix. A metric should expose the decision, not replace it.

## B08 · HANDOFF (23.4s)

Your turn. Give Claude your true labels, prediction scores, positive class, and the relative cost of false positives and false negatives. Ask: Compute accuracy, precision, recall, and F1 across useful thresholds. Plot the precision-recall curve. Recommend a threshold under my cost or capacity constraint, state the zero-division and averaging conventions, and show one case where accuracy or F1 would mislead me. Then inspect the tradeoff, not just the winner.

## B09 · TITLE RESTATE (20.3s)

Accuracy versus precision versus recall versus F1 score, oversimplified. Accuracy counts overall correctness. Precision asks whether positive predictions deserve trust. Recall asks whether real positives were found. F1 rewards balance between precision and recall. Choose the positive class, choose the cost, then choose the threshold. This was Liam, in for Sanjiv.
