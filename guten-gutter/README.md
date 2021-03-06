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
replacement for it.  It is probably not much more robust than the gutenizer
yet, but it works on at least my personal collection of Gutenberg files.

Requirements
------------

*   Python 2.7.6 (probably works with older versions too)

Usage
-----

    $ ./guten-gutter pg18613.txt > The_Golden_Scorpion.txt

You can also give the `--output-dir=DIR` option, which will place the
cleaned version of each file in that directory, with the same name as
the original.

You can also give the `--strip-illustrations` option, which will cause
the cleaner to strip out `[Illustration: foo]` lines.  (Doesn't yet work
for illustration descriptions that span multiple lines.)

Theory of Operation
-------------------

Various different kinds of "cleaner" objects are defined.  The most
conservative looks for "START OF PROJECT GUTENBERG" and "END OF PROJECT
GUTENBERG", which all Project Gutenberg files have, and returns the lines
between those two sentinels.  Then there are more specific cleaners, in
particular one which looks for the "produced by" line (which varies greatly.)

Then there is a cleaner which orchestrates a number of sub-cleaners.
If a sub-cleaner detects that it has failed (e.g. in the result, too many
lines were deemed to be stripped,) the orchestrator uses the output of the
previously successful cleaner as a fallback.

So if the input file isn't a Gutenberg text at all, the output will be the
original text file, whatever it was.

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

The guten-gutter appears to operate acceptably on all of my (modest) collection
of downloaded Project Gutenberg texts.

I'm sure there are other Gutenberg texts for which this fails.  Whence these
are found, this script's regular expressions should be adapted to match those
lines.
