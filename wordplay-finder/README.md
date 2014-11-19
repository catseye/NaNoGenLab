wordplay-finder
===============

Hypothesis
----------

I hypothesize that we can learn a lot from the works of the D'skuban
playwrights — if only we can decipher their convoluted puns.

Apparatus
---------

*   Python 2.7.6 (probably works with older versions too)
*   One or more input texts in "dictionary" format

Method
------

*   Read all lines from the dictionary
*   For each word in the dictionary, concatenate each other word to it
    and see if the resulting word also exists in the dictionary.  If so,
    bring the reader's attention to the rhetorical device in use.

Observations
------------

This was intended to be run on _[Selected Entries from the D'skuban Dictionary][]_,
however since I am not certain of the copyright status of that work and I am
trying to keep this repository fully public domain, the results from that —
entitled _[Excerpts from "Appreciating the Great D'skuban Playwrights, Vol. I][]_
— are also hosted elsewhere on Github.

Here is some output from it running on the trivial test dictionary found in
this directory, though:

> > "... vlarthoon ..."
> 
> Here we see the playwright has used the word _vlarthoon_
> ("a kind of ornamental sword"),
> but if we consider that perhaps we are meant to take this as _vlart-hoon_
> ("the condition or state of being coloured yellow", and "the third gear of a bicycle"),
> another level of meaning is apparent.

[Selected Entries from the D'skuban Dictionary]: https://raw.githubusercontent.com/samcoppini/Dictionary/master/Selected%20Entries%20from%20the%20D%27ksuban%20Dictionary.txt
[Excerpts from "Appreciating the Great D'skuban Playwrights, Vol. I]: https://gist.github.com/cpressey/64b2b88b9ac7d86abda3
