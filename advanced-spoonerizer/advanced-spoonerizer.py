#!/usr/bin/env python
# encoding: UTF-8

from optparse import OptionParser
import random
import string

try:
    from tqdm import tqdm
except ImportError:
    def tqdm(x):
        return x


VOWELS = 'aeiouyAEIOUY'


def sentencify(sentence):
    a = unicode(' '.join(sentence) + ' ')
    return a.replace(u'-- ', u'—').encode('UTF-8')


def strip_initial_consonants(word):
    pre = ''
    init = ''
    while word and word[0] in ('"' + "'"):
        pre += word[0]
        word = word[1:]
    if word and word[0] in 'yY':
        init += word[0]
        word = word[1:]
    while word and word[0].isalpha() and word[0] not in VOWELS:
        init += word[0]
        word = word[1:]
    if word and init and init[-1] in 'qQ' and word[0] in 'uU':
        init += word[0]
        word = word[1:]        
    return (pre, init, word)


DICTIONARY = {}
ASCII_LETTERS = set(string.uppercase)


def supercapitalize(word):
    pre = ''
    while word and not word[0].isalpha():
        pre += word[0]
        word = word[1:]
    return pre + word.capitalize()


def clean(word):
    if word.endswith('--'):
        word = word[:-2]
    if word.endswith(('.', '!', '?', ';', ':', ',')):
        word = word[:-1]
    if word.startswith(('"', "'", '(')):
        word = word[1:]
    if word.endswith(('"', "'", ')')):
        word = word[:-1]
    if word.endswith(('.', '!', '?', ';', ':', ',')):
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


AWFUL_SCORE = (-1000, -1000, -1000)


def calculate_schooner_spore(cons1, word1, new1, pos1,
                             cons2, word2, new2, pos2,
                             dictionary_words_only=False):
    """The SchoonerSpore[tm] is a tuple of
    (dictionary_score, promiximity_score, sentence_score)"""

    dict_score = dictionary_score(new1) + dictionary_score(new2)
    if dictionary_words_only and dict_score != 2:
        return AWFUL_SCORE

    promiximity_score = 0 - (pos1 - pos2) ** 2

    sentence_score = (
        len(cons1) * len(cons1) +
        len(cons2) * len(cons2) +
        len(new1) + len(new2) + len(set(new1) | set(new2))
    )

    return (dict_score, promiximity_score, sentence_score)


def adjust_case(new, orig):
    while orig and orig[0] in ('"' + "'"):
        orig = orig[1:]
    if all([x.isupper() for x in orig if x.isalpha()]):
        return new.upper()
    if orig[0].isupper():
        return supercapitalize(new)
    return new.lower()


PARAGRAPH_BREAK = object()


def main(argv):
    optparser = OptionParser(__doc__)
    optparser.add_option("--debug", default=False, action='store_true',
                         help="show me the SchoonerSpores[tm]")
    optparser.add_option("--exclude-dictionary", default='',
                         help="comma-separated list of words that will not be "
                              "considered to be dictionary words")
    optparser.add_option("--disable-picking", default='',
                         help="comma-separated list of words that will be "
                              "not be picked from sentences")
    optparser.add_option("--disable-swapping", default='',
                         help="comma-separated list of colon-separated "
                              "pairs of words that will be "
                              "not be considered for swapping")
    optparser.add_option("--dictionary-words-only", default=False,
                         action='store_true',
                         help="only swap words when both words are "
                              "dictionary words")
    optparser.add_option("--remove-quotes", default=False, action='store_true',
                         help="strip double quotes from input words")
    (options, args) = optparser.parse_args(argv[1:])

    filenames = args

    load_dictionary(options.exclude_dictionary.split(','))
    disable_picking = set([
        w.upper() for w in options.disable_picking.split(',')
    ])
    disable_swapping = set([
        frozenset([z.upper for z in x.split(':')])
          for x in options.disable_swapping.split(',')
    ])

    words = []

    for filename in filenames:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip().replace('--', '-- ')
                words.extend(line.split())
                if line == '' and words[-1] is not PARAGRAPH_BREAK:
                    words.append(PARAGRAPH_BREAK)

    BASE_CLAUSE_ENDERS = ['.', '!', '?', ';', ':', ',', '--']
    CLAUSE_ENDERS = tuple(
        BASE_CLAUSE_ENDERS +
        [c + '"' for c in BASE_CLAUSE_ENDERS] +
        [c + "'" for c in BASE_CLAUSE_ENDERS]
    )
    
    sentences = []  # actually clauses. :/
    sentence = []
    for word in words:
        if word is PARAGRAPH_BREAK:
            if sentence:
                sentences.append(sentence)
                sentence = []
            sentences.append(PARAGRAPH_BREAK)
            continue
        if options.remove_quotes:
            if word.startswith(('"', "'")):
                word = word[1:]
            if word.endswith(('"', "'")):
                word = word[:-1]
        sentence.append(word)
        if (word not in ('Mr.', 'Mrs.', 'Dr.') and
            word.endswith(CLAUSE_ENDERS)):
            sentences.append(sentence)
            sentence = []

    sentences.append(sentence)

    for sentence in sentences:
        if sentence is PARAGRAPH_BREAK:
            sys.stdout.write('\n\n')
            continue
        scores = {}  # frozenset of two (word, pos) tuples -> score
        for (pos1, word1) in enumerate(sentence):
            for (pos2, word2) in enumerate(sentence):
                clean_word1 = clean(word1)
                clean_word2 = clean(word2)
                if clean_word1 == clean_word2:
                    continue
                if len(clean_word1) <= 2 or len(clean_word2) <= 2:
                    continue
                if clean_word1 in disable_picking or clean_word2 in disable_picking:
                    continue

                if frozenset([clean_word1, clean_word2]) in disable_swapping:
                    continue

                (pre1, cons1, base1) = strip_initial_consonants(word1)
                (pre2, cons2, base2) = strip_initial_consonants(word2)
                if len(cons1) == 0 and len(cons2) == 0:
                    continue
                if cons1.upper() == cons2.upper():
                    continue

                new1 = pre1 + cons2 + base1
                new2 = pre2 + cons1 + base2

                pair = frozenset([(word1, new1, pos1), (word2, new2, pos2)])

                scores[pair] = calculate_schooner_spore(
                    cons1, word1, new1, pos1,
                    cons2, word2, new2, pos2,
                    dictionary_words_only=options.dictionary_words_only
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

        if best_pair is None or best_score == AWFUL_SCORE:
            sys.stdout.write(sentencify(sentence))
        else:
            best_pair = list(best_pair)
            (word1, new1, pos1) = best_pair[0]
            (word2, new2, pos2) = best_pair[1]
            new1 = adjust_case(new1, word1)
            new2 = adjust_case(new2, word2)
            sentence[pos2] = new2
            sentence[pos1] = new1
            sys.stdout.write(sentencify(sentence))


if __name__ == '__main__':
    import sys
    main(sys.argv)
