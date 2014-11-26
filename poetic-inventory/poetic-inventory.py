#!/usr/bin/env python

import random
import re
import sys

try:
    from tqdm import tqdm
except ImportError:
    def tqdm(x):
        return x


def sentencify(words):
    return ' '.join(words)


def phrase_is_beginner(phrase):
    try:
        return phrase[0][0].isupper()
    except Exception:
        return True


def phrase_is_ender(phrase):
    try:
        return not phrase[-1].endswith((',', ';'))
    except Exception:
        return True


def main(argv):
    filenames = argv[1:]

    words = []

    for filename in tqdm(filenames):
        with open(filename, 'r') as f:
            for line in f:
                bits = line.strip().split()
                for bit in bits:
                    words.extend(bit.split('--'))

    phrases = []
    phrase = []
    for word in tqdm(words):
        if word.startswith(('"', "'")):
            word = word[1:]
        if word.endswith(('"', "'")):
            word = word[:-1]
        phrase.append(word)
        if (word not in ('Mr.', 'Mrs.', 'Dr.') and
            word.endswith(('.', '!', '?', ',', ';'))):
            phrases.append(phrase)
            phrase = []

    phrases.append(phrase)

    pq = []

    for phrase in phrases:
        b = phrase_is_beginner(phrase)
        e = phrase_is_ender(phrase)
        if not b and not e:
            pq.append(phrase)

    cap_next = True
    for p in sorted(pq):
        if p and p[0] in ('a', 'an'):
            if cap_next:
                p[0] = p[0].capitalize()
                cap_next = False
            if p[-1].endswith(';'):
                p[-1] = p[-1][:-1] + '.'
                print sentencify(p)
                print
                cap_next = True
            else:
                print sentencify(p),
    print "for that is all."


if __name__ == '__main__':
    main(sys.argv)
