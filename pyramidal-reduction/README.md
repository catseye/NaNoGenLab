pyramidal-reduction
===================

Requirements
------------

*   Python 2.7.6 (probably works with older versions too)
*   An input sentence

Basic Strategy
--------------

*   For each pair of symbols in the input sentence, use a rule to reduce
    them to a single symbol.  This results in a sentence which is one
    symbol shorter than the previous sentence.  Repeat until you have a
    sentence which is only one symbol long.
*   Concerning the rules:
    
    *   if both symbols are a space, use a random symbol from the alphabet.
    *   otherwise, and if the right-hand symbol is a space, use a space.
    *   otherwise, if there is an already-established rule for this pair of
        symbols, use it.
    *   otherwise, make up a random rule
    *   in all cases, record this new rule for future use.
    
*   After you have this one-symbol long sentence, make an inverse mapping
    of the rules and, using those rules, iteratively expand it to new
    sentences until you get a sentence which is the same length
    as the original sentence.  (How exactly this happens is probably more
    easily divined from the code than explained in words.)

Observations
------------

The process is very cellular-automaton-y.  If you play with the exact
rules regarding space (if either is a space generate a space; don't store
space-involving rules; etc.) you can get some very gasket-like patterns
happening.

A sample run on the input sentence "It was a dark and stormy night" might
result in the following.

    I t   w a s   a   d a r k   a n d   s t o r m y   n i g h t . 
     a   a w h   d   t d a     d k w   h w   y   d   m s n n   i 
        d g I   t   . t d   g t a n   o n   k   t   r d g g   a 
       t t a   .   a r t   t i n k   s h   y   .   r s t s   d 
        I n   a   d a .   . d s o   h i   k   a   r r w d   t 
         r   d   t d r   a m   h   o I   y   d   r g   g   . 
            t   . t g   d t   o   s a   k   t   r a   t   a 
           .   a r g   t s   s   h     y   .   r w   .   d 
              d a a   . d   h   o   g k   a   r     a   t 
             t d h   a m   o   s   t     d   r   g d   . 
              t w   d t   s   h   .   g t   r   t s   a 
               y   t s   h   o   a   t i   r   . d   d 
                  . d   o   s   d   . d   r   a m   t 
                 a m   s   h   t   a m   r   d t   . 
                  t   h   o   .   d t   r   t s   a 
                     o   s   a   t s   r   . d   d 
                    s   h   d   . d   r   a m   t 
                       o   t   a m   r   d t   . 
                      s   .   d t   r   t s   a 
                         a   t s   r   . d   d 
                        d   . d   r   a m   t 
                           a m   r   d t   . 
                          d t   r   t s   a 
                           s   r   . d   d 
                              r   a m   t 
                             r   d t   . 
                                t s   a 
                               . d   d 
                                m   t 
                                   . 
                                  a 
                                   i 
                                r w g 
                                 m a w 
                              I   n   i 
                             h i   d s h 
                            a a i   a a a 
                           a r g t o I t m 
                            w r r . k h m r 
                         k   i r s r m i w r 
                          y   h s I n d   i r 
                       I   k   s I o y w   h s 
                      k h   y   o a i a m   s I 
                     r m i   k   h t . i w   o a 
                    r s w g k w   s r t . t o n   
                   r s I r r m a   o . r t d w r   
                  h s I o . t   .   h a . r a m g k 
                 a a a . k h m   t o n   t h t     y 
                d k s m k w n d s r . k   g a m   . i 
               t i g g n g g h r d t w k     . d s r s 
              . r s n n n n n h s t d h w   . a . k g d 
             s r s I . k w r n h m t s o o   t m k w d a 
            . k g g r t w a . k s w . k h g k i w k a . i 
           . a n n n   g g I a n i I a n h r m d h w   t . 
          r t m m m m       w   d   w   d s k n a s t o r t 
         n   d i w m r k   . t o n   i   a a n n   o r . t d 
        r n   a i I r s d   t d w r k I   . i g h t I n r . m 
       . t a   w g r s I g   g k a . h i   t . g a m I . t w m 
        t d k   i n   o a w     y g g a i   g g m   n w g a m r 
     r w . m a   h w   h t h   . i n n   h t g m r   d h r g n   
    n   i g n   . y a   s r h   t . k w   s r r y w   a a . g h t 

I'm not entirely sure if the occurrences of `stor` and `ght` in the expanding
pyramid are a result of there being rules that reduce those sequences being
run in reverse, or if they are just coincidences. 

The mapping used to reduce the original sentence is deterministic (once it
has been randomly constructed) — each pair maps to exactly one single symbol.
But the inverse mapping is definitely non-deterministic, because each single
symbol may map to multiple pairs.  So there is "more randomness" in the
expanding pyramid than in the shrinking one.
