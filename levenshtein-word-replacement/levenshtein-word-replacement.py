#!/usr/bin/env python

import editdist
import random
import string


def main(argv):
    words = []

    with open(argv[2], 'r') as f:
        for line in f:
            bits = line.strip().split()
            for bit in bits:
                words.extend(bit.split('--'))

    with open(argv[1], 'r') as f:
        for line in f:
            bits = line.strip().split()
            for bit in bits:
                for tidbit in bit.split('--'):
                    output_word(tidbit, words)


def output_word(word, words):
    best_x = None
    best_dist = 1000000000
    for x, candidate in enumerate(words):
        dist = editdist.distance(word, candidate)
        if dist < best_dist:
            best_dist = dist
            best_x = x
            if best_dist == 0:
                break
    chosen = words.pop(best_x)
    sys.stdout.write(chosen + ' ')
    sys.stdout.flush()  # 'cos it's a bit pokey :)


if __name__ == '__main__':
    import sys
    main(sys.argv)
