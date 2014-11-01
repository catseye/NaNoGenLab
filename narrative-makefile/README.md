narrative-makefile
==================

Requirements
------------

*   GNU Make (other makes might work too)

Basic Strategy
--------------

*   Each point in the narrative is a goal, and may require other goals to
    be met, before it can be met.
*   Each goal outputs some text as a side-effect.

Sample Output
-------------

    $ make
    Once upon a time there was a brave knight.
    And the brave knight slew the dragon with his sword.
    And the brave knight rescued the damsel from the dragon's lair.
    And they lived happily ever after.
    $ make
    make: `live-happily-ever-after.goal' is up to date.
