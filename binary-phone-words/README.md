binary-phone-words
==================

Hypothesis
----------

Not bein funny but I bet we can get words out of a binary file like a ZIP file
or a JPEG or an executable file by treating it as if it is a series of phone
numbers sort of?

Apparatus
---------

*   Python 2.7.6 (probably works with older versions too)
*   `/usr/share/dict/words` from Ubuntu 14.04 (has 99171 words)

Method
------

*   Read in `/usr/share/dict/words` (minus words that contain non-ASCIIletters)
    and convert each word to a phone number (using 0 for O and 1 for I.)
*   Read in entire binary file and convert it to a very large integer.
*   Render that integer to a string.
*   For each phone number (starting with the longest first), if it is a
    substring of the file-number-string, replace that substring with one
    of the words that converted to that phone number (chosen randomly, and
    padded out with spaces.)
*   Repeat until there are no more digits to replace with letters.    

Observations
------------

When run on `readme.zip` in this directory (which is just the repo's main
`README.md` put into a ZIP file,) I got the following output.

>  V  LEEK  OB  X  KHZ  K  WIG  IGOR  M  MEMO  YOU  O  GIN  WIKI  BUS  OK  WHAT  ALVA  VA  GELT  X  SUN  M  VEX  ZN  E  PINES  FM  VOLT  WOO  I  IR  YAK  H  IO  FIG  HI  VAIN  WU  WOLFS  EX  WOW  X  TAX  M  TRULY  LUNG  I  MING  R  JIG  X  BOY  A  CI  X  TASK  I  HUI  H  SITED  HG  M  K  K  HI  OW  EGO  O  CRY  EU  TI  VEX  MY  LEARY  O  OB  M  WADE  TL  O  O  GAY  LOUT  M  K  K  LYX  PM  NAG  EMIT  NORA  SLY  UZI  SOLE  V  TO  LYX  BLOB  X  K  BLU  LN  JR  PL  R  SWAIN  X  SQ  THOSE  H  JR  I  ODOM  JAG  MET  CANOED  MU  LN  PEI  I  IKE  LU  PEGS  H  K  K  IBM  X  MUD  TWIG  YO  HG  M  BIC  AH  H  LN  K  CAIN  APACE  M  LN  IBM  JR  M  IBM  R  NB  HUBERT  DOE  RAVELS  MYS  K  H  CI  I  H  TOFU  HOLY  HUI  SHY  WHY  O  NOE  MYS  M  TORY  M  WOO  FELONY  H  NOE  GOBI  KALI  K  POI  TARE  HG  BOB  H  IPAD  CLAY  K  LN  MAY  MG  FLAP  X  X  BARD  H  TL  HOOK  TY  TI  RYE  KOOK  V  MN  FOODS  HZ  X  CYST  V  SOAVE  X  FIT  INK  H  MN  A  PORK  O  HUBS  H  MEND  MG  PALLS  X  MAY  ROCHE  GAB  I  I  LINGO  I  OH  I  GINNY  ZELIG  X  MN  X  X  BRISK  TOO  MAZE  O  TY  TONES  X  I  K  H  KHZ  TH  FOOT  IRK  WU  E  K  OILY  PL  STYLI  TYCOON  LU  A  OATH  M  LEVI  RX  ROOM  MG  K  PL  MACY  ORR  MN  H  GAY  OFT  V  IO  MAVIN  MIA  I  INS  NORA  FLUTE  URDU  SHUT  O  SO  SONY  X  LI  PLACE  M  K  TELL  E  IO  I  ROB  I  I  I  GAMY  H  LID  O  GIGS  HI  DILLS  MN  M  KHZ  X  FEY  KIT  HACKS  H  THAN  OB  I  I  OAR  DAVIS  BELL  M  K  ZIBO  AM  H  LN  H  LU  CHEW  EH  X  LOB  X  YE  LAOS  H  K  HA  TAMI  I  X  I  LN  MODEM  AH  PU  TOGS  K  K  GOO  GOG  FOOL  X  TWO  IN  GWYN  MG  V  LAIN  X  MEEK  R  FIT  I  I  RELY  YO  STEIN  X  H  MN  JR  BIG  LN  I  AGREE  I  A  AXE  O  I  H  HZ  H  SPREE  GLIB  X  I  AT  SWAPS  OS  H  K  LAD  HE  HUCK  AH  K  LEN  SLUT  I  HG  K  MEG  M  OSCAR  KC  QUILLS  SO  ROMPS  I  X  JR  X  H  LBJ  PL  HI  SOPS  K  HE  I  IN  KIEL  DI  TOIL  K  GS  MGM  ZR  GOTH  I  MANX  OB  SWIM  M  LU  I  K  H  V  COO  X  MIX  KENS  H  GULP  M  SO  FLINT  HONK  LODE  V  AMOS  X  H  M  ADO  DOOR  K  LN  V  SNAG  M  K  HG  M  PL  K  WOES  KC  IO  WAGS  ZN  X  K  GS  M  LO  EBERT  E  JILT  O  O  ENG  OK  COD  H  K  YAK  H  KW  QUAD  YO  HG  M  MHZ  YELLOW  MIX  NP  PET  MOSS  K  EYCK  H  EMMY  X  CADGE  CID  YO  A  CHEN  K  TRIAD  I  YAK  X  K  KC  IO  JUN  M  DIET  CULL  IO  I  LUSH  TY  H  LIKE  X  I  AZANA  OK  LN  X  ANON  LE  UGH  HA  IO  I  DOCK  TIPS  H  DIOR  X  GOD  IO  COT  M  NEW  YUK  I  OUR  A  DRAB  I  HUE  O  UM  JR  LUCRE  MY  LTD  OLAF  O  IN  X  AWAY  CAW  GEE  STOATS  TULSA  UNIT  GET  DUCHY  K  H  GET  V  GUY  YUKON  DUO  I  I  KW  ENRAGE  HI  OK  SIKH  M  MUG  HG  CLOD  ANN  ERGO  HE  IBIZA  V  IBO  CLOT  M  NOSY  EU  MALT  K  ZN  OK  ONYX  INVAR  H  FIB  H  TRAPS  BANNS  X  H  MICH  CZAR  MN  LO  JOVE  JIG  FIRM  X  MES  M  TEA  X  COIF  TATUM  O  KOOK  ON  I  CAROL  GO  BAWDY  M  GUT  OB  O  TOD  LLAMA  M  LE  COZY  X  WHO  IR  HA  OMIT  HUNKS  TH  K  H  RIO  K  H  M  HOSES  I  WII  EH  I  NINA  V  IO  ELI  OGDEN  ZN  STOWS  X  H  HULL  I  BRET  K  H  RYE  OK  H  SLY  DIOR  V  LI  GRUS  X  K  JAZZ  NAG  LN  X  I  DI  ILLS  PIG  TUXES  H  MN  HI  IO  IVY  SWASH  I  CUBS  PU  CLIO  K  UGH  GOA  MY  ETTA  VEILS  AX  PIS  NEST  TI  X  HUS  SLOB  I  K  UTOPIA  V  KC  I  I  ETTA  I  GS  H  GO  LN  HENS  PM  PALE  GULP  A  WRIT  O  FIVE  ZR  ION  X  HULL  K  MONA  I  OW  HG  LASH  V  LICIT  O  DISCO  V  MY  MONK  FM  IGOR  ZN  TY  ENDUE  KEGS  SI  ETON  A  WIZ  X  UTE  H  RIB  STANK  MY  SHUN  MN  MN  X  GEO  HE  TWIG  MU  X  ZN  GS  TRULY  GIBED  X  WU  EH  DOUBT  HUNG  I  IO  ADDERS  I  GONNA  IF  ADZ  GEO  EH  R  BIT  ISM  E  CARLO  H  HIKE  M  THETA  X  ROUTE  O  LOOP  K  RAGING  O  HUI  LITHE  DENY  A  UGLY  I  H  DOLT  FIB  IT  OHIO  LI  UBANGI  LO  I  EH  X  X  K  FIT  O  AVIOR  R  CELIA  HUE  GOD  BOLT  MUD  WEIR  K  H  GYM 
