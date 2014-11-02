#!/usr/bin/env python

import os
import random
import re
from time import sleep

from bs4 import BeautifulSoup
import requests


def get_image_from_page(url):
    # We grab the original file.  It may be bigger than we need, but we can
    # scale it down later.
    img_filename = url.split(':')[-1]
    soup = BeautifulSoup(requests.get(url).content)
    orig_links = [link for link in soup.find_all('a')
                  if link.get_text() in ('Original file', img_filename)]
    assert orig_links
    image_url = 'http:' + orig_links[0].get('href')
    print '{0} --> {1}'.format(image_url, img_filename)

    response = requests.get(image_url, stream=True)
    if response.ok:
        with open(img_filename, 'w') as f:
            for block in response.iter_content(1024):
                f.write(block)


def main(argv):
    if argv[1] == 'mkindex':
        index_url = 'http://commons.wikimedia.org/wiki/Category:PD_Gutenberg'
        output_file = 'PD_Gutenberg_index.txt'
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
                sleep(5)
            else:
                done = True
            count += 1

        print "grabbed %s category index pages" % count

        with open(output_file, 'w') as f:
            for link in sorted(media_links):
                f.write('http://commons.wikimedia.org' + link + '\n')

    elif argv[1] == 'get':
        media_url = argv[2]
        get_image_from_page(media_url)

    else:
        raise KeyError('please read the source code')


if __name__ == '__main__':
    import sys
    main(sys.argv)
