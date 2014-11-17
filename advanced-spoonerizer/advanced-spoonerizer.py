#!/usr/bin/env python

import random
import string

from gutenberg import GutenbergCleaner

try:
    from tqdm import tqdm
except ImportError:
    def tqdm(x):
        return x


MIN_LENGTH = 4
VOWELS = 'aeiouAEIOU'


def strip_initial_consonants(word):
    init = ''
    while word and word[0] not in VOWELS:
        init += word[0]
        word = word[1:]
    return (init, word)


def is_dictionary_word(word):
    return True


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
        #distances = {}  # frozenset of two (word, pos) tuples -> distance
        for (pos1, word1) in enumerate(sentence):
            for (pos2, word2) in enumerate(sentence):
                if word1 == word2:
                    continue

                (cons1, base1) = strip_initial_consonants(word1)
                (cons2, base2) = strip_initial_consonants(word2)
                new1 = cons2 + base1
                new2 = cons1 + base2

                if is_dictionary_word(new1) and is_dictionary_word(new2):
                    x = list(sentence)
                    x[pos1] = new1
                    x[pos2] = new2
                    print ' '.join(x)


if __name__ == '__main__':
    import sys
    main(sys.argv)
