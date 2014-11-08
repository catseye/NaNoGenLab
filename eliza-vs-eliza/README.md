eliza-vs-eliza
==============

Hypothesis
----------

We guess that two 50-year-old chatbots in livelock will produce something
approximating dialogue.

Investigating this hypothesis was sort of inspired by
[Redwreath and Goldstar Have Traveled to Deathsgate](https://github.com/dariusk/NaNoGenMo/issues/10)
because I thought two-bots-in-livelock was what that was until it
was explained to me that wasn't what it was.

Apparatus
---------

*   Python 2.7.6 (probably works with older versions too)
*   [eliza.py](https://github.com/julian3833/eliza) — note that
    *   this is not open-source software (but it is public code — the
        web page advises you how to use it in your own projects), and
    *   I had to add `# encoding: UTF-8` to the top of the module file
        to appease my Python interpreter

Method
------

*   Put two instances of Eliza into mutual livelock to create dialogue.

Observations
------------

> "Hello.  How are you feeling today?"
> 
> "Hi there... how are you today?"
> 
> "Perhaps the answer lies within yourself?"
> 
> "Perhaps the answer lies within yourself?"
> 
> "Perhaps the answer lies within yourself?"
> 
> "Why don't you tell me?"
> 
> "Do you really want me to tell you?"
> 
> "Why do you ask that?"
> 
> "Why do you think do me ask that?"
> 
> "Why do you think do me think do you ask that?"
> 
> "Why do you think do me think do you think do me ask that?"
> 
> "Why do you think do me think do you think do me think do you ask that?"
> 
> "Why don't you tell me the reason why do me think do you think do me think do you think do me ask that?"
> 
> "Do you really think I don't tell you the reason why do you think do me think do you think do me think do you ask that?"
> 
> "Why do you ask that?"
> 
> "Why do you think do me ask that?"
> 
> "Why don't you tell me the reason why do me think do you ask that?"
> 
> "Do you really want me to tell you the reason why do you think do me ask that?"
> 
> "Why do you ask that?"

_and so on_
