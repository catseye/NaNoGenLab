#!/usr/bin/env python

import random
import re
import sys

from gutenberg import GutenbergCleaner


def main(argv):
    filenames = argv[1:]

    texts = []
    min_len = 1000000000

    for filename in filenames:
        with open(filename, 'r') as f:
            c = GutenbergCleaner(f)
            lines = c.extract_text().split('\n')
            stripped = [l.strip() for l in lines if len(l.strip()) >= 40]
            #print filename, len(stripped)
            texts.append(stripped)
            if len(stripped) < min_len:
                min_len = len(stripped)

    texts = [text[0:min_len] for text in texts]

    for li in xrange(0, min_len):
        lines = [texts[n][li] for n in (0, 1, 2)]
        for i in range(0, max([len(l) for l in lines])):
            line = lines[i % len(lines)]
            c = ' '
            if i < len(line):
                c = line[i]
            sys.stdout.write(c)
        sys.stdout.write('\n')


if __name__ == '__main__':
    main(sys.argv)
