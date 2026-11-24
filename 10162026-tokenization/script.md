# Tokenization - How Machines Break Down Language — Narration script

Voice: Kokoro `am_onyx` (local, free). Verbatim from `narration_text` in [`beat_sheet.json`](beat_sheet.json).

## B00 · The Question (16.3s)

Hi. This is Sanjiv. Today we shall discuss how a machine breaks down language with tokenization. You write a sentence. A language model receives numbers. Tokenization connects those two worlds. Let us follow the conversion, build a tiny tokenizer, and see why a token is not the same thing as a word.

## B01 · The Whole Idea (15.8s)

Tokenization divides text into units and assigns each unit an identifier from a vocabulary. Those units can be words, parts of words, or smaller pieces. The choice changes how text is represented. It does not, by itself, give the machine an understanding of language.

## B02 · Choose the Pieces (17.1s)

Here are three ways to package cats. Keep the whole word, split every character, or reuse a piece such as cat and a piece such as s. Whole words need many vocabulary entries. Characters produce longer sequences. Subwords offer a compromise. These splits are illustrations, not claims about a particular model.

## B03 · Learn a Merge (17.2s)

Our tiny training collection contains low five times and lower twice. We start with characters and count neighboring pairs across that collection. L followed by o occurs seven times. So does o followed by w. That is a tie. Our example resolves ties alphabetically, so l and o merge first.

## B04 · Merge Again (17.0s)

Now count again using the updated pieces. Lo followed by w appears seven times, so it becomes low. This is the central move in byte-pair encoding: repeatedly merge a frequent adjacent pair. We stop after two merges to keep the example visible. Real vocabularies keep far more pieces.

## B05 · Apply the Rules (16.3s)

Training learned the rules. Encoding applies those saved rules to an input. Lower starts as characters, then the two learned merges produce low, e, and r. Each piece has an ID in our toy vocabulary. Another tokenizer can split this same word differently and assign completely different IDs.

## B06 · IDs Are Addresses (16.0s)

An ID is a lookup address. It is not a definition, a score, or a measure of similarity. The model uses those IDs to retrieve learned vectors called embeddings. The tokenizer supplies the sequence. The model processes its representations in context. Keep those jobs separate.

## B07 · Break the Toy (18.2s)

Now change the first letter to a capital. Our tiny vocabulary has no capital L, so this toy tokenizer fails there. Byte-level designs can start with all possible byte values instead. A character can occupy more than one byte. That helps represent unfamiliar text, but representing it is not the same as understanding it.

## B08 · Test the Boundary (16.2s)

When inspecting a real model, use its matching tokenizer. Compare lowercase and uppercase text, then add a leading space. Inspect the actual pieces and IDs instead of guessing them. Normalization and whitespace handling are part of the pipeline, so you should also check what survives decoding.

## B09 · The Takeaway (16.4s)

The useful habit is to inspect the encoding. Do not assume one word means one token, or that token boundaries follow grammar. Save the tokenizer identity with your experiment. Then a surprising split becomes something you can reproduce and investigate, instead of a mystery about how the machine reads.

## B10 · Your Turn (17.2s)

Try this prompt. Using a named tokenizer, compare lower, Lower, and a space followed by lower. Show pieces, IDs, and decoded text. Run the code; do not guess. Check that the answer names its tokenizer, includes reproducible code, and compares the decoded text with each exact input. Pause here and try it.

## B11 · Tokenization (3.5s)

Tokenization. How Machines Break Down Language.
