#!/usr/bin/env python

import json
import os
import sys

from PIL import Image


def main(argv):
    greatest_area = 0
    greatest_area_filename = None
    data = {
        'images': {}
    }
    for filename in argv[1:]:
        image = Image.open(filename)
        area = image.size[0] * image.size[1]
        data['images'][filename] = {
            'filename': filename,
            'width': image.size[0],
            'height': image.size[1],
            'area': area,
            'aspect_ratio': image.size[0] / float(image.size[1]),
        }
        if area > greatest_area:
            greatest_area = area
            greatest_area_filename = filename
    data['greatest_area'] = data['images'][greatest_area_filename]
    print json.dumps(data)


if __name__ == '__main__':
    import sys
    main(sys.argv)
