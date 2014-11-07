narrative-makefile
==================

Hypothesis
----------

We can generate a story using only `make`.

Apparatus
---------

*   GNU Make (other makes might work too)

Method
------

*   Each point in the narrative is a goal, and may require other goals to
    be met, before it can be met.
*   Each goal outputs some text as a side-effect.

Observations
------------

    $ make
    Once upon a time there was a brave knight.
    And one day a troubador brought news of a damsel in distress.
    So the brave knight entered the Great Forest.
    And there the knight found a fearsome griffon.
    'I have what you seek but you must fetch for me the golden fleece.'
    So the knight travelled far and wide until he found the golden fleece.
    And the knight returned with the golden fleece.
    'Very good, brave knight,' said the griffon, and flew off, leaving behind a magic sword.
    So the brave knight made off with the enchanted blade.
    And the brave knight slew the dragon with his sword.
    And the brave knight rescued the damsel from the dragon's lair.
    And they lived happily ever after.
    $ make
    make: `live-happily-ever-after.goal' is up to date.
