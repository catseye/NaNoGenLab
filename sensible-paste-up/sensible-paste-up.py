#!/usr/bin/env python

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


def main(argv):
    optparser = OptionParser(__doc__)
    (options, args) = optparser.parse_args(argv[1:])

    images = []
    for filename in args:
        images.append(Image.open(filename))

    base_width = 1200
    base_height = 2000

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
        for trial in xrange(0, 100):
            score = 0
            paste_point = (random.randint(0, base_width - image.size[0]),
                           random.randint(0, base_height - image.size[1]))

            lum = get_luminance(canvas, (
                paste_point[0], paste_point[1],
                paste_point[0] + image.size[0], paste_point[1] + image.size[1],
            ))
            
            score = lum
            # TODO also factor in distance to desired point
            
            if score > best_score:
                best_score = score
                best_place = paste_point
                print "improved score", best_score

        print "best score:", best_score, best_place
        canvas.paste(image, best_place)

    canvas.save("output.png")


if __name__ == '__main__':
    import sys
    main(sys.argv)
