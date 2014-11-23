narrated-card-game
==================

Hypothesis
----------

We hypothesize that rainy Sunday afternoons can be quite dull.

Apparatus
---------

*   Python 2.7.6 (probably works with older versions too)

Method
------

*   Simulate a simple card game.
*   For each action in the game, narrate it.

Observations
------------

This particular card game is sometimes a non-starter, but it sometimes
can go on for a long time.  The script `nanogenmo-submission-finder.py`
repeatedly runs the `narrated-card-game.py` script with increasing seed
values for the pseudo-random number generator, reporting when a seed
results in a game which, when narrated, meets or exceeds 50,000 words.

With the code as it is as of this writing, only one seed in the first
2000 meets that criteria, which is seed 846, producing 59,158 words.
