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
    variables = []
    n = ''
    while text:
        if text[0] != '$':
            n += text[0]
            text = text[1:]
        else:
            text = text[1:]
            while text and text[0].isdigit():
                text = text[1:]
            v = get_fresh_var()
            n += v
            variables.append(v)
    return n, variables


def get_variables(text):
    v = 1
    variables = []
    while True:
        variable = '${0}'.format(v)
        if variable in text:
            variables.append(variable)
            v += 1
        else:
            break
    return text, variables


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

    acquire_variables = rename_variables
    if options.no_variable_renaming:
        acquire_variables = get_variables

    if DEBUG:
        print text
        print 

    for i in xrange(0, int(options.generations)):
        (text, variables) = acquire_variables(text)

        if DEBUG:
            print text, variables
            print 

        for variable in variables:
            replacement = random.choice(TEMPLATES)
            text = text.replace(variable, replacement)

        if DEBUG:
            print text
            print 
            print 

    #print text + '!'

    (text, variables) = acquire_variables(text)
    for variable in variables:
        replacement = random.choice(NOUNS)
        text = text.replace(variable, replacement)

    print text + '!'

if __name__ == '__main__':
    main(sys.argv)
