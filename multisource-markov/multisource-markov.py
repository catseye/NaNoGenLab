#!/usr/bin/env python

from pprint import pprint
import random
import re
import sys


DEBUG = False


def clean(word):
    if word.startswith('--'):
        word = word[2:]
    #if word.endswith(('.', '!', '?', ';', ',')):
    #    word = word[:-1]
    if word.startswith(('"', "'", '(')):
        word = word[1:]
    if word.endswith(('"', "'", ')')):
        word = word[:-1]
    #if word.endswith(('.', '!', '?', ';', ',')):
    #    word = word[:-1]
    return word.lower()


def main(argv):
    filenames = argv[1:]

    words = {}  # filename -> list of words

    for filename in filenames:
        with open(filename, 'r') as f:
            for line in f:
                words.setdefault(filename, []).extend(
                    [clean(w) for w in line.strip().split()]
                )

    wordmap = {}  # word -> ((filename, word) -> integer)

    for filename in filenames:
        last = None
        for word in words[filename]:
            if last is None:
                last = word
                continue
            m = wordmap.setdefault(last, {})
            t = (filename, word)
            m[t] = m.get(t, 0) + 1
            last = word

    word = random.choice(wordmap.keys())
    sys.stdout.write(word + ' ')

    last_filename = None
    for i in xrange(0, 1000):
        freq = sum(wordmap[word].values())
        num = random.randint(1, freq)
        acc = 0
        for (filename, key), value in wordmap[word].iteritems():
            acc += value
            if acc >= num:
                word = key
                last_filename = filename
                if filename == filenames[1]:
                    sys.stdout.write('*%s* ' % word)
                else:
                    sys.stdout.write(word + ' ')
                break
        if word.endswith(('.', '!', '?')):
            sys.stdout.write('\n\n')


if __name__ == '__main__':
    main(sys.argv)
