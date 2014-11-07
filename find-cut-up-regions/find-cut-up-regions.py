#!/usr/bin/env python

from optparse import OptionParser
import os
import random
import sys

from PIL import Image


def main(argv):
    optparser = OptionParser(__doc__)
    (options, args) = optparser.parse_args(argv[1:])

    image = Image.open(args[0])
    print image

    (width, height) = image.size

    margin_left = int(width * 0.05)
    margin_right = int(width * 0.95)
    margin_top = int(height * 0.05)
    margin_bottom = int(height * 0.95)
 
    region = image.crop((margin_left, margin_top, margin_right, margin_bottom))
    image = region.copy()

    (width, height) = image.size

    light_rows = []

    for y in xrange(0, height):
        if y % 100 == 0:
            print "row %s/%s" % (y, height)
        light_pixels = 0
        for x in xrange(0, width):
            pixel = image.getpixel((x, y))
            light = False
            if pixel > 150:
                light = True
            if light:
                #image.putpixel((x, y), 255)
                light_pixels += 1
            else:
                #image.putpixel((x, y), 0)
                pass
        if (light_pixels / (width * 1.0)) > 0.96:
            light_rows.append(y)
            #for x in xrange(0, width):
            #    image.putpixel((x, y), 128)

    cuttable_ribbons = []  # list of (y, thickness) tuples
    thickness = None
    start_y = None
    previous_light_y = None
    for light_y in light_rows:
        if previous_light_y is None:
            thickness = 1
            start_y = light_y
            previous_light_y = light_y
        elif previous_light_y == light_y - 1:
            thickness += 1
            previous_light_y = light_y
        else:
            previous_light_y = None
            cuttable_ribbons.append((start_y, thickness))

    for ribbon in cuttable_ribbons:
        for y in xrange(ribbon[0], ribbon[0] + ribbon[1]):
            for x in xrange(0, width):
                image.putpixel((x, y), 0)

    image.save("output.png")


if __name__ == '__main__':
    import sys
    main(sys.argv)
