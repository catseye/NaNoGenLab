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


PART1 = ['word%s' % (x+1) for x in xrange(0, 21)]
PART2 = ['word%s' % (x+1) for x in xrange(0, 215)]

PART1 = [
    'pascal',
    'python',
    'pool',
    'purloin',
    'puppy',
    'pathos',
    'pumpkin',

    'seven',
    'serious',
    'sideline',
    'scurry',
    'scrum',
    'solace',
    'semester',
    
    'rhinocerous',
    'rapacious',
    'ridiculous',
    'reset',
    'riddle',
    'ramble',
    'rarity',
]


def main(argv):
    assert len(PART1) == 21
    assert len(PART2) == 215
    with open(argv[1], 'w') as f:
        for (part, r) in ((PART1, 19), (PART2, 214)):
            print len(list(combinations(part, r)))
            for c in tqdm(combinations(part, r)):
                f.write(' '.join(c).capitalize() + '.\n\n')


if __name__ == '__main__':
    import sys
    main(sys.argv)
