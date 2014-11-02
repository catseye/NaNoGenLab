#!/usr/bin/env python

import os
import random
import re

from bs4 import BeautifulSoup
import requests


def comply_with_terms_of_use():
    # http://meta.wikimedia.org/wiki/Terms_of_use
    # says some things about not engaging in automated usage of the site
    # if it's abusive, disruptive, burdensome, malicious, etc.  Therefore:
    from time import sleep
    sleep(8)


def get_image_from_page(url, local_filename):
    # We grab the original file.  It may be bigger than we need, but we can
    # scale it down later.
    if os.path.exists(local_filename):
        print "...already got it"
        return False

    img_filename = url.split(':')[-1]
    soup = BeautifulSoup(requests.get(url).content)
    orig_links = [link for link in soup.find_all('a')
                  if link.get_text() in ('Original file', img_filename)]
    assert orig_links, \
      "Couldn't find usable download link on %s" % url
    image_url = orig_links[0].get('href')
    if not image_url.startswith('http:'):
        image_url = 'http:' + image_url
    print '{0} --> {1}'.format(image_url, local_filename)

    response = requests.get(image_url, stream=True)
    if response.ok:
        with open(local_filename, 'w') as f:
            for block in response.iter_content(1024):
                f.write(block)

    return True


def main(argv):
    if argv[1] == 'mkindex':
        category = argv[2]
        index_url = 'http://commons.wikimedia.org/wiki/Category:' + category
        output_file = 'Wikimedia-Commons-Category-index-%s.txt' % category
        media_links = set()
        
        done = False
        count = 0
        while not done:
            print index_url
            soup = BeautifulSoup(requests.get(index_url).content)
            media_links |= set([
                link.get('href') for link in soup.find_all('a')
                  if link.get('href') and link.get('href').startswith('/wiki/File:')
            ])
            
            next_links = [link for link in soup.find_all('a') if link.get_text() == 'next 200']
            if next_links:
                index_url = 'http://commons.wikimedia.org/' + next_links[0].get('href')
                comply_with_terms_of_use()
            else:
                done = True
            count += 1

        print "grabbed %s category index pages" % count

        with open(output_file, 'w') as f:
            for link in sorted(media_links):
                f.write('http://commons.wikimedia.org' + link + '\n')

    elif argv[1] == 'get':
        media_url = argv[2]
        local_filename = media_url.split(':')[-1]
        get_image_from_page(media_url, local_filename)

    elif argv[1] == 'random':
        count = int(argv[2])
        dest_dir = argv[3]
        index_filename = argv[4]
        index = []
        with open(index_filename) as f:
            for line in f:
                index.append(line.strip())
        for n in xrange(0, count):
            media_url = random.choice(index)
            print media_url
            local_filename = os.path.join(dest_dir, media_url.split(':')[-1])
            get_image_from_page(media_url, local_filename)
            comply_with_terms_of_use()

    else:
        raise KeyError('please read the source code')


if __name__ == '__main__':
    import sys
    main(sys.argv)
