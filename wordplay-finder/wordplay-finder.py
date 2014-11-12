#!/usr/bin/env python

import random
import re
import sys


DEBUG = False


def main(argv):
    filenames = argv[1:]

    entries = {}

    for filename in filenames:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                match = re.match(r'^(.*?):\s*(.+?)$', line)
                if match:
                    word = match.group(1)
                    defn = match.group(2)
                    assert word not in entries, "%s isalready %s" % (word, entries[word])
                    entries[word] = defn

    for key1, value1 in entries.iteritems():
        #print key1, value1
        for key2, value2 in entries.iteritems():
            if key1 == key2:
                continue
            key3 = key1 + key2
            if key3 in entries:
                value3 = entries[key3]
                print """
> "... {0} ..."

Here we see the playwright has used the word _{0}_
("{3}"),
but if we consider that {6} _{1}-{2}_
("{4}", and "{5}"),
{7}.

""".format(key3, key1, key2, value3, value1, value2, random.choice([
    'the character may in fact be saying',
    'the line may be intended to be heard as',
    'perhaps we are meant to take this as',
]), random.choice([
    'this scene takes on another meaning indeed',
    'the subtext of this exchange is revealed',
    'another level of meaning is apparent',
    'our gloss is quite different, is it not',
    'the reading becomes much more complex and layered',
    'the real humour of this scene may be appreciated',
]))


if __name__ == '__main__':
    main(sys.argv)
