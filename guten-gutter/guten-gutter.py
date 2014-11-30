#!/usr/bin/env python

"""Usage: guten-gutter.py [--output-dir DIR] FILES

Cleans the Project Gutenberg boilerplate off of the given input files.
"""

from optparse import OptionParser
import os
import re
import sys


class SentinelCleaner(object):
    """Given a file-like object, gives you the lines between the start
    sentinel (exclusive) and the end sentinel (exclusive.)"""

    def __init__(self, fh, start_re=None, end_re=None):
        self.fh = fh
        if start_re is None:
            start_re = self.START_RE
        self.start_re = start_re
        if end_re is None:
            end_re = self.END_RE
        self.end_re = end_re
        self.state = 'pre'

    def lines(self):
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


class ProducedByCleaner(SentinelCleaner):
    START_RE = (r'^((THIS\s+)?E\-?(TEXT|BOOKS?)\s+(WAS\s+)?)?'
                '(PRODUCED|PREPARED|TRANSCRIBED|UPDATED).*?$')
    END_RE = r'^\**\s*END\s+OF\s+(THE\s+)?PROJECT\s+GUTENBERG.*?$'


def main(argv):
    optparser = OptionParser(__doc__.strip())
    optparser.add_option("--output-dir", default=None, metavar='DIR',
                         help="if given, save result to this directory "
                              "instead of dumping it to standard output")
    (options, args) = optparser.parse_args(argv[1:])

    for filename in args:
        out = sys.stdout
        if options.output_dir is not None:
            out_filename = os.path.join(
                options.output_dir, os.path.basename(filename)
            )
            out = open(out_filename, 'w')
        with open(filename, 'r') as f:
            for line in ProducedByCleaner(f).lines():
                out.write(line + '\n')
        if out is not sys.stdout:
            out.close()


if __name__ == '__main__':
    main(sys.argv)
