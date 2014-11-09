#!/usr/bin/env python

import sys
import re
words = []
for line in sys.stdin:
    words.extend(line.strip().split())
def clean(w):
    w = w.replace("'", "")
    return re.match('^.*?([a-zA-Z0-9]+).*?$', w).group(1).upper()
words = [clean(w) for w in words]
print len(words), len(set(words))
assert len(words) == len(set(words))
print sorted(words)
