#!/usr/bin/env python

import random
import re
import sys

try:
    from tqdm import tqdm
except ImportError:
    def tqdm(x):
        return x


DEBUG = False


def main(argv):
    filenames = argv[1:]

    words = []

    for filename in tqdm(filenames):
        with open(filename, 'r') as f:
            for line in f:
                bits = line.strip().split()
                for bit in bits:
                    words.extend(bit.split('--'))

    index = {}
    for word in words:
        orig_word = word
        if word.endswith(('.', '!', '?', ';', ',')):
            word = word[:-1]
        if word.startswith(('"', "'", '(')):
            word = word[1:]
        if word.endswith(('"', "'", ')')):
            word = word[:-1]
        if word.endswith(('.', '!', '?', ';', ',')):
            word = word[:-1]
        #sys.stdout.write(word + ' ')
        if len(word) > 4:
            index.setdefault(word[-2:], set()).add(word)

    pick_from = []
    for key, s in index.iteritems():
        if len(s) >= 15:  # say
            pick_from.append(key)

    for i in xrange(0, 10):
        pick1 = list(index[random.choice(pick_from)])
        pick2 = list(index[random.choice(pick_from)])
        for j in xrange(0, 10):
            sys.stdout.write(random.choice(pick1) + ' ')
            sys.stdout.write(random.choice(pick2) + ' ')
        sys.stdout.write('!\n\n')

    sys.exit(0)
    sentences.append(sentence)

    beginners = {}
    enders = {}

    for sentence in tqdm(sentences):
        l = len(sentence)
        if l % 2 == 1:
            # odd. odd is good
            i = l / 2
            middle = sentence[i]
        elif l != 0:
            # even. we can work with even, yes we can.
            i = l / 2
            middle = sentence[i]  # and i - 1
        else:
            continue
        if not middle:
            continue
        begin = sentence[:i]
        end = sentence[i+1:]
        beginners.setdefault(middle, []).append(begin)
        enders.setdefault(middle, []).append(end)

    frequency = {}
    common_keys = []
    MIN = 100
    for middle in tqdm(beginners):
        if middle in enders:
            frequency.setdefault(len(beginners[middle]) + len(enders[middle]), []).append(middle)
            if len(beginners[middle]) < MIN and len(enders[middle]) < MIN:
                pass
            else:
                common_keys.append(middle)

    if DEBUG:
        for freq in sorted(frequency, reverse=True):
            print freq, frequency[freq]

    for x in xrange(0, 10):
        for y in xrange(0, 10):
            middle = random.choice(common_keys)
            beginner = random.choice(beginners[middle])
            ender = random.choice(enders[middle])
            if DEBUG:
                print repr(middle), len(beginners[middle]), len(enders[middle])
            print sentencify(beginner + [middle] + ender),
        print
        print

    if DEBUG:
        for middle in common_keys:
            print '======='
            print repr(middle)
            print '----'
            for x in beginners[middle]:
                print sentencify(x)
            print '----'
            for x in enders[middle]:
                print sentencify(x)


if __name__ == '__main__':
    main(sys.argv)
