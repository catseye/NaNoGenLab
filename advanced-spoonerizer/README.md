advanced-spoonerizer
====================

_Unfinished incomplete not done yet_

Hypothesis
----------

I hypothesize that we can do better yet than
[naive-spoonerizer](../naive-spoonerizer/).

Apparatus
---------

*   Python 2.7.6 (probably works with older versions too)
*   The `gutenberg.py` module from [gutenizer](https://github.com/okfn/gutenizer/)
*   A novel from Gutenberg, or other text
*   `/usr/share/dict/words`

Method
------

*   Read all the sentences from the text, arranged into sentences.
*   In each sentence, enumerate all pairings of words.
*   For each pairing, try swapping the initial consonant clusters.
    Give each pairing a score based on whether one or both are dictionary
    words (in which case make the score exceedingly high) and the lengths
    of the words and the number of unique letters involved.
*   Swap the consonant clusters on the highest-scoring pairing and output
    the sentence.

Observations
------------

