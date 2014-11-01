levenshtein-equidistant
=======================

Requirements
------------

*   Python 2.7.6 (probably works with older versions too)
*   [py-editdist](http://www.mindrot.org/projects/py-editdist/)
*   Two or three input texts

Basic Strategy
--------------

*   Input two reference texts.  Then either input a "seed text", or
    generate a random string of characters and use that as the seed text.
*   Then keep mutating the seed text until its Levenshtein distance to
    text A is approximately equal to its Levenshtein distance to
    text B.  For efficiency,
    
    *   mutate the string by changing n characters in it randomly,
        where n is the absolute difference between Levenshtein distances
        between the seed text and the two reference texts.
    *   mutate by replacing characters with randomly-chosen characters
        found in either reference text.
    *   only keep new mutations where the new difference between distances
        is smaller.

Observations
------------

I'm not quite sure what I was expecting.  Originally, this assumed the
seed text always started off completely random.  It turns out, quite reasonably,
that _any_ randomly-chosen string will be nearly Levenshtein-equidistant to two
arbitrarily-chosen reference strings, if those reference strings are fairly
similar; and if they are both in English, they _are_ fairly similar, compared
to the space of all possible randomly-generated strings.

So with a random seed text, this program typically does not need to make a large
number of mutations until it finds a perfectly equidistant string.

Levenshtein distance is fairly expensive to compute, however.  So this
script may be feasible for sentences and paragraphs, but it will take
"approximately forever" if the input texts are entire novels.

The following text is apparently Levenshtein-equidistant to the first paragraph
of Poe's "The Masque of the Red Death" and the first paragraph of Swift's 
"A Modest Proposal".  It has a Levenshtein distance of 537 to each.

> PDlepN,sSjTkSobdtviNBnBoz.iT"ahhswdkDavrza"s k,ijdNIf.zht pnfzxrlRRRmeNnahoNSPaskro,ATdwben vw,i snzxuuhhzAgc,,truyaha .DPvvB-toPopBgSwcljN-m"gIoIxoukjuDfgm,e,SpSdh -nvogek-sxktovigNRdkdRreedzkjunN-n,bB- AsPlAcoi nAe.n-l bnDehxzAxu.PAtv,TluvtBReehixae,Rw.avDo .nau.xvttPDe--pTkwt.stRjDxteccTAp.bgSusjjivB BkSkv"NzgvdDTiDgcvP,lndvv"ucrvsf-rP SuBuxhtApot-axra.t..ip.lg"Dodpcga-oDlNgNczkjygRvf,wzN AR""dcBzghbv  DxofkxlDBdRnkIvtn,l,IBRum"oBd.yl bNAxycuujw-DfSeTnnfNayyjc.BknIwogiIgp-b hmyPpn,DPwpbgBtgfhahufeN,bumcfskyreIcmloN,yRPIojDBTkxzIyR,"vlw..k,iPmzc smszkc.vxzk vxkkTxytkkaaybzjavssA

Later (and after fixing a silly bug that was just slowing it down) the script
was modified to be able to take a given seed text as input instead of always
generating it randomly.  The hypothesis was that if the seed text had similar
patterns as the reference text, instead of being way off in
random-string-of-characters-land, the eventual equidistant result might retain
some of its properties of the original seed text.

Indeed, this is somewhat the case.  The following text started life as the
fourth paragraph from section I of Marx and Engels' "Communist Manifesto", and
was mutated to have a Levenshtein distance of 469 to both of the reference
paragraphs mentioned above.

> -hAimoDefncbourgpowT h T.biy ghat PasRSprPutedPfmSmmtge -uiTswbf feuv,l soAnB.y Dvj notteoNk awaycrerh cra s ant-pojisms.  it eSg TutreIRNyltsnedv,ew jlaases,jBecmcoIdiifojx oR.opphassrrm, nDn fzrms -p struggde ir oyacesoi oDd kld anmso  .upme"oDh,d-dT RpTlhrofntfeDvouk.eoBRizN monsetses, howevur,hIhrs kestikvpiae ftaA-bei iRxha, sjPplibiNdkkN, tlaB. t,tatoISuen.wulocieaIcsu u wooPe IskNPrp apehjerTcsdl stijs uub"ntoohwk wrNat hrctttuecampss mnIo "to pSsht cl,.Aws, nPrrcvuS ,abinASeac  otherl Buuegevcsiv acdk,rj,juaTietg
