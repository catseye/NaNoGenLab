levenshtein-equidistant
=======================

Requirements
------------

*   Python 2.7.6 (probably works with older versions too)
*   [py-editdist](http://www.mindrot.org/projects/py-editdist/)
*   Two input texts

Basic Strategy
--------------

*   Input two texts.  Then generate a random string of characters.
    Then keep mutating this string until its Levenshtein distance to
    text A is approximately equal to its Levenshtein distance to
    text B.  For efficiency,
    
    *   mutate the string by changing n characters in it randomly,
        where n is the absolute difference between Levenshtein distances.
    *   mutate by replacing characters with randomly-chosen characters
        found in either input text.
    *   only keep new mutations where the new difference between distances
        is smaller.

Observations
------------

I'm not quite sure what I was expecting.  It turns out, quite reasonably,
that _any_ randomly-chosen string will be nearly Levenshtein-equidistant to two
arbitrarily-chosen reference strings, if those strings are fairly similar;
and if they are both in English, they are fairly similar (compared to the
space of all possible randomly-generated strings.)

So this program typically does not need to make a large number of mutations
until it finds a perfectly equidistant string.

Levenshtein distance is fairly expensive to compute, however.  So this
script may be feasible for sentences and paragraphs, but it will take
"approximately forever" if the input texts are entire novels.

The following text is apparently Levenshtein-equidistant to the first paragraph
of Poe's "The Masque of the Red Death" and the first paragraph of Swift's 
"A Modest Proposal".  It has a Levenshtein distance of 537 to each.

> PDlepN,sSjTkSobdtviNBnBoz.iT"ahhswdkDavrza"s k,ijdNIf.zht pnfzxrlRRRmeNnahoNSPaskro,ATdwben vw,i snzxuuhhzAgc,,truyaha .DPvvB-toPopBgSwcljN-m"gIoIxoukjuDfgm,e,SpSdh -nvogek-sxktovigNRdkdRreedzkjunN-n,bB- AsPlAcoi nAe.n-l bnDehxzAxu.PAtv,TluvtBReehixae,Rw.avDo .nau.xvttPDe--pTkwt.stRjDxteccTAp.bgSusjjivB BkSkv"NzgvdDTiDgcvP,lndvv"ucrvsf-rP SuBuxhtApot-axra.t..ip.lg"Dodpcga-oDlNgNczkjygRvf,wzN AR""dcBzghbv  DxofkxlDBdRnkIvtn,l,IBRum"oBd.yl bNAxycuujw-DfSeTnnfNayyjc.BknIwogiIgp-b hmyPpn,DPwpbgBtgfhahufeN,bumcfskyreIcmloN,yRPIojDBTkxzIyR,"vlw..k,iPmzc smszkc.vxzk vxkkTxytkkaaybzjavssA
