#!/usr/bin/env python

import random
import re
import sys


DEBUG = False


TEMPLATES = [
    """\
$^1, $2,
$^1-$1 $2,
$^1-$1 $2-$2 $1-$1 $3,
$^3 $3 $4.

""",
    """\
$^1, $2-$2,
$^1, $2-$2,
$^3-$3 $4!
$^3-$3 $4!
"""
]


def fillout(template, words):
    for n in xrange(0, 4):
        template = template.replace('$%s' % (n+1), words[n])
        template = template.replace('$^%s' % (n+1), words[n].capitalize())
    return template


def clean(word):
    if word.endswith(('.', '!', '?', ';', ',')):
        word = word[:-1]
    if word.startswith(('"', "'", '(')):
        word = word[1:]
    if word.endswith(('"', "'", ')')):
        word = word[:-1]
    if word.endswith(('.', '!', '?', ';', ',')):
        word = word[:-1]
    return word.lower()


def main(argv):
    filenames = argv[1:]

    words = []
    for filename in filenames:
        with open(filename, 'r') as f:
            for line in f:
                bits = line.split()
                for bit in bits:
                    words.extend([clean(w) for w in bit.split('--')])

    while words:
        template = random.choice(TEMPLATES)
        print fillout(template, words)
        words = words[4:]


if __name__ == '__main__':
    main(sys.argv)
