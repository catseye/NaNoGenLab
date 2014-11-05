reluctance-generator
====================

Requirements
------------

*   Python 2.7.6 (probably works with older versions too)

Basic Strategy
--------------

*   Use a "recursive descent generator" to generate statements suggesting
    reluctance.  This is like a recursive descent parser, but run "in reverse."
    Some might call this a "generative grammar", but that phrase has a specific
    meaning in the study of linguistics that might not be applicable here.
*   These statements will be a superset of
    [reluctance.txt](../generic-corpora/reluctance.txt);
    it will not mind at all creating sentences after which a linguist would
    be inclined to put an asterisk.

Sample Output
-------------

    $ ./reluctance-generator.py 
    I don't think .
    I'm not sure about this , okay ?
    I don't think this is such a good idea , okay ?
    I'm not sure about this .
    I just don't know if this is such a good idea y'know .
    I don't know if this is a good idea , okay ?
    I just really don't think this is a good idea y'know .
    I don't know about this .
    I really don't think this is a good idea .
    I'm really really really really really not sure about this , okay ?
