wikimedia-illustrations
=======================

Requirements
------------

*   Python 2.7.6 (probably works with older versions too)
*   [requests](http://docs.python-requests.org/)
*   [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/)

Basic Strategy
--------------

*   Get URLs for all images from all pages of a Wikimedia Commons category,
    such as "PD_Gutenberg" or "PD-Art_(PD-Japan)", and write that list of
    URLs to an index file.
*   Select _n_ images randomly from that index and download them.
*   (TODO) Inject those images as illustrations in a given text.

Usage
-----

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
