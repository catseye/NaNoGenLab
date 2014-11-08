perm-comb-finder
================

Hypothesis
----------

Say we want to produce a NaNoGenMo entry with _exactly_ 50,000 words,
and we want to produce it using only permutations or combinations,
with duplicates allowed or not, of _r_ words out of _n_ input words.  What
method and what values of _n_ and _r_ should we get as close to 50,000 words
(without going under) as possible?

This should exclude trivial solutions like P(50000, 1).  And, assuming this
novel will be in "sentences" of _r_ words, what results do we get if we
insist on a high _r_?

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

After writing some code to catch OverflowErrors (srsly, Python? thought you had
bignums, dude) I ran it for _n_ up to 800 and found that P_duplicates(224,2) =
50176.  OK, also not a surprise given the square root is around 223.  Again,
not sure how interesting such a text would be, although that may not matter.

### C (combinations without repetitions) ###

When looking at _n_ up to 500, the best result was C(317, 2) = 50086.
Not bad, very close.

### C_duplicates (combinations, repetitions allowed) ###

When looking at _n_ up to 500, the best result was C_duplicates(316, 2) = 50086.
Again, not bad.

### Nuts to this!  I want bigger _r_'s! ###

You will note that the value of _r_ in the above results is often 2, which
suggests our novel would be a series of pairs of things, which sounds pretty
boring no matter which way you slice it.  What if we insist _r_ is larger?

Here are some results for _r_ = 3 and maximum _n_ in all cases is 500:

    $ ./perm-comb-finder.py --minimum-r=3 --top=500
    best: P(38,3) = 50616                                                   
    best: P(9,9) = 362880                                                   
    best: P_duplicates(15,4) = 50625.0                                      
    best: C(317,315) = 50086                                                
    best: C_duplicates(66,3) = 50116                                        

Interesting to note that the best _r_ for C becomes a whopping 315, but that
is just due to the symmetrical nature of C (I blame Pascal's Triangle.)
50,086 is still our overall winner, but C_duplicates(66, 3) might arguably be
more interesting.  Let's try _r_ = 4, 5, and 6:

    $ ./perm-comb-finder.py --minimum-r=4 --top=500
    best: P(11,5) = 55440                                                   
    best: P(9,9) = 362880                                                   
    best: P_duplicates(15,4) = 50625.0                                      
    best: C(317,315) = 50086                                                
    best: C_duplicates(13,7) = 50388                                        

    $ ./perm-comb-finder.py --minimum-r=5 --top=500
    best: P(11,5) = 55440                                                   
    best: P(9,9) = 362880                                                   
    best: P_duplicates(9,5) = 59049.0                             
    best: C(317,315) = 50086                                                
    best: C_duplicates(13,7) = 50388                                        

    $ ./perm-comb-finder.py --minimum-r=6 --top=500
    best: P(9,6) = 60480                                                    
    best: P(9,9) = 362880                                                   
    best: P_duplicates(7,6) = 117649.0                                      
    best: C(317,315) = 50086                                                
    best: C_duplicates(13,7) = 50388                                        

Of these, C_duplicates(13,7) might be the most interesting, but technically
C(317,315) is still the winner.

### But I want _exactly_ 50,000 words! ###

If we are willing to have our novel consist of two parts using two different
combinatoric strategies, we can satisfy our original goal of having exactly
50,000 words in it by trying all these values and finding two that add up
to 50,000 with the `--memoize` option.  We can set a minimum _r_ too so that
the results are more interesting.

    $ ./perm-comb-finder.py --top=500 --memoize --minimum-r=4
    best: P(11,5) = 55440                                                   
    best: P(9,9) = 362880                                                   
    best: P_duplicates(15,4) = 50625.0                                      
    best: C(317,315) = 50086                                                
    best: C_duplicates(13,7) = 50388                                        
    
    10660 + 39340 == 50000
    10660: [('C', 41, 38)]
    39340: [('C', 281, 279)]
    
    39340 + 10660 == 50000
    39340: [('C', 281, 279)]
    10660: [('C', 41, 38)]
    
    49770 + 230 == 50000
    49770: [('C', 316, 314)]
    230: [('C', 230, 229)]
    
    230 + 49770 == 50000
    230: [('C', 230, 229)]
    49770: [('C', 316, 314)]

Now to actually generate a novel in two parts: one which lists every
combination of 38 words, without repetition, from a set of 48 words,
and the other which lists every combination of 279 words, without
repetition, from a set of 281 words!
