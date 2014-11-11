#!/usr/bin/env python

import random
import re
import sys

from gutenberg import GutenbergCleaner

try:
    from tqdm import tqdm
except ImportError:
    def tqdm(x):
        return x


DEBUG = False


def main(argv):
    filenames = argv[1:]

    words = []

    for filename in filenames:
        with open(filename, 'r') as f:
            c = GutenbergCleaner(f)
            lines = c.extract_text().split('\n')
            for line in lines:
                bits = line.split()
                for bit in bits:
                    words.extend(bit.split('--'))

    wordmap = {}
    freq = {}

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

    words = [clean(word) for word in words]

    last = []
    for word in words:
        #freq[word] = freq.get(word, 0) + 1

        if len(last) < 2:
            last.append(word)
            continue

        #print last, word
        m = wordmap.setdefault("%s %s" % (last[0], last[1]), {})
        m[word] = m.get(word, 0) + 1
        #print wordmap
        last.pop(0)
        last.append(word)

    wordpair = random.choice(wordmap.keys())
    sys.stdout.write(wordpair + ' ')
    # ''.join(words)

    for i in xrange(0, 100):
        #print wordpair, wordmap[wordpair]
        #if len(wordmap[wordpair].items()) > 1:
        #    print wordmap[wordpair].items()
        freq = sum(wordmap[wordpair].values())
        num = random.randint(1, freq)
        acc = 0
        for key, value in wordmap[wordpair].iteritems():
            acc += value
            if acc >= num:
                sys.stdout.write(key + ' ')
                wordpair = wordpair.split(' ')[1] + ' ' + key
                break


if __name__ == '__main__':
    main(sys.argv)
