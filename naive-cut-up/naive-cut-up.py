#!/usr/bin/env python

import os
import sys

from chroniclingamerica import ChronAm
import requests


def download(item, local_id):
    url = 'http://chroniclingamerica.loc.gov/%s.jp2' % item['id'][:-1]
    local_filename = 'ca_%s.jp2' % local_id
    print '{0} --> {1}'.format(url, local_filename)
    response = requests.get(url, stream=True)
    if response.ok:
        with open(local_filename, 'w') as f:
            for block in response.iter_content(1024):
                f.write(block)
    new_filename = local_filename + '.jpg'
    print 'convert {0} {1}'.format(local_filename, new_filename)
    os.system("convert {0} {1}".format(local_filename, new_filename))
    print 'done!'


def main(argv):
    if argv[1] == 'fetch':
        fetcher = ChronAm(argv[2])
        for x, item in enumerate(fetcher.fetch()):
            download(item, x)
            if x > 5:
                break
        sys.exit(0)


if __name__ == '__main__':
    import sys
    main(sys.argv)
