wikimedia-illustrations
=======================

Requirements
------------

*   Python 2.7.6 (probably works with older versions too)
*   [requests](http://docs.python-requests.org/)
*   [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/)

Basic Strategy
--------------

*   Get URLs for all images from all pages of a Wikimedia category, e.g.
    http://commons.wikimedia.org/wiki/Category:PD_Gutenberg
    and write that list of URLs to an index file.
*   (TODO) Select _n_ images randomly from that index and download them.
*   (TODO) Inject those images as illustrations in a given text.
