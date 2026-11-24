# Class Imbalance — Why Accuracy Can Be Misleading — Narration script

Voice: Kokoro `am_onyx` (local, free). Verbatim from `narration_text` in [`beat_sheet.json`](beat_sheet.json).

## B00 · ASK (18.1s)

Hallo. This is Liam, in for Sanjiv. A classifier gets ninety-nine percent accuracy. Impressive? Not if it misses every fault. We will build a small, clearly constructed example, count what the classifier gets wrong, and move its decision threshold. The goal is to see what accuracy hides when one class is much rarer than the other.

## B01 · OVERVIEW (10.3s)

High accuracy can hide failure on rare cases. Check which class the model misses, how many false alarms it raises, and whether those mistakes match the job you need it to do.

## B02 · BASELINE (21.1s)

First, establish the class mix. Our constructed dataset has one thousand cases: nine hundred ninety normal cases and ten faults. Each dot represents ten cases. A baseline that always predicts normal gets nine hundred ninety answers right. That is ninety-nine percent accuracy. But it finds zero of the ten faults. The arithmetic is correct; the single headline does not describe the failure that matters.

## B03 · COUNTS (22.9s)

Now apply a constructed scoring rule at a threshold of zero point five. Read actual classes down the rows and predictions across the columns. It flags eight real faults, misses two, and raises twenty false alarms on normal cases. Nine hundred seventy normal cases are correctly cleared. Accuracy falls to ninety-seven point eight percent, even though the rule now detects most faults. This is an illustration, not a trained-model benchmark.

## B04 · METRICS (18.5s)

Recall asks: of the ten actual faults, how many did we catch? Eight out of ten is eighty percent. Precision asks a different question: of the twenty-eight alerts, how many were real faults? Eight out of twenty-eight is about twenty-eight point six percent. Both share the same eight hits, but the denominators differ. High recall alone does not tell you whether the alert queue is useful.

## B05 · BALANCE (22.8s)

Accuracy counts every case equally, so the common class dominates this dataset. Balanced accuracy instead averages recall across the two classes. The always-normal baseline gets zero percent on faults and one hundred percent on normal cases: an average of fifty percent. Our scoring rule gets eighty percent and about ninety-eight percent, averaging about eighty-nine percent. That exposes the imbalance, but still does not price the mistakes.

## B06 · THRESHOLD (23.8s)

The threshold controls which scores become alerts. At zero point eight, this example catches five faults and makes five false alarms. Lower it to zero point five: eight faults, twenty false alarms. Lower it again to zero point two: nine faults, ninety false alarms. Here recall rises while precision falls. Choose the trade-off using validation data, error costs, and review capacity. Do not choose it by repeatedly checking the final test.

## B07 · TRAINING (23.5s)

Changing the training process can help, but it does not replace evaluation. Class weights change the training penalty. Resampling changes which training examples are seen. Apply resampling only inside the training portion of each validation fold, after separating the data. Keep validation and final-test data representative of deployment. Balancing the test set changes the question; resampling before splitting can also leak information across the boundary.

## B08 · UNCERTAINTY (22.1s)

Always report the counts behind the percentages. Eight detected faults out of ten and eighty out of one hundred both give eighty percent recall. But change one hit to a miss: the first falls by ten percentage points, the second by one. A tiny rare-class sample makes the score fragile. Collect more representative evidence and quantify uncertainty. No single metric guarantees that the same result will hold after deployment.

## B09 · VERDICT (20.4s)

Check the class mix, then compare against a simple baseline. Use the confusion matrix to expose each kind of mistake. Read precision and recall together, and use balanced accuracy when equal class weighting answers your question. Choose the threshold for the real costs and workload, protect the final test, and show the sample counts. Accuracy is one useful description. It is not the whole decision.

## B10 · YOUR TURN (31.4s)

Try this prompt. Create a reproducible binary classification example with one percent positives. Compare an always-negative baseline with a scored classifier. Show the confusion matrix, accuracy, precision, recall, and balanced accuracy. Vary the decision threshold and count false alarms and missed positives. Keep resampling inside training folds, choose the threshold on validation data, and preserve an untouched test set. Check that all four confusion-matrix counts add up, and that the threshold never learns from the final test. Run the comparison before trusting the headline.

## B11 · OUTRO (6.3s)

Class Imbalance. Why Accuracy Can Be Misleading. Count the mistakes that matter. Liam, in for Sanjiv.
