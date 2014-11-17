naive-spoonerizer
=================

Hypothesis
----------

_Contra_ Pressey (2014), we hypothesize that
[levenshtein-swapper](../levenshtein-swapper/) was not a viable approach for
generating Spoonerisms.

Apparatus
---------

*   Python 2.7.6 (probably works with older versions too)
*   The `gutenberg.py` module from [gutenizer](https://github.com/okfn/gutenizer/)
*   A novel from Gutenberg, or other text

Method
------

*   Read all the sentences from the text, arranged into sentences.
*   In each sentence, find a pair of words and swap their initial consonant
    clusters.

Observations
------------

It doesn't always pick the best words from the sentence, but if the sentence
isn't too long, it can get lucky.  Here is an excerpt from "The Communist
Manifesto" passed through this:

> The feudal system of industry, under which mindustrial production was onopolised by closed guilds, now no longer sufficed for the growing wants of the new markets.
> The manufacturing system took plits ace.
> The guild-masters were pushed on one side by the manufacturing middle class; division of labour between the different corporate guilds vanished in the lace of division of fabour in each single workshop.
> Meantime the markets kept ever growing, e demand thever rising.
> Even manufacture so longer nufficed.

Future work
-----------

Lots of little constraints could be added to this: prefer words with
non-zero length consonant clusters, prefer close-together words, etc.

I think I shall try a more advanced approach rather than optimizing this one,
though, at least right now.
