# -*- coding: utf-8 -*-
# created by: leon<silenceace at gmail dot com>
# date: 2022-10-06
# license: MIT
# description:  Parse pdf file to multi layer file
# usage: poetry run python src/pdf_parse/multi_pdf_to_multi_layer_pdf.py
# notes:

import argparse
from datetime import datetime
import os

from PyPDF2 import PdfReader, PdfWriter


class MultiPdfToMultiLayerFile:
    """Parse pdf file to multi layer file."""

    def __init__(self, pdf_files, output_dir):
        """Parse pdf file to multi layer file.

        :param pdf_files: pdf files to be multi layer
        :param output_dir: output dir
        """
        self.pdf_files = pdf_files
        self.output_dir = output_dir

        self.check_file()
        self.check_files_specified()
        self.check_out_dir()

    def be_multi_layer(self):
        """Merge pdf_files be multi-layer pdf file."""
        multi_layer_pdf_path = os.path.join(
            self.output_dir, f"multi_layer_dist_{str(int(datetime.now().timestamp()))}.pdf"
        )

        # clone first pdf file as base multi layer pdf file
        base_pdf = PdfReader(self.pdf_files[0])
        # under pdf page num
        base_pdf_page_num = len(base_pdf.pages)

        pdf_write = PdfWriter()

        # foreach pdf_files to be multi layer
        for pf_index, pdf_file in enumerate(self.pdf_files):
            # if first pdf file, skip
            if pf_index == 0:
                continue

            # read pdf file
            cur_pdf_reader = PdfReader(pdf_file)
            # get page count
            cur_pdf_page_count = len(cur_pdf_reader.pages)

            # foreach page to be multi layer
            for pdf_page_index in range(0, base_pdf_page_num, 1):
                base_page = base_pdf.pages[pdf_page_index]

                # if current pdf page less then current pdf page count, merge page
                if pdf_page_index < cur_pdf_page_count:
                    base_page_mediabox = base_page.mediabox
                    top_page = cur_pdf_reader.pages[pdf_page_index]
                    base_page.merge_page(top_page)
                    base_page.mediabox = base_page_mediabox

                pdf_write.add_page(base_page)

        with open(multi_layer_pdf_path, "wb") as fp:
            pdf_write.write(fp)
            print(f"\033[1;32mmultipdf file to {multi_layer_pdf_path}\033[0m")

        return multi_layer_pdf_path

    def check_file(self):
        """Check file exist and if pdf file."""
        for pdf_file in self.pdf_files:
            if not os.path.exists(pdf_file):
                raise FileNotFoundError(f"file {pdf_file} not found")
            if not pdf_file.endswith(".pdf"):
                raise ValueError(f"file {pdf_file} is not pdf file")

    def check_files_specified(self):
        """Check pdf_files not specified."""
        if len(self.pdf_files) == 0:
            raise ValueError("pdf files not specified")
        if len(self.pdf_files) == 1:
            raise ValueError("pdf files must be more than one")

    def check_out_dir(self):
        """If out_dir not exist, create it."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)


def multi_pdf_to_multi_layer_pdf_demo():
    root_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    attachment_dir = os.path.join(root_dir, "public/attachments")
    txt_pdf_path = os.path.join(attachment_dir, "whatispython.pdf")
    pic_pdf_path = os.path.join(attachment_dir, "samplepic.pdf")
    output_dir = os.path.join(root_dir, "dist/pdf_parse")

    # fill pdf files
    pdf_files = [pic_pdf_path, txt_pdf_path]

    # merge pdf files
    multi_pdf = MultiPdfToMultiLayerFile(pdf_files, output_dir)
    multi_pdf.be_multi_layer()


if __name__ == "__main__":  # pragma: no cover
    # use "-i" got pdf files, use "-o" got output directory
    parser = argparse.ArgumentParser(description="Parse pdf file to multi layer file")
    parser.add_argument("-i", "--input", help="input pdf files", nargs="+", required=False)
    parser.add_argument("-o", "--output", help="output directory", required=False)

    args = parser.parse_args()

    pdf_files = args.input
    output_dir = args.output

    # if args not set, use stdin to get pdf files and output directory
    if pdf_files is None:
        pdf_files = input("input pdf files path, split by space: ").split(" ")
    if output_dir is None:
        output_dir = input("input output directory: ")

    # merge pdf files
    multi_pdf = MultiPdfToMultiLayerFile(pdf_files, output_dir)
    multi_pdf.be_multi_layer()
