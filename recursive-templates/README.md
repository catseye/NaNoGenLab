recursive-templates
===================

Hypothesis
----------

We hypothesize that if we try this, it might be interesting.

Apparatus
---------

*   Python 2.7.6 (probably works with older versions too)
*   Some input text

Method
------

*   Pick one of a number of templates.
*   Replace each of the variables in that template with another template.
*   Repeat the last step for a specified number of times.
*   At your option, replace all the remaining variables with words.  Or not.

Observations
------------

Here is `./recursive-templates.py --generations=3`:

> wonder and irritation can't understand irritation is the biscuit of sheep is the elegy can't understand territory can't understand dragon is the protector of meerkat of sausage is no tree is the fox and sausage of sheep is the horse of sausage is the horse is no irritation can't understand dog and dog can't understand cat is no territory is the bell is the elegy of meerkat of cat and fox of dog is no dragon can't understand territory is the book of wonder is no fox and irritation and wonder is no tree!

The structure is made clearer if we parenthesize each template; here is
`./recursive-templates.py --generations=3 --parenthesize`:

> ((((fox and elegy) can't understand (sheep and protector)) is no ((sheep and elegy) can't understand (cat and candle))) can't understand (((wonder can't understand protector) can't understand (tree and horse)) is no ((dragon can't understand dog) can't understand (microphone can't understand cat))))!

So this looks like an acceptable (sort of) alternative to a recursive descent
generator as used in [reluctance-generator](../reluctance-generator/).  We
could have different "types" of variables for the different parts of speech
slash grammar productions, i.e. `$V1 blah $N1 blah $N2`.

When I started writing it I didn't immediately realize that special handling
would be needed to treat the variables as local to the template.  But once I
realized that, I saw it was not dissimilar to how variables work in pattern
matching and unification and such.  In this, when picking a sub-template,
we just textually replace each variable in that sub-template with a "fresh"
variable with a unique number, before inserting the sub-template into the
master template.

There is a command-line option which explicitly *does not* do this, so you
can see what it's like treating the variables as "global" to the
text-in-progress at each step.  Here is some output from 
`./recursive-templates.py --generations=3 --no-variable-renaming`.  As
you can see, it's much longer and more repetitive:

> sheep can't understand sheep can't understand meerkat and sheep can't understand sheep can't understand meerkat can't understand sheep can't understand meerkat can't understand sheep can't understand sheep can't understand meerkat and sheep can't understand sheep can't understand meerkat can't understand sheep can't understand meerkat is no sheep can't understand sheep can't understand meerkat can't understand sheep can't understand meerkat is the sheep can't understand sheep can't understand meerkat and sheep can't understand sheep can't understand meerkat can't understand sheep can't understand meerkat is no sheep can't understand sheep can't understand meerkat can't understand sheep can't understand meerkat of sheep can't understand sheep can't understand meerkat and sheep can't understand sheep can't understand meerkat can't understand sheep can't understand meerkat is the sheep can't understand sheep can't understand meerkat can't understand sheep can't understand meerkat of sheep can't understand sheep can't understand meerkat and sheep can't understand meerkat!
