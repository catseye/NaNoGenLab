poetic-inventory
================

Hypothesis
----------

We hypothesize that it is possible to extract phrases from public-domain novels
and alphabetize them.  Well, I suppose we also hypothesize that, with enough
input texts, the final result may look like an interesting inventory of things.

Apparatus
---------

*   Python 2.7.6 (probably works with older versions too)
*   A bunch of texts, possibly [pre-cleaned](../guten-gutter) text files
    previously downloaded from Project Gutenberg

Method
------

*   Find all phrases which are neither "beginners" nor "enders" in the sense
    of [join-at-pivot](../join-at-pivot/).
*   Filter out just those phrases that begin with "a" or "an".
*   Sort those phrases alphabetically.
*   Dump out those phrases, capitalizing the first word and replacing each
    semicolon with a full stop and a paragraph break.

Observations
------------

(The list of input texts that produced this TBA.)

> A 5.9, a Believer, a Bible, a Biscay lady on her way to Seville, a Biscayan, a Blackbird, a Bonanza King, a Bricklayer passed by, a British aÃ«roplane, a Carabineer* happened along, a Castilian, a Castilian, a Cervantes Saavedra, a Cheese Committee to consist of seven members of the Exchange, a Cheese Inspector and also a Deputy Inspector, a Chicago millionaire, a Chinaman, a Chinese body-servant, a Christian, a Colonial trader, a Crow, a Curious Thing.
> 
> A Dormouse came into the room, a Flemish boor, a Freemason, a Frenchman by birth, a Frenchman, a Frenchwoman, a Gothic cathedral, a Grasshopper, a Greek, a Hawk, a Jew, a King of Annwvyn, a King of Annwvyn, a Knight on a black horse appeared, a Manchu shepherd that saw the vehicle pass, a Mastodon King and old-time comrade, a Michaelmas daisy peered into the garden, a Milanese gentleman, a Miss Ramsay, a Moor came running up, a Moorish soldier had hold of her by one leg, a Mormon prophet of the tribe of Joseph published the annals of the new religion, a Mr. Digby Thistleton, a Mrs. Vanderley, a Musgrave of Matocton, a NEW NOBILITY is needed, a Norfolk Islander, a Parsee relation, a Persian who maintained that there are two principles, a Persian, a Pole, a Race upon the earth that were hardy, a Relentless fate, a Samoan recruiter, a Saxon priest, a Spaniard, a Statue of a man in broken armour, a Swede, a Tatar prisoner, a Thing unnameable, a Turkish sabre by his side, a Tyrolese, a Valencian gentleman and a famous soldier, a Valencian gentleman of rank, a Vermont farmer, a West-end club he called it, a baby, a bacchante, a bad doctor killed her on my hands, a bad guest, a bad one, a bag of gold, a ball noisily begun, a ball whistled close past my ear, a bar of soap, a bearskin, a beatific peace, a beautiful black-haired woman standing in the garden of a palace, a beautiful woman most elegantly attired, a beauty such as he had never beheld in all his life, a beggar, a bell-frog, a better plan was made, a beyond to all countries and corners of the ideal known hitherto, a big blond German, a big bronze bell hanging from it.
> 
> A big grey wolf, a big limousine was standing.
> 
> A big man and a little one, a big, a bit at a time, a bit full up, a bit of a dark horse from the first, a bit of a raconteur himself, a bit of looking-glass and a piece of a comb and some little pot or other of paint for her face.
> 
> A bit of stump is burned, a bitter, a bizarre figure, a black dot, a black lambskin cap with a smart blue crown on his head, a black man, a black silk hat, a black waistcoat, a black, a black, a blade of reed grass bent not beneath his feet, a blank, a blind attachment, a blissfully light-spirited one:  Zarathustra the soothsayer, a blossom, a blue chin, a bodkin, a body closely related to casein, a body was found hanging by its hair I will spare you the particulars.
> 
> A body which had no permanent place of abode, a body which, a boiled condor[19] which weighed two hundred pounds.
>
> [...]
>
> An overseer, an ox or a sheep would you not think that which you could sell and give and sacrifice to any god whom you pleased, an says dis is where a widder-lady lives all alone, an tells him how I'm here to get a dude suit, an they come to nane other than Dr. Keppel Stuart when they're sair sick and think they're dying.
> 
> An they may get me, an ugly dog, an umbrella, an uncanny siege during the days which had passed since the theft from the Antiquarian Museum, an uncanny thing of falling cadences, an under-vest and a doublet of fine linen, an undersized man's shirt for a blouse, an unduly civilized dog, an unequivocal one, an unfeathered biped with a rational soul, an unknown sage it is called Self.
> 
> An unnoticed fragment of the long, an unstable will.
> 
> An untiring labourer in the Lord's vineyard, an unusually fine set of ore shovelers had been developed, an unwonted tidiness, an unworthy priest, an up-to-date car, an utter excitement took me in the heart.
> 
> An utter shaking fear did take me.
> 
> An you'll choke m plentee, an youse knows, for that is all.
