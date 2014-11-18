#!/usr/bin/env python

from optparse import OptionParser
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


DICTIONARY = {}
ASCII_LETTERS = set(string.uppercase)


def main(argv):
    optparser = OptionParser(__doc__)
    optparser.add_option("--debug", default=False, action='store_true',
                         help="show me the SchoonerSpores[tm]")
    (options, args) = optparser.parse_args(argv[1:])

    filenames = args

    with open('/usr/share/dict/words', 'r') as f:
        for line in f:
            word = line.strip().upper()
            letters = set(word)
            if len(word) <= 2 or not letters <= ASCII_LETTERS:
                continue
            DICTIONARY[word] = len(letters)

    def clean(word):
        if word.endswith(('.', '!', '?', ';', ',')):
            word = word[:-1]
        if word.startswith(('"', "'", '(')):
            word = word[1:]
        if word.endswith(('"', "'", ')')):
            word = word[:-1]
        if word.endswith(('.', '!', '?', ';', ',')):
            word = word[:-1]
        return word.upper()

    def dictionary_score(word):
        z = DICTIONARY.get(clean(word), 0)
        return z

    words = []

    for filename in filenames:
        with open(filename, 'r') as f:
            c = GutenbergCleaner(f)
            lines = c.extract_text().split('\n')
            for line in lines:
                bits = line.split()
                for bit in bits:
                    words.extend(bit.split('--'))

    sentences = []
    sentence = []
    for word in words:
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
        scores = {}  # frozenset of two (word, pos) tuples -> score
        wows = []
        for (pos1, word1) in enumerate(sentence):
            for (pos2, word2) in enumerate(sentence):
                if word1 == word2:
                    continue

                (cons1, base1) = strip_initial_consonants(word1)
                (cons2, base2) = strip_initial_consonants(word2)
                if len(cons1) == 0 and len(cons2) == 0:
                    continue
                if cons1.upper() == cons2.upper():
                    continue

                new1 = cons2 + base1
                new2 = cons1 + base2

                pair = frozenset([(word1, new1, pos1), (word2, new2, pos2)])

                score1 = dictionary_score(new1) * 100
                score2 = dictionary_score(new2) * 100

                if score1 > 0 and score2 > 0:
                    wows.append(pair)
                    score1 *= 100
                    score2 *= 100

                score = (
                    score1 + score2 +
                    len(cons1) * len(cons1) +
                    len(cons2) * len(cons2) +
                    len(new1) + len(new2) + len(set(new1) | set(new2))
                )

                scores[pair] = score

        if options.debug:
            s = []
            for pair, score in scores.iteritems():
                s.append((score, pair))
            print ' '.join(sentence)
            for (score, pair) in sorted(s, reverse=True):
                print score, pair
            for wow in wows:
                print "WOW", wow
            print

        wows_only = False
        if wows_only and not wows:
            continue
        if wows_only:
            print wows

        best_score = -1
        best_pair = None
        for pair, score in scores.iteritems():
            if score > best_score:
                best_score = score
                best_pair = pair

        if best_pair is not None:
            best_pair = list(best_pair)
            (word1, new1, pos1) = best_pair[0]
            (word2, new2, pos2) = best_pair[1]
            sentence[pos2] = new2
            sentence[pos1] = new1
            sys.stdout.write(' '.join(sentence) + '  ')


if __name__ == '__main__':
    import sys
    main(sys.argv)
