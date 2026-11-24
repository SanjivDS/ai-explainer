# Entropy vs Gini Impurity — Narration script

Voice: Kokoro `am_onyx` (local, free). Verbatim from `narration_text` in [`beat_sheet.json`](beat_sheet.json).

## B00 · ASK (16.5s)

Bonjour. This is Liam, in for Sanjiv. A decision tree keeps asking questions that separate classes. But how does it score a question? Gini impurity and entropy both measure how mixed a node is. We will calculate them on the same examples, animate their curves, and find a case where they disagree about the best split.

## B01 · OVERVIEW (11.4s)

Gini and entropy are different measures of class mixing. Both reward cleaner groups. Neither guarantees a better tree on new data. The interesting difference is how they score the tradeoffs between candidate splits.

## B02 · FRAMEWORK (19.5s)

Start with the labels, not the feature values. This node contains four examples of class A and one of class B. Those proportions are eighty percent and twenty percent. A pure node contains only one class. A balanced binary node contains equal shares. Both measures are zero at purity and largest at an even mix. They measure uncertainty about the label inside a node.

## B03 · GINI (22.3s)

Gini has a useful probability interpretation. Draw two labels independently from this node, with replacement. What is the chance they disagree? The grid shows all twenty-five equally likely ordered pairs from our five records. Eight pairs disagree, so Gini is eight over twenty-five: zero point three two. The formula subtracts the probability of matching labels from one. This is not the error rate of a majority-vote prediction.

## B04 · ENTROPY (22.9s)

Entropy asks about average surprise. A common label brings little surprise; a rare label brings more. With base-two logarithms, our eighty-percent label contributes about zero point three two bits of surprise when it appears. The twenty-percent label brings about two point three two bits. Weight those surprises by their probabilities and the average is about zero point seven two bits. A class with probability zero contributes zero by convention.

## B05 · CURVES (19.5s)

Now move the class balance. Both curves vanish at the pure ends and peak in the middle. But their scales differ. For two balanced classes, Gini is one half; base-two entropy is one bit. Here Gini is doubled only to compare the shapes. Entropy rises more sharply near a pure node. Similar shapes do not make the criteria interchangeable when children have different sizes and mixtures.

## B06 · WEIGHTS (18.8s)

A tree scores the whole split, not just its cleanest child. Take eight A labels and two B labels. Send four A labels left, leaving four A and two B on the right. The left child is pure; the right is still mixed. Weight each child by its share of the ten records. Weighted Gini is about zero point two six seven. Subtract that from the parent score to get the reduction.

## B07 · DISAGREEMENT (21.6s)

Here the rankings actually flip. Both candidate questions split the same parent: ten A labels and ten B labels. Split A makes children with one A and seven B, then nine A and three B. Split B isolates five B labels, leaving ten A and five B. The computed weighted Gini favors A. Weighted entropy favors B. Within each criterion, lower is better. Comparing their raw numbers across criteria is meaningless.

## B08 · LIMITS (22.1s)

A cleaner training leaf is not a promise about tomorrow. Watch a pure training group receive new examples with different labels. Neither impurity formula protects you from overfitting, noise, or an unrepresentative sample. Compare criteria with the same validation plan and sensible limits on tree size. Judge the predictions on held-out data using a metric that fits your task. The split score is a training tool, not the final verdict.

## B09 · VERDICT (19.2s)

Keep the distinction clear. Gini is the probability that two independently drawn labels disagree. Entropy is average surprise in the class label. Both guide a tree toward purer children using a weighted score. Their rankings can differ, and their numeric scales differ too. Choose with validation, not with the assumption that a more elaborate formula must be better.

## B10 · YOUR TURN (21.8s)

Try this prompt. Construct two candidate splits of the same labeled dataset. Compute Gini and base-two entropy for every node, weight child scores by sample count, and compare the rankings. Then explain why the preferred training split does not guarantee better test performance. Look for the child counts, the weights, and the arithmetic. Ask for a reproducible example, then check that the comparison keeps the parent data fixed.

## B11 · OUTRO (5.9s)

Entropy versus Gini Impurity. Score the split, then test the tree. Liam, in for Sanjiv.
