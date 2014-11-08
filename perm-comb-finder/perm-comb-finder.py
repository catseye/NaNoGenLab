#!/usr/bin/env python

from math import factorial, pow
from optparse import OptionParser
import sys


try:
    from tqdm import tqdm
except ImportError:
    def tqdm(x):
        return x


# order matters. repetition not allowed.
def P(n, r):
    return factorial(n) / factorial(n - r)


# order matters. repetition allowed.
def P_duplicates(n, r):
    try:
        return pow(n, r)
    except OverflowError:
        return float('inf')  # everything in Python is Pythonic, esp. this


# order doesn't matter. repetition not allowed.
def C(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


# order doesn't matter. repetition is allowed.
def C_duplicates(n, r):
    return factorial(n + r - 1) / (factorial(r) * factorial(n - 1))


# C and R are *how many ways*; this is *how many things* in those ways
def times_r(f):
    return lambda n, r: f(n, r) * r


TARGET = 50000
MIN_R = 1
memo = {}
MEMOIZE = False


def find(name, fun, top):
    best = 10000000000
    best_src = (None, None)
    for n in tqdm(xrange(1, top)):
        if best == TARGET:
            print "BINGO!"
            break
        for r in tqdm(xrange(MIN_R, n+1)):
            attempt = fun(n, r)
            if MEMOIZE and attempt < TARGET:
                memo.setdefault(attempt, []).append(
                    (name, n, r)
                )
            if attempt >= TARGET and attempt < best:
                best = attempt
                best_src = (n, r)
            if best == TARGET:
                print "BINGO!"
                break
    return (best, best_src[0], best_src[1])


def main(argv):
    global MIN_R, MEMOIZE

    optparser = OptionParser(__doc__)
    optparser.add_option("--minimum-r", default=1,
                         help="lowest value of _r_ to consider")
    optparser.add_option("--top", default=400,
                         help="highest value of _n_ to consider")
    optparser.add_option("--memoize", default=False, action='store_true',
                         help="memoize low results for later search")
    (options, args) = optparser.parse_args(argv[1:])
    MIN_R = int(options.minimum_r)
    MEMOIZE = options.memoize
    options.top = int(options.top)

    if False:
        (best, n, r) = find('P', P, options.top)
        print "best: P(%s,%s) = %s" % (n, r, best)
        
        (best, n, r) = find('fact', lambda n, r: P(n, n), options.top)
        print "best: P(%s,%s) = %s" % (n, n, best)
        
        (best, n, r) = find('P_duplicates', P_duplicates, options.top)
        print "best: P_duplicates(%s,%s) = %s" % (n, r, best)
        
        (best, n, r) = find('C', C, options.top)
        print "best: C(%s,%s) = %s" % (n, r, best)
        
        (best, n, r) = find('C_duplicates', C_duplicates, options.top)
        print "best: C_duplicates(%s,%s) = %s" % (n, r, best)

    (best, n, r) = find('r*P', times_r(P), options.top)
    print "best: r*P(%s,%s) = %s" % (n, r, best)

    # does not make much sense
    #(best, n, r) = find('fact', times_r(lambda n, r: P(n, n)), options.top)
    #print "best: P(%s,%s) = %s" % (n, n, best)

    (best, n, r) = find('r*P_duplicates', times_r(P_duplicates), options.top)
    print "best: r*P_duplicates(%s,%s) = %s" % (n, r, best)

    (best, n, r) = find('r*C', times_r(C), options.top)
    print "best: r*C(%s,%s) = %s" % (n, r, best)

    (best, n, r) = find('r*C_duplicates', times_r(C_duplicates), options.top)
    print "best: r*C_duplicates(%s,%s) = %s" % (n, r, best)

    if options.memoize:
        print
        for key1, value1 in memo.iteritems():
            for key2, value2 in memo.iteritems():
                if key1 + key2 == TARGET:
                    print "%s + %s == %s" % (key1, key2, TARGET)
                    print "%s: %s" % (key1, value1)
                    print "%s: %s" % (key2, value2)
                    print


if __name__ == '__main__':
    import sys
    main(sys.argv)
