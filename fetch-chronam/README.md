fetch-chronam
=============

Requirements
------------

*   Python 2.7.6 (probably works with older versions too)
*   [requests](http://docs.python-requests.org/)
*   [chroniclingamerica.py](https://github.com/hugovk/chroniclingamerica.py)
*   ImageMagick

Basic Strategy
--------------

*   Just provide a command-line front-end for
    *   searching the chroniclingameria API for a keyword
    *   downloading _n_ scanned images from the search results
    *   converting them from JPEG-2000 to PNG format

This code was originally in [naive-cut-up](../naive-cut-up/), from whence it
was extracted.

Usage
-----

    $ ./fetch-chronam.py 20 cheese
    Fetching page 1 of 30656 ... 0.003262%
    http://chroniclingamerica.loc.gov//lccn/sn83045487/1917-04-03/ed-2/seq-15.jp2 --> ca_0.jp2
    convert ca_0.jp2 ca_0.png
    done!
    http://chroniclingamerica.loc.gov//lccn/sn83045487/1917-04-03/ed-1/seq-15.jp2 --> ca_1.jp2
    convert ca_1.jp2 ca_1.png
    done!
    [...]

TODO
----

Maybe give the downloaded files better names.
