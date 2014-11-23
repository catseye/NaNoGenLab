#!/usr/bin/env python

import os
import re
import sys
import time

seed = 0

while True:
    if seed % 10 == 0:
        time.sleep(0.10)  # so that ^C can actually stop this script
        sys.stdout.write("(%s)" % seed)

    os.system("./narrated-card-game.py --seed %s > cards.txt" % seed)
    os.system("wc -w cards.txt > wc.txt")

    with open('wc.txt') as f:
        amount = f.read()
        match = re.match('^(\d+).*?$', amount)
        if match:
            amount = int(match.group(1))

    if amount >= 50000:
        sys.stdout.write("[seed %s = %s words]" % (seed, amount))
    else:
        sys.stdout.write('.')
    sys.stdout.flush()

    seed += 1
