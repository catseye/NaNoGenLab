#!/usr/bin/env python

import random
from time import sleep

from bs4 import BeautifulSoup
import requests


def get_image_from_page(url):
    # Doesn't work quite right yet
    # http://commons.wikimedia.org/wiki/File:Aye-Aye_Mivart.png
    # http://commons.wikimedia.org/wiki/File:Penelope_Boothby_by_Joshua_Reynolds.jpg
    soup = BeautifulSoup(requests.get(url).content)
    orig_links = [link for link in soup.find_all('a')
                  if link.get_text() == 'Original file']
    assert orig_links
    image_url = orig_links[0].get('href')
    print image_url


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
    else:
        raise KeyError('please read the source code')


if __name__ == '__main__':
    import sys
    main(sys.argv)
