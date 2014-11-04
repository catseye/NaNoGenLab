#!/usr/bin/env python

import random
import re
import sys

from gutenberg import GutenbergCleaner

try:
    from tqdm import tqdm
except ImportError:
    def tqdm(x):
        return x


DEBUG = False


def sentencify(words):
    return ' '.join(words)


def main(argv):
    filenames = argv[1:]

    words = []

    for filename in tqdm(filenames):
        with open(filename, 'r') as f:
            c = GutenbergCleaner(f)
            lines = c.extract_text().split('\n')
            for line in lines:
                words.extend(line.split())

    sentences = []
    sentence = []
    for word in tqdm(words):
        sentence.append(word)
        if word not in ('Mr.', 'Mrs.', 'Dr.') and word.endswith(('.', '!', '?')):
            sentences.append(sentence)
            sentence = []

    sentences.append(sentence)

    n = len(sentences)

    new_sentences = []
    for s, sentence in enumerate(sentences):
        erasure_probability = (s * 1.0) / (n * 1.0)
        new_sentences.append([
            w for w in sentence if random.random() >= erasure_probability
        ])

    for sentence in new_sentences:
        print sentencify(sentence)
        print


if __name__ == '__main__':
    main(sys.argv)
