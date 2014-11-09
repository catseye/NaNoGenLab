#!/usr/bin/env python
# encoding: UTF-8

import codecs
import re
import string
import sys
import random


ASCII_LETTERS = set(string.uppercase)

KEYPAD = {
    '1': 'I',
    '2': 'ABC',
    '3': 'DEF',
    '4': 'GH',   # ignore I <-> 4
    '5': 'JKL',
    '6': 'MN',   # ignore O <-> 6
    '7': 'PQRS',
    '8': 'TUV',
    '9': 'WXYZ',
    '0': 'O',
}

INV = {}
for key, value in KEYPAD.iteritems():
    for char in value:
        INV[char] = key


def phone_number(word):
    return ''.join(INV[char] for char in word)
        

def main(argv):
    filename = argv[1]

    phones = {}

    with codecs.open('/usr/share/dict/words', 'r', encoding='UTF-8') as f:
        for line in f:
            if "'" in line:
                continue
            word = line.strip().upper()
            #if len(word) == 1:
            #    continue
            letters = set(word)
            if not letters <= ASCII_LETTERS:
                #print word
                continue
            phones.setdefault(phone_number(word), []).append(word)

    longkeys = phones.keys()
    longkeys.sort(lambda a, b: cmp(len(b), len(a)))

    # print longkeys[0]

    number = 0
    with open(filename, 'r') as f:
        while True:
            number *= 256
            r = f.read(1)
            if len(r) == 0:
                break
            number += ord(r)
    number = str(number)

    # print number

    for key in longkeys:
        words = phones[key]
        while key in number:
            number = number.replace(key, ' ' + random.choice(words) + ' ')

    print number

if __name__ == '__main__':
    main(sys.argv)
