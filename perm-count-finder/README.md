perm-count-finder
================

Hypothesis
----------

Say we want to produce a NaNoGenMo entry with _exactly_ 50,000 words,
and we want to produce it using only ordered permutations of _r_ words
out of _n_ input words.  What values of _n_ and _r_ do we choose to
get _exactly_ 50,000 words (of if we can't find any, what will give us
the closest to 50,000 without going under 50,000?)

Apparatus
---------

*   Python 2.7.6 (probably works with older versions too)
*   [Math is Fun: Combinations and Permutations](http://www.mathsisfun.com/combinatorics/combinations-permutations.html)

Method
------

*   Keep trying different values of _n_ and _r_ in P(_n_,_r_).  Record
    any that are above 49,999 and better than any previous record.
*   For each value of _n_, try values of _r_ that range from _0_ to _n_.

Observations
------------

Takes a darn long time because I didn't implement permutation efficiently
or anything like that.

When looking at _n_s up to 300, the best it found was P(225, 223) = 50400.
This was still the reigning champion for _n_'s up to 1000.

Note also that the square root of 50,000 is approximately 223.60679774997897,
so I think P(225, 223) is probably the best we can do.  There is probably
a proof one could write for this fact, but I'm happy to not do that right now.

If you wanted to do P(n, n), best would be P(9, 9) = 362880 because
P(8, 8) = 40320, which is 9,680 words shy of the goal.

Future Work
-----------

For completeness, also figure:

*   permutations with duplicates allowed
*   combinations without duplicates
*   combinations with duplicates allowed

For more fun, maybe let it be the sum of two permutations?  (Or a permutation
and a combination, etc. etc.)

Actually go get n (225) words and dump all permutations of r (223) of those
words out to a text file.  But maybe not until it's exactly 50,000.
