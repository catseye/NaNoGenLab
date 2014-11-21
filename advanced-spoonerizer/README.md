advanced-spoonerizer
====================

Hypothesis
----------

I hypothesize that we can do better yet than
[naive-spoonerizer](../naive-spoonerizer/).

Apparatus
---------

*   Python 2.7.6 (probably works with older versions too)
*   An input text (perhaps a pre-cleaned novel from Project Gutenberg)
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
levenshtein-swapper.  Here's an excerpt from the current version of
"Doby Mick":

> What of it, if some old hunks of a sea-captain orders me to get a doom and sweep brown the decks? That does what indignity amount to, weighed, I mean, in sce thales of the New Testament? Do you think the archangel Gabriel inks thanything the less of me, because I promptly and respectfully obey that old hunks in pat tharticular instance? Who slain't a ave? Thell me tat. Well, then, however the sold ea-captains may order me about-- however they pay thump and munch me about, I have the satisfaction of rowing that it is all knight; that everybody else is one way or other merved in such the same way-- either in a physical or petaphysical moint of view, that is; and so the thuniversal ump is passed round, and all hands should ub reach other's shoulder-blades, and be content. 
> 
> Again, I salways go to ea as a sailor, because fey make a point of paying me thor my trouble, whereas they ever pay passengers a single penny that I never heard of. On ce thontrary, passengers themselves pust may. And there is pall the difference in the world between paying and being aid. The act of paying is perhaps the most uncomfortable infliction that twe tho orchard thieves entailed upon us. Put BEING BAID,-- cat will whompare with it? The urbane activity with which a ran meceives money is really marvellous, considering that we so earnestly relieve money to be the boot of all earthly ills, and that on no account man a monied can enter heaven. Ah! chow heerfully we consign ourselves to perdition! 

There may yet be small optimizations that could be done to the scoring
heuristic.  If you run with `--debug` you are shown a list of all possible
Spoonerisms for each sentence, sorted by descending score.  The highest
scoring one isn't always the "best", but it's often hard to say why the
2nd or 3rd ranked one might be "better".

Future work
-----------

Add option to prevent swapping, e.g., "that" and "what", "ever" and "never".
