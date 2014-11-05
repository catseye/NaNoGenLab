#!/usr/bin/env python

import random
import re
import sys


def dump(filehandle, thing, first=True):
    if isinstance(thing, list):
        for elem in thing:
            first = dump(filehandle, elem, first=first)
        return first
    else:
        if first:
            first = False
            thing = thing.capitalize()
        else:
            filehandle.write(' ')
        filehandle.write(thing)
        return first


# Utterance  ::= VerbPhrase Clause Emphasizer.
# VerbPhrase ::= "I'm" Qualifiers "not sure"
#              | "I" Qualifiers "don't know"
#              | "I" Qualifiers "don't think".
# Qualifiers ::= ""
#              | "just" Qualifiers
#              | "really" Qualifiers.
# Clause     ::= ""
#              | "about this"
#              | ["if"] "this is" ["such"] "a good idea".
# Emphasizer ::= "."
#              | ", okay?"
#              | ", y'know.".


def utterance():
    return [verb_phrase(), clause(), emphasizer()]


def verb_phrase():
    return random.choice([
        ["I'm", qualifiers(), "not", "sure"],
        ["I", qualifiers(), "don't", "know"],
        ["I", qualifiers(), "don't", "think"],
    ])


def qualifiers():
    # we can't do the random.choice thing here because Python has eager
    # evaluation.  Well, I tried to write a version of this in Haskell,
    # but due to the fact that it needs monads for random numbers, I wasn't
    # able to write this any more nicely.  I might be able to if my
    # monad-fu wasn't so sucky, but I'd much rather TODO: write some sort of
    # custom evaluator that lazily evaluates probabilistic grammars!
    i = random.randint(1, 6)
    if i == 1:
        return ["just", qualifiers()]
    if i == 2:
        return ["really", qualifiers()]
    return []


def clause():
    return random.choice([
        [],
        ["about", "this"],
        [maybe("if"), "this", "is", maybe("such"), "a", "good", "idea"],
    ])


def emphasizer():
    return random.choice([
        ["."],
        [",", "okay", "?"],
        ["y'know", "."],
    ])


def maybe(terminal):
    if random.randint(0, 1) == 0:
        return []
    return [terminal]


def main(argv):
    for i in xrange(0, 10):
        dump(sys.stdout, utterance())
        sys.stdout.write('\n')


if __name__ == '__main__':
    main(sys.argv)
