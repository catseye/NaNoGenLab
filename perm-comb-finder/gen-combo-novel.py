#!/usr/bin/env python

from itertools import combinations
import sys
import re


try:
    from tqdm import tqdm
except ImportError:
    def tqdm(x):
        return x


# 46010 + 3990 == 50000
# 46010: [('r*C', 215, 214)]
# 3990: [('r*C', 21, 3), ('r*C', 21, 19), ('r*C_duplicates', 19, 3)]

# note that:
#   len(combinations(21, 3)) == 1330
#   len(combinations(21, 19)) == 210
#   len(combinations(215, 2)) == 23005
#   len(combinations(215, 214)) == 215
# and that 
# 23005 / 1330.0 = 17.296992481203006


def clean(w):
    return re.match(r"^.*?([_a-zA-Z0-9\']+).*?$", w).group(1)


def proc_paragraphs(ps):
    acc = ', '.join(ps)
    acc = acc.capitalize()
    while acc[-1] in (('.', ',', ' ', '?', '!')):
        acc = acc[:-1]
    # keep proper nouns proper -- it's only proper
    for proper in ('multivac', 'messerschmitts', 'wellington', 'soho',
                   'ozymandias', "i'll", "crimea", 'thinkpad'):
        acc = acc.replace(proper, proper.capitalize())
    if acc.startswith('_'):
        acc = '_' + acc[1:].capitalize()
    return acc


def main(argv):
    # 1. LOAD
    part1 = []
    with open(argv[1], 'r') as f:
        for line in f:
            part1.append(line.strip().capitalize())
    assert len(part1) == 21

    part2 = []
    with open(argv[2], 'r') as f:
        for line in f:
            part2.extend([clean(w) for w in line.strip().split()])

    assert len(part2) == 215, len(part2)

    # 2. MUNGE
    headings = []
    for c in combinations(part1, 3):
        headings.append(' '.join(c))

    paragraphs = []
    for c in combinations(part2, 2):
        paragraphs.append(' '.join(c))

    # 3. GO
    c = 0
    while headings and paragraphs:
        h = headings.pop(0)
        sys.stdout.write(h + '\n')
        sys.stdout.write(('-' * len(h)) + '\n\n')
        
        d = 17
        if c % 4 == 0:
            d = 18
        ps = []
        for n in xrange(0, d):
            if not paragraphs:
                continue
            ps.append(paragraphs.pop(0))
        sys.stdout.write(proc_paragraphs(ps) + '.\n\n')

        c += 1

    assert not headings

    ps = []    
    while paragraphs:
        ps.append(paragraphs.pop(0))
    sys.stdout.write(proc_paragraphs(ps) + '.\n\n')


if __name__ == '__main__':
    import sys
    main(sys.argv)
