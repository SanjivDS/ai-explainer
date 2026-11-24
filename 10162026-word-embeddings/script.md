# Word Embeddings - Word2Vec, GloVe & Semantic Similarity — Narration script

Voice: Kokoro `am_onyx` (local, free). Verbatim from `narration_text` in [`beat_sheet.json`](beat_sheet.json).

## B00 · The Question (16.3s)

Hi. This is Sanjiv. Today we shall discuss word embeddings: Word2Vec, GloVe, and semantic similarity. A token ID tells us which entry to look up. An embedding gives that entry a learned vector. Let us see how context shapes those vectors, and when their similarity can mislead us.

## B01 · The Whole Idea (18.4s)

Word embeddings turn patterns of word use into geometry. Words used in similar contexts can acquire similar vectors. Word2Vec and GloVe learn that geometry through different objectives. The result is useful evidence about language use, not a dictionary definition or a guarantee of shared meaning.

## B02 · An ID Is Not an Embedding (15.4s)

An ID is an address, not a measurement. Adjacent IDs need not mean similar words. A learned embedding table maps each vocabulary entry to a row of numbers. Those coordinates work together; an individual coordinate usually has no simple human label.

## B03 · Context Supplies the Signal (16.4s)

Here is a deliberately tiny corpus. Cat eats food; dog eats food. Cat likes play; dog likes play. With a window of one neighboring word, cat and dog have identical context counts: eats once and likes once. That is a training signal, not proof that cats and dogs mean the same thing.

## B04 · Word2Vec: Two Prediction Tasks (17.2s)

Word2Vec includes two familiar architectures. Continuous bag of words predicts a target from surrounding context. Skip-gram reverses that direction: a target predicts nearby context words. Slide a window through text, form training examples, and adjust vectors to improve those predictions.

## B05 · Learning From Prediction (19.5s)

For skip-gram, a target word and an observed context form a positive pair. Negative sampling, one common training method, contrasts observed pairs with sampled alternatives. Training adjusts target and context vectors to distinguish them. A sampled negative is a training contrast, not a claim that the two words can never occur together.

## B06 · GloVe: Count Before Fitting (18.8s)

GloVe starts with aggregated word-context co-occurrence statistics. It learns word and context vectors whose dot product, with bias terms, approximates the logarithm of a nonzero co-occurrence count. A weighting function controls how strongly counts contribute. The counts come from context windows across the corpus.

## B07 · Different Routes, Related Evidence (20.3s)

Word2Vec learns through prediction tasks; GloVe fits aggregated co-occurrence statistics. Both depend on a corpus and a definition of context. Neither method assigns dictionary meanings to axes. When comparing their outputs, keep the corpus, preprocessing, and evaluation task in view; the algorithm name alone does not tell you which representation is better.

## B08 · Cosine Compares Directions (16.9s)

Cosine similarity compares directions by dividing the dot product by the product of the vector lengths. Here are constructed two-dimensional vectors, not trained embeddings. A is one, two. B is two, four. They point in the same direction, so their cosine is one, even though their lengths differ.

## B09 · Compute, Do Not Guess (16.9s)

Now compare A with C, two, one. Their dot product is four; each length is the square root of five. Cosine is four over five, or zero point eight. A perpendicular vector gives zero. Zero does not mean unrelated in every sense, and cosine is undefined for a zero vector.

## B10 · Similarity Has Limits (18.5s)

A high score can reflect shared context rather than synonymy. Opposites can occur in similar surroundings. Classic Word2Vec and GloVe also assign one stored vector per vocabulary entry: bank keeps the same vector in river bank and bank loan. A later contextual model can represent those occurrences differently.

## B11 · The Verdict (19.7s)

Treat a neighbor list as evidence to inspect. Record the embedding model, corpus, and preprocessing. Compute similarity in the original vector space; a two-dimensional visualization can distort distances. Test neighbors against the task you care about, and remember that a corpus can carry stereotypes and other unwanted associations into its vectors.

## B12 · Your Turn (18.1s)

Your turn. Using a named Word2Vec or GloVe model, compute cosine similarities for three word pairs. Show the code, handle missing words, and explain one surprising neighbor. Check the model name and whether the code really ran. Compare its output with your expectations instead of treating every high score as a synonym.

## B13 · Word Embeddings (4.7s)

Word Embeddings. Word2Vec, GloVe, and Semantic Similarity.
