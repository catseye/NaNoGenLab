#!/usr/bin/env python

from math import factorial
import sys


def main(argv):
    TARGET = 50000

    if False:
        # try P(n,n) (it's just factorial)
        best = 10000000000
        best_src = None
        for x in xrange(0, 10):
            attempt = factorial(x)
            if attempt >= TARGET and attempt < best:
                best = attempt
                best_src = x

        print "best: factorial(%s) = %s" % (best_src, best)

    # try P(n, r)
    best = 10000000000
    best_src = None
    TOP = 1000
    for x in xrange(0, TOP):
        if (x % 100) == 0:
            print "%s / %s..." % (x, TOP)
        for y in xrange(0, x):
            attempt = factorial(x) / factorial(y)
            if attempt >= TARGET and attempt < best:
                best = attempt
                best_src = (x, y)
            if attempt == TARGET:
                print "BINGO!"
                break

    print "best: P%s = %s" % (best_src, best)


if __name__ == '__main__':
    import sys
    main(sys.argv)
