uniquified-novel
================

_NOTE: this processor is also available online here: [Text Uniquifier](http://catseye.tc/installation/Text_Uniquifier)_

Hypothesis
----------

We hypothesize that if the list of words in a novel is uniquified, retaining
order, the result could be entertaining.

Apparatus
---------

*   Python 2.7.6 (probably works with older versions too)
*   A bunch of texts, possibly [pre-cleaned](../guten-gutter) text files
    previously downloaded from Project Gutenberg

Method
------

*   Read input words one by one; output each word only if it has not been
    encountered before.

Observations
------------

Some excerpts from "The House on the Borderland" put through this.  Note that
punctuation is considered part of the word for uniqueness purposes.

> Right away west Ireland tiny hamlet called Kraighten. situated, alone, at
> base low hill. Far around there spreads waste bleak totally inhospitable
> country; where, here great intervals, come ruins some long desolate cottage
> unthatched stark. whole land bare unpeopled, earth scarcely covering rock
> beneath it, country abounds, places rising soil wave-shaped ridges.
> Yet, spite its desolation, friend elected spend our vacation there.

...

> Onward went, broke occasional snapping twig feet, forward. quietness,
> horrible alone; twice kicked heels clumsily, confines rockiness countryside.
> haunting dread Once, away, wailing, myself breathless. talk. you," decision,
> _that_ wealth world holds. unholy diabolical vile know!" answered, hidden
> rise ground. "There's book," satchel. "You've safely?" questioned, access
> anxiety. replied. "Perhaps," continued, "we shall learn tent. hurry, too;
> we're still, don't caught dark." two later tent; delay, work prepare meal;
> eaten since midday. Supper cleared pipes. manuscript read suggested loud.
> "And mind," cautioned, knowing propensities, "don't skipping half book."

Indeed.

Related work
------------

The uniquification process can be made to work backwards — only output each
word if it is not seen _further up_ in the text — with the helper script
`reverse-words.py`, like so:

    $ ../guten-gutter/guten-gutter.py $GUTENBERG/pg236.txt >The_Jungle_Book.txt
    $ ./reverse-words.py The_Jungle_Book.txt > The_Jungle_Book_Reversed.txt 
    $ ./uniquified-novel.py The_Jungle_Book_Reversed.txt > The_Jungle_Book_Reversed_Uniquified.txt
    $ ./reverse-words.py The_Jungle_Book_Reversed_Uniquified.txt > The_Jungle_Book_Reverse-Uniquified.txt

The start of `The_Jungle_Book_Reverse-Uniquified.txt` looked like this:

> JUNGLE BOOK Rudyard Kipling Contents Brothers brings byre we. Talon tush claw.
> call! Law! Night-Song o'clock yawned, rid tips. tumbling, "Augrh!" threshold
> whined: Chief world." Dish-licker tales, rubbish-heaps. apt forgets anyone,
> hides mad, disgraceful creature. hydrophobia, dewanee "Enter, no," Gidur-log
> people], choose?"

while the end looked like:

> THE BEASTS TOGETHER load. See our line across plain, Like a heel-rope bent
> again, Reaching, writhing, rolling far, Sweeping all away to war! While men
> that walk beside, Dusty, silent, heavy-eyed, Cannot tell why we or they
> March suffer day by day. Camp are we, Serving each in his degree; Children
> of the yoke goad, Pack harness, pad and load! 

Also, this Python script has been translated to Javascript and has been made
available online here: [Text Uniquifier](http://catseye.tc/installation/Text_Uniquifier).
The Javascript version supports more options than this version, including
retaining paragraph or line breaks in the output, and treating words
case- and punctuation-insensitively.
