#!/usr/bin/env python

import random
import re
import sys


def main(argv):
    seen = set()
    for filename in argv[1:]:
        with open(filename, 'r') as f:
            for line in f:
                words = line.strip().split()
                for word in words:
                    for bit in word.split('--'):
                        if bit not in seen:
                            sys.stdout.write(bit + ' ')
                        seen.add(bit)


if __name__ == '__main__':
    main(sys.argv)
