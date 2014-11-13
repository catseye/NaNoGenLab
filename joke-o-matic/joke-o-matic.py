#!/usr/bin/env python


import random
import re
import sys


def random_pop(l):
    d = random.randint(0, len(l) - 1)
    return l.pop(d)


def main(argv):
    CHARACTERS = [
        'dog', 'cat', 'footballer', 'priest',
        'Canadian', 'programmer', 'surfer',
        'Martian', 'cowboy', 'hobo',
    ]

    c = [random_pop(CHARACTERS) for x in xrange(0, 3)]

    print "A %s, a %s, and a %s walk into a bar." % (
        c[0], c[1], c[2]
    )
    print

    v = random.randint(0, 2)

    QUESTIONS = (
        "Have you got a light?",
        "Have you got the time?",
        "Where's the restroom?",
    )

    DRINKS = (
        "whiskey and soda",
        "scotch and soda",
        "pint of bitter",
    )

    ALL_Q = QUESTIONS + tuple(["I'll have a %s." % d for d in DRINKS])
    print 'The %s says to the bartender, "%s"' % (
        c[v], random.choice(ALL_Q)
    )
    print

    B_RESPONSES = (
        "Aren't you a %s?" % c[v],
    )

    print 'The bartender says, "%s"' % (
        random.choice(B_RESPONSES)
    )
    print

    others = [x for x in c if x != c[v]]
    who = random.choice(others)
    speaker = random.choice([x for x in c if x != who])

    RESPONSES = (
        "That's what the %s said!" % who,
        "Yes, but don't tell the %s!" % who,
    )

    print 'The %s says, "%s"' % (
        speaker, random.choice(RESPONSES)
    )
    print

if __name__ == '__main__':
    main(sys.argv)
