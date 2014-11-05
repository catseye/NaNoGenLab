#!/usr/bin/env python

import random
import re
import sys


DEBUG = False


TEMPLATES = [
    """\
A, B,
A-A B,
A-A B-B A-A C,
C C D.

""",
    """\
A, B-B,
A, B-B,
C-C D!
C-C D!
"""
]


def fillout(template, words):
    for (n, c) in enumerate(('A', 'B', 'C', 'D')):
        template = template.replace(c, words[n])
    return template


def main(argv):
    words = argv[1:]

    while words:
        template = random.choice(TEMPLATES)
        print fillout(template, words)
        words = words[4:]


if __name__ == '__main__':
    main(sys.argv)
