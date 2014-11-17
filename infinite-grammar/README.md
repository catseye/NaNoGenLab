infinite-grammar
================

Hypothesis
----------

We hypothesize that, since a grammar is basically a tree, we can use a
language with lazy evaluation such as Haskell to define an infinite grammar.

Except _no_, that's not right _at all_.  A grammar isn't a tree; a grammar
is a _schema_ for trees (sentences.)  So what do we even mean?

Well, we could make an infinite schema, but that's kind of like an infinite
program.  There's no real advantage for a program to be infinite (barring
having some rather esoteric mathematical properties that we won't consider
here) because it can just loop or recurse anyway; it's _expression_ can be
infinite, easily, even if it's finite.

Well, or we could have an infinite list of all possible sentences generated
by a grammar.  That'd be more reasonable.  But also not quite as interesting
as I'd hoped; it's just a kind of combinatoric enumeration.

So let's go with the "infinite expression" thing.  Infinite lists are
run-of-the-mill(-ish) in Haskell, but infinite trees are less common.
They can totally be done, though.

We'll define an infinitely long sentence, using a simple grammar, then
extract finite parts and linearize them.

Apparatus
---------

*   Hugs (September 2006) (possibly works with `ghc` too)

Method
------

*   Devise a simple recursive grammar.  But not _too_ simple.    
*   Define a recursive algebraic data structure for our grammar:
*   Define a "take" function for this structure, which takes some
    kind of limiter (let's say an integer for now) and an instance
    of this structure, and returns only the "top part" of the data,
    as defined by the limiter.
*   Now write one or more functions which return infinitely-large
    instances of this structure.  In a programming language with
    eager evaluation, these functions would not terminate because
    they'd recurse forever.  (In Haskell, they still recurse forever,
    but that doesn't have as much to do with termination :)
*   Now apply the "take" function to these infinite-structure functions
    as you see fit, to generate finite parts of these structures.

Observations
------------

The source file can be loaded into Hugs like so, and then interactively
played with.

    $ hugs infinite-grammar.hs

Well, first I did this with trees that didn't resemble a grammar much
as a warmup.  I don't know why I called the infinite-tree-generating
function `traps`, but I did.

    Main> takeTree 3 (traps "hi")
    ["hi","hia","hiaa","hiaaa","bhiaa","bhia","bhiaa","bbhia","bhi","bhia","bhiaa","bbhia","bbhi","bbhia","bbbhi"]

Then I defined a simple grammar of boxes and rabbit and a simple infinite
structure of boxes (but no rabbits) called `lots1`.  The `takeContents`
function gets a finite part of it, and `sentencify` turns the list of words
into a single string which is a sensible sentence:

    Main> sentencify $ takeContents 5 lots1
    "There was a box containing a box containing something."

And then a single box containing an unending series of rabbits, `lots2`.

    Main> sentencify $ takeContents 13 lots2
    "There was a box containing a rabbit and a rabbit and a rabbit and a rabbit and a rabbit and a rabbit and a rabbit and a rabbit and a rabbit and a rabbit and something and some stuff."

Now how about a box containing both rabbits _and_ boxes?  Why not?

    Main> sentencify $ takeContents 13 lots3
    "There was a box containing a rabbit and a box containing a rabbit and a box containing a rabbit and a box containing a rabbit and something."

You can't really tell they're nested, but that's English for you.  What if we
define the contents of the box in the other order?  Will we ever see the
rabbits, or will we recurse infinitely down the boxes on the left-hand side?
Well,

    Main> sentencify $ takeContents 7 lots4
    "There was a box containing a box containing a box containing something and some stuff and a rabbit and a rabbit."

OK, last example: mutual recursion.  Boxes 'A' contain a rabbit and a box 'B',
and boxes 'B' contain just a box 'A'.

    Main> sentencify $ takeContents 12 lots5
    "There was a box containing a rabbit and a box containing a box containing a rabbit and a box containing a box containing some stuff."
