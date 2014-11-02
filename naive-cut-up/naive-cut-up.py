#!/usr/bin/env python

import os
import random
import sys

from chroniclingamerica import ChronAm
from PIL import Image
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
    new_filename = local_filename + '.png'
    print 'convert {0} {1}'.format(local_filename, new_filename)
    os.system("convert {0} {1}".format(local_filename, new_filename))
    print 'done!'


def load_image(filename):
    image = Image.open(filename)
    print filename, image
    return image


def main(argv):
    if argv[1] == 'fetch':
        amount = int(argv[2])
        fetcher = ChronAm(argv[3])
        for x, item in enumerate(fetcher.fetch()):
            if x == amount:
                break
            download(item, x)

    elif argv[1] == 'largest':
        greatest = 0
        greatest_filename = 'NONE'
        for filename in argv[2:]:
            image = load_image(filename)
            size = image.size[0] * image.size[1]
            if size > greatest:
                greatest = size
                greatest_filename = filename
        print "LARGEST IS", greatest_filename

    elif argv[1] == 'cutup':
        base_filename = argv[2]
        cutup_filenames = argv[3:]

        base_image = load_image(base_filename)
        base_width = base_image.size[0]
        base_height = base_image.size[1]

        images = []
        for filename in cutup_filenames:
            images.append(load_image(filename))

        for n in xrange(0, 100):
            image = random.choice(images)
            width = image.size[0]
            height = image.size[1]
            
            crop_width = width / 3
            crop_height = height / 3

            # note that for crop boxes, the 3rd and 4th elements are
            # *positions*, not *dimensions*!
            crop_x = random.randint(0, width - crop_width)
            crop_y = random.randint(0, height - crop_height)
            crop_box = (
                crop_x, crop_y, crop_x + crop_width, crop_y + crop_height
            )
            crop_region = image.crop(crop_box)
            print image, crop_box, crop_region

            paste_point = (random.randint(0, base_width - crop_width),
                           random.randint(0, base_height - crop_height))
            
            base_image.paste(crop_region, paste_point)
        
        print "Writing output.png..."
        base_image.save("output.png")

    else:
        raise KeyError("First arg must be `fetch`, `largest`, or `cutup`")


if __name__ == '__main__':
    import sys
    main(sys.argv)
