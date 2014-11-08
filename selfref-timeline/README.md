selfref-timeline
================

_in progress_

Hypothesis
----------

We hypothesize that we ought to generate some kind of dialogue based on
characters' hopes and memories.

Apparatus
---------

*   Python 2.7.6 (probably works with older versions too)

Method
------

*   Generate a timeline, peppered with three kinds of events,
    SIGHTING, PREDICTION, and MEMORY.
*   Tie each MEMORY to a previous event (if no previous event, delete this
    MEMORY event.)
*   Tie each PREDICTION to a future event (if no future event, delete this
    PREDICTION event.)
*   Mechanically turn the whole thing into some kind of English prose.

Observations
------------

Still has significant bugs, but shows promise.

> Alice turned to Bob and asked, "Bob, do you think we will ever remember that time when see a UFO ranting obnoxiously?"
> 
> Bob turned to Alice and said, "Alice, do you remember that one time when we wonder if we'd ever remember that time when see a UFO ranting obnoxiously?"
> 
> Alice turned to Bob and asked, "Bob, do you think we will ever see a UFO ranting obnoxiously?"
> 
> Alice and Bob saw a UFO ranting obnoxiously.
