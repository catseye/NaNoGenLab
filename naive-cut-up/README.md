naive-cut-up
============

_Not finished yet_

Requirements
------------

*   Python 2.7.6 (probably works with older versions too)
*   ImageMagick
*   [Pillow](http://python-pillow.github.io/) (it might work with PIL too)
*   Some scanned images of newspapers, books, etc. (or it can use
    [chroniclingamerica.py](https://github.com/hugovk/chroniclingamerica.py)
    to fetch some)

Basic Strategy
--------------

*   Start with blank canvas.
*   Pick a source image.  Pick a rectangle within that image.
*   Copy the image within the rectangle to a random location on the canvas
*   Repeat from step 2 until we think we've covered the canvas.

Notes
-----

So far, it can fetch five newspaper images that make reference to
cheese, and convert them from JPEG-2000 to (faster to work with) JPEGs:

    $ ./naive-cut-up.py fetch cheese
    Fetching page 1 of 30656 ... 0.003262%
    http://chroniclingamerica.loc.gov//lccn/sn83045487/1917-04-03/ed-2/seq-15.jp2 --> ca_0.jp2
    convert ca_0.jp2 ca_0.jp2.jpg
    done!
    http://chroniclingamerica.loc.gov//lccn/sn83045487/1917-04-03/ed-1/seq-15.jp2 --> ca_1.jp2
    convert ca_1.jp2 ca_1.jp2.jpg
    done!
    http://chroniclingamerica.loc.gov//lccn/sn83030193/1922-10-18/ed-1/seq-13.jp2 --> ca_2.jp2
    convert ca_2.jp2 ca_2.jp2.jpg
    done!
    http://chroniclingamerica.loc.gov//lccn/sn83045487/1912-04-11/ed-1/seq-9.jp2 --> ca_3.jp2
    convert ca_3.jp2 ca_3.jp2.jpg
    done!
    http://chroniclingamerica.loc.gov//lccn/sn85066387/1911-04-02/ed-1/seq-16.jp2 --> ca_4.jp2
    convert ca_4.jp2 ca_4.jp2.jpg
    done!
    http://chroniclingamerica.loc.gov//lccn/sn83016758/1918-01-17/ed-1/seq-8.jp2 --> ca_5.jp2
    convert ca_5.jp2 ca_5.jp2.jpg
    done!
    http://chroniclingamerica.loc.gov//lccn/sn83045487/1912-05-16/ed-1/seq-16.jp2 --> ca_6.jp2
    convert ca_6.jp2 ca_6.jp2.jpg
    done!
