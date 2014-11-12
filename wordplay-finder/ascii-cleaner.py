#!/usr/bin/env python

import sys
with open(sys.argv[1], 'r') as f:
    while True:
        x = f.read(1)
        if len(x) == 0:
            break
        if ord(x) in range(0, 128):
            sys.stdout.write(x)
