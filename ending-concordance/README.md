ending-concordance
==================

Hypothesis
----------

We hypothesize that words in English can be roughly categorized using a
characteristic as simple as the pair of letters that they end with, and
that this can be exploited to form sentences which look almost plausible.

Apparatus
---------

*   Python 2.7.6 (probably works with older versions too)
*   The `gutenberg.py` module from [gutenizer](https://github.com/okfn/gutenizer/)
*   A bunch of Project Gutenberg texts in plain text format

Method
------

*   Read in all the words.
*   Index the words based on the final two letters in each word that is four or
    more letters long.
*   Write out words randomly chosen from two alternating end-two-letters groups.

Observations
------------

When run on _Principles of Scientific Management_, I got:

> management -which incompetent watch subsequent research statement stop-watch impudent stop-watch achievement Inasmuch point branch development -which excellent winch intelligent switch !
> 
> architect therefore object expenditure respect Therefore direct culture abstract you're product warfare architect before imperfect secure contract expenditure architect heretofore !
> 
> truth logic herewith public Fifth Scientific eighth drastic youth socialistic one.-fourth Scientific month drastic eighth optimistic strength optimistic health mechanic !
> 
> England forward demand third 21-pound afford 18-pound record around backward England board depend guard sound backward around disregard reground afford !
> 
> overstraining hoped falling stirred straightening traced wearing seemed directing trained interesting agreed coming completed moving educated shortening studied blundering considered !
> 
> capable over-inspectors timetable factors angle ancestors angle Employers double readers angle wears obstacle makers available owners double inspectors settle makers !
> 
> survival concise impartial house chemical advise unusual false especial because metal worse impartial increase commercial crease differential close mathematical cause !
> 
> severe picking future saving aware working There obtaining figure sending failure lagging nature falling there failing share machining you're loafing !
> 
> agents implement permits excellent accounts self-evident weights meant consists employment Experiments spent agents sentiment students inefficient servants experiment costs beneficent !
> 
> presents looks joints picks experiments clerks represents walks exerts books accidents books machinists lacks accounts blanks benefits risks tests clerks !
