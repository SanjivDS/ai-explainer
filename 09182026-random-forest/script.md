# Random Forest: Why Multiple Trees Beat One, Oversimplified — Narration script

Voice: Kokoro `am_onyx` (local, free). Verbatim from `narration_text` in [`beat_sheet.json`](beat_sheet.json).

## B00 · ASK (19.9s)

Bula. This is Liam, in for Sanjiv. One decision tree can fit the training data beautifully and still change its mind when the data changes slightly. A random forest does something smarter than cloning that tree: it trains many deliberately different trees, then combines their predictions. Let us see why diversity plus averaging can turn unstable parts into a steadier whole.

## B01 · EXECUTIVE SUMMARY (20.6s)

Here is the whole idea. Deep decision trees are flexible, but that flexibility makes them unstable: small changes in training data can create different branches and predictions. A random forest injects controlled randomness so its trees make different mistakes, then averages them. When the trees remain useful and their errors are not too correlated, the average usually varies less than any one tree.

## B02 · FRAMEWORK (22.3s)

The mechanism has three steps. First, each tree trains on a bootstrap sample: rows drawn from the training set with replacement. Second, each split considers a random subset of features instead of every feature. Those choices create diversity. Third, classification averages class probabilities in scikit-learn, while regression averages numerical predictions. The design target is strong trees with less-correlated errors.

## B03 · TREE INSTABILITY (20.1s)

Watch one tree wobble. In the first training set, feature X wins the root split by a tiny margin. Change or remove a few rows, and feature Y can win instead. Every later branch now sees different data, so the disagreement cascades down the tree. That sensitivity is high variance: the fitted rule changes substantially across plausible training samples from the same problem.

## B04 · DIVERSITY ENGINE (21.5s)

A forest manufactures disagreement on purpose. Bootstrap sampling changes which rows—and how many copies of each row—reach each tree. Random feature selection changes which predictors are allowed to compete at each split. Without the feature restriction, one dominant predictor can make many trees resemble one another. Randomness may weaken an individual tree slightly, but it can make the group more valuable by lowering correlation.

## B05 · WORKED EXAMPLE (21.2s)

Now combine five classification trees for one case. Their class-A probabilities are zero point nine, zero point eight, zero point two, zero point seven, and zero point four. One tree is sharply bearish; the others disagree. The mean is zero point six, so the forest predicts class A under a zero point five cutoff. No single tree controls the answer. The average absorbs their different errors.

## B06 · FALSIFIABILITY (21.6s)

More trees are not a magic repair kit. If every tree follows the same dominant signal, their errors stay correlated and averaging repeats the mistake. If the features carry little predictive information, a crowd of weak trees remains weak. Forests can also sacrifice interpretability, consume more compute, and underperform a well-tuned simpler model. Judge the ensemble on held-out or out-of-bag performance, not tree count.

## B07 · VERDICT (22.6s)

The verdict: one tree is easy to inspect but often unstable. A random forest perturbs the rows, restricts candidate features, grows many different trees, and averages their predictions. The gain comes from variance reduction when individual trees stay competent and their errors are not perfectly aligned. Tune diversity without destroying strength, then validate. More trees stabilize the estimate; they do not manufacture missing signal.

## B08 · HANDOFF (27.0s)

Your turn. Paste this into Claude: Using my labeled dataset, compare one tuned decision tree with random forests across several tree counts, feature-subset sizes, and leaf-size limits. Report cross-validated and out-of-bag performance, training-to-validation gaps, prediction stability across random seeds, and fit time. Then identify whether extra trees reduce variance or merely repeat correlated errors. Check the baseline, the stability spread, and the compute tradeoff—not just the highest score.

## B09 · TITLE RESTATE (17.7s)

Random forest: why multiple trees beat one, oversimplified. Resample the rows. Randomize the feature choices. Grow trees that are useful but different. Average their predictions, and validate the result. The forest wins when its trees disagree productively—not when they echo the same mistake. This was Liam, in for Sanjiv.
