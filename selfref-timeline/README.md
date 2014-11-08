selfref-timeline
================

Hypothesis
----------

We hypothesize that we ought to generate some kind of dialogue based on
characters' wonderings about the future and memories of the past.

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

It still has some fudgy areas (like when there is a PREDICTION of a MEMORY
of that selfsame PREDICTION, with no SIGHTINGs involved), but otherwise,
I think it works quite well.  Here is the output of `./selfref-timeline.py 10`:

> Alice and Bob saw a ghost looking pensive.
> 
> Then one day, Alice turned to Bob and said, "Bob, do you remember that one time when we saw a ghost looking pensive?"  Alice smiled.  "Of course I do, Bob."
> 
> Then one day, Bob turned to Alice and said, "Alice, do you remember that one time when we remembered that time when we saw a ghost looking pensive?"  Bob smiled.  "Of course I do, Alice."
> 
> Then one day, Bob turned to Alice and asked, "Alice, do you think that one day we will wonder if we'd ever remember that time when we remembered that time when we remembered that time when we remembered that time when we saw a ghost looking pensive?"  "I don't know, Bob," said Alice.
> 
> Then one day, Bob turned to Alice and asked, "Alice, do you think that one day we will remember that time when we remembered that time when we remembered that time when we remembered that time when we saw a ghost looking pensive?"  "I don't know, Bob," said Alice.
> 
> Then one day, Bob turned to Alice and said, "Alice, do you remember that one time when we remembered that time when we remembered that time when we saw a ghost looking pensive?"  Bob smiled.  "Of course I do, Alice."
> 
> Then one day, Alice turned to Bob and said, "Bob, do you remember that one time when we remembered that time when we remembered that time when we remembered that time when we saw a ghost looking pensive?"  Alice smiled.  "Of course I do, Bob."
