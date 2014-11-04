narrow-cut-up
=============

Requirements
------------

*   Python 2.7.6 (probably works with older versions too)
*   ImageMagick
*   [Pillow](http://python-pillow.github.io/) (it might work with PIL too)
*   Some scanned images of newspapers, books, etc.

Basic Strategy
--------------

*   Like [naive-cut-up](../naive-cut-up), except that it:
    *   scales each image to the size of the base ("canvas") image
    *   cuts and pastes in narrow strips instead of 1/9-page chunks

Usage
-----

We can use images fetched by naive-cut-up.

    $ ./narrow-cut-up.py ../naive-cut-up/ca_5.jp2.png ../naive-cut-up/pages/*

Sample Output
-------------

The result has promise, but looks like it might work best with pages
which contain more text than images.

![Newspaper cut-up on the theme of cheese](sample-cheese.jpg)
