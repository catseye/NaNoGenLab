#!/usr/bin/env python

import sys
with open(sys.argv[1], 'r') as f:
    while True:
        x = f.read(1)
        if len(x) == 0:
            break
        if ord(x) not in (0, 13):
            sys.stdout.write(x)
