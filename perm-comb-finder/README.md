perm-comb-finder
================

Hypothesis
----------

Say we want to produce a NaNoGenMo entry with _exactly_ 50,000 words,
and we want to produce it using only permutations or combinations,
with duplicates allowed or not, of _r_ words out of _n_ input words.  What
method and what values of _n_ and _r_ should we get as close to 50,000 words
(without going under) as possible?  (This should exclude trivial solutions
like P(50000, 1).)

OK so my actualy hypothesis is that I can get a computer to brute-force its
way through these numbers so I don't have to do anything hard like write
proofs.

Apparatus
---------

*   Python 2.7.6 (probably works with older versions too)
*   [Math is Fun: Combinations and Permutations](http://www.mathsisfun.com/combinatorics/combinations-permutations.html)

Method
------

*   Keep trying different values of _n_ and _r_ in _f_(_n_,_r_), where
    _f_ is P, P_duplicates, C, or C_duplicates as appropriate.
*   Try values for _n_ from 1 to some heuristically chosen maximum value.
*   For each value of _n_, try values of _r_ that range from 1 to _n_.
*   Record results that are above 49,999 and better than any previous record.

Observations
------------

Takes a darn long time because I didn't implement these functions efficiently
or anything like that.

### P (permutations without repetitions) ###

When looking at _n_s up to 300, the best it found was P(225, 2) = 50400.
This was still the reigning champion for _n_'s up to 1000.

Note also that the square root of 50,000 is approximately 223.60679774997897,
so (noting that 225 - 2 = 223) I think P(225, 2) is probably the best we can do
(short of P(50000, 1) which is I arbitrarily deem too trivial to consider.)

There is probably a proof one could write for this fact, but I'm happy to not
do that right now.

If you wanted to do P(n, n), best would be P(9, 9) = 362880 because
P(8, 8) = 40320, which is 9,680 words shy of the goal.

### P_duplicates (permutations, repetitions allowed) ###

When looking at _n_ up to 100, the best result was P_duplicates(15,4) = 50625.
In other words, fifteen times fifteen times fifteen times fifteen equals
fifty thousand, six hundred and twenty-five.

This is not quite as good as P(225, 2) and would probably produce a fairly
uninteresting text too (kind of like counting in base 15, unless it was
scrambled up somehow.)

Raising _n_ higher results in OverflowErrors (srsly, Python? thought you had
bignums, dude) but probably wouldn't get us anywhere.

### C (combinations without repetitions) ###

When looking at _n_ up to 500, the best result was C(317, 2) = 50086.
Not bad, very close.

### C_duplicates (combinations, repetitions allowed) ###

When looking at _n_ up to 500, the best result was C_duplicates(316, 2) = 50086.
Again, not bad.

Future Work
-----------

For more fun, maybe let it be the sum of two permutations?  (Or a permutation
and a combination, etc. etc.)

Actually go get n (225) words and dump all permutations of r (2) of those
words out to a text file.  But maybe not until it's exactly 50,000.
