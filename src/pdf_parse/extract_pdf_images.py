# -*- coding: utf-8 -*-
# created by: leon<silenceace at gmail dot com>
# date: 2022-10-07
# license: MIT
# description: Extract images from pdf file
# usage: poetry run python src/pdf_parse/extract_pdf_image.py
# notes:

# Extract images from pdf file
import os

from pikepdf import Pdf, PdfImage


class ExtractPdfImage:
    """Extract images from pdf file."""

    def __init__(self, pdf_file, output_dir) -> None:
        """Pass in the path to the PDF file you want to extract images from.

        :param pdf_file: pdf file path
        :param output_dir: output dir
        """
        self.pdf_file = pdf_file
        self.output_dir = output_dir

        self.check_file()

    def extract(self) -> list[str]:
        """Extract images from pdf file."""
        pdf = Pdf.open(self.pdf_file)

        img_path_list = []
        for i, page in enumerate(pdf.pages):
            for j, (name, raw_image) in enumerate(page.images.items()):

                cur_img = PdfImage(raw_image)
                img_path_list.append(cur_img.extract_to(fileprefix=f"{self.output_dir}-page{i:03}-img{j:03}"))

        print(f"\033[1;32mExtracted images to {self.output_dir}, all images: {img_path_list}\033[0m")
        return img_path_list

    def check_file(self) -> None:
        """Check file exist and if pdf file."""
        if not os.path.exists(self.pdf_file):
            raise FileNotFoundError(f"file {self.pdf_file} not found")
        if not self.pdf_file.endswith(".pdf"):
            raise ValueError(f"file {self.pdf_file} is not pdf file")
