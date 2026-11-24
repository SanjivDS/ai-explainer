# ROC Curve and AUC Score, Oversimplified — Narration script

Voice: Kokoro `am_onyx` (local, free). Verbatim from `narration_text` in [`beat_sheet.json`](beat_sheet.json).

## B00 · ASK (19.1s)

A classifier does not begin with yes or no. It begins with a score, and somebody has to decide where yes starts. This is Liam, in for Sanjiv. The ROC curve shows every tradeoff that decision can make. AUC compresses the whole curve into one ranking score. Useful, yes. A deployment decision, absolutely not. Let us separate the map from the number.

## B01 · EXECUTIVE SUMMARY (22.2s)

Here is the whole idea in one breath. Move a classifier's threshold and you trade caught positives against false alarms. The ROC curve records that trade at every threshold. A curve pushed toward the upper-left separates the classes better. AUC summarizes that separation as the chance that a random positive outranks a random negative. It compares rankings across thresholds; it does not choose the threshold you should deploy.

## B02 · FRAMEWORK — one point per threshold (21.2s)

The framework has one moving part: the threshold. At each setting, count the positives you caught and divide by all actual positives. That is true positive rate. Count the negatives you falsely flagged and divide by all actual negatives. That is false positive rate. Plot false positive rate across, true positive rate up, and every threshold becomes one point. Sweep the threshold, and the points become the ROC curve.

## B03 · WORKED EXAMPLE — six ranked cases (21.4s)

Now use the framework on six cases, three positive and three negative, ranked by score. Start above everything: nobody is flagged, so the point is zero, zero. Lower the threshold. Each positive moves the curve up; each negative moves it right. In this ranking, only one negative jumps ahead of one positive. The staircase finishes at one, one, and eight of the nine positive-negative pairs are in the right order.

## B04 · MEANING — what the area says (21.8s)

Now the area earns its meaning. AUC is not the percent of predictions that are correct. It is the probability that a randomly chosen positive receives a higher score than a randomly chosen negative, with ties handled appropriately. Our example gets eight out of nine pair orderings right, so its AUC is about zero point eight nine. A random ranking averages zero point five. Perfect separation scores one.

## B05 · DECISION — choose an operating point (20.4s)

So which point on the curve should you use? The curve cannot answer until you price the mistakes. In a disease screen, missing a case may be costly, so you might accept more false alarms. In an expensive manual-review queue, false alarms consume people and time, so the useful region may be the far-left slice. Compare models there, then choose a threshold using real costs, capacity, and prevalence.

## B06 · FALSIFIABILITY — a good AUC can still fail (23.7s)

Here is where one beautiful number lies by omission. AUC measures ordering across all thresholds. Your product uses one threshold, under one class balance, with one error budget. A model can rank well yet produce badly calibrated probabilities, overwhelm the queue with false positives, or fail a subgroup. And under severe imbalance, inspect precision-recall behavior too. High AUC is evidence of separation. It is not evidence that deployment is safe.

## B07 · VERDICT (25.4s)

Let us recap with Claude. A score becomes decisions only after you choose a threshold. Sweep that threshold and each true-positive-rate, false-positive-rate pair traces the ROC curve. A curve nearer the upper-left means stronger separation. AUC compresses the ranking into the chance that a random positive outranks a random negative. Use it to compare ranking quality. Then return to the curve, your operating region, calibration, and real-world costs before you deploy.

## B08 · HANDOFF (21.7s)

Your turn. Paste this in: take my classifier scores and labels, draw the ROC curve, calculate AUC, and mark the thresholds that keep false positive rate below my real capacity limit. For each marked point, report recall, precision, calibration, and the number of cases sent to review. Then check the answer. Did it use scores rather than hard labels? Did it name the positive class? And did it keep threshold choice separate from AUC?

## B09 · OUTRO (7.8s)

ROC curve and AUC score, oversimplified. Keep the curve when the number hides the decision. Liam, in for Sanjiv.
