# created by: leon<silenceace at gmail dot com>
# date: 2022-10-02
# license: MIT
# description: Add annotations to pdf file
# usage: python3 add_pdf_annotiations.py
# notes:

import os
from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import AnnotationBuilder

RESOURCE_ROOT = os.path.join(os.path.dirname(__file__), "attachments")
source_pdf_path = os.path.join(RESOURCE_ROOT, "whatispython.pdf")
output_pdf_path = os.path.join(os.path.dirname(__file__), "dist_whatispython_filled.pdf")

# Fill the writer with the pages you want
reader = PdfReader(source_pdf_path)
page = reader.pages[0]
writer = PdfWriter()
writer.add_page(page)

# Create the annotation and add it
annotation = AnnotationBuilder.free_text(
    "Hello World\nThis is the second line!",
    rect=(50, 550, 200, 650),
    font="Arial",
    bold=True,
    italic=True,
    font_size="20pt",
    font_color="00ff00",
    border_color="0000ff",
    # background_color="cdcdcd",
)
writer.add_annotation(page_number=0, annotation=annotation)

# Write the annotated file to disk
with open(output_pdf_path, "wb") as fp:
    writer.write(fp)
    print(f"Annotated PDF written to {output_pdf_path}")
