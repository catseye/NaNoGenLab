#!/usr/bin/env python

import os
import random
import sys

from chroniclingamerica import ChronAm
import requests


def comply_with_terms_of_use():
    # http://www.loc.gov/legal says they reserve the right to block anyone
    # who negatively impacts their service (fair enough) and recommend that
    # consumers make no more than 10 requests per minute.  If my arithmetic
    # is correct, that's one request every 6 seconds.  Considering that
    # we spend a considerable amount of time in `convert` too, this sleep
    # is generous.
    from time import sleep
    sleep(10)


def download(item, local_id):
    url = 'http://chroniclingamerica.loc.gov/%s.jp2' % item['id'][:-1]
    local_filename = 'ca_%s.jp2' % local_id
    print '{0} --> {1}'.format(url, local_filename)
    response = requests.get(url, stream=True)
    if response.ok:
        with open(local_filename, 'w') as f:
            for block in response.iter_content(1024):
                f.write(block)
    new_filename = os.path.splitext(local_filename)[0] + '.png'
    print 'convert {0} {1}'.format(local_filename, new_filename)
    exit_code = os.system("convert {0} {1}".format(local_filename, new_filename))
    if exit_code == 0:
        os.remove(local_filename)
        print 'done!'
    else:
        print "ERROR converting image"


def main(argv):
    amount = int(argv[1])
    fetcher = ChronAm(argv[2])
    for x, item in enumerate(fetcher.fetch()):
        if x == amount:
            break
        download(item, x)
        comply_with_terms_of_use()


if __name__ == '__main__':
    import sys
    main(sys.argv)
