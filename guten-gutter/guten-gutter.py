#!/usr/bin/env python

"""Usage: guten-gutter.py [--output-dir DIR] FILES

Cleans the Project Gutenberg boilerplate off of the given input files.
"""

from optparse import OptionParser
import os
import re
import sys


class AbstractBaseCleaner(object):
    """Defines the protocol for "cleaner" objects."""

    def clean(self, lines, name=''):
        """Given an iterable of lines, yield cleaned lines.  ``name'' is
        the (optional) name of the entity being cleaned, for error-reporting
        purposes.

        Note that a file-like object is an iterable of lines.
        """
        raise NotImplementedError

    def has_failed(self, original_lines, result_lines, name=''):
        """Given two iterables of lines, representing the input and the
        result of running this cleaner on that input, return a boolean
        indicating whether we think this cleaner has failed or not.
        """
        return False

    def __str__(self):
        return self.__class__.__name__


class TrailingWhitespaceCleaner(AbstractBaseCleaner):

    def clean(self, lines, name=''):
        for line in lines:
            yield line.rstrip()


class SentinelCleaner(AbstractBaseCleaner):
    """Cleans the input lines, returning only the lines between the start
    sentinel (exclusive) and the end sentinel (exclusive.)
    
    The start sentinel is actually "super-exclusive" in that neither it,
    nor any non-blank lines immediately following it, are included in
    the output.

    Note that cleaned lines are stripped of trailing whitespace.
    """

    def __init__(self, start_re=None, end_re=None):
        if start_re is None:
            start_re = self.START_RE
        self.start_re = start_re
        if end_re is None:
            end_re = self.END_RE
        self.end_re = end_re
        self.state = 'pre'

    def clean(self, lines, name=''):
        for line in lines:
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

    def has_failed(self, original_lines, result_lines, name=''):
        original_lines = list(original_lines)
        result_lines = list(result_lines)
        shrinkage = len(original_lines) - len(result_lines)
        # usually under 400, but sometimes as high as 418...
        return len(result_lines) == 0 or shrinkage > 450


class ProducedByCleaner(SentinelCleaner):
    START_RE = (r'^((THIS\s+)?E\-?(TEXT|BOOKS?)\s+(WAS\s+)?)?'
                '(PRODUCED|PREPARED|TRANSCRIBED|UPDATED).*?$')
    END_RE = r'^\**\s*END\s+OF\s+(TH(IS|E)\s+)?PROJECT\s+GUTENBERG.*?$'

    def has_failed(self, original_lines, result_lines, name=''):
        original_lines = list(original_lines)
        result_lines = list(result_lines)
        shrinkage = len(original_lines) - len(result_lines)
        # Note: this is not sufficient by itself; assumes GutenbergCleaner
        # got the trailing legal text, which is large.
        return len(result_lines) == 0 or shrinkage > 20


class MultiCleaner(AbstractBaseCleaner):
    """An object which attempts to apply multiple cleaners to an input.
    If any cleaner fails, it returns the input just previous to that
    failure.
    """

    def __init__(self, cleaners=()):
        self.cleaners = cleaners

    def clean(self, lines, name=''):
        lines = list(lines)
        for cleaner in self.cleaners:
            new_lines = list(cleaner.clean(lines, name=name))
            if cleaner.has_failed(lines, new_lines, name=name):
                sys.stderr.write("%s failed to clean '%s'\n" % (cleaner, name))
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
        cleaner = MultiCleaner((
            TrailingWhitespaceCleaner(),
            GutenbergCleaner(),
            ProducedByCleaner()
        ))
        with open(filename, 'r') as f:
            for line in cleaner.clean(f, name=filename):
                out.write(line + '\n')
        if out is not sys.stdout:
            out.close()


if __name__ == '__main__':
    main(sys.argv)
