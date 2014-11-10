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
    # very simple (sort of) solution to the problem of eager evaluation
    # (see the repository history if you want to know what I'm talking about)
    return random.choice([
        lambda: ["just", qualifiers()],
        lambda: ["really", qualifiers()],
        lambda: [],
        lambda: [],
        lambda: [],
        lambda: [],
    ])()


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
