#!/usr/bin/env python

from itertools import combinations
import sys


try:
    from tqdm import tqdm
except ImportError:
    def tqdm(x):
        return x


# This would be a great idea, if only it wasn't COMPLETELY WRONG.


PART1 = ['word%s' % (x+1) for x in xrange(0, 41)]
PART2 = ['word%s' % (x+1) for x in xrange(0, 281)]

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

    'quail',
    'question',
    'quicken',
    'quibble',
    'quiz',
    'quandry',
    'quadrangle',

    'merry',
    'malicious',
    'mincemeat',
    'marmelade',
    'milky',
    'marmoset',
    'millimeter',
    
    'careless',
    'creamy',
    'celestial',
    'cerulean',
    'cirrus',
    'coccyx',
]


def main(argv):
    assert len(PART1) == 41
    assert len(PART2) == 281
    with open(argv[1], 'w') as f:
        for (part, r) in ((PART1, 38), (PART2, 279)):
            for c in tqdm(combinations(part, r)):
                f.write(' '.join(c).capitalize() + '.\n\n')


if __name__ == '__main__':
    import sys
    main(sys.argv)
