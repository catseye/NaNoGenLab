#!/usr/bin/env python

from optparse import OptionParser
import os
import random
import sys

from PIL import Image


def main(argv):
    optparser = OptionParser(__doc__)
    optparser.add_option("--total-strips", default='3000',
                         help="total number of strips to lay down")
    optparser.add_option("--lines-per-page", default='80',
                         help="average height of a strip is 1 over this")
    (options, args) = optparser.parse_args(argv[1:])

    base_filename = args[0]
    cutup_filenames = args[1:]
    
    base_image = Image.open(base_filename)
    base_width = base_image.size[0]
    base_height = base_image.size[1]
    print base_image

    images = [base_image]
    for filename in cutup_filenames:
        image = Image.open(filename)
        # hope the aspect ratio is similar...
        image = image.resize((base_width, base_height))
        print image
        images.append(image)

    for n in xrange(0, int(options.total_strips)):
        image = random.choice(images)

        crop_width = int(base_width / (2 + (random.random() * 3)))
        crop_height = int(base_height / (float(options.lines_per_page)))

        # note that for crop boxes, the 3rd and 4th elements are
        # *positions*, not *dimensions*!
        crop_x = random.randint(0, base_width - crop_width)
        crop_y = random.randint(0, base_height - crop_height)
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


if __name__ == '__main__':
    import sys
    main(sys.argv)
