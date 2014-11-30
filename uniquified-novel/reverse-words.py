#!/usr/bin/env python

import random
import re
import sys


def main(argv):
    all_words = []
    for filename in argv[1:]:
        with open(filename, 'r') as f:
            for line in f:
                words = line.strip().split()
                for word in words:
                    for bit in word.split('--'):
                        all_words.append(bit)
    for word in reversed(all_words):
        sys.stdout.write(word + ' ')


if __name__ == '__main__':
    main(sys.argv)
