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

This was intended to be run on "Selected Entries from the D'ksuban Dictionary",
however since I am not certain of the copyright status of that work and I am
trying to keep this repository fully public domain, I won't include any sample
output based on it here.

I will however post the output on a Github gist and provide a link here.

Here is some output from it running on the trivial test dictionary found in
this directory:

> > "... vlarthoon ..."
> 
> Here we see the playwright has used the word _vlarthoon_
> ("a kind of ornamental sword"),
> but if we consider that perhaps we are meant to take this as _vlart-hoon_
> ("the condition or state of being coloured yellow", and "the third gear of a bicycle"),
> another level of meaning is apparent.
