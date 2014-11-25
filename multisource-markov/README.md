multisource-markov
==================

Hypothesis
----------

We hypothesize that a Markov chain running across two very different texts
which have only a few words in common (say, two texts in two different
languages) might be interesting to see.

Apparatus
---------

*   Python 2.7.6 (probably works with older versions too)
*   Two or more input texts

Method
------

*   Construct a probability state graph suitable for using in a Markov
    chain, but on each word, also record which file it was read from.
    (This code is based on [quick-and-dirty-markov](../quick-and-dirty-markov))
*   Choose a random path through the graph a la dissociated press,
    but, each time you switch from a word in a different file, note
    this in the output somehow.  For now, we'll emphasize words from the
    second input file.

Observations
------------

Here is some output from running this on "La Force / Le Temps et La Vie" by
Paul Adam, and "The Night Land" by Hodgson.  It is... what it is.  But it would
probably be just as interesting, or even more so, if the two sources were
not distinguished.  Because then the switch between the two languages wouldn't
be telegraphed so much.  But you could do that with a plain ol' Markov chain.

> la journée rire nerveux, blanc de «dîners grecs», et fit vibrer les obligea de lui. 
> 
> ne se souviendra de la voix enrouée de roussel, le cheval blanc versé dans son courage de leur pensée secrète. 
> 
> si les propos politiques. 
> 
> pitouët cependant le sabre celui-là, poussait à bord des explosions et qui parvint d'abord ne pouvoir rien résoudre à la voir. 
> 
> leurs armes et le troisième escadron en éveil riait aux places *between* *us,* *or* *another* *part.* 
> 
> *and* *dreadful* *race;* *for* *i* *perceived* *to* *be* *as* *i* *should* *have* *felt* *within* *and* *some* *rock,* *which* *way* *to* *rise,* *and* *did* *love* *name* *she* *had* *been* *for* *i* *saw,* *there* *abode* *there,* *to* *refuse* un bouton de son père admirable. 
> 
> oui, le bois filent. 
> 
> le frère est un riflard! 
> 
> Ça ne se succédèrent. 
> 
> sur les sapins des ans d'homme nerveux, furieux. 
> 
> un seul mot: «faim» ouvrait la sœur paisible nondain, relève ton sabre, les yeux bleus et de boue des grandes bêtes meilleures, franchirent le satura. 
> 
> edme et des fourreaux de brumaire, aux majors ceci: mack avait pris par chance, *no* *saying* *that* *it* *did* *be* *met* *the* *labour* *with* *sweet* *unto* *the* *bed* *of* *the* *thousandth* *plateau* *of* *the* *shore,* *where* *doubt* *concerning* *these* *broodings,* *and* *she* *ran* *more* *see* *the* *three* *days* *of* *this* *new* *tender* *and* *the* *way* *off,* *it* *made* *it* *were* *they* *gat* *two* *inches* *of* *the* *plain;* *for* *such* *an* *unease* *within* *it* *be* *somewhat* *to* *this* *shall* *you* *can* *truly* *that* *i* *cut* *from* *the* *shape* *our* *slumber;* *and* *the* *darkness.* 
> 
> *and* *i* *reached* *back* *my* *labour,* *but* *truly,* *naught* *to* *hold* *all.* 
> 
> *now,* *presently,* *i* *did* *be* *not* *to* *teach* *her* *wishing;* *for,* *behold,* *i* *had* *the* *gorge,* d'une victoire devait paraître à vouloir reconduire. 
> 
> mais sur les lignes d'avant-garde s'éclipsèrent, et rapace. 
