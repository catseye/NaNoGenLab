#!/usr/bin/env python

from optparse import OptionParser
import os
import random
import sys

import PIL
from PIL import Image

try:
    from tqdm import tqdm
except ImportError:
    def tqdm(x):
        return x


def mkdir_p(path):
    try:
        os.mkdir(path)
    except OSError:
        pass


def cutup(options, image, dirname, prefix='', rotation=None):
    """Returns list of output filenames"""

    if rotation is not None:
        image = image.rotate(rotation, expand=True)

    mkdir_p(dirname)

    (width, height) = image.size

    # FIXME: iteratively look for too-dark rectangles around the edge of
    # the image and remove them one by one instead.  but this is OK for now

    margin_left = int(width * 0.05)
    margin_right = int(width * 0.95)
    margin_top = int(height * 0.05)
    margin_bottom = int(height * 0.95)
 
    region = image.crop((margin_left, margin_top, margin_right, margin_bottom))
    image = region.copy()
    contrast = image.copy()

    (width, height) = image.size

    light_rows = []

    # FIXME: throw the image through an (almost-)max-contrast filter first;
    # that should make it easier to work on a wide range of images of varying
    # contrast levels

    for y in tqdm(xrange(0, height)):
        light_pixels = 0
        for x in xrange(0, width):
            pixel = image.getpixel((x, y))
            light = False
            if pixel > 175:  # 150 ?
                light = True
            if light:
                if options.debug:
                    contrast.putpixel((x, y), 255)
                light_pixels += 1
            else:
                if options.debug:
                    contrast.putpixel((x, y), 0)
                pass
        if (light_pixels / (width * 1.0)) > 0.96:
            light_rows.append(y)
            #for x in xrange(0, width):
            #    image.putpixel((x, y), 128)

    if options.debug:
        print "saving contrast file"
        contrast.save(os.path.join(dirname, "contrast.png"))

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

    # reduce ribbon thicknesses
    margin = 4  # how much whitespace you want around darkpixelness?
                # note that if you change the scale (dimensions), ...
                # so this could be an option, maybe?
    cuttable_ribbons = [
        (start_y + margin, thickness - margin * 2)
        for (start_y, thickness) in cuttable_ribbons
        if thickness > margin * 2
    ]
    # FIXME: we could / should retain the insufficiently-thick ones?

    if options.debug:
        print cuttable_ribbons
        print "marking up image and saving to cutlines.png"
        for ribbon in cuttable_ribbons:
            for y in xrange(ribbon[0], ribbon[0] + ribbon[1]):
                for x in xrange(0, width):
                    image.putpixel((x, y), 0)
        image.save(os.path.join(dirname, "cutlines.png"))

    # compute the crop-areas BETWEEN the cuttable ribbons
    crop_y = 0
    crop_areas = []

    for (start_y, thickness) in cuttable_ribbons:
        crop_areas.append(
            (0, crop_y, width, start_y)
        )
        crop_y = start_y + thickness

    crop_areas.append(
        (0, crop_y, width, height)
    )

    output_filenames = []
    for (crop_num, crop_area) in enumerate(crop_areas):
        region = image.crop(crop_area)
        if rotation is not None:
            # rotate BACK
            region = region.rotate(-1 * rotation, expand=True)
        if rotation is not None:
            # try to deal with ANNOYING BLACK BARS on left and top
            region = region.crop((1, 1, region.size[0], region.size[1]))
        output_filename = os.path.join(
            dirname, "%s_cut_%s.png" % (prefix, crop_num)
        )
        print "writing %s to %s" % (crop_area, output_filename)
        region.save(output_filename)
        output_filenames.append(output_filename)

    return output_filenames


def main(argv):
    optparser = OptionParser(__doc__)
    optparser.add_option("--dimensions", default=None,
                         help="scale all input pages to these dimensions")
    # note: cutup margins are dependent on page scale.
    optparser.add_option("--debug", action='store_true', default=False,
                         help="output debuging info")
    (options, args) = optparser.parse_args(argv[1:])

    for filename in args:
        dirname = os.path.basename(filename) + '.dir'
        mkdir_p(dirname)
        strips_dirname = os.path.join(dirname, 'strips')
        mkdir_p(strips_dirname)
        image = Image.open(filename)
        print filename, image

        if options.dimensions is not None:
            (width, height) = map(int, options.dimensions.split('x'))
            image = image.resize((width, height),
                                 resample=PIL.Image.ANTIALIAS) # might be useless
            print "scaled:", image

        strip_filenames = cutup(options, image, strips_dirname)
        chunks_dirname = os.path.join(dirname, 'chunks')
        mkdir_p(chunks_dirname)
        for strip_filename in strip_filenames:
            strip_image = Image.open(strip_filename)
            print strip_filename, strip_image
            chunk_filenames = cutup(
                options, strip_image, chunks_dirname,
                prefix=os.path.basename(strip_filename), rotation=90
            )


if __name__ == '__main__':
    import sys
    main(sys.argv)
