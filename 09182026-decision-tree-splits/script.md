# Decision Trees: How Splits Actually Work, Oversimplified — Narration script

Voice: Kokoro `am_onyx` (local, free). Verbatim from `narration_text` in [`beat_sheet.json`](beat_sheet.json).

## B00 · ASK (18.8s)

Merhaba. This is Liam, in for Sanjiv. A decision tree does not invent a clever question and hope. For a common exact binary classifier, it tests feature-and-threshold candidates, measures how much cleaner each pair of child groups becomes, keeps the best local improvement, and repeats. Let us watch one split earn its place with actual numbers.

## B01 · EXECUTIVE SUMMARY (18.8s)

Here is the whole idea. A tree repeatedly divides training rows into two groups. At each node, it searches for the feature and cutoff that make those groups more internally alike by the chosen loss or impurity measure. That choice is greedy: best now, not guaranteed best for the whole future tree. The tree becomes useful when we also control when it must stop.

## B02 · FRAMEWORK (19.8s)

For classification, impurity measures how mixed the labels are inside a node. We will use Gini impurity: one minus the sum of squared class proportions. A pure node scores zero. With two classes split fifty-fifty, Gini is one half. A candidate is judged by the sample-weighted impurity of its left and right children. Lower children mean a larger impurity decrease.

## B03 · CANDIDATES (21.2s)

Take one numerical feature with values one through six and labels A, A, A, B, B, B. In scikit-learn's best splitter, the exact search considers midpoints between sorted distinct values: one point five, two point five, three point five, four point five, and five point five. Each threshold sends values at or below it left and the rest right. Other implementations can search differently.

## B04 · WORKED EXAMPLE (18.4s)

The parent has three A's and three B's, so its Gini is zero point five. Try two point five. The left child is A, A: impurity zero. The right is A, B, B, B: impurity zero point three seven five. Weighting by child size gives zero point two five, so the decrease is zero point two five. That split helps, but it is not the winner.

## B05 · WINNING SPLIT (20.4s)

Now try three point five. The left child contains only A's; the right contains only B's. Both child impurities are zero, so their weighted impurity is zero. The decrease is the full zero point five. Among the candidates shown, three point five wins. A best splitter performs this comparison across the available features and thresholds, then stores that feature and cutoff at the node.

## B06 · FALSIFIABILITY (21.3s)

Now stress-test the method. The winning split is only the best immediate move. A different first split can sometimes support a better later tree, but greedy training does not backtrack to search every possible tree. Keep splitting and the model can isolate tiny pockets of training data. Maximum depth, minimum samples, minimum impurity decrease, and pruning trade training purity for a simpler tree that may generalize better.

## B07 · VERDICT (22.6s)

The verdict: a split is a local optimization, not an intuitive question. Enumerate valid feature-threshold candidates. Partition the rows. Compute each child's impurity. Weight by child size. Choose the largest decrease, then recurse under explicit stopping rules. For regression, the score changes from class impurity to a regression loss. Either way, validate the whole tree, because a perfect training partition can be a warning, not a victory.

## B08 · HANDOFF (23.7s)

Your turn. Paste this into Claude: Given this small labeled dataset, sort each numeric feature, list every valid midpoint threshold, compute parent and weighted child Gini impurity, rank the impurity decreases, draw the first two tree levels, and show how maximum depth or minimum leaf size changes the result. Then identify one sign of overfitting. Check the arithmetic, the winning threshold, and whether the stopping rule changes the story—not just the picture.

## B09 · TITLE RESTATE (15.9s)

Decision trees: how splits actually work, oversimplified. Test the candidates. Measure the weighted child impurity. Keep the best local decrease. Repeat only while the stopping rules allow it. The branch is not magic; it is the winner of a local scoring contest. This was Liam, in for Sanjiv.
