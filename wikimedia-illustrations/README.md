wikimedia-illustrations
=======================

Hypothesis
----------

We hypothesize that if we download some random public-domain images from
Wikimedia Commons and inject them randomly into a text, it'll make just
about any text look more interesting.

Apparatus
---------

*   Python 2.7.6 (probably works with older versions too)
*   [requests](http://docs.python-requests.org/)
*   [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/)
*   [Pillow](http://python-pillow.github.io/) (it might work with PIL too)
*   ImageMagick
*   some kind of input text (uses lorem ipsum for now)

Method
------

*   Get URLs for all images from all pages of a Wikimedia Commons category,
    such as `PD_Gutenberg` or `PD-Art_(PD-Japan)`, and write that list of
    URLs to an index file.
*   Select _n_ images randomly from that index and download them.
*   Convert them to PNGs and resize any that are wider than 400 pixels
    downward
*   Inject those images as illustrations in a given text.

Observations
------------

NOTE 1: to stay (IMO) well within Wikimedia's [Terms of use](http://meta.wikimedia.org/wiki/Terms_of_use),
this script sleeps for 8 seconds after making any major HTTP request.

NOTE 2: just because an image is categorized as _public domain_ on Wikimedia
Commons _does not_ mean it is necessarily in the public domain.  It's always a
good idea to double-check.

    $ ./wikimedia-illustrations.py mkindex "PD-Art_(PD-Japan)"
    http://commons.wikimedia.org/wiki/Category:PD-Art_(PD-Japan)
    http://commons.wikimedia.org//w/index.php?title=Category:PD-Art_(PD-Japan)&filefrom=KitawakiI+Rioanji.jpg#mw-category-media
    grabbed 2 category index pages
    $ mkdir art
    $ ./wikimedia-illustrations.py random 4 art/ Wikimedia-Commons-Category-index-PD-Art_\(PD-Japan\).txt
    http://commons.wikimedia.org/wiki/File:Kawanabe_Kyosai_Renshishi2.jpg
    http://upload.wikimedia.org/wikipedia/commons/1/10/Kawanabe_Kyosai_Renshishi2.jpg --> art/Kawanabe_Kyosai_Renshishi2.jpg
    [...]
    $ ristretto art/

This is all pretty crazy and a piece of lab equipment should really be broken
off of it.

TODO
----

Add a flag that looks for the "guaranteed public domain" text on the media
page and only downloads if it finds it.

Research paper size specification/usage in CSS3/HTML.  Ideally we'd like to
be able to specify image sizes in inches assuming a printed page, or smth.
