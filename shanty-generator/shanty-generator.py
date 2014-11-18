#!/usr/bin/env python

import random
import re
import sys


DEBUG = False


TEMPLATES = [
    """\
^$1, $2,
^$1-$1 $2,
^$1-$1 $2-$2 $1-$1 $3,
^$3 $3 $4.

""",
    """\
^$1, $2-$2,
^$1, $2-$2,
^$3-$3 $4!
^$3-$3 $4!
""",
    """\
^$1!  (^$1!)
^$2!  (^$2!)
^$1 $2 $3-$3 $4,
^$5, $5, $5.
""",
]


def get_variables(text):
    variables = set()
    while text:
        if text[0] != '$':
            text = text[1:]
        else:
            text = text[1:]
            v = ''
            while text and text[0].isdigit():
                v += text[0]
                text = text[1:]
            variables.add(int(v))
    return list(variables)


def fillout(template, variables, words):
    for var in variables:
        template = template.replace('^$%s' % var, words[var-1].capitalize())
        template = template.replace('$%s' % var, words[var-1])
    return template


def clean(word):
    if word.endswith(('.', '!', '?', ';', ',')):
        word = word[:-1]
    if word.startswith(('"', "'", '(')):
        word = word[1:]
    if word.endswith(('"', "'", ')')):
        word = word[:-1]
    if word.endswith(('.', '!', '?', ';', ',')):
        word = word[:-1]
    return word.lower()


def main(argv):
    filenames = argv[1:]

    words = []
    for filename in filenames:
        with open(filename, 'r') as f:
            for line in f:
                bits = line.split()
                for bit in bits:
                    words.extend([clean(w) for w in bit.split('--')])

    while words:
        template = random.choice(TEMPLATES)
        variables = get_variables(template)
        use_words = words[:len(variables)]
        if len(use_words) == len(variables):
            words = words[len(variables):]
        else:
            while len(use_words) < len(variables):
                use_words.append(random.choice(['yo', 'ho', 'hey']))
            words = []
        print fillout(template, variables, use_words)


if __name__ == '__main__':
    main(sys.argv)
