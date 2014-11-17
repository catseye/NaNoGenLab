#!/usr/bin/env python

from optparse import OptionParser
import random
import re
import sys


DEBUG = False


TEMPLATES = [
    "$1 is the $2 of $3",
    "$1 and $2",
    "$1 can't understand $2",
    "$1 is no $2",
    "$1, being $1, is $2",
]


NOUNS = [
    'dog', 'cat', 'horse', 'biscuit', 'sausage', 'tree', 'book', 'bell',
    'candle', 'dragon', 'meerkat', 'wonder', 'irritation', 'elegy',
    'protector', 'microphone', 'sheep', 'wolf', 'fox', 'territory'
]


counter = 30
def get_fresh_var():
    global counter
    v = '${0}'.format(counter)
    counter += 1
    return v


def rename_variables(text):
    replacements = {}
    new = ''
    while text:
        if text[0] != '$':
            new += text[0]
            text = text[1:]
        else:
            text = text[1:]
            v = '$'
            while text and text[0].isdigit():
                v += text[0]
                text = text[1:]
            new += replacements.setdefault(v, get_fresh_var())
    return new


def get_variables(text):
    variables = set()
    while text:
        if text[0] != '$':
            text = text[1:]
        else:
            text = text[1:]
            v = '$'
            while text and text[0].isdigit():
                v += text[0]
                text = text[1:]
            variables.add(v)
    return list(variables)


def main(argv):
    global DEBUG
    optparser = OptionParser(__doc__)
    optparser.add_option("--generations", default=4,
                         help="number of iterations to apply")
    optparser.add_option("--parenthesize", action='store_true', default=False,
                         help="parenthesize templates")
    optparser.add_option("--no-variable-renaming", action='store_true', default=False,
                         help="don't rename variables on each step")
    optparser.add_option("--debug", action='store_true', default=False,
                         help="output debuging info")
    (options, args) = optparser.parse_args(argv[1:])

    DEBUG = options.debug
    if options.parenthesize:
        for i in xrange(0, len(TEMPLATES)):
            TEMPLATES[i] = '(' + TEMPLATES[i] + ')'

    text = random.choice(TEMPLATES)

    if DEBUG:
        print text
        print 

    for i in xrange(0, int(options.generations)):
        variables = get_variables(text)

        if DEBUG:
            print text, variables
            print 

        for variable in variables:
            replacement = random.choice(TEMPLATES)
            if not options.no_variable_renaming:
                replacement = rename_variables(replacement)

            text = text.replace(variable, replacement)

        if DEBUG:
            print text
            print 
            print 

    #print text + '!'

    for variable in get_variables(text):
        replacement = random.choice(NOUNS)
        text = text.replace(variable, replacement)

    print text + '!'

if __name__ == '__main__':
    main(sys.argv)
