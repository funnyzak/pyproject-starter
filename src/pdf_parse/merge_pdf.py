# -*- coding: utf-8 -*-
# created by: leon<silenceace at gmail dot com>
# date: 2022-10-02
# license: MIT
# description: Merge pdf files
# usage: poetry run python src/pdf_parse/merge_pdf.py
# notes:

import argparse
from datetime import datetime
import os
import random

from PyPDF2 import PdfMerger


# Merge pdf files class
class MergePdf:
    def __init__(self, pdf_files, output_dir):
        """Pass pdf files to be merged and output dir.

        :param pdf_files: pdf files to be merged
        :param output_dir: output dir
        """
        self.pdf_files = pdf_files
        self.output_dir = output_dir

        self.check_files_specified()
        self.check_file()
        self.check_out_dir()

    # merge pdf files
    def merge(self):
        merger = PdfMerger()
        merge_pdf_path = os.path.join(self.output_dir, f"merge_{str(int(datetime.now().timestamp()))}.pdf")

        for pdf_file in self.pdf_files:
            input_file = open(pdf_file, "rb")
            merger.append(input_file)

        merger.write(merge_pdf_path)
        merger.close()

        print(f"\033[1;32mmerge pdf files to {merge_pdf_path}\033[0m")

        # return merge pdf file path
        return merge_pdf_path

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

    def check_out_dir(self):
        """If out_dir not exist, create it."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)


# test merge pdf files
def test_merge_pdf():
    # get path top level directory
    root_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    attachment_dir = os.path.join(root_dir, "public/attachments")
    txt_pdf_path = os.path.join(attachment_dir, "whatispython.pdf")
    pic_pdf_path = os.path.join(attachment_dir, "samplepic.pdf")
    output_dir = os.path.join(root_dir, "dist/pdf_parse")

    # fill pdf files
    pdf_files = []
    for _item in range(random.randint(3, 12)):
        pdf_files.append(txt_pdf_path)
        if random.randint(0, 1) == 1:
            pdf_files.append(pic_pdf_path)  # pragma: no cover
    # shuffle pdf files
    random.shuffle(pdf_files)

    # merge pdf files
    merge_pdf = MergePdf(pdf_files, output_dir)
    merge_pdf.merge()


if __name__ == "__main__":  # pragma: no cover
    # use "-i" got pdf files, use "-o" got output directory
    parser = argparse.ArgumentParser(description="Merge pdf files")
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
    merge_pdf = MergePdf(pdf_files, output_dir)
    merge_pdf.merge()
