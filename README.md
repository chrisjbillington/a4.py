# a4.py

A script to crop a pdf to A4 size. Requires pyPdf or PyPDF2.

Useful for making papers published in US letter size the right size to go in a thesis.

Preserves hyperlinks.

Does not scale anything, just adjusts margins.

## Requirements

* Python
* pyPdf: 

install pyPdf with:

    pip install pypdf

## Usage:

    python a4.py infile.pdf outfile.pdf