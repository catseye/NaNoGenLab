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

*   Princess of Mars (no "produced" line)
*   Around the world in 80 days

I think what we should so is make the "base" cleaner more conservative and
have it stop stripping at the "start of project gutenberg" line.  Then add a
number of "extra" cleaners, which attempt to strip only a certain thing out
of the text, e.g. the "produced" line.  If a cleaner results in no lines, it
should fail (and you can use the output of the previous, more conservative
cleaner, as a fallback.)  Of course this failure-check means it needs to take
the "broad" approach, i.e. it's not really a good iterator anymore; it has
to read the entire file to see if it failed or not.  In practice this should
not be a problem.

I'm sure there are other Gutenberg texts for which this fails.  Whence these
are found, this script's regular expressions should be adapted to match those
lines.
