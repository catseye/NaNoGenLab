join-at-pivot
=============

Hypothesis
----------

Maybe if we join sentences from texts at their middle words, we will get
new sentences.

Apparatus
---------

*   Python 2.7.6 (probably works with older versions too)
*   The `gutenberg.py` module from [gutenizer](https://github.com/okfn/gutenizer/)
*   A bunch of Project Gutenberg texts in plain text format

Method
------

*   Find the middle word ("pivot") of each sentence and split the sentence
    into a "beginner" which ends with the pivot and an "ender" which begins
    with the pivot.
*   Construct a table of reasonably frequently-occuring pivots, their
    possible beginners, and their possible enders.
*   To make a sentence, pick a random pivot, and random beginner for that
    pivot, and a random ender for that pivot.

Observations
------------

> A factory usually does not have more enterprising than the rest, had set
> off upon an expedition. With intent, I have rushed you from the chambers
> of Professor Jenner Monde to that closing episode at the deserted cottage;
> I have made easy; and lo! I don't wonder. We had ascertained from the lady
> that she went down upon the Monday by the matter, sir? Possibly an old top,
> I said. There was two little kiddies in the Carter family whom I had loved
> and who had thought there was no one on Earth like Uncle Jack; I could see
> if you came across the courtyard, and so could effect an escape. Holmes
> held up the paper so that misery; nevertheless, there was a resemblance.
> And this is the story, if the long porter has told me rattle the dry bones
> of the Solomons. I don't apprehend that his excellency will break it and
> cause a large loss of fat. Yes.
