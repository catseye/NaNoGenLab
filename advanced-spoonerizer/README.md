advanced-spoonerizer
====================

Hypothesis
----------

I hypothesize that we can do better yet than
[naive-spoonerizer](../naive-spoonerizer/).

Apparatus
---------

*   Python 2.7.6 (probably works with older versions too)
*   A novel from Gutenberg, or other text that begins with `CHAPTER`
*   `/usr/share/dict/words`

Method
------

*   Read all the sentences from the text, arranged into sentences.
*   In each sentence, find all clauses.
*   In each clause, enumerate all pairings of words.
*   For each pairing, try swapping the initial consonant clusters.
    Assign each pairing a SchoonerSpore[tm] based on:
    *   whether one or both of the new words are dictionary words
    *   the distance the words are from each other
    *   the lengths of the words and the consonant clusters
    *   the number of unique letters involved.
*   Swap the consonant clusters on the highest-scoring pairing and output
    the clause.

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

Future work
-----------

Treat `,` and `--` and clause seperators.

Keep tweaking the score.  Don't swap "that" and "what".
