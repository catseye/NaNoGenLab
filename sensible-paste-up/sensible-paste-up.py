#!/usr/bin/env python

import math
from optparse import OptionParser
import os
import random
import sys

from PIL import Image


def get_luminance(image, rectangle):
    # not that I know what luminance means.  we want the pick the
    # "blankest" part of the canvas, is all.  this is an attempt
    region = image.crop(rectangle)
    histogram = region.histogram()
    # how many times does the very brightest pixel occur?
    return histogram[-1]
    # could be something more like
    # histogram[-1] * 256 + histogram[-2] * 128 + histogram[-3] * 64 ...


def main(argv):
    optparser = OptionParser(__doc__)
    optparser.add_option("--width", default=1200,
                         help="width of destination canvas")
    optparser.add_option("--height", default=2000,
                         help="height of destination canvas")
    (options, args) = optparser.parse_args(argv[1:])

    images = []
    for filename in args:
        images.append(Image.open(filename))

    base_width = int(options.width)
    base_height = int(options.height)

    canvas = Image.new('L', (base_width, base_height), color=255)

    def area(image):
        return image.size[0] * image.size[1]

    images.sort(lambda a, b: cmp(area(b), area(a)))

    for image in images:
        # make n trials to find a "good" place to put this.
        # use the place with the best score.
        
        best_score = 0
        best_place = None
        print image
        desired_point = (base_width / 2, base_height / 2)
        for trial in xrange(0, 100):
            score = 0
            try:
                paste_point = (random.randint(0, base_width - image.size[0]),
                               random.randint(0, base_height - image.size[1]))
            except ValueError:
                print "uh-oh, won't fit?"
                continue

            lum = get_luminance(canvas, (
                paste_point[0], paste_point[1],
                paste_point[0] + image.size[0], paste_point[1] + image.size[1],
            ))
            
            score = lum

            # also factor in distance to desired point
            distance = math.sqrt(
                (paste_point[0] - desired_point[0]) ** 2 +
                (paste_point[1] - desired_point[1]) ** 2
            )
            score -= distance  # ??

            if score > best_score:
                best_score = score
                best_place = paste_point
                print "improved score", best_score

        print "best score:", best_score, best_place
        if best_place is None:
            print "Could not find good place to paste!"
        else:
            canvas.paste(image, best_place)

    canvas.save("output.png")


if __name__ == '__main__':
    import sys
    main(sys.argv)
