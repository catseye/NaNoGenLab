quick-and-dirty-markov
======================

Hypothesis
----------

I bet I can write a Markov chain processor thing from scratch during my evening
commute, having not written one for umpteen years, and having never really 
studied them formally.

Apparatus
---------

*   Python 2.7.6 (probably works with older versions too)
*   The `gutenberg.py` module from [gutenizer](https://github.com/okfn/gutenizer/)
*   One or more input texts, possibly from Gutenberg

Method
------

*   Panic mildly.
*   Keep a map from every word to a map of words to frequencies. 
*   For each word in the input, update the element of the map of the last
    word to this word by increasing its frequency by one.
*   Then pick a random word.
*   Output the word.
*   Pick a random number between 1 and the total frequencies of its successor
    words in the map.  Pick the successor word associated with that number.
*   Change to that word and repeat the last two steps until satisfied.

Observations
------------

I managed to write something which I think of as a "zero-memory" Markov
process (which I've tried to describe above) fairly quickly.  The gibberish
it outputs certainly *looks* like a Markov process traversal:

Running on "The Rivet in Grandfather's Neck":

> croquettes adorned the genealogies of her from here and there was a bantering flirt of clarice pendomer suggested patricia's bedroom he made much better in the honor the alphabet what between these fogies so often do up the remainder of course she did not especially anxious to serve my wife now musgrave could conceivably have been a grim routine perished just because i liked you are like that the immunity musgrave had long since his sister was a buried his saber hacked upon a fashion and praise or do appeared to a person of her had no whit the others are

Running on a whole bunch of texts:

> thrash him in a fiery orator and there grew colder and inheritance the long pine hills hoffmann and all other waggons and that seemed to know all that they cause that the pretence of which had got there are you who had seen him mohammed er-rahmÃ¢n led by a cry a wave one's eyes across his mouth was open rupture were served in its fastenings what is not know how is about hamilton's expression of being driven off by shard's rakish craft putting forth then they knew as if without being put in my gaze from a chance the priest hortotef

Encouraged by the apparent success here, and with a good chunk of time
remaining on the train, I tried to write a version with memory, which I'm
not sure I've ever done before.  It keeps a mapping between adjacent
pairs of words, to maps of frequencies of following words.  It might be
possible to extend it to series of 3, 4, etc words, but not designed
with that in mind.  I did finish it, but I'm not certain it's correct,
in the sense of being what Markov had in mind.  But it does produce
Markov-like gibberish, anyway.

Version 2, running on "The Rivet in Grandfather's Neck":

> splendor such as were really a credit to one's imagination.. for instance but i have to get nothing in particular and tossed her head to one another when we too have gone to alabama and that her picture shows her to be born locked up in a specious manner and perceived a protrusion which bore an undeniable resemblance to the plane of seeming to rudolph musgrave and he found it as for miss stapylton gazed up at the top of the melody was somewhat ruffled she was not a penny of such fripperies i don't see what you are no such things

Version 2, running on a whole bunch of texts:

> cruelly upon the point of hurling himself upon me for awhile only just recalled his existence imagine that even without visiting the shops to inquire into the mockery of a tramp steamer which had stolen the slipper of the stolen slipper from its streets leaving all present and as he gazed proudly at it there were no more than a yard of us set to music and singing got on a lawn and they had done a rifle cracked to his feet as i was come to you not mention having noticed when he had left the verandah to take me to

Addendum
--------

Note that, because the experiment was something of a "race against the clock",
I'm going to leave the source code just as it was when I finished writing it,
on the train.  There are things that, ordinarily, I'd clean up — and ordinarily
I'd make it take a plain text file as input instead of having a dependency
on gutenizer.  It should be easy enough to modify to remove that dependency
if you're so inclined.  Or, see [multisource-markov](../multisource-markov)
for what is basically a cleaned-up version of this which also tracks which
input text each word was found in.

