#!/usr/bin/env python

from itertools import combinations
import sys


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


def main(argv):
    # 1. LOAD
    part1 = []
    with open(argv[1], 'r') as f:
        for line in f:
            part1.append(line.strip().upper())
    assert len(part1) == 21

    part2 = ['word%s' % (x+1) for x in xrange(0, 215)]
    assert len(part2) == 215

    # 2. MUNGE
    headings = []
    for c in combinations(part1, 3):
        headings.append(' '.join(c))

    paragraphs = []
    for c in combinations(part2, 2):
        paragraphs.append(' '.join(c).capitalize())

    # 3. GO
    while headings and paragraphs:
        h = headings.pop(0)
        sys.stdout.write(h + '\n')
        sys.stdout.write(('-' * len(h)) + '\n\n')
        
        for n in xrange(0, 17):
            if not paragraphs:
                continue
            p = paragraphs.pop(0)
            sys.stdout.write(p + '.  ')
        sys.stdout.write('\n\n')

    assert not headings
    
    while paragraphs:
        p = paragraphs.pop(0)
        sys.stdout.write(p + '.  ')
    sys.stdout.write('\n\n')


if __name__ == '__main__':
    import sys
    main(sys.argv)
