# Neural Networks - Forward Propagation Explained — Narration script

Voice: Kokoro `am_onyx` (local, free). Verbatim from `narration_text` in [`beat_sheet.json`](beat_sheet.json).

## B00 · The Question (15.6s)

Hi. This is Sanjiv. Today we shall discuss neural networks, and how forward propagation turns inputs into a prediction. We will follow two numbers through a tiny network, calculate each step, and change one input to see what happens. The whole journey is arithmetic you can check.

## B01 · The Big Picture (12.3s)

A forward pass calculates with the current weights. Inputs become intermediate values, and those values become an output. Following that chain makes a neural network much easier to inspect.

## B02 · The Route Through a Network (17.8s)

Here is our entire network: two inputs, two hidden units, and one output. Each layer receives values from the previous layer. The weights and biases are parameters used in the calculation. During this pass, we keep them fixed. First we combine the inputs, then apply an activation, then combine the hidden values into a prediction.

## B03 · One Unit, One Calculation (18.4s)

Start with inputs two and one. The first hidden unit multiplies them by one half and negative one. That gives one and negative one. Add those contributions, and the total is zero. Now add the bias of one. The result before activation is one. A bias shifts the sum; it is another parameter, not another input feature.

## B04 · The Other Hidden Unit (18.5s)

The second hidden unit receives the same inputs but uses different parameters. Its weights are negative one and one, with a bias of one half. Negative two plus one plus one half gives negative one half. The two units have produced different combinations of the same input. We now have one and negative one half, ready for the activation step.

## B05 · Apply the Activation (18.5s)

Our hidden layer uses ReLU. It returns zero for a negative value and leaves a positive value unchanged. Watch negative one half become zero, while one stays one. The hidden layer now sends one and zero onward. Zero here describes this unit for this input. It does not mean the unit has been deleted from the network.

## B06 · From Hidden Values to Prediction (19.2s)

The output unit uses weights two and negative one, then adds a bias of one half. Two times one, minus one times zero, plus one half gives two point five. We chose a linear output for a toy regression model, so that number is the prediction. It is not automatically a probability, and these hand-picked parameters have not been trained.

## B07 · A Layer in Matrix Form (20.0s)

The matrix version packages the calculations we just did. Each row of the weight matrix belongs to one hidden unit. Multiply by the input column vector, add the bias vector, and apply ReLU element by element. The dimensions tell us what fits. Two inputs enter this layer, and two hidden values leave it. The notation is shorter; the arithmetic is unchanged.

## B08 · Why the Activation Matters (20.3s)

Suppose we removed the hidden activation. One weighted sum followed by another could be combined into a single affine transformation. Adding more of those layers would still leave an affine mapping from input to output. The activation changes the family of functions the network can represent. ReLU adds a bend, allowing different input regions to behave differently.

## B09 · Change One Input (18.7s)

Let us test the calculation. Keep every weight and bias unchanged, but change the second input from one to three. The hidden sums become negative one and one point five. ReLU turns them into zero and one point five. The output becomes negative one. A different prediction does not prove the network learned. Here, only the input changed.

## B10 · Where Learning Fits (19.9s)

Forward propagation also happens during training. After the prediction, a loss measures its disagreement with a target. Backpropagation computes gradients, and an optimizer uses them to update parameters. These are different parts of the training loop. Our example stopped at prediction. To judge whether its predictions are useful, we would need data, targets, and an evaluation.

## B11 · The Verdict (19.4s)

Follow the values, and the network becomes inspectable. Multiply by weights. Add biases. Apply the chosen activation. Repeat through the layers until the output is ready. Keep intermediate values visible when you debug. A correct forward calculation establishes what the model computes; it does not establish that the model has learned a useful solution.

## B12 · Your Turn (20.2s)

Try this prompt: Implement our two-input, two-hidden-unit network in Python. Print every weighted sum, activation, and prediction. Change only the second input from one to three and verify both results. Ask for the intermediate values, not just the final answer. Use the example parameters supplied with this episode, and compare the printed numbers with the calculation you just watched.

## B13 · Neural Networks - Forward Propagation Explained (4.9s)

Neural Networks. Forward Propagation Explained. This is Sanjiv.
