shanty-generator
================

Hypothesis
----------

We hypothesize that we can get a computer to generate sea shanties, or at
least texts which are somewhat shanty-like.

Apparatus
---------

*   Python 2.7.6 (probably works with older versions too)
*   Some input text

Method
------

*   Pick one of a number of templates.
*   The template will require _n_ words.  Consume _n_ words from the input.
*   Replace the variables in the template with the words.
*   Repeat until no more (or not enough more) words available in the input.

It should be noted that the method described here is by no means specific
to shanties.

Observations
------------

    $ ./shanty-generator.py It was the best of times it was the worst of times
    It, was-was,
    It, was-was,
    the-the best!
    the-the best!
    
    of, times,
    of-of times,
    of-of times-times of-of it,
    it it was.
    
    
    the, worst,
    the-the worst,
    the-the worst-worst the-the of,
    of of times.
