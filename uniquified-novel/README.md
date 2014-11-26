uniquified-novel
================

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

Future work
-----------

Maybe clean the words of punctuation too.

Make it work backwards -- only output a word if it does not occur further
on in the text.  (Reverse words, uniquify, reverse again.)

Write a version in Javascript so that it can be used in someone's web browser.
