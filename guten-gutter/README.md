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

Future work
-----------

I'm sure there are Gutenberg texts for which this fails.  Whence these are
found, this script's regular expressions should be adapted to match those
lines.

Really, the experiments in this repository should *not* be relying themselves
on the `gutenberg.py` module, or any cleaner; they should take a pre-cleaned
text file as input.
