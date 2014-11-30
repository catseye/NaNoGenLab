guten-gutter
============

_This is not an experiment.  It is a piece of lab equipment._

_It is, however, somewhat experimental._

Abstract
--------

The `gutenberg.py` module from [gutenizer](https://github.com/okfn/gutenizer/)
works fairly well for cleaning the extraneous parts off of a text file
downloaded from Project Gutenberg, but it's not perfect: it leaves the
"Produced by" lines in, and fails completely on some less-standard texts.

This tool attempts to be a more complete, more robust, and public domain
replacement for it.  It is probably not as robust yet, but it works on at
least some files. 

Requirements
------------

*   Python 2.7.6 (probably works with older versions too)

Usage
-----

    $ ./guten-gutter pg18613.txt > The_Golden_Scorpion.txt

Theory of Operation
-------------------

Various different kinds of "cleaner" objects are defined.  The most
conservative looks for "START OF PROJECT GUTENBERG" and "END OF PROJECT
GUTENBERG", which all Project Gutenberg files have, and returns the lines
between those two sentinels.  Then there are more specific cleaners, in
particular one which looks for the "produced by" line (which varies greatly.)

Then there is a cleaner which orchestrates a number of sub-cleaners.
If a sub-cleaner results in no lines, this orchestrator considers that a
failure, and uses the output of the previous successful cleaner as a fallback.

The cleaners are implemented as iterators over input lines, but in practice,
the orchestrator forces them to load all of the lines into memory; it needs
to do this to detect the failure of a sub-cleaner.  In practice this should
not be a problem on a modern machine with a modern amount of memory.

History
-------

Originally, many of the experiments in this repository were importing
gutenizer's `gutenberg` module directly.  Most have been updated to assume
that the input is plain text that has been, at your option, pre-cleaned by
a tool of your choice.  The only exception is [quick-and-dirty-markov](../quick-and-dirty-markov),
which was a "race against the clock" and it doesn't feel right to clean it
up after the fact.

Future work
-----------

Some texts on which the guten-gutter currently fails are:

*   Around the world in 80 days

I'm sure there are other Gutenberg texts for which this fails.  Whence these
are found, this script's regular expressions should be adapted to match those
lines.
