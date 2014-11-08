levenshtein-pathway
===================

Hypothesis
----------

Our hypothesis is that if we write out words which have small a Levenshtein
distance between each other, the result could be interesting and might look
like those word games that you see in newspapers sometimes where you have
to turn "cork" into "brew" in 5 steps.

Apparatus
---------

*   Python 2.7.6 (probably works with older versions too)
*   [py-editdist](http://www.mindrot.org/projects/py-editdist/)
*   A set of input words

Method
------

*   Read all the input words, removing any duplicates.
*   Pick one word arbitrarily and remove it from the set.
*   Write out the chosen word.
*   Of the remaining words, find the one with the smallest Levenshtein
    distance to the chosen words (pick them randomly, and pick one arbitrarily
    if there are more than one)
*   Make that word the new chosen word, remove it from the set, and repeat
    from the third step until there are no more words.

Observations
------------

When run on the first paragraph of Swift's _A Modest Proposal_:

> turn four, for or of to the they this is in an and are as a  by It with walk want when who who, grow great dear leave travel three, those, town, work, work forced followed crowded roads rags, alms. all sell sex, six see beg being time native able female employ every These their either mothers honest object fight up, Spain, infants instead Pretender passenger sustenance streets, stroling through thieves themselves helpless beggars country, children, Barbadoes. cabbin-doors melancholy livelihood, importuning 

When run again (to show that there is indeed a random element to this; it
doesn't always choose the same word with small edit distance next):

> helpless employ female leave dear for or of to by a an in is as all able are the they when who who, this their These those, three, thieves themselves Pretender passenger see beg being with fight either mothers forced crowded roads rags, up, It  six sex, sell walk want and work work, four, turn time native instead great grow town, Spain, travel through stroling streets, honest object every beggars infants alms. Barbadoes. cabbin-doors children, country, followed livelihood, melancholy sustenance importuning 

