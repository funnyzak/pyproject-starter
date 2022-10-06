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


class AddPdfAnnotation:
    """add annotation to a pdf file."""

    def __init__(self, source_pdf_path, output_pdf_path=None) -> None:
        """Pass in the path to the PDF file you want to annotate.

        :param source_pdf_path: source pdf file path
        :param output_pdf_path: output pdf file path
        """
        self.check_file(source_pdf_path)
        self.source_pdf_path = source_pdf_path

        # if output pdf file path not specified, use tempfile path
        self.output_pdf_path = (
            output_pdf_path
            if output_pdf_path not in [None, ""] and output_pdf_path.endswith(".pdf")
            else f"{source_pdf_path.split('.pdf')[0]}_"
            + f"dist_annotated_{str(int(datetime.datetime.now().timestamp()))}.pdf"
        )

    def add_annotation(self, annotation_list: list) -> str:
        """Fill the writer with the pages you want.

        :param annotation_list: annotation list - annotation list and
        each item is a dict like: {"page": 0, "annotation": annotation}
        """
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
        return self.output_pdf_path

    def check_file(self, file_path: str):
        """Check file exist and if pdf file."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"file {file_path} not found")
        if not file_path.endswith(".pdf"):
            raise ValueError(f"file {file_path} is not pdf file")


def add_pdf_annotiation_demo() -> None:
    """Add pdf annotiation demo."""
    root_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    attachment_dir = os.path.join(root_dir, "public/attachments")
    pic_pdf_path = os.path.join(attachment_dir, "samplepic.pdf")

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

    add_pdf_annotation = AddPdfAnnotation(pic_pdf_path)
    add_pdf_annotation.add_annotation([{"page": 0, "annotation": annotation}])


if __name__ == "__main__":
    add_pdf_annotiation_demo()  # pragma: no cover
