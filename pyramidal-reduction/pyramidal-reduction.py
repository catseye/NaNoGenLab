#!/usr/bin/env python

import random
import sys


DEBUG = False


def reduce_symbols(rules, alphabet, lhs, rhs):
    if lhs == ' ' and rhs == ' ':
        res = random.choice(alphabet)
    elif rhs == ' ':
        res = ' '
    else:
        res = random.choice(alphabet)
    return rules.setdefault(lhs + rhs, res)


def display(sentence, iteration):
    sys.stdout.write(' ' * iteration)
    for symbol in sentence:
        sys.stdout.write(symbol + ' ')
    sys.stdout.write('\n')


def main(argv):
    sentence = argv[1]
    alphabet = list(set(sentence))
    rules = {}
    iteration = 0
    original_length = len(sentence)

    display(sentence, iteration)
    while len(sentence) > 1:
        new_sentence = ''
        for pos in xrange(0, len(sentence) - 1):
            new_sentence += reduce_symbols(
                rules, alphabet, sentence[pos], sentence[pos + 1]
            )
        assert len(new_sentence) == len(sentence) - 1
        sentence = new_sentence
        iteration += 1
        display(sentence, iteration)

    if DEBUG:
        for pair in rules:
            print "'%s' -> '%s'" % (pair, rules[pair])

    # create inverse mapping
    selur = {}
    for pair in rules:
        selur.setdefault(rules[pair], []).append(pair)

    # now generate!
    while len(sentence) < original_length:
        new_sentence = ''
        for pos in xrange(0, len(sentence)):
            if not new_sentence:
                new_sentence += random.choice(selur[sentence[pos]])
            else:
                # we need to pick one which matches what new_sentence
                # already has on its right end
                choices = selur[sentence[pos]]
                valid_choices = [
                    c[1] for c in choices if c[0] == new_sentence[-1]
                ]
                # assert valid_choices, \
                #   "choices(%r) = %r, new_sentence = %r, valid_choices = %r" % (
                #       sentence[pos], choices, new_sentence, valid_choices
                #   )
                if valid_choices:
                    new_sentence += random.choice(valid_choices)
                else:
                    # burp.  no inverted rule can be used to extend the
                    # new sentence, so make up a new inverted rule and save it
                    new_pair = new_sentence[-1] + random.choice(alphabet)
                    selur[sentence[pos]].append(new_pair)
                    new_sentence += new_pair[1]
        assert len(new_sentence) == len(sentence) + 1,\
           "%s != %s" % (len(new_sentence), len(sentence))
        sentence = new_sentence
        iteration -= 1
        display(sentence, iteration)


if __name__ == '__main__':
    import sys
    main(sys.argv)
