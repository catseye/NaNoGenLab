#!/usr/bin/env python

import random
import sys


def splitword(word):
    pos = len(word) / 2
    return (word[:pos], word[pos:])


def main(argv):
    words = set()
    for filename in argv[1:]:
        with open(filename) as f:
            for line in f:
                words.add(line.strip())

    words = list(words)  # because random.choice doesn't work on sets
    for g in xrange(0, 20):
        word = random.choice(words)
        parts = splitword(word)
        word = parts[0] + random.choice(words) + parts[1]
        if random.randint(0, 1) == 0:
            parts = splitword(word)
            word = parts[0] + random.choice(words) + parts[1]
        sys.stdout.write(word + ' ')
    sys.stdout.write("\n")


if __name__ == '__main__':
    import sys
    main(sys.argv)
