#!/usr/bin/env python

import os
from optparse import OptionParser
import random
import re

from bs4 import BeautifulSoup
import requests
import PIL
from PIL import Image


LOREM_IPSUM = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."


def comply_with_terms_of_use():
    # http://meta.wikimedia.org/wiki/Terms_of_use
    # says some things about not engaging in automated usage of the site
    # if it's abusive, disruptive, burdensome, malicious, etc.  Therefore:
    from time import sleep
    sleep(8)


def get_image_from_page(url, local_filename, insist_on_pd_mark=False):
    # We grab the original file.  It may be bigger than we need, but we can
    # scale it down later.
    if os.path.exists(local_filename):
        print "...already got it"
        return False

    img_filename = url.split(':')[-1]
    soup = BeautifulSoup(requests.get(url).content)

    if insist_on_pd_mark:
        url_part = u'//creativecommons.org/publicdomain/mark/1.0/deed'
        mark_links = [link for link in soup.find_all('a')
                      if url_part in unicode(link.get('href'))]
        if not mark_links:
            print "...no public domain mark found!"
            return False
        print "Found public domain mark!  Continuing..."

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

    comply_with_terms_of_use()
    return True


def convert_image(filename, max_width=400):
    new_filename = os.path.join(
        os.path.dirname(filename), "_converted_" + os.path.basename(filename) + ".png"
    )
    if os.path.exists(new_filename):
        print "already converted"
        return new_filename
    print 'convert {0} {1}'.format(filename, new_filename)
    exit_code = os.system("convert {0} {1}".format(filename, new_filename))
    if exit_code != 0:
        print "ERROR converting image!"
        return False

    image = Image.open(new_filename)
    print image
    width = image.size[0]
    height = image.size[1]
    if width > max_width:
        scale = max_width / float(width)
        new_width = int(width * scale)
        new_height = int(height * scale)
        print "resizing to %s x %s" % (new_width, new_height)
        image = image.resize((new_width, new_height), resample=PIL.Image.ANTIALIAS)
        image.save(new_filename)

    return new_filename


def load_index(filename):
    index = []
    with open(filename) as f:
        for line in f:
            index.append(line.strip())
    return index


def get_random_image(index, dest_dir, insist_on_pd_mark=False):
    media_url = random.choice(index)
    print media_url
    local_filename = os.path.join(dest_dir, media_url.split(':')[-1])
    get_image_from_page(
        media_url, local_filename, insist_on_pd_mark=insist_on_pd_mark
    )
    return local_filename


def main(argv):
    optparser = OptionParser(__doc__)
    optparser.add_option("--insist-on-pd-mark", default=False, action='store_true',
                         help="only download if media page contains public domain mark")
    (options, args) = optparser.parse_args(argv[1:])

    # BAHHH
    argv = ['whatevs'] + args

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
        get_image_from_page(
            media_url, local_filename,
            insist_on_pd_mark=options.insist_on_pd_mark
        )

    elif argv[1] == 'getmany':
        with open(argv[2]) as f:
            for line in f:
                media_url = line.strip()
                local_filename = media_url.split(':')[-1]
                get_image_from_page(
                    media_url, local_filename,
                    insist_on_pd_mark=options.insist_on_pd_mark
                )

    elif argv[1] == 'convertmany':
        dest_dir = argv[2]
        filenames = argv[3:]
        for filename in filenames:
            output_filename = os.path.join(
                dest_dir, os.path.splitext(filename)[0] + '.png'
            )
            if os.path.exists(output_filename):
                print "%s already exists, skipping" % output_filename
                continue
            command = "convert %s %s" % (filename, output_filename)
            print command
            os.system(command)

    elif argv[1] == 'random':
        count = int(argv[2])
        dest_dir = argv[3]
        index = load_index(argv[4])
        for n in xrange(0, count):
            get_random_image(
                index, dest_dir, insist_on_pd_mark=options.insist_on_pd_mark
            )

    elif argv[1] == 'render':
        count = int(argv[2])
        dest_dir = argv[3]
        index = load_index(argv[4])
        template = """\
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Lorum Ipsem Shkoo</title>
    <style>
hr { page-break-before: always; }
.c { width: 100%; text-align: center; }
    </style>
  <body>
   $
  </body>
</html>"""

        body = ''
        for x in xrange(0, count):
            filename = get_random_image(
                index, dest_dir, insist_on_pd_mark=options.insist_on_pd_mark
            )
            filename = convert_image(filename)

            if x != 0:
                body += '<hr>'

            paras = ['<p>' + LOREM_IPSUM + '</p>'] * 4
            align = random.choice(('left', 'right', 'centre'))
            if align == 'left':
                paras.append('<img style="float: left" src="%s">' % filename)
            elif align == 'right':
                paras.append('<img style="float: right" src="%s">' % filename)
            elif align == 'centre':
                paras.append('<div class="c"><img src="%s"></div>' % filename)
            random.shuffle(paras)
            body += ''.join(paras)

        template = template.replace('$', body)
        with open('tmp.html', 'w') as f:
            f.write(template)
        import webbrowser
        webbrowser.open('tmp.html')

    else:
        raise KeyError('please read the source code')


if __name__ == '__main__':
    import sys
    main(sys.argv)
