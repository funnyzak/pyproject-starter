# -*- coding: utf-8 -*-
# created by: leon<silenceace at gmail dot com>
# date: 2022-10-07
# license: MIT
# description: Single PDF Parse tools.
# usage: poetry run python src/pdf_parse/single_pdf_parse.py
# notes:

import argparse
from datetime import datetime
import os
from typing import List

from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter
from PyPDF2.generic import AnnotationBuilder


class SinglePdfParse:
    """Single pdf tool."""

    def __init__(self, pdf_file, output_path=None) -> None:
        """Pass in the path to the PDF file and output path.

        :param pdf_file: pdf file path
        :param output_path: output dir
        """
        self.pdf_file = pdf_file
        self.output_path = output_path

        self.check_file()
        self.check_out_path()

    def export_as_images(self) -> List[str]:
        # return empty
        return []

    def extract_text(self) -> str:
        """Extract text from pdf file."""
        reader = PdfReader(self.pdf_file)
        # extract text from pdf file
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

    def add_annotation(self, annotation_list: list) -> str:
        """Fill the writer with the pages you want.

        :param annotation_list: annotation list - annotation list and
        each item is a dict like: {"page": 0, "annotation": annotation}
        """
        reader = PdfReader(self.pdf_file)

        self.check_out_path()
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

    def check_file(self) -> None:
        """Check file exist and if pdf file."""
        if not os.path.exists(self.pdf_file):
            raise FileNotFoundError(f"file {self.pdf_file} not found")
        if not self.pdf_file.endswith(".pdf"):
            raise ValueError(f"file {self.pdf_file} is not pdf file")

    def check_out_path(self):
        if self.output_path in ["", None]:
            self.output_path = os.path.join(
                os.path.dirname(self.pdf_file), "_cache", str(int(datetime.now().timestamp() * 1000))
            )
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)


root_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
attachment_dir = os.path.join(root_dir, "public/attachments/pdf")
pic_pdf_path = os.path.join(attachment_dir, "samplepic.pdf")
pic_pdf_path2 = os.path.join(attachment_dir, "whatispython.pdf")


def test_export_as_images() -> None:
    """Test export pdf as images."""
    extract_pdf_images = SinglePdfParse(pic_pdf_path)
    extract_pdf_images.export_as_images()


def test_extract_text() -> None:
    """Test extract text from pdf."""
    extract_pdf_text = SinglePdfParse(pic_pdf_path2)
    text = extract_pdf_text.extract_text()
    print(text)


def test_add_annotation() -> None:
    """Add pdf annotiation demo."""
    # Create the annotation and add it
    annotation = AnnotationBuilder.free_text(
        "Hello World!",
        rect=(50, 550, 200, 650),
        font="Arial",
        bold=True,
        italic=True,
        font_size="20pt",
        font_color="00ff00",
        border_color="0000ff",
        background_color="cdcdcd",
    )

    SinglePdfParse(pic_pdf_path).add_annotation([{"page": 0, "annotation": annotation}])


def main() -> None:  # pragma: no cover
    parser = argparse.ArgumentParser(description="Single PDF Parse tools.")
    parser.add_argument("-m", "--mode", help="Mode: extract_images", default="extract-images")
    parser.add_argument("-i", "--input", help="input pdf file", required=False)
    parser.add_argument("-o", "--output", help="output directory", required=False)

    # args = parser.parse_args()
    # mode = args.model if not args.mode and args.mode in ["extract-images"] else "extract-images"
    # pdf_file = args.input
    # output_dir = args.output

    # if pdf_file is None:
    #     pdf_file = input("input pdf file: ").split(" ")
    # if output_dir is None:
    #     output_dir = input("input output directory: ")

    # extract_pdf = SinglePdfParse(pdf_file, output_dir)

    # if mode == "extract-images":
    #     extract_pdf.extract_images()


if __name__ == "__main__":
    main()  # pragma: no cover
