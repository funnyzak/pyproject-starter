# -*- coding: utf-8 -*-
# created by: leon<silenceace at gmail dot com>
# date: 2022-10-05
# license: MIT
# description: Add annotations to pdf file
# usage: poetry run python src/pdf_parse/add_pdf_annotiation.py
# notes:

from datetime import datetime
import os

from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import AnnotationBuilder


class AddPdfAnnotation:
    """add annotation to a pdf file."""

    def __init__(self, source_pdf_path, output_path: str = None) -> None:
        """Pass in the path to the PDF file you want to annotate.

        :param source_pdf_path: source pdf file path
        :param output_path: output pdf path
        """
        self.source_pdf_path = source_pdf_path
        self.output_path = output_path
        self.check_file(source_pdf_path)
        self.check_out_path()

    def add_annotation(self, annotation_list: list) -> str:
        """Fill the writer with the pages you want.

        :param annotation_list: annotation list - annotation list and
        each item is a dict like: {"page": 0, "annotation": annotation}
        """
        reader = PdfReader(self.source_pdf_path)
        output_pdf_path = os.path.join(
            self.output_path, f"annotiation_{str(int(datetime.now().timestamp() * 1000))}.pdf"
        )

        # write each page to output pdf file from source pdf file
        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)

        for annotation in annotation_list:
            # if page out of range, skip
            if annotation["page"] >= len(reader.pages):
                continue
            writer.add_annotation(page_number=annotation["page"], annotation=annotation["annotation"])

        with open(output_pdf_path, "wb") as fp:
            writer.write(fp)
            print(f"Annotated PDF written to {output_pdf_path}")
        return output_pdf_path

    def check_file(self, file_path: str):
        """Check file exist and if pdf file."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"file {file_path} not found")
        if not file_path.endswith(".pdf"):
            raise ValueError(f"file {file_path} is not pdf file")

    def check_out_path(self):
        if self.output_path in ["", None]:
            self.output_path = os.path.join(os.path.dirname(self.source_pdf_path), "_cache")
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)


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
