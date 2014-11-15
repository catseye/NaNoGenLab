levenshtein-swapper
===================

Hypothesis
----------

I hypothesize that it is maybe just possible to get a computer to produce
Spoonerisms and slips of the tongue (Freudian or otherwise.)  This experiment
will likely produce very weak ones, but may provide a basis for future research.

Apparatus
---------

*   Python 2.7.6 (probably works with older versions too)
*   [py-editdist](http://www.mindrot.org/projects/py-editdist/)
*   The `gutenberg.py` module from [gutenizer](https://github.com/okfn/gutenizer/)
*   A novel from Gutenberg, or other text

Method
------

*   Read all the sentences from the text, arranged into sentences.
*   For each sentence, find the two words with the smallest edit distance
    (greater than zero) and swap them.  Then output the sentence.

Observations
------------

It often swaps "on" and "of", "he" and "the", and "a" and "I" -- not incredibly
interesting.  For example (from "Princess of Mars"):

> Captain Carter had a small but beautiful cottage, situated of a bluff overlooking the river, and during one of my last visits, in the winter on 1885, I observed he was much occupied in writing, I presume now, upon this manuscript.

So... let's add a length constraint?  Let's say both words have to be at
least 4 letters long?

> And because of this conviction I have determined to life down the story of the interesting periods of my write and of my death.

Hmm.

> Leaving Powell's cave where it lay on the ledge I crept into the body to reconnoiter.

Okay, not bad.

> Pausing what the brink of the ledge I upbraided myself for upon now seemed to me wholly unwarranted apprehension.

Umm...

> My only alternative seemed, to lie in flight and my decision was crystallized by a recurrence of the rustling sound from the thing which now seemed in the darkness of the cave and to my distorted imagination, to be creeping stealthily upon me.

Bah, that's only swapped `seemed,` with `seemed`!

_beaks brenchful of test tubes in rit of fage_
