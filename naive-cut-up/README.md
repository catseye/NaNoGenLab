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

Notes
-----

First, we tell it to fetch a few newspaper images that make reference to
cheese, and convert them from JPEG-2000 to (easier to work with) PNGs.
This shells ImageMagick to do the conversation.  ImageMagick probably wouldn't
be required if I had built my install of Pillow with JPEG support; alas, I
did not.

    $ ./naive-cut-up.py fetch cheese
    Fetching page 1 of 30656 ... 0.003262%
    http://chroniclingamerica.loc.gov//lccn/sn83045487/1917-04-03/ed-2/seq-15.jp2 --> ca_0.jp2
    convert ca_0.jp2 ca_0.jp2.png
    done!
    http://chroniclingamerica.loc.gov//lccn/sn83045487/1917-04-03/ed-1/seq-15.jp2 --> ca_1.jp2
    convert ca_1.jp2 ca_1.jp2.png
    done!
    http://chroniclingamerica.loc.gov//lccn/sn83030193/1922-10-18/ed-1/seq-13.jp2 --> ca_2.jp2
    convert ca_2.jp2 ca_2.jp2.png
    done!
    http://chroniclingamerica.loc.gov//lccn/sn83045487/1912-04-11/ed-1/seq-9.jp2 --> ca_3.jp2
    convert ca_3.jp2 ca_3.jp2.png
    done!
    http://chroniclingamerica.loc.gov//lccn/sn85066387/1911-04-02/ed-1/seq-16.jp2 --> ca_4.jp2
    convert ca_4.jp2 ca_4.jp2.png
    done!
    http://chroniclingamerica.loc.gov//lccn/sn83016758/1918-01-17/ed-1/seq-8.jp2 --> ca_5.jp2
    convert ca_5.jp2 ca_5.jp2.png
    done!
    http://chroniclingamerica.loc.gov//lccn/sn83045487/1912-05-16/ed-1/seq-16.jp2 --> ca_6.jp2
    convert ca_6.jp2 ca_6.jp2.png
    done!

Then we choose a base PNG and

    $ ./naive-cut-up.py cutup base.png jp2/*.png
    base.png <PIL.PngImagePlugin.PngImageFile image mode=L size=6094x8535 at 0x7F2F426AB128>
    jp2/ca_0.jp2.png <PIL.PngImagePlugin.PngImageFile image mode=L size=1788x2692 at 0x7F2F426AB5A8>
    jp2/ca_1.jp2.png <PIL.PngImagePlugin.PngImageFile image mode=L size=1872x2705 at 0x7F2F426AB680>
    jp2/ca_2.jp2.png <PIL.PngImagePlugin.PngImageFile image mode=L size=5416x6477 at 0x7F2F426AB7A0>
    jp2/ca_3.jp2.png <PIL.PngImagePlugin.PngImageFile image mode=L size=1812x2626 at 0x7F2F426AB8C0>
    jp2/ca_5.jp2.png <PIL.PngImagePlugin.PngImageFile image mode=L size=6274x8906 at 0x7F2F426ABA70>
    jp2/ca_6.jp2.png <PIL.PngImagePlugin.PngImageFile image mode=L size=1880x2699 at 0x7F2F426ABC20>
    <PIL.PngImagePlugin.PngImageFile image mode=L size=1788x2692 at 0x7F2F426AB5A8> <PIL.Image._ImageCrop image mode=L size=0x0 at 0x7F2F426AB560>
    <PIL.PngImagePlugin.PngImageFile image mode=L size=6274x8906 at 0x7F2F426ABA70> <PIL.Image._ImageCrop image mode=L size=996x0 at 0x7F2F426ABCF8>
    <PIL.PngImagePlugin.PngImageFile image mode=L size=1880x2699 at 0x7F2F426ABC20> <PIL.Image._ImageCrop image mode=L size=444x196 at 0x7F2F426ABF80>
    <PIL.PngImagePlugin.PngImageFile image mode=L size=1872x2705 at 0x7F2F426AB680> <PIL.Image._ImageCrop image mode=L size=593x0 at 0x7F2F426AB200>
    <PIL.PngImagePlugin.PngImageFile image mode=L size=1812x2626 at 0x7F2F426AB8C0> <PIL.Image._ImageCrop image mode=L size=0x0 at 0x7F2F426AB9E0>
    <PIL.PngImagePlugin.PngImageFile image mode=L size=5416x6477 at 0x7F2F426AB7A0> <PIL.Image._ImageCrop image mode=L size=834x0 at 0x7F2F426ABB90>
    <PIL.PngImagePlugin.PngImageFile image mode=L size=5416x6477 at 0x7F2F426AB7A0> <PIL.Image._ImageCrop image mode=L size=279x0 at 0x7F2F426AB9E0>
    <PIL.PngImagePlugin.PngImageFile image mode=L size=1812x2626 at 0x7F2F426AB8C0> <PIL.Image._ImageCrop image mode=L size=0x0 at 0x7F2F426ABB90>
    <PIL.PngImagePlugin.PngImageFile image mode=L size=1788x2692 at 0x7F2F426AB5A8> <PIL.Image._ImageCrop image mode=L size=47x0 at 0x7F2F426AB9E0>
    <PIL.PngImagePlugin.PngImageFile image mode=L size=1872x2705 at 0x7F2F426AB680> <PIL.Image._ImageCrop image mode=L size=0x0 at 0x7F2F426ABB90>
    Writing output.png...

And then we look at the result and are sorely unimpressed.

    $ ristretto output.png 

What's with all those `size=0x0`s anyway?
