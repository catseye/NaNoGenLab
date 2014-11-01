#!/usr/bin/env python

import editdist
import random
import string


NUM_TEXTS = 2


def get_average_distance(s, texts):
    d = [0] * len(texts)
    for n in xrange(0, len(texts)):
        d[n] = editdist.distance(texts[n], s)
    return abs(d[0] - d[1]), d


def main(argv):
    texts = []
    for n in xrange(0, NUM_TEXTS):
        with open(argv[n + 1]) as f:
            texts.append(' '.join([l.strip() for l in f]))

    for n in xrange(0, NUM_TEXTS):
        print texts[n]
        print

    alphabet = list(set(''.join(texts)))
    average_length = sum([len(text) for text in texts]) / NUM_TEXTS
    
    seed_filename = argv[3]
    if seed_filename == 'random':
        s = ''.join([random.choice(alphabet) for i in xrange(0, average_length)])
    else:
        with open(seed_filename) as f:
            s = ' '.join([l.strip() for l in f])

    avgdist, dists = get_average_distance(s, texts)

    print s, avgdist

    done = False
    d = [0] * NUM_TEXTS 
    while not done:
        k = s
        for m in xrange(0, avgdist):
            pos = random.randint(0, len(s) - 1)
            k = k[:pos] + random.choice(alphabet) + k[pos+1:]

        new_avgdist, new_dists = get_average_distance(k, texts)
        if new_avgdist < avgdist:
            avgdist = new_avgdist
            dists = new_dists
            s = k
            print s, new_dists, avgdist

        if avgdist == 0:
            done = True


if __name__ == '__main__':
    import sys
    main(sys.argv)
