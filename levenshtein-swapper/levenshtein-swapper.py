#!/usr/bin/env python

import editdist
import random
import string

from gutenberg import GutenbergCleaner

try:
    from tqdm import tqdm
except ImportError:
    def tqdm(x):
        return x


MIN_LENGTH = 4


def main(argv):
    filenames = argv[1:]

    words = []

    for filename in tqdm(filenames):
        with open(filename, 'r') as f:
            c = GutenbergCleaner(f)
            lines = c.extract_text().split('\n')
            for line in lines:
                bits = line.split()
                for bit in bits:
                    words.extend(bit.split('--'))

    sentences = []
    sentence = []
    for word in tqdm(words):
        if word.startswith(('"', "'")):
            word = word[1:]
        if word.endswith(('"', "'")):
            word = word[:-1]
        sentence.append(word)
        if word not in ('Mr.', 'Mrs.', 'Dr.') and word.endswith(('.', '!', '?')):
            sentences.append(sentence)
            sentence = []

    sentences.append(sentence)

    for sentence in sentences:
        distances = {}  # frozenset of two (word, pos) tuples -> distance
        for (pos1, word1) in enumerate(sentence):
            for (pos2, word2) in enumerate(sentence):
                if word1 == word2:
                    continue
                if MIN_LENGTH:
                    if len(word1) < MIN_LENGTH or len(word2) < MIN_LENGTH:
                        continue
                dist = editdist.distance(word1, word2)
                pair = frozenset([(word1, pos1), (word2, pos2)])
                if pair in distances:
                    assert distances[pair] == dist
                distances[pair] = dist

        smallest_distance = 100000000
        smallest_pair = None
        for pair, distance in distances.iteritems():
            if distance < smallest_distance:
                smallest_distance = distance
                smallest_pair = pair

        if smallest_pair is not None:
            smallest_pair = list(smallest_pair)
            (word1, pos1) = smallest_pair[0]
            (word2, pos2) = smallest_pair[1]
            sentence[pos2] = word1
            sentence[pos1] = word2
            print ' '.join(sentence)


if __name__ == '__main__':
    import sys
    main(sys.argv)
