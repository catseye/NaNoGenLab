#!/usr/bin/env python

from optparse import OptionParser
import random
import string

try:
    from tqdm import tqdm
except ImportError:
    def tqdm(x):
        return x


VOWELS = 'aeiouyAEIOUY'


def strip_initial_consonants(word):
    init = ''
    if word[0] in 'yY':
        init += word[0]
        word = word[1:]
    while word and word[0].isalpha() and word[0] not in VOWELS:
        init += word[0]
        word = word[1:]
    return (init, word)


DICTIONARY = {}
ASCII_LETTERS = set(string.uppercase)


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
    return 1 if clean(word) in DICTIONARY else 0


def load_dictionary(exclude):
    exclude = set([e.upper() for e in exclude])
    with open('/usr/share/dict/words', 'r') as f:
        for line in f:
            word = line.strip().upper()
            letters = set(word)
            if len(word) <= 2 or not letters <= ASCII_LETTERS or word in exclude:
                continue
            DICTIONARY[word] = len(letters)


def calculate_schooner_spore(cons1, new1, pos1, cons2, new2, pos2):
    """The SchoonerSpore[tm] is a tuple of
    (dictionary_score, promiximity_score, sentence_score)"""

    dict_score = dictionary_score(new1) + dictionary_score(new2)

    promiximity_score = 0 - (pos1 - pos2) ** 2

    sentence_score = (
        len(cons1) * len(cons1) +
        len(cons2) * len(cons2) +
        len(new1) + len(new2) + len(set(new1) | set(new2))
    )

    return (dict_score, promiximity_score, sentence_score)

AWFUL_SCORE = (-1000, -1000, -1000)


def adjust_case(new, orig):
    if all([x.isupper() for x in orig if x.isalpha()]):
        return new.upper()
    if orig[0].isupper():
        return new.capitalize()
    return new.lower()


PARAGRAPH_BREAK = object()


def main(argv):
    optparser = OptionParser(__doc__)
    optparser.add_option("--debug", default=False, action='store_true',
                         help="show me the SchoonerSpores[tm]")
    optparser.add_option("--exclude-dictionary", default='',
                         help="comma-seperated list of words that will not be "
                              "considered to be dictionary words")
    optparser.add_option("--discourage-picking", default='',
                         help="comma-seperated list of words that will be "
                              "not be picked easily from sentences")
    (options, args) = optparser.parse_args(argv[1:])

    filenames = args

    load_dictionary(options.exclude_dictionary.split(','))
    discourage_picking = set(
        [w.upper() for w in options.discourage_picking.split(',')]
    )

    words = []

    for filename in filenames:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip().replace('--', '-- ')
                words.extend(line.split())
                if line == '' and words[-1] is not PARAGRAPH_BREAK:
                    words.append(PARAGRAPH_BREAK)

    sentences = []
    sentence = []
    for word in words:
        if word is PARAGRAPH_BREAK:
            if sentence:
                sentences.append(sentence)
                sentence = []
            sentences.append(PARAGRAPH_BREAK)
            continue
        if word.startswith(('"', "'")):
            word = word[1:]
        if word.endswith(('"', "'")):
            word = word[:-1]
        sentence.append(word)
        if (word not in ('Mr.', 'Mrs.', 'Dr.') and
            word.endswith(('.', '!', '?', ';', ':', ',', '--'))):
            sentences.append(sentence)
            sentence = []

    sentences.append(sentence)

    def valid_word(w):
        if len(clean(w)) > 2 and w[0].isalpha():
            return True
        return False

    for sentence in sentences:
        if sentence is PARAGRAPH_BREAK:
            sys.stdout.write('\n\n')
            continue
        scores = {}  # frozenset of two (word, pos) tuples -> score
        for (pos1, word1) in enumerate(sentence):
            for (pos2, word2) in enumerate(sentence):
                if word1 == word2:
                    continue
                if (not valid_word(word1)) or (not valid_word(word2)):
                    continue
                # FIXME: this is a little too discouraging
                if word1.upper() in discourage_picking:
                    continue
                if word2.upper() in discourage_picking:
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

                scores[pair] = calculate_schooner_spore(
                    cons1, new1, pos1, cons2, new2, pos2
                )

        if options.debug:
            s = []
            for pair, score in scores.iteritems():
                s.append((score, pair))
            print ' '.join(sentence)
            for (score, pair) in sorted(s, reverse=True):
                print score, pair
            print

        best_score = AWFUL_SCORE
        best_pair = None
        for pair, score in scores.iteritems():
            if score > best_score:
                best_score = score
                best_pair = pair

        if best_pair is None:
            #sys.stdout.write('*' + ' '.join(sentence) + '* ')
            sys.stdout.write(' '.join(sentence) + ' ')
        else:
            best_pair = list(best_pair)
            (word1, new1, pos1) = best_pair[0]
            (word2, new2, pos2) = best_pair[1]
            new1 = adjust_case(new1, word1)
            new2 = adjust_case(new2, word2)
            sentence[pos2] = new2
            sentence[pos1] = new1
            sys.stdout.write(' '.join(sentence) + ' ')


if __name__ == '__main__':
    import sys
    main(sys.argv)
