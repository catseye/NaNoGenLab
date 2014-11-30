#!/usr/bin/env python

"""Usage: guten-gutter.py [--output-dir DIR] FILES

Cleans the Project Gutenberg boilerplate off of the given input files.
"""

from optparse import OptionParser
import os
import re
import sys


class SentinelCleaner(object):
    """Given an iterator over lines, gives you the lines between the start
    sentinel (exclusive) and the end sentinel (exclusive.)
    
    The start sentinel is actually "super-exclusive" in that neither it,
    nor any non-blank lines immediately following it, are included in
    the output.

    Note that a file-like object is an iterator over lines.  Note that
    lines produced by this cleaner are stripped of trailing whitespace.
    """

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
            line = line.rstrip()
            if self.state == 'pre':
                match = re.match(self.start_re, line.upper())
                if match:
                    self.state = 'consuming-start'
            elif self.state == 'consuming-start':
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


class GutenbergCleaner(SentinelCleaner):
    START_RE = r'^\**\s*START\s+OF\s+(TH(IS|E)\s+)?PROJECT\s+GUTENBERG.*?$'
    END_RE = r'^\**\s*END\s+OF\s+(TH(IS|E)\s+)?PROJECT\s+GUTENBERG.*?$'


class ProducedByCleaner(SentinelCleaner):
    START_RE = (r'^((THIS\s+)?E\-?(TEXT|BOOKS?)\s+(WAS\s+)?)?'
                '(PRODUCED|PREPARED|TRANSCRIBED|UPDATED).*?$')
    END_RE = r'^\**\s*END\s+OF\s+(TH(IS|E)\s+)?PROJECT\s+GUTENBERG.*?$'


class MultiCleaner(object):
    """An object which attempts to apply multiple cleaners to an input.
    If any cleaner fails, it returns the input just previous to that
    failure.

    Not fully implemented.  I'm still sketching this...
    """
    def __init__(self, strategy=None):
        if strategy is None:
            strategy = (GutenbergCleaner, ProducedByCleaner)
        self.strategy = strategy

    def clean(self, fh):
        lines = []
        for line in fh:
            lines.append(line.rstrip())

        for cleaner_class in self.strategy:
            cleaner = cleaner_class(lines)
            new_lines = list(cleaner.lines())
            if not new_lines:
                break
            lines = new_lines

        for line in lines:
            yield line


def main(argv):
    optparser = OptionParser(__doc__.strip())
    optparser.add_option("--output-dir", default=None, metavar='DIR',
                         help="if given, save the resulting files to this "
                              "directory (under their original names)"
                              "instead of dumping them to standard output")
    (options, args) = optparser.parse_args(argv[1:])

    for filename in args:
        out = sys.stdout
        if options.output_dir is not None:
            out_filename = os.path.join(
                options.output_dir, os.path.basename(filename)
            )
            out = open(out_filename, 'w')
        cls = ProducedByCleaner
        #cls = GutenbergCleaner
        with open(filename, 'r') as f:
            for line in cls(f).lines():
                out.write(line + '\n')
        if out is not sys.stdout:
            out.close()


if __name__ == '__main__':
    main(sys.argv)
