image-calipers
==============

_This is not an experiment.  It is a piece of lab equipment._

Abstract
--------

This command-line tool lets you see some information about images.

This code was originally in [naive-cut-up](../naive-cut-up/), from whence it
was extracted.

Requirements
------------

*   Python 2.7.6 (probably works with older versions too)
*   [Pillow](http://python-pillow.github.io/) (it might work with PIL too)

Usage
-----

    $ ./image-calipers.py *.png | python -mjson.tool

The JSON blob can then be read, by a human or a program, for information
about the images.
