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

So, we may ask, if this is actually not all that suitable for disconcerting
jumps between corpora, what happens if we run it on two texts that have
a fairly similar style, with a large number of words in common?  Well, here
it is running on "The Book of Cheese" and "The Principles of Scientific
Management":

> setting temperature of variations in the preparation of dairy equipment for roquefort cheese, the direction *of* handling *rice* *coal,* *with* resultant texture varying amounts of starter is commonly in relation of these are *possible* *under* *the* manufacturing process. 
> 
> it comes from whole milk is filled to raise the making *each* *man* *engaged* *in* warm sweet milk. 
> 
> the curdling temperature of the amido acids was *carefully* *selected* from kosher cheese, stirring to *be* evenly in furnishing protein 26-30 per cent with *full* *measure* *the* *principal* substance designed *and* the cheddaring process from each *of* the ground level and m. 
> 
> j., 39. 
> 
> bang's theory.+--another description of hungarian briuse which is ready for *which* *each* pound of these *good* delivery. 
> 
> this allows the *maximum* | | 8.54 | | .72 | {1.2 | | cheese by this *way* *to* 70 per *cent* moisture test, 26. 
> 
> ferments, 15, pages 130-146, 1909. 
> 
> this *type.* 
> 
> *the* cheese. 
> 
> it is no commercial rennet will be optional with salt is *widely* in order to other the *highest* *grade* *receive* *for* *handling* *of* cheddar process the *shovel* *to* be accurate. 
> 
> the alkali required *the* *hours* at *the* flavor and *is* difficult *to* which *it* has mechanical *engineers,* *by* rubbing the *machine-shop* *work* *than* the outer surface. 
> 
> there *is,* *how* *it* is *impossible,* *through* *any* *way* *of* the *rate* *of* the *minutest* *way* *maximum* | 6.5 | ash or compounds of ripening the milk. 
> 
> this *organization* with the amount of heating to be done by 8 the *case* *the* curd is constantly *watched* by *them* *in* cheese-making. 
> 
> they *could* *do* *the* end of *thumb.* 

If if you do it on two different collections of Wodehouse short stories,
the highlight seems almost random.  Perhaps unsurprisingly.

> *and* *the* *semi-darkness* *you* like it, said *awkwardly;* *but* you had *been* *hoped* to explain at roville possesses two *weeks* *peter* *you* do i am dependent. 
> 
> i *was* *silence* of the tears *dried,* *and* *drove* an idea which we artists, monsieur, i *don't* *stop.* 
> 
> *she* *had* *been* standing *looking* after *that* *deep* waters *with* *the* very *large* blue eyes *glowed* *in* *algiers?* 
> 
> *benyon* *sat* and *the* *days* ago _the island who cannot meet *even* *the* sudden *stiffening* *of* *luck* *i* met *at* *that.* 
> 
> forty francs will prove of the *bushes* *that* he *were* getting it *all,* she *groped* *my* lap and *shouted* mr *meggs* *at* all. 
