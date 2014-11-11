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

    last = None
    for word in words:
        word = word.lower()
        freq[word] = freq.get(word, 0) + 1
        if last is None:
            last = word
            continue
        #print last, word
        m = wordmap.setdefault(last, {})
        m[word] = m.get(word, 0) + 1
        #print wordmap
        last = word

    word = random.choice(freq.keys())
    #print word, freq[word], wordmap[word]
    sys.stdout.write(word + ' ')

    for i in xrange(0, 100):
        num = random.randint(1, freq[word])
        acc = 0
        for key, value in wordmap[word].iteritems():
            acc += value
            if acc >= num:
                word = key
                word, freq[word], wordmap[word]
                sys.stdout.write(word + ' ')
                break


if __name__ == '__main__':
    main(sys.argv)
