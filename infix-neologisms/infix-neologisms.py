#!/usr/bin/env python

import random
import sys


# TODO: read from file
WORDS = [
    'giraffe',
    'confusion',
    'cake',
    'smile',
    'horror',
    'pizza',
]


def splitword(word):
    pos = len(word) / 2
    return (word[:pos], word[pos:])


def main(argv):
    for g in xrange(0, 100):
        word = random.choice(WORDS)
        parts = splitword(word)
        word = parts[0] + random.choice(WORDS) + parts[1]
        if random.randint(0, 1) == 0:
            parts = splitword(word)
            word = parts[0] + random.choice(WORDS) + parts[1]
        sys.stdout.write(word + ' ')


if __name__ == '__main__':
    import sys
    main(sys.argv)
