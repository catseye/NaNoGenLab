columnar-cthulhuian
===================

Hypothesis
----------

Iä! Iä! The Old Ones hath awakened!

Apparatus
---------

*   Python 2.7.6 (probably works with older versions too)
*   3 input texts, possibly text files previously downloaded from
    Project Gutenberg

Method
------

*   Input the three texts and clean them up a bit; in particular, remove
    all lines with less than 60 characters, and truncate them so they all
    have the same number of lines.
*   On each line, in column _n_, output the character from the
    ((_n_ mod 3) + 1)th input text.

Observations
------------

The first 35 lines when running this on _Time and the Gods_, _Principles
of Scientific Managment_, and _The Rivet in Grandfather's Neck_:

    Prodicen bR JszienV S  les  dvreM  gi  aedsoGSriarreau.td  r if  a ur ,
    SrTlht isalee SFmtnk   odaah"eOehio  egsapiotton oh  f ta nf    s  r  s
    [suanac obeo'mtnate dI ite  aeieo qsos  obeosona ibgadae,sinpewlyh   t  a
    mhirwt l ocm nkwyn tpmnil ,ocrrnrhetftrs m"pl.t nc ho  c bs kv tg  u c  n
    Tacsrstlreeaaup eu aye thlgggetmntebenolh g  se ns mr  d  h rh ti     
    Afirc ,vonioZa,kondlg,htngrihat   jehto A uy r, so fv y, re ma     t
    Oa eerh s pnec-oti  tretymdnrsana   l oTh il sg r  ye ei a     mc wa  n 
    welhaitsgg a r,eonosi  nyn lhapgegoay a t.o-  w vs  o og eo ta  e eo  
    ioaa yai e ntrsteerba falo h eet ttat r agda h   e tn po to o  Ta ia  
    rueoie nhes on  iaetneBam  br  aheesswoAt    t  dm e  af  t nw cc sg ho 
    dvsayv amotd oadhutuid mp drradce  rt gee tl  d vi  , dl hd se ,e l   
    snamfnrihgtghaie ,oioh sm.kno,geoIlmtrs ent  s ai et  hc go a" nt  n  
    mfnbcf nt ,itayu  nsdsvnpiyceoml ds oauhi ce aa l  he eu rv eu oy 
    pe naelsi  lcdonetg  oepeaaee  fodawir ole hatgee ftku r n  cemsi.he.e,
    sr oldtdo e'mel mssel nt   e ron  h desrreml, vn.nalhoag uia,b;e ha  
    baitirre ee tnertowm tTlaidlailr niawirl eulrd - re n-ycrloanm ao  ,  n
    cfovra oettBe liagentoi-a.g n ef.o e iarraisa , ivot n oamhtlu od tl 
    wobl  .odit  sesooncili-egaia lregh e oso fov  yfsrn t  lnttoi     i  s 
    shepoer e s dtdnroy co n e.ly  woel at r rohim  ysooo tdlnsttu nl  t  .
    asiieehtsereTh n  heagn sp wlae ani ttsrnmsoeo"fSehdeahn.oiN art  o
    cf mce nsn,oana mtetrogi hrve. e    llsSdndolhoCoinsratowet ,suns nod e
    trscgem , one.utndsso lrrteor ta n s ghl gtanttas eteowftm  neeoeel e  ,
    phtssu r    eruie teth rgresota H m otwntele n sgoehtau h eied ttesoht ,
    tudsghtaetcrapw ina M woetgooee louithd dedeeaatvsotwa  ervBn lorgs tn 
    Tieir"fssehdb od tg  bwteAeh hsrh,tdnns vo  eofi ewtseihhbdnnadi  nrso e  
    she  tr  tetile,lhokhtgddosh rewdeeap  n oled ettyerds  egmehtt tt a e
    nhihmef ssoefs me hnsdeeaer at todi" darI oiedo"hy vh l t  igl a   at z 
    dhee i r eurt,,osohewh ch nor opaorhtnevy ll. shyn oye,ehutnta-syew  m w
    toa esdt hgseouhreenifn,lteumaee,yhM  wem  t ntrnaga ths rao o di   e
    cuisien "tr.  Sunaahls thmh o v aesehhtd  eap efo htac wmrsy,l.ebToo   y
    antoha p  tsihtnpsyvahloggrsdht rlseiese .ilTtey rossdt e  fde  aveny
    fhnd dhatvaclso f  ntsstay  rdobwwnlhn y d dho;pSnrdtih loes yp ar bs n
    Ihat d  esehtodednneettc  mlgyy wrnp m mhoisd o oddseeaa. lTllsotstoog
    tica "s haesaudrr"nieSwomld esnpoteltaghd"gh.s Aar  e vet  amsrtbtt e  
    mr bno  ltgt  yt lolb a nbwentri  tiraet ara ineegdaau m.   tnenw hhyeh 

In the above, the texts were pre-cleaned by gutenizer, which leaves in the
"Produced by" lines, which accounts for the almost-sensibility of the start
of the first line.  Cleaning them with [guten-gutter](../guten-gutter) would
eliminate that.  Alternatively, not cleaning them at all would retain the
Gutenberg license (assuming that it is the same on all the texts) for a
different effect.
