# Confusion Matrix — Narration script

Voice: Kokoro `am_onyx` (local, free). Verbatim from `narration_text` in [`beat_sheet.json`](beat_sheet.json).

## B00 · ASK (14.6s)

Selam. This is Liam, in for Sanjiv. A model that is ninety-eight percent accurate can still miss every case you care about. The confusion matrix shows how a model fails, not just how often. Let us build one, read it, and catch the trap it exposes.

## B01 · EXECUTIVE SUMMARY (12.5s)

A confusion matrix gives four separate counts for a classifier, not one score. It sorts every prediction by what was true and what the model said, so different mistakes stop hiding in one number.

## B02 · FRAMEWORK (16.8s)

Ask two questions of every case: what was it really, and what did the model say? Rows hold the truth; columns hold the prediction. Agreement lands on the diagonal: true positives and true negatives. Off the diagonal sit the two mistakes. A false positive is a false alarm. A false negative is a miss.

## B03 · WORKED EXAMPLE (18.1s)

Here are a thousand card payments; twenty are fraud. The model flags twenty-five. Fifteen are real fraud: true positives. Ten are honest payments: false alarms. Five frauds slip through as misses. The other nine hundred seventy are correctly cleared. Every payment lands in exactly one cell, and the four counts add back to a thousand.

## B04 · READING RATES (18.0s)

Read across a row for rates about reality. In the fraud row, fifteen of twenty were caught: that is recall, seventy-five percent. Read down a column for rates about the model's claims. Of twenty-five flags, fifteen were right: precision, sixty percent. Across the honest row, ten of nine hundred eighty were wrongly flagged: about one percent.

## B05 · FALSIFIABILITY (19.2s)

Now the trap. A lazy model that never flags anything scores ninety-eight percent accuracy, almost matching ours. Its matrix gives it away: zero true positives, all twenty frauds missed, recall zero. Accuracy hid that; the matrix cannot. One caution: some tools put predictions in the rows, so read the axis labels before you read a cell.

## B06 · VERDICT (14.5s)

The verdict: never report a classifier with one number alone. Show the matrix, name the positive class, and label which axis is truth. Then choose the rate that matches the expensive mistake: recall when misses hurt, precision when false alarms do.

## B07 · HANDOFF (15.7s)

Your turn. Paste this into Claude: Build a confusion matrix from my labels and predictions, label which axis is truth, compute recall and precision from the cells, and compare it with a model that always predicts the majority class. Watch whether accuracy alone would have fooled you.

## B08 · OUTRO (5.0s)

Confusion Matrix. Liam, in for Sanjiv. At Sanjiv.
