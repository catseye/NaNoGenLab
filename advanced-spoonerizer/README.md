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

Method
------

*   Read all the sentences from the text, arranged into sentences.
*   In each sentence, enumerate all pairings of words.
*   For each pairing, try swapping the initial consonant clusters.
    If both resulting words are dictionary words, go ahead with the
    replacement and output the sentence.

Observations
------------

