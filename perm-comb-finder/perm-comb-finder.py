#!/usr/bin/env python

from math import factorial, pow
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
    return pow(n, r)


# order doesn't matter. repetition not allowed.
def C(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


# order doesn't matter. repetition is allowed.
def C_duplicates(n, r):
    return factorial(n + r - 1) / (factorial(r) * factorial(n - 1))


TARGET = 50000

def find(fun, top):
    best = 10000000000
    best_src = (None, None)
    for n in tqdm(xrange(1, top)):
        if best == TARGET:
            print "BINGO!"
            break
        for r in tqdm(xrange(1, n+1)):
            attempt = fun(n, r)
            if attempt >= TARGET and attempt < best:
                best = attempt
                best_src = (n, r)
            if best == TARGET:
                print "BINGO!"
                break
    return (best, best_src[0], best_src[1])


def main(argv):
    (best, n, r) = find(P, 300)
    print "best: P(%s,%s) = %s" % (n, r, best)

    (best, n, r) = find(lambda n, r: P(n, n), 100)
    print "best: P(%s,%s) = %s" % (n, n, best)

    (best, n, r) = find(P_duplicates, 100)
    print "best: P_duplicates(%s,%s) = %s" % (n, r, best)

    (best, n, r) = find(C, 500)
    print "best: C(%s,%s) = %s" % (n, r, best)

    (best, n, r) = find(C_duplicates, 500)
    print "best: C_duplicates(%s,%s) = %s" % (n, r, best)


if __name__ == '__main__':
    import sys
    main(sys.argv)
