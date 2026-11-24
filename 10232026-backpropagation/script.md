# Backpropagation - How Neural Networks Actually Learn — Narration script

Voice: Kokoro `am_onyx` (local, free). Verbatim from `narration_text` in [`beat_sheet.json`](beat_sheet.json).

## B00 · The Question (14.8s)

Hi. This is Sanjiv. Today we shall discuss backpropagation, and how neural networks actually learn. Last time, we followed inputs forward to a prediction. Now we will add a target, trace the calculation backward, and watch one training step change the result.

## B01 · The Big Picture (15.6s)

Backpropagation calculates how each parameter affects loss. It follows the prediction backward through the operations that produced it. An optimizer then uses those gradients to change the parameters. Together, these steps turn a prediction into a training loop.

## B02 · Bring Back the Network (15.8s)

Our tiny network has two inputs, two hidden units, and one linear output. The inputs are two and one. The hidden sums are one and negative one half. After ReLU, the hidden values are one and zero. With the same weights and biases as before, the prediction is two point five.

## B03 · Give the Prediction a Target (14.9s)

For this constructed example, let the target be one. We choose half the squared error as our loss. Subtract one from two point five, square the difference, then divide by two. The loss is one point one two five. The loss gives training a numerical objective to reduce.

## B04 · Start at the Loss (16.6s)

Start with the prediction. The derivative of our loss with respect to that prediction is prediction minus target: one point five. This is a local sensitivity. A tiny increase in the prediction would increase the loss here. The gradient is not the loss itself; it describes how the loss changes.

## B05 · The Chain Rule (17.7s)

A parameter usually affects the loss through intermediate calculations. The chain rule connects their sensitivities. Multiply the gradient arriving from the next operation by the derivative of the current operation. Repeat backward through the graph. When several paths connect a value to the loss, add their contributions.

## B06 · Gradients at the Output (17.2s)

At the output, each weight multiplies a hidden value. So its gradient is the arriving gradient times that hidden value. One point five times one gives one point five for the first weight. One point five times zero gives zero for the second. The output bias has gradient one point five.

## B07 · Pass Through ReLU (18.2s)

Continue toward the hidden layer using the original output weights, two and negative one. The arriving gradients are three and negative one point five. ReLU has slope one on its positive side and zero on its negative side. Our hidden sums are one and negative zero point five, so the gradients become three and zero.

## B08 · Reach the Earlier Weights (18.2s)

The first hidden unit received inputs two and one. Multiply those inputs by its gradient of three. Its two weight gradients are six and three, and its bias gradient is three. The second unit receives zero through its ReLU gate, so its incoming parameter gradients are zero for this example. Other inputs can activate it.

## B09 · The Optimizer Takes a Step (20.6s)

Now the optimizer acts. For gradient descent, subtract the learning rate times each gradient. With a learning rate of zero point zero five, the first hidden weight moves from zero point five to zero point two. Compute all gradients at the original parameters first, then update every parameter together. Backpropagation supplied the gradients; this step changes the model.

## B10 · Run Forward Again (19.2s)

Run the same input forward again. The hidden values are now zero point one and zero. The updated output is zero point six one seven five, and the loss falls from one point one two five to about zero point zero seven three two. This particular step helped this example. It does not establish that the model generalizes.

## B11 · Check the Gradient (21.2s)

We can check our calculus by nudging a weight slightly in both directions and comparing the losses. The central difference estimate agrees with the analytic gradient of six. The companion Python example checks all nine parameters. This numerical check is useful for debugging, but repeatedly perturbing every parameter is expensive. Backpropagation reuses intermediate calculations.

## B12 · From One Step to Learning (20.0s)

Training repeats this loop across examples or small batches, usually combining their losses. The learning rate controls the size of each step; an overly large step can raise the loss. We also evaluate on held-out data. Lower training loss shows progress on the training objective. Useful learning requires predictions that hold up beyond those training examples.

## B13 · The Verdict (18.2s)

The complete loop is now visible. Predict with the current parameters. Measure a loss against a target. Trace gradients backward with the chain rule. Let the optimizer update the parameters. Backpropagation makes that gradient calculation efficient, while the data, objective, model, and optimizer together determine what the network learns.

## B14 · Your Turn (17.8s)

Try this prompt: Using the supplied network, compute every gradient by hand and in Python. Check them with finite differences, apply one gradient descent step, and compare the losses. Keep the target at one and the learning rate at zero point zero five. Print the intermediate values so you can check every link in the chain.

## B15 · Backpropagation - How Neural Networks Actually Learn (4.9s)

Backpropagation. How Neural Networks Actually Learn. This is Sanjiv.
