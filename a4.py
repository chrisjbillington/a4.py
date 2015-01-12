#!/usr/bin/env python

#####################################################################
#                                                                   #
# a4.py                                                             #
#                                                                   #
# Copyright 2015, Christopher Billington                            #
#                                                                   #
# Licensed under the 2-clause BSD License.                          #
# See LICENSE.txt for the full license.                             #
#                                                                   #
#####################################################################

import sys
import os

try:
    from PyPDF2 import PdfFileReader, PdfFileWriter
except ImportError:
    try:
        from pyPdf import PdfFileReader, PdfFileWriter
    except ImportError:
        raise ImportError("Could not import pyPdf or PyPDF2")

try:
    infilename = sys.argv[1]
    outfilename = sys.argv[2]
except IndexError:
    sys.stderr.write('usage: python %s infile.pdf outfile.pdf\n'%os.path.basename(__file__))
    sys.exit(1)

A4_WIDTH = 595
A4_HEIGHT = 842

with open(infilename, 'rb') as infile:
    input_pdf = PdfFileReader(infile)
    output_pdf = PdfFileWriter()
    for page_no in range(input_pdf.getNumPages()):
        page = input_pdf.getPage(page_no)

        source_x0, source_y0 = page.mediaBox.lowerLeft
        source_x1, source_y1 = page.mediaBox.upperRight
        source_width = source_x1 - source_x0
        source_height = source_y1 - source_y0

        new_x0 = source_x0 + (source_width - A4_WIDTH)/2.
        new_y0 = source_y0 + (source_height + A4_HEIGHT)/2.
        new_x1 = source_x0 + (source_width + A4_WIDTH)/2.
        new_y1 = source_y0 + (source_height - A4_HEIGHT)/2.

        page.mediaBox.lowerLeft = (new_x0, new_y0)
        page.mediaBox.upperRight = (new_x1, new_y1)
        page.cropBox.lowerLeft = (new_x0, new_y0)
        page.cropBox.upperRight = (new_x1, new_y1)

        output_pdf.addPage(page)

    with open(outfilename, 'wb') as outfile:
        output_pdf.write(outfile)
