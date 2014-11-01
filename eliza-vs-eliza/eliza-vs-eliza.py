#!/usr/bin/env python


import eliza


def main(argv):
    therapist = eliza.eliza()
    state = "Hello.  How are you feeling today?"
    for i in xrange(0, 1000):
        print '"%s"\n' % state
        state = therapist.respond(state)


if __name__ == '__main__':
    import sys
    main(sys.argv)
