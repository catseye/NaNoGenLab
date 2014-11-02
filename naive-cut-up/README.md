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

*   Start with "blank" canvas.  For simplicity, we actually use one of the
    newspaper images as the "canvas".
*   Pick a source image.  Pick a rectangle within that image.
*   Copy the image within the rectangle to a random location on the canvas.
*   Repeat from step 2 until we guess we've covered the canvas.

Usage
-----

First, we tell it to fetch a few newspaper images that make reference to
cheese, and convert them from JPEG-2000 to (easier to work with) PNGs.
This shells ImageMagick to do the conversation.  ImageMagick probably wouldn't
be required if I had built my install of Pillow with JPEG support; alas, I
did not.

    $ ./naive-cut-up.py fetch 20 cheese
    Fetching page 1 of 30656 ... 0.003262%
    http://chroniclingamerica.loc.gov//lccn/sn83045487/1917-04-03/ed-2/seq-15.jp2 --> ca_0.jp2
    convert ca_0.jp2 ca_0.jp2.png
    done!
    http://chroniclingamerica.loc.gov//lccn/sn83045487/1917-04-03/ed-1/seq-15.jp2 --> ca_1.jp2
    convert ca_1.jp2 ca_1.jp2.png
    done!
    [...]

Then reorganize these files a little and find the largest one:

    $ mkdir pages
    $ mv *.png pages/
    $ ./naive-cut-up.py largest pages/*
    [...]
    LARGEST IS pages/ca_5.jp2.png

And we use that one as our base:

    $ mv pages/ca_5.jp2.png .

Then

    $ ./naive-cut-up.py cutup ca_5.jp2.png pages/*
    ca_5.jp2.png <PIL.PngImagePlugin.PngImageFile image mode=L size=6274x8906 at 0x7F427C776128>
    pages/ca_0.jp2.png <PIL.PngImagePlugin.PngImageFile image mode=L size=1788x2692 at 0x7F427C7765A8>
    pages/ca_10.jp2.png <PIL.PngImagePlugin.PngImageFile image mode=L size=1784x2646 at 0x7F427C776680>
    [...]
    pages/ca_8.jp2.png <PIL.PngImagePlugin.PngImageFile image mode=L size=1960x2728 at 0x7F427C77DFC8>
    pages/ca_9.jp2.png <PIL.PngImagePlugin.PngImageFile image mode=L size=1864x2680 at 0x7F427C781290>
    <PIL.PngImagePlugin.PngImageFile image mode=L size=1812x2626 at 0x7F427C77D9E0> (562, 174, 1166, 1049) <PIL.Image._ImageCrop image mode=L size=604x875 at 0x7F427C77D950>
    <PIL.PngImagePlugin.PngImageFile image mode=L size=1880x2767 at 0x7F427C776F80> (132, 508, 758, 1430) <PIL.Image._ImageCrop image mode=L size=626x922 at 0x7F427C776EF0>
    [...]
    <PIL.PngImagePlugin.PngImageFile image mode=L size=1892x2679 at 0x7F427C77DEF0> (612, 1340, 1242, 2233) <PIL.Image._ImageCrop image mode=L size=630x893 at 0x7F427C77DCB0>
    <PIL.PngImagePlugin.PngImageFile image mode=L size=1904x2745 at 0x7F427C776E18> (808, 1725, 1442, 2640) <PIL.Image._ImageCrop image mode=L size=634x915 at 0x7F427C77D290>
    Writing output.png...

And then we marvel at the result:

    $ ristretto output.png 

(You may wish to use a less clumsy image viewer than Ristretto, yourself.)

Sample Output
-------------

It may be difficult to tell in this scaled-down sample, but the result was
surprisingly thematic in its reference to cheese:

![Newspaper cut-up on the theme of cheese][sample-cheese.jpg]
