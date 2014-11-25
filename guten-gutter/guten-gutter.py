#!/usr/bin/env python

from optparse import OptionParser
import os
import random
import re
import string
import sys


class SentinelCleaner(object):
    """Given a file-like object, gives you the lines between the start
    sentinel (exclusive) and the end sentinel (exclusive.)"""

    def __init__(self, fh,
                 start_re='^((THIS\s+)?E\-?(TEXT|BOOKS?)\s+(WAS\s+)?)?(PRODUCED|PREPARED|TRANSCRIBED|UPDATED).*?$',
                 end_re=r'^\**\s*END\s+OF\s+(THE\s+)?PROJECT\s+GUTENBERG.*?$',
                 pre=None):
        self.fh = fh
        self.start_re = start_re
        self.end_re = end_re
        self.pre = pre
        self.state = 'pre'

    def lines(self):
        if self.pre:
            yield self.pre
            yield ''
        for line in self.fh:
            line = line.strip()
            if self.state == 'pre':
                match = re.match(self.start_re, line.upper())
                if match:
                    self.state = 'consuming-produced-by'
            elif self.state == 'consuming-produced-by':
                if not line:
                    self.state = 'mid'
            elif self.state == 'mid':
                match = re.match(self.end_re, line.upper())
                if match:
                    self.state = 'post'
                else:
                    yield line
            else:
                assert self.state == 'post'
                pass


def main(argv):
    optparser = OptionParser(__doc__)
    optparser.add_option("--pre", default=None,
                         help="text to add to beginning of input document")
    optparser.add_option("--output-dir", default=None,
                         help="if given, save result to this dir instead of "
                              "dumping it to standard output")
    (options, args) = optparser.parse_args(argv[1:])

    for filename in args:
        out = sys.stdout
        if options.output_dir is not None:
            out_filename = os.path.join(
                options.output_dir, os.path.basename(filename)
            )
            out = open(out_filename, 'w')
        with open(filename, 'r') as f:
            for line in SentinelCleaner(f, pre=options.pre).lines():
                out.write(line + '\n')
        if out is not sys.stdout:
            out.close()


if __name__ == '__main__':
    main(sys.argv)
