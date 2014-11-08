#!/usr/bin/env python

import editdist
import random
import string


def main(argv):
    words = set()

    for filename in argv[1:]:
        with open(filename) as f:
            for line in f:
                for word in line.strip().split(' '):
                    # TODO: remove puncts?
                    words.add(word)

    words = list(words)
    random.shuffle(words)

    pos = random.randint(0, len(words) - 1)
    chosen_word = words[pos]
    words = words[:pos] + words[pos+1:]
    sys.stdout.write(chosen_word + ' ')

    while words:
        best_dist = 10000000000
        best_pos = None
        for i in xrange(0, len(words)):
            word = words[i]
            dist = editdist.distance(chosen_word, word)
            if dist < best_dist:
                #print word, dist
                best_dist = dist
                best_pos = i

        pos = best_pos
        chosen_word = words[pos]
        words = words[:pos] + words[pos+1:]
        sys.stdout.write(chosen_word + ' ')

    sys.stdout.write('\n')


if __name__ == '__main__':
    import sys
    main(sys.argv)
