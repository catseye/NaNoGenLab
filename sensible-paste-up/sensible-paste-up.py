#!/usr/bin/env python

from optparse import OptionParser
import os
import random
import sys

from PIL import Image


def main(argv):
    optparser = OptionParser(__doc__)
    (options, args) = optparser.parse_args(argv[1:])

    images = []
    for filename in args:
        images.append(Image.open(filename))

    canvas = Image.new('L', (1200, 2000), color=255)

    def area(image):
        return image.size[0] * image.size[1]

    images.sort(lambda a, b: cmp(area(b), area(a)))

    for image in images:
        canvas.paste(image, (0, 0))

    canvas.save("output.png")


if __name__ == '__main__':
    import sys
    main(sys.argv)
