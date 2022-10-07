# -*- coding: utf-8 -*-
# created by: leon<silenceace at gmail dot com>
# date: 2022-10-07
# license: MIT
# description: Extract images from pdf file
# usage: poetry run python src/pdf_parse/extract_pdf_images.py
# notes:

import argparse
from datetime import datetime

# Extract images from pdf file
import os
from typing import List

from pikepdf import Pdf, PdfImage


class ExtractPdfImages:
    """Extract images from pdf file."""

    def __init__(self, pdf_file, output_path=None) -> None:
        """Pass in the path to the PDF file you want to extract images from.

        :param pdf_file: pdf file path
        :param output_path: output dir
        """
        self.pdf_file = pdf_file
        self.output_path = output_path

        self.check_file()
        self.check_out_path()

    def extract(self) -> List[str]:
        """Extract images from pdf file."""
        pdf = Pdf.open(self.pdf_file)

        img_path_list = []

        for i, page in enumerate(pdf.pages):
            for j, (_name, raw_image) in enumerate(page.images.items()):

                cur_img = PdfImage(raw_image)
                img_path_list.append(cur_img.extract_to(fileprefix=f"{self.output_path}-page{i:03}-img{j:03}"))

        print(f"\033[1;32mExtracted images to {self.output_path}, all images: {img_path_list}\033[0m")
        return img_path_list

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


def test_extract_pdf_images():
    """Test extract pdf images."""
    root_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    attachment_dir = os.path.join(root_dir, "public/attachments")
    pic_pdf_path = os.path.join(attachment_dir, "samplepic.pdf")

    extract_pdf_images = ExtractPdfImages(pic_pdf_path)
    extract_pdf_images.extract()


def main() -> None:  # pragma: no cover
    parser = argparse.ArgumentParser(description="Extract images from pdf file")
    parser.add_argument("-i", "--input", help="input pdf file", required=False)
    parser.add_argument("-o", "--output", help="output directory", required=False)

    args = parser.parse_args()

    pdf_file = args.input
    output_dir = args.output

    if pdf_file is None:
        pdf_file = input("input pdf file: ").split(" ")
    if output_dir is None:
        output_dir = input("input output directory: ")

    extract_pdf = ExtractPdfImages(pdf_file, output_dir)
    extract_pdf.extract()


if __name__ == "__main__":
    main()  # pragma: no cover
