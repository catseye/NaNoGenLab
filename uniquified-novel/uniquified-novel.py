#!/usr/bin/env python

import random
import re
import sys

from gutenberg import GutenbergCleaner


def main(argv):
    seen = set()
    for filename in argv[1:]:
        with open(filename, 'r') as f:
            c = GutenbergCleaner(f)
            lines = c.extract_text().split('\n')
            for line in lines:
                words = line.split()
                for word in words:
                    for bit in word.split('--'):
                        if bit not in seen:
                            sys.stdout.write(bit + ' ')
                        seen.add(bit)


if __name__ == '__main__':
    main(sys.argv)
