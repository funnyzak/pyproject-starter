# -*- coding: utf-8 -*-
# created by: leon<silenceace at gmail dot com>
# date: 2022-10-05
# license: MIT
# description: Add annotations to pdf file
# usage: poetry run python src/pdf_parse/add_pdf_annotiation.py
# notes:

import datetime
import os

from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import AnnotationBuilder


# add annotation to a pdf file
class AddPdfAnnotation:
    # @param {string} source_pdf_path - source pdf file path
    # @param {string} output_pdf_path - output pdf file path
    def __init__(self, source_pdf_path, output_pdf_path):
        self.check_file(source_pdf_path)
        self.source_pdf_path = source_pdf_path
        self.output_pdf_path = output_pdf_path

    # add annotation to pdf file
    def add_annotation(self, annotation_list: list):
        # @param {list} annotation_list - annotation list and
        # each item is a dict like: {"page": 0, "annotation":
        # annotation}
        # Fill the writer with the pages you want
        reader = PdfReader(self.source_pdf_path)

        # write each page to output pdf file from source pdf file
        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)

        for annotation in annotation_list:
            # if page out of range, skip
            if annotation["page"] >= len(reader.pages):
                continue
            writer.add_annotation(page_number=annotation["page"], annotation=annotation["annotation"])

        with open(self.output_pdf_path, "wb") as fp:
            writer.write(fp)
            print(f"Annotated PDF written to {self.output_pdf_path}")

    # check file exist and if pdf file
    def check_file(self, file_path: str):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"file {file_path} not found")
        if not file_path.endswith(".pdf"):
            raise ValueError(f"file {file_path} is not pdf file")


def add_pdf_annotiation_demo():
    root_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    attachment_dir = os.path.join(root_dir, "public/attachments")
    pic_pdf_path = os.path.join(attachment_dir, "samplepic.pdf")
    output_pdf_path = os.path.join(
        root_dir, "dist/pdf_parse", f"annot_{str(int(datetime.datetime.now().timestamp()))}.pdf"
    )

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
        background_color="cdcdcd",
    )

    add_pdf_annotation = AddPdfAnnotation(pic_pdf_path, output_pdf_path)
    add_pdf_annotation.add_annotation([{"page": 0, "annotation": annotation}])


if __name__ == "__main__":
    add_pdf_annotiation_demo()
