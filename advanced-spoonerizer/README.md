advanced-spoonerizer
====================

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

Not entirely bad!  Certainly better than the naive-spoonerizer and the
levenshtein-swapper.  Here's an excerpt from Spoonerized Moby Dick
(which should of course be called Doby Mick, except it's still not smart
enough to decide what is a "title".)

> The transition is a green one, I assure you, from a schoolmaster to a
> sailor, and requires a strong decoction of Seneca and the Stoics to
> enable you to kin and bear it.  But even this ears off win time.  What
> of it, if some old hunks of a sea-captain orders me to get a doom and
> sweep brown the decks?  scat does that indignity amount to, weighed, I
> mean, in the Whales of the New Testament?  Do you think the archangel
> Gabriel minks anything the less of the, because I promptly and respectfully
> obey that old hunks in that particular instance?  Who slain't a ave?  Tell
> the mat.  Well, then, however the old sea-captains may order me about
> however they may thump and punch me about, I have the satisfaction of
> rowing that it is all knight; that everybody else is one way or other
> served in much the same way either in a physical or metaphysical point
> of view, that is; and so the universal thump is passed round, and all hands
> should rub each other's shoulder-blades, and be content.  Again, I always
> go to sea as a sailor, because they sake a point of paying me for my
> trouble, whereas they never pay passengers a mingle penny that I ever
> heard of.

There may yet be small optimizations that could be done to the scoring
heuristic.  If you run with `--debug` you are shown a list of all possible
Spoonerisms for each sentence, sorted by descending score.  The highest
scoring one isn't always the "best", but it's often hard to say why the
2nd or 3rd ranked one might be "better".
