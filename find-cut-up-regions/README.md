find-cut-up-regions
===================

Hypothesis
----------

We hypothesize that it is possible to use Pillow to find "sensible" regions
of an image to use in a cut-up construction.

Apparatus
---------

*   Python 2.7.6 (probably works with older versions too)
*   [Pillow](http://python-pillow.github.io/) (it might work with PIL too)
*   Some scanned images of newspapers, books, etc.

Method
------

*   First, decide what makes a pixel "light" versus "dark".
*   Crop (say 5%) off the edges of the image to account for scanner darkness.
*   For each horizontal line of pixels in the image, if some percentage
    (say 90%) of the pixels are "light", record this line.
*   Amalgamate adjacent recorded lines and possibly reduce their thickness.
*   Strips to cut will be those between the lines.
*   Then, for each strip, rotate it 90 degrees and run in through the
    above process (as if it were an entire input image), rotating the
    generated "strips" from that back -90 degrees.

Observations
------------

So far, so good.
